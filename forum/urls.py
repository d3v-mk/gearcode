from django.urls import path, include
from . import views
from usuarios.views import logout_view


urlpatterns = [
    path('criar_area/', views.criar_area, name='criar_area'),
    path('/', views.area_detail, name='area_detail'),
    path('<slug:area_slug>/<int:pk>/', views.post_detail, name='post_detail'),
    path('nova_postagem/', views.nova_postagem, name='nova_postagem'),
]
