from django.shortcuts import render
from galeria.models import Fotografia

def index(request):
    dados = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {"cards": dados})


def imagem(request):
    return render(request, 'galeria/imagem.html')
