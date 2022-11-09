from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

class PaginaInicial(TemplateView):
    template_name = 'raspador/index.html'