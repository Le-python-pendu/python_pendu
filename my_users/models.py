from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.utils import timezone


class Users(AbstractBaseUser):
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    email = models.EmailField(unique=True)
    last_name = None
    first_name = None
    user_name = models.CharField(max_length=60)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    score = models.IntegerField(default=0)
    USERNAME_FIELD = 'email'

    objects = BaseUserManager()