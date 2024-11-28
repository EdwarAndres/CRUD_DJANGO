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


def signup(request):
    if request.method == 'GET':
        return render(request, 'register.html', {
            'form': forms.SignUpForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                first_name=request.POST['first_name'],
                                                last_name=request.POST['last_name'],
                                                email=request.POST['email'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('/')
            except IntegrityError:
                return render(request, 'register.html', {
                    'form': forms.SignUpForm,
                    'error': 'Usuario ya existe',
                })

        return render(request, 'register.html', {
            'form': forms.SignUpForm,
            'error': 'Las contraseñas no coinciden',
        })


def signout(request):
    logout(request)
    return redirect('home')