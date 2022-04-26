from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from dictionary.models import Dictionary_t

import dictionary, random
from dictionary import views, models

@login_required
def home(request):
    return render(request, 'python_pendu/home.html')

@login_required
def profil(request):
    return render(request, 'python_pendu/profil.html')


def registration(request):
    return render(request, 'python_pendu/registration.html')


def connexion(request):
    return render(request, 'python_pendu/connexion.html')


def history(request):


    return render(request, 'python_pendu/history.html')

def game(request):
    return render(request, 'python_pendu/game.html')

def game2(request):
    # compte le numbre des mot au dictionnaire
    len_mot = Dictionary_t.objects.count()
    # choisi au azar un mot de 6 a 10 lettres
    state = True
    while state:
        n = random.randint(1,len_mot)
        res_mot_mystere = Dictionary_t.objects.get(pk=n)
        mot = res_mot_mystere.word
        if len(mot)<6 or len(mot) >10:
            print(n)
            continue
        else:
            break

    # verifié si exist le niveau
    if 'level' not in locals() or globals():
        level = 1

    # remove des lettres doublés
    key = set()
    {key.add(c) for c in mot}

    # create de lettres du clavier
    tab = []
    z = 0
    alpha = set([chr(n+65) for n in range(26)])
    # remove des lettres déjà au mot mystère
    alpha_dif = list(alpha.difference(key))
    # remplis le clavier basée au niv. difficulté
    difficulty = len(key)*(.7+level*.3)
    while z < difficulty:
        guess = random.choice(alpha_dif)
        if guess not in tab:
            tab.append(guess)
            z = len(tab)
        else:
            continue
    # verifié le variables envoyer au template
    solution_mot = res_mot_mystere.word
    index = res_mot_mystere.definition
    # envoi des variables (dictionnaire) au template dans le context
    return render(request,
                  'python_pendu/game2.html', context={"mot_mystere": res_mot_mystere.word, "index": res_mot_mystere.definition,  "tab": tab, "key": list(key), "level": level})

def update_history(request, pk_mot, field, value):
    obj = Dictionary_t.objects.get(pk=pk_mot)
    obj.field = value
    obj.save()

