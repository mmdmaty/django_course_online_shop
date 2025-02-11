from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    age = models.PositiveIntegerField(blank=True,null=True)
