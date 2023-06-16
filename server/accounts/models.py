from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    profile = models.ImageField(default='accounts/blank.png')
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')