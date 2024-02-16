from django.db import models
from django.conf import settings
from accounts.models import customUser


class Post(models.Model):
    author = models.ForeignKey(customUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
