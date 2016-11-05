from django.shortcuts import render
from models import *

# Create your views here.

def flipper(request):
    foods = Food.objects.all()
    return render(request, 'flipper.html', {'foods': foods})

def garden(request):
    plants = Plant.objects.all()
    return render(request, 'garden.html', {'plants': plants})

def menu(request):
    return render(request, 'menu.html')
