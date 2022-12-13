from django.shortcuts import render, redirect
from .backend import urls, filtragem

# Create your views here.
def home(request):
    return render(request, 'index.html', {'filtragem': filtragem()})

def gerenciador(request):
    return render(request, 'gerenciador.html', {'urls': urls})