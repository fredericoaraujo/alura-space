from django.urls import path
from galeria.views import index, imagem, buscar

urlpatterns = [
    path('', index, name='galeria.index'),
    path('imagem/<int:foto_id>', imagem, name='galeria.imagem'),
    path('buscar', buscar, name='buscar')
]