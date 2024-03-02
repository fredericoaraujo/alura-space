from django.urls import path
from usuarios.views import login, cadastro

urlpatterns = [
    path('login/', login, name='usuarios.login'),
    path('cadastro/', cadastro, name='usuarios.cadastro'),
]