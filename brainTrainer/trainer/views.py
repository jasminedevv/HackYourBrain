from django.shortcuts import render
from django.contrib.auth.models import User

from trainer.models import Food, Plant
import random

# Create your views here.

def flipper(request):
    foods = Food.objects.all()
    food = random.choice(foods).image.url
    return render(request, 'flipper.html', {'food':food})

# def garden(request):
#     plants = Plant.objects.all()
#     return render(request, 'garden.html', {'plants': plants})

def menu(request):
    return render(request, 'menu.html')

def increment_points(request):
    user_profile = request.user.profile
    user_profile.score += 1
    request.user.save()
    foods = Food.objects.all()
    food = random.choice(foods)
    return render(request, 'flipper.html', {'food':food})

def decrement_points(request):
    user_profile = request.user.profile
    user_profile.score -= 1
    request.user.save()
    foods = Food.objects.all()
    food = random.choice(foods)
    return render(request, 'flipper.html', {'food':food})
