from django.urls import path
from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('perfil', views.perfil, name='perfil'),
    path('editar_perfil', views.editar_perfil, name='editar_perfil'),
    path('cadastro_form', views.cadastro_form, name='cadastro_form'),
    path('confirma_cadastro_form', views.confirma_cadastro_form, name='confirma_cadastro_form'),
]
