from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.shortcuts import redirect
from django.urls import reverse



class Area(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Area, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    




class Postagem(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    num_respostas = models.IntegerField(default=0)
    num_visualizacoes = models.IntegerField(default=0)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, default='postagem-sem-titulo')

    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Postagem, self).save(*args, **kwargs)


    
