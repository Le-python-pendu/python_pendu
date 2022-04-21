from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('<h1> Page d\'acceuil </h1>')

def profil(request):
    return HttpResponse('<h1> Profil utilisateur</h1>')

def registration(request):
    return HttpResponse('<h1> Inscription </h1>')

def connexion(request):
    return HttpResponse('<h1> Se connecter </h1>')

def history(request):
    return HttpResponse('<h1> Historique et statistiques </h1>')

def game(request):
    return HttpResponse('<h1> Jeu </h1>')
