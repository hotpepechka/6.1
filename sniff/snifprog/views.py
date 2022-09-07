from django.shortcuts import render
from .models import Pepe
from django.views.generic import ListView

class bloglistview(ListView):
    model = Pepe
    template_name = 'home.html'
# Create your views here.
