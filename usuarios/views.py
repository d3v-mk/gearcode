from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Profile

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not (senha == confirmar_senha):    
            return redirect(reverse('cadastro'))
        
        user = User.objects.filter(username=username)

        if user.exists():
            return redirect(reverse('cadastro'))   
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return redirect(reverse('login'))
    

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=username, password=senha)
        
        if not user:
            return redirect(reverse('login'))
        
        auth.login(request, user)
        return redirect(reverse('index'))
    
def logout_view(request):
    logout(request)
    return redirect(reverse('index'))


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        profile.save()
        
        user = instance  # obtem o objeto User criado
        username = user.username  # obtem o nome de usuario do objeto User
        
        user_profile = Profile.objects.get(user=user)
        user_profile.username = username  # atribui o nome de usuario ao campo username do perfil
        user_profile.save()


def profile(request, username):
    profile = get_object_or_404(Profile, username=username)
    return render(request, 'profile.html', {'profile': profile})