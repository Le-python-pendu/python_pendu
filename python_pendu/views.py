from django.http import HttpResponse
from django.shortcuts import render


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
    return render(request, 'python_pendu/game.html')
