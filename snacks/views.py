from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Snack
from django.views.generic import (
  ListView,
  DetailView,
  CreateView,
  UpdateView,
  DeleteView,
)

class SnackListView(ListView):
  template_name = 'snack_list.html'
  model = Snack

class SnackDetailView(DetailView):
  template_name = 'snack_detail.html'
  model = Snack

class SnackCreateView(CreateView):
  template_name = 'snack_create.html'
  model = Snack
  fields = ['name', 'description', 'purchaser']
  

class SnackUpdateView(UpdateView):
  Template_name = 'snack_update.html'
  model = Snack
  fields = ['name', 'description', 'purchaser']
  

class SnackDeleteView(DeleteView):
  Template_name = 'snack_delete.html'
  model = Snack
  fields = ['name', 'description', 'purchaser']
  success_url = reverse_lazy('snack_list')





