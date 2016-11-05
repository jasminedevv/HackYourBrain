from __future__ import unicode_literals

from django.db import models
from PIL import Image

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Food(models.Model):
    good = models.BooleanField(default=True)
    image = models.ImageField(upload_to='food-images')

class Plant(models.Model):
    weed = models.BooleanField(default=True)
    image = models.ImageField(upload_to='plant-images')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return 'Profile of user: {}'.format(self.user.username)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
