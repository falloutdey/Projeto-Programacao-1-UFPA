from django.shortcuts import render, redirect
from .backend import urls

# Create your views here.
def home(request):
    return render(request, 'index.html')

def gerenciador(request):
    return render(request, 'gerenciador.html', {'urls': urls})