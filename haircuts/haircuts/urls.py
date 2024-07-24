# haircuts/urls.py
from django.urls import path

from .views import HaircutListView, HaircutDetailView, AddHaircutView, HaircutDeleteView

urlpatterns = [
    path('', HaircutListView.as_view(), name='haircut_list'),
    path('add/', AddHaircutView.as_view(), name='add_haircut'),
    path('<uuid:pk>', HaircutDetailView.as_view(), name='haircut_detail'),
    path('<uuid:pk>/delete/', HaircutDeleteView.as_view(), name='haircut_delete')
]
