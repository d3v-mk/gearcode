from django.urls import path, include
from . import views
from usuarios.views import logout_view


urlpatterns = [
    path('python/', views.python_geral, name="python_geral"),
    path('nova_postagem/', views.nova_postagem, name="nova_postagem"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('fundamentos_basicos_python/', views.python_basico, name='python_basico'),
]
