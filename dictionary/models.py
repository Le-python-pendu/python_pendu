from django.db import models
# from django.contrib.auth import authenticate
from my_users.models import Users

# Create your models here.

# class User():
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class Dictionary_t(models.Model):
    word= models.CharField(max_length=100)
    classification = models.CharField(max_length=150)
    definition = models.CharField(max_length=150)
    url_image = models.URLField(max_length=100, blank=True, default="")
    frequency = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return str(self.word)+str(self.definition)

class History_t(models.Model):
    user_name = models.CharField(max_length=100, default="")  #
    created_at = models.DateTimeField(auto_now_add=True)  # date of the game
    score = models.IntegerField(default=0)  #
    words = models.CharField(max_length=200, default="")  # List of words
    duration = models.FloatField(default=0)  # time to find the word

    def __str__(self):
        return self.word
