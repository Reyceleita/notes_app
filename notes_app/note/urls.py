from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('note/', notes, name='notes'),
    path('create-note/', form, name='form'),
    path('note-detail/<int:id>/', note_detail, name='note_detail'),
    path('delete-note/<int:id>/', delete_note, name='delete_note'),
]
