from django.db import models

from django.contrib.auth.models import AbstractUser


class customUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=100)
