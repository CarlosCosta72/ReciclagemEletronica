from django.shortcuts import render
from django.views.generic import ListView

from .models import componente

class ComponenteListView(ListView):
    model = componente
