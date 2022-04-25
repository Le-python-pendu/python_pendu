from django.db import models

# Create your models here.
import dictionary.models

class history(models.Model):
    word = models.ForeignKey(dictionary.models.dictionary, on_delete=models.PROTECT)
    username = models.ForeignKey(user.models.user, on_delete=models.PROTECT)
    duration = models.FloatField(default=None)
    created_at = models.DateField(auto_created)

    def __str__(self):
        return self.word

    # class Meta:
    #     ordering = ['batiment', 'piece']
    #     verbose_name_plural = "Bureaux"

# class Personne(models.Model):
#     first_name = models.CharField(max_length=50, default=None)
#     last_name  = models.CharField(max_length=50, default=None)
#     bureau = models.ForeignKey(Bureau, on_delete= models.PROTECT)
#
#     def __str__(self):
#         return self.first_name
#
#     class Meta:
#         ordering = ['first_name']