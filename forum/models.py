from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Area(models.Model):
    title = models.TextField(max_length=100, default='')
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Area, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Postagem(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    num_respostas = models.IntegerField(default=0)
    num_visualizacoes = models.IntegerField(default=0)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
