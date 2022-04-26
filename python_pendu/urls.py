"""python_pendu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import dictionary.views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    #Template login
    path('profil/', views.profil, name="profil"),
    path('registration/', views.registration, name="registration"),
    path('connexion/', views.connexion, name="connexion"),
    # Template game
    path('level/', views.level, name="level"),
    path('game/', views.game, name="game"),
    path('game2/', views.game2, name="game2"),
    path('history/', views.history, name="history"),
    # M4rch
    path('dictionary', include('dictionary.urls')),

]
