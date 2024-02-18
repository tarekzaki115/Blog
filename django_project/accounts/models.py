from django.db import models

from django.contrib.auth.models import AbstractUser
from .manager import customUserManager


class customUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=100)
    object = customUserManager()
