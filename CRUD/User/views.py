from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from User import forms

# Create your views here.

def home(request):
    return render(request, 'Home.html')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'signin.html', {
                'form' : AuthenticationForm,
                'error' : 'Credenciales incorrectas',
            })
        else:
            login(request, user)
            return redirect('/')


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.core.exceptions import ValidationError
from . import forms

def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)  
                user.set_password(form.cleaned_data['password1'])  
                user.save()  
                login(request, user)  
                return redirect('/') 
            except ValidationError:
                return render(request, 'register.html', {
                    'form': form,
                    'error': 'Hubo un problema al crear el usuario, intenta nuevamente.',
                })
        else:
            return render(request, 'register.html', {
                'form': form,
                'error': 'Por favor corrige los errores en el formulario.',
            })
    else:
        form = forms.SignUpForm()
        return render(request, 'register.html', {
            'form': form
        })



def signout(request):
    logout(request)
    return redirect('home')