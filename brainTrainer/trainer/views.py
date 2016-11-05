from django.shortcuts import render
from models import *

# Create your views here.

def front_page(request):
    foods = Food.objects.all()
    return render(request, 'index.html', {'foods': foods})
