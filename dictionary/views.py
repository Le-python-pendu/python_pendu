from django.shortcuts import render
from .models import Dictionary_t
from random import randint


# Create your views here.

def index(request):
    liste = Dictionary_t.objects.all()[:10]

    context = {'title': '*Dictionary*',
               'content': liste,
               }



    return render(request,
                  'dictionary/index.html', context)
