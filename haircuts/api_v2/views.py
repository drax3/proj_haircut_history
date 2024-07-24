from django.shortcuts import render
from rest_framework import generics

from haircuts.models import Haircut
from .serializers import HaircutSerializer
# Create your views here.

class HaircutList(generics.ListCreateAPIView):
    queryset = Haircut.objects.all()
    serializer_class = HaircutSerializer

class HaircutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Haircut.objects.all()
    serializer_class = HaircutSerializer
