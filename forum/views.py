from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Area, Postagem
from django.utils.text import slugify
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib.auth.models import Group


def area_detail(request, area_slug):
    links = {
        'link1': '/forum/',
        'link2': '/fo222rum/',
    }
    
    area = get_object_or_404(Area, slug=area_slug)
    postagens = Postagem.objects.all().order_by('-created_at')

    context = {'postagens': postagens, 
               'links': links, 
               'area': area,
               'user': request.user,
    }

    return HttpResponse(render_to_string(['fundamentos-basicos-python.html', 'recursos-avancados-python.html'], context))


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
def novo_topico(request, area_slug):
    area = get_object_or_404(Area, slug=area_slug)
    if request.method == 'GET':
        return render(request, 'novo_topico.html', {'area': area})
    elif request.method == "POST":
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')

        postagem = Postagem(
            titulo=titulo,
            conteudo=conteudo,
            autor=request.user,
        )

        if area_slug == 'fundamentos-basicos-python': # slug da área
            postagem.area = area
            postagem.save()
        elif area_slug == 'recursos-avancados-python': # slug da área
            postagem.area = area
            postagem.save()
        # add more areas here if necessary
        else:
            return redirect(reverse('area_detail', kwargs={'area_slug': area_slug}))
    return redirect(reverse('area_detail', kwargs={'area_slug': area_slug}))

    






def post_detail(request, area_slug, post_slug):
    posts = get_object_or_404(Postagem, slug=post_slug)
    owner_group = Group.objects.get(user=posts.autor)

    context = {
        'owner_group': owner_group,
        'posts': posts,
    }
    
    return render(request, 'post_detail.html', context)


