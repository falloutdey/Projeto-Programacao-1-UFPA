from django.contrib import admin
from django.urls import path
from .views import home, gerenciador, adicionar, deletar

urlpatterns = [
    path('', home),
    path('gerenciador-fontes/', gerenciador),
    path('adicionar/', adicionar, name='adicionar'),
    path('deletar/<int:id>/', deletar, name='deletar'),
]
