from django import forms

class create_note_form(forms.Form):
    title = forms.CharField(label='Title', max_length=200, required=False, widget=forms.TextInput(attrs={
        'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-20 bg-white-700 border-gray-600 placeholder-gray-400 text-black focus:ring-blue-500 focus:border-blue-500', 'placeholder': 'Tilte'
    }))
    content = forms.CharField(label='Content', required=True, widget=forms.TextInput(attrs={
        'class': 'bg-gray-50 border border-gray-300 text-black-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 bg-white-700 border-gray-600 placeholder-gray-400 text-black focus:ring-blue-500 focus:border-blue-500', 'placeholder': 'Content'
    }))
