from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render, get_object_or_404
from .forms import *
from .models import Note

# Create your views here.
def notes(request):
    return render(request, 'notes_list.html')

def index(request):
    notas = Note.objects.all()
    return render(request, 'index.html', {'notas': notas})

def form(request):
    if request.method == 'GET':
        return render(request, 'form.html', {'form': create_note_form})
    else:
        Note.objects.create(title= request.POST['title'], content = request.POST['content'])
        return redirect("/")

def note_detail(request, id:int):
    note = Note.objects.get(pk=id)
    if request.method == 'GET':
        init_data = {'title': note.title, 'content': note.content}
        form = create_note_form(initial=init_data)
        return render(request, 'note_detail.html', {'form': form, 'note': note})
    else:
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('/')

def delete_note(request, id:int):
    note = get_object_or_404(Note, pk = id)
    
    if request.method == 'POST':
        note.delete()
        return redirect('/')
    
    return render(request, 'delete_note.html', {'note': note})