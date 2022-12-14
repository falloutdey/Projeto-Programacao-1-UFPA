from django.shortcuts import render, redirect
from .backend import filtragem
from .models import Fontes

# Create your views here.
def home(request):
    return render(request, 'index.html', {
        'filtragem': filtragem(),
        })

def gerenciador(request):
    fontes = Fontes.objects.all()
    return render(request, 'gerenciador.html', {
            'fontes': fontes,
    })

def adicionar(request):
    link = request.POST.get('nome_fonte')
    Fontes.objects.create(fonte=link)
    return redirect(gerenciador)

def deletar(request, id):
    link = Fontes.objects.get(id=id)
    link.delete()
    return redirect(gerenciador)