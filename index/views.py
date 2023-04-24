from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.urls import reverse
from django.contrib import auth
from django.contrib.sessions.models import Session
from django.utils import timezone


def users_online(request):
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []
    for session in sessions:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))
    users_online = User.objects.filter(id__in=user_id_list)
    return render(request, 'index.html', {'users_online': users_online})

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=username, password=senha)
        
        if not user:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha incorretos.')
            return redirect(reverse('login'))
        
        auth.login(request, user)
        return redirect(reverse('login'))










def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não são iguais')
            return redirect(reverse('cadastro'))

        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuario já existe')
            return redirect(reverse('cadastro'))
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        messages.add_message(request, constants.SUCCESS, 'Usuario cadastrado com sucesso')

        return redirect(reverse('login'))