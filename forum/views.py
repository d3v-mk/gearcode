from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Postagem


def python(request):
    return render(request, 'python.html')


@login_required
def nova_postagem(request):
    if request.method == 'GET':
        return render(request, 'nova_postagem.html')
    elif request.method == "POST":
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')

        postagem = Postagem(
        titulo=titulo,
        conteudo=conteudo,
        autor=request.user,
        )

        postagem.save()
        return redirect('post_detail', pk=postagem.pk)
    else:
        return redirect(reverse('nova_postagem'))
    

def post_detail(request, pk):
    posts = get_object_or_404(Postagem, pk=pk)
    return render(request, 'post_detail.html', {'posts': posts})