from django.db import models
# from django.contrib.auth import authenticate



# Create your models here.

# class User():
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


class Dictionary_t(models.Model):
    word= models.CharField(max_length=30)
    classification = models.CharField(max_length=10)
    definition = models.CharField(max_length=100)
    url_image = models.URLField(max_length=50, blank=True, default="")
    frequency = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return str(self.word)+str(self.definition)


class History_t(models.Model):
    duration = models.FloatField(default=None) # time to find the word
    created_at = models.DateField() # date of the game
    word = models.ForeignKey(Dictionary_t, on_delete=models.PROTECT) #
    #username = models.ForeignKey(user.models.username, on_delete=models.PROTECT) # gamer's name

    def __str__(self):
        return self.word

    # class Meta:
    #     ordering = ['batiment', 'piece']
    #     verbose_name_plural = "Bureaux"