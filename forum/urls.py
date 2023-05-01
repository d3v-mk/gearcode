from django.urls import path, include
from . import views
from usuarios.views import logout_view


urlpatterns = [
    path('<str:area_slug>/', views.area_detail, name='area_detail'),
    path('<str:area_slug>/novo_topico/', views.novo_topico, name='novo_topico'),
    path('<str:area_slug>/<str:post_slug>/delete', views.delete_topico, name='delete_topico'),
    path('<str:area_slug>/<str:post_slug>/', views.post_detail, name='post_detail'),
]
