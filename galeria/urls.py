from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path('', index, name='galeria.index'),
    path('imagem', imagem, name='galeria.imagem'),
]