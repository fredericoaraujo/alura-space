from django.urls import path
from usuarios.views import cadastro, login, logout

urlpatterns = [
    path('login/', login, name='usuarios.login'),
    path('cadastro/', cadastro, name='usuarios.cadastro'),
    path('logout/', logout, name='usuarios.logout'),
]