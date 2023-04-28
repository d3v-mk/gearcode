from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Area, Postagem
from django.utils.text import slugify
from django.http import HttpResponseForbidden



@login_required
def criar_area(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        name = request.POST.get('nome')
        description = request.POST.get('descricao')
        slug = slugify(name)

        nova_area = Area(name=name, title=title, description=description, slug=slug)
        nova_area.save()

        context = {
            'nova_area': nova_area,
        }
        return render(request, 'area_detail.html', context)

    return render(request, 'criar_area.html')








@login_required
def nova_postagem(request, area_slug):
    try:
        area = Area.objects.get(slug=area_slug)
    except Area.DoesNotExist:
        return redirect('criar_area')
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        postagem = Postagem(
            titulo=titulo,
            conteudo=conteudo,
            autor=request.user,
            area=area
        )
        postagem.save()
        return redirect('nova_postagem', slug=area_slug)
    return render(request, 'nova_postagem.html', {'area': area})
    






def post_detail(request, area_slug, pk):
    posts = get_object_or_404(Postagem, pk=pk)
    return render(request, 'post_detail.html', {'posts': posts})


def area_detail(request, area_slug):
    return render(request, 'area_detail.html')
)