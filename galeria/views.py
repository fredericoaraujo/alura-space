from django.shortcuts import render
from galeria.models import Fotografia

def index(request):
    lista_fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": lista_fotografias})


def imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia' : fotografia})

def buscar(request):
    lista_fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            lista_fotografias = lista_fotografias.filter(nome__icontains=nome_a_buscar)
    return render(request, 'galeria/buscar.html', {'cards': lista_fotografias})
