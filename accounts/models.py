from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from accounts.managers import ToDoAppUserManager


# class ToDoUser(AbstractUser):
#     points = models.IntegerField(
#         blank=True,
#         null=True
#     )

class TodoAppUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(
        unique=True
    )
    username = models.CharField(
        max_length=150,
        unique=True
    )
    is_active = models.BooleanField(
        default=True
    )
    is_staff = models.BooleanField(
        default=False
    )

    objects = ToDoAppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(
        TodoAppUser,
        on_delete=models.CASCADE,
    )
    age = models.IntegerField(
        blank=True,
        null=True,
    )
    points = models.IntegerField(
        blank=True,
        null=True,
    )
    phone_number = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )

