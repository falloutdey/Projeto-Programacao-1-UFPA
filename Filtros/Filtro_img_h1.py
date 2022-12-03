from bs4 import BeautifulSoup
import requests

urls = ['https://www.cnnbrasil.com.br/tudo-sobre/violencia-contra-a-mulher/', 'https://www12.senado.leg.br/institucional/datasenado/publicacoesportema?tema=Mulher'] #Sites que serão minerados

palavras_chaves = ['mulheres', 'violencia-domestica', 'mulher', 'Mulheres', 'Feminicídio'] #palavras_chaves que serão utilizadas para filtrar as noticias

def get_soup(urls):
    """Função reponsável por realizar um request GET ao site e criar um objeto bs4"""
    try:
        req = requests.get(urls)
        soup  = BeautifulSoup(req.text,'html.parser')
        return soup
    except:
        print("Não foi possivel fazer o request !")
        
def filtragem():
    "Função responsável por filtrar as noticias baseada nas palavras-chaves"
    lista_links = []
    for j in urls:
    #urls que serão mineradas
        soup = get_soup(j)  #criação do objeto beautifulSoup
        for k in palavras_chaves:
            for link in soup.find_all('a'):
              try:
               if '' not in link.get('href'):
                pass
               elif (k in link.get('href')): #inserção das palavras chaves
                lista_links.append((link.get('href')))
              except:
               pass
    return list(set(lista_links))
links_filtrados = filtragem()
print(*links_filtrados)

##############################################
from urllib.request import urlopen
from bs4 import BeautifulSoup

#obter link das imagens dos sites filtrados

site = "https://www.cnnbrasil.com.br/politica/eleicao-2022-sera-a-1a-com-lei-de-combate-a-violencia-politica-contra-mulheres/ "
html = urlopen(site)
bs = BeautifulSoup(html, 'html.parser')

images = bs.find_all('img')
for img in images:
    if img.has_attr('src'):
        print(img['src'])

      
#################################################
from bs4 import BeautifulSoup
from re import sub

#obter o titulo das matérias filtradas

site = "https://www.cnnbrasil.com.br/politica/eleicao-2022-sera-a-1a-com-lei-de-combate-a-violencia-politica-contra-mulheres/ "
html = urlopen(site)
bs = BeautifulSoup(html, 'html.parser')

tits = str(bs.find_all('h1'))
tits = sub("<.>", "", tits)
print(tits)
