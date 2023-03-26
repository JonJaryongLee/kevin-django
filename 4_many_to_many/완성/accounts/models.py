from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
