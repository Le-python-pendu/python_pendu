from django.http import HttpResponse
from django.shortcuts import render
from dictionary.models import Dictionary_t

import dictionary, random
from dictionary import views, models


def home(request):
    return render(request, 'python_pendu/home.html')


def profil(request):
    return render(request, 'python_pendu/profil.html')


def registration(request):
    return render(request, 'python_pendu/registration.html')


def connexion(request):
    return render(request, 'python_pendu/connexion.html')


def history(request):
    return render(request, 'python_pendu/history.html')


def game(request):


    len_mot = Dictionary_t.objects.count()
    n = random.randint(1,len_mot)
#    res_mot_mystere = Dictionary_t.objects.all()[35:39]

    res_mot_mystere = Dictionary_t.objects.get(pk=n)
    mot = res_mot_mystere.word
#     definition = res_mot_mystere.definition

    print(">>",type(res_mot_mystere), dir(res_mot_mystere))
    lista_teste = [1,2,3,4,5,6,7]


    #mot=""
    definition=""
    solution_mot = res_mot_mystere.word
    index = res_mot_mystere.definition



    return render(request,
                  'python_pendu/game.html', context={"res_mot_mystere": res_mot_mystere, "mot_mystere": mot, "solution_mot": solution_mot, "index":index, "definition": definition, "len": len_mot, "lista_teste": lista_teste})
