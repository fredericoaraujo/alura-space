from django.shortcuts import render
from galeria.models import Fotografia

def index(request):
    dados = Fotografia.objects.filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": dados})


def imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia' : fotografia})
