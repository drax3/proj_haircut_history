# haircuts/urls.py
from django.urls import path

from .views import HaircutListView, HaircutDetailView

urlpatterns = [
    path('', HaircutListView.as_view(), name='haircut_list'),
    path('<uuid:pk>', HaircutDetailView.as_view(), name='haircut_detail'),
]