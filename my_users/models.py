from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class Users(AbstractBaseUser):
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    email = models.EmailField(unique=True)
    last_name = None
    first_name = None
    user_name = models.CharField()
    score = models.IntegerField()
    USERNAME_FIELD = 'email'
