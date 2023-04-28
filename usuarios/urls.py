from django.urls import path
from . import views
from .views import logout_view, profile


urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.login, name="login"),
    path('logout/', logout_view, name='logout'),
    path('<str:username>/', views.profile, name='profile'),
]