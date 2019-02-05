from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect

### IMPORT DJANGO CREATE/UPDATE/DELETE VIEWS ###
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


## IMPORT FILES ON APPLICATIONS
from .models import Notes

# START VIEWS #
class Index(ListView):
    model = Notes
    template_name = 'notes/index.html'

class New_Note(CreateView):
    model = Notes
    fields = '__all__'
    template_name = 'notes/add.html'
    success_url = reverse_lazy('index')

class Delete_Note(DeleteView):
    model = Notes
    template_name = 'notes/delete.html'
    success_url = reverse_lazy('index')

class Edit_Note(UpdateView):
    model = Notes
    fields = ['note']
    template_name = 'notes/edit.html'
    success_url = reverse_lazy('index')
