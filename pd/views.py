from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, DeleteView
from .models import record
from django.urls import reverse_lazy



class recordListView(ListView):
    model=record
    template_name='home.html'

class recordDetailView(DetailView):

    model = record

    template_name = 'record_detail.html'

class recordCreateView(CreateView):
    model=record
    template_name='record_new.html'
    fields='__all__'
    
    
class recordDeleteView(DeleteView):
    model=record
    template_name='record_delete.html'
    success_url=reverse_lazy('home')
# Create your views here.
