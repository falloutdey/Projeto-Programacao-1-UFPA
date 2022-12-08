from django.contrib import admin
from django.urls import path
from .views import home, gerenciador

urlpatterns = [
    path('', home),
    path('gerenciador-fontes/', gerenciador)
]