from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .backend import filtragem
# Create your views here.

class PaginaInicial(TemplateView):
    template_name = 'raspador/index.html'

filtro = filtragem()

def segundo(request):
    
    name = request.POST.get("name")
    print(name)
    return render(request, 'raspador/segundo.html', {'filtragem': filtro})