from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Food(models.Model):
    good = models.BooleanField(default=True)
    image = models.ImageField(upload_to='food-images')

class Plant(models.Model):
    weed = models.BooleanField(default=True)
    image = models.ImageField(upload_to='plant-images')
