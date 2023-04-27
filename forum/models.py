from django.db import models
from django.contrib.auth.models import User


class Postagem(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    num_respostas = models.IntegerField(default=0)
    num_visualizacoes = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo


class Forum(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.nome

