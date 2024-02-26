from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Haircut

class HaircutListView(ListView):
    model = Haircut
    context_object_name = 'haircut_list'
    template_name = 'haircuts/haircut_list.html'

class HaircutDetailView(DetailView):
    model = Haircut
    context_object_name = 'haircut'
    template_name = 'haircuts/haircut_detail.html'