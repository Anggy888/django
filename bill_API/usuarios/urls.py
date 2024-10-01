# usuarios/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.usuario_list, name='usuario-list'),          # Listar usuarios
    path('usuarios/create/', views.usuario_create, name='usuario-create'),  # Crear usuario
    path('usuarios/<int:pk>/', views.usuario_detail, name='usuario-detail'), # Detalle de usuario
    path('usuarios/update/<int:pk>/', views.usuario_update, name='usuario-update'), # Actualizar usuario
    path('usuarios/delete/<int:pk>/', views.usuario_delete, name='usuario-delete'), # Borrar usuario
]
