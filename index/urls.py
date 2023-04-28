from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('usuarios/', include('usuarios.urls'), name='usuarios'),
    path('forum/', include('forum.urls')),
]
