from django.db import models

from django.contrib.auth.models import AbstractUser
from .managers import customUserManager


class customUser(AbstractUser):
    # name = models.CharField(null=True, blank=True, max_length=100)
    age = models.PositiveIntegerField(blank=True, null=True)
    object = customUserManager()
