from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.db.models import Avg

from django.urls import reverse_lazy
from django.shortcuts import redirect

from .forms import HaircutForm, RatingForm
from .models import Haircut, Rating

class HaircutListView(LoginRequiredMixin,ListView):
    model = Haircut
    context_object_name = 'haircut_list'
    template_name = 'haircuts/haircut_list.html'
    login_url = 'account_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        haircut_list = context['haircut_list']
        for haircut in haircut_list:
            avg_rating = Rating.objects.filter(haircut=haircut).aggregate(avg_rating=Avg('rating'))['avg_rating']
            haircut.avg_rating = int(avg_rating) if avg_rating is not None else None
            latest_rating = Rating.objects.filter(haircut=haircut).order_by('-id').first()
            haircut.last_rating = latest_rating.rating if latest_rating else None

        return context


class HaircutDetailView(LoginRequiredMixin,DetailView):
    model = Haircut
    context_object_name = 'haircut'
    template_name = 'haircuts/haircut_detail.html'
    login_url = 'account_login'

    def post(self, request, *args, **kwargs):
        form = RatingForm(request.POST)
        if form.is_valid():
            rating_value = form.cleaned_data['rating']
            haircut = self.get_object()
            person = request.user
            Rating.objects.create(haircut=haircut, rating=rating_value, person=person)
        return redirect('haircut_detail', pk=self.kwargs['pk'])
        # return reverse_lazy('haircut_list')
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rating_form'] = RatingForm()  # Add rating form to context
        return context

class AddHaircutView(LoginRequiredMixin,CreateView):
    model = Haircut
    form_class = HaircutForm
    template_name = 'haircuts/add_haircut.html'
    success_url = reverse_lazy('haircut_list')
    login_url = 'account_login'

    # def form_valid(self, form):
    #     form.instance.username = self.request.user
    #     return super().form_valid(form)
    
    def form_valid(self, form):
        form.instance.person = self.request.user
        return super().form_valid(form)


class HaircutDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Haircut
    template_name = 'haircuts/haircut_delete.html'
    success_url = reverse_lazy('haircut_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.person == self.request.user
    
    def handle_no_permission(self):
        return JsonResponse({'error_message': 'You are not authorized to delete this object.'})