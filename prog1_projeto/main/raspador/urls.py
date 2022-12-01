from django.urls import path
from .views import segundo
from .views import PaginaInicial

urlpatterns = [
    # path('endereco/', Minha_view.as_view(), name = 'nome_da_url') ---> estrutura
    path('', PaginaInicial.as_view(), name = 'inicio'),
    path('home/',  segundo, name="link")
]