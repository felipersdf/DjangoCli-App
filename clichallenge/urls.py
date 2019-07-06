"""clichallenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from clients.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('list-clients/', list_clients,  name='listar_clients'),
    path('create/', create_client, name='criar_cliente'),
    path('edit/<int:pk>/', edit_client, name='atualizar_cliente'),
    path('delete/<int:pk>/', delete_client, name='excluir_cliente'),
    path('login/', user_login, name='login'),
    path('register/', register, name='cadastro'),
    path('logout/', user_logout, name='sair'),
    path('auth/', include('social_django.urls', namespace='social')),
]
