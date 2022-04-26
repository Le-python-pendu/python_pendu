# my_users/views.py
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from . import forms

"""""
class LoginPage(View):
    form_class = forms.LoginForm
    template_name = 'python_pendu/connexion.html'

    def get(self, request):
        form = self.form_class
        message = ''
        return render(
            request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        message = ''
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['mot de passe'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')

            else:
                message = 'Identifiants invalides.'

        return render(
            request, self.template_name, context={'form': form, 'message': message})

"""
def registration_page(request):
    form = forms.RegistrationForm()
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # connecter l'utilisateur directement apres son innscription
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'python_pendu/registration.html', context={'form': form})

