# core/models.py
from djongo import models
from django.contrib.auth.models import AbstractUser, UserManager

class CustomUserManager(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        user = super().create_user(username, email, password, **extra_fields)
        return user

class CustomUser(AbstractUser):
    objects = CustomUserManager()
    
    class Meta:
        db_table = 'Users'  