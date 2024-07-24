from django.urls import path

from .views import HaircutDetail, HaircutList

urlpatterns = [
    path('<uuid:pk>/', HaircutDetail.as_view()),
    path('', HaircutList.as_view())
]