
from django.shortcuts import render
from .models import Ace
from django.views.generic.list import ListView


# Create your views here.


class AceList(ListView):
    model = Ace
    fields = '__all__'
    template_name = 'index.html'
