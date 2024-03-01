from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.db.models import Avg
from django.urls import reverse_lazy
from .forms import HaircutForm
from .models import Haircut, Rating

class HaircutListView(ListView):
    model = Haircut
    context_object_name = 'haircut_list'
    template_name = 'haircuts/haircut_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        haircut_list = context['haircut_list']
        for haircut in haircut_list:
            haircut.avg_rating = Rating.objects.filter(haircut=haircut).aggregate(avg_rating=Avg('rating'))['avg_rating']
            latest_rating = Rating.objects.filter(haircut=haircut).order_by('-id').first()
            haircut.last_rating = latest_rating.rating if latest_rating else None
        return context


class HaircutDetailView(DetailView):
    model = Haircut
    context_object_name = 'haircut'
    template_name = 'haircuts/haircut_detail.html'


class AddHaircutView(CreateView):
    model = Haircut
    form_class = HaircutForm
    template_name = 'haircuts/add_haircut.html'
    success_url = reverse_lazy('haircut_list')

