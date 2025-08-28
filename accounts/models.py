from django.contrib.auth.models import AbstractUser
from django.db import models

class ToDoUser(AbstractUser):
    points = models.IntegerField(
        blank=True,
        null=True
    )

