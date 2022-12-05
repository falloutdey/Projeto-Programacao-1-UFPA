from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re

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

#obter link das imagens dos sites filtrados

site = "https://www.cnnbrasil.com.br/politica/eleicao-2022-sera-a-1a-com-lei-de-combate-a-violencia-politica-contra-mulheres/ "
html = urlopen(site)
bs = BeautifulSoup(html, 'html.parser')

images = bs.find_all('img')
for img in images:
    if img.has_attr('src'):
        print(img['src'])

      
#################################################

# obter o titulo das matérias filtradas

site = ["https://www.cnnbrasil.com.br/politica/eleicao-2022-sera-a-1a-com-lei-de-combate-a-violencia-politica-contra-mulheres/ ", 'https://www.bbc.com/portuguese/geral-63815180']

for search in site:

    html = urlopen(search)
    bs = BeautifulSoup(html, 'html.parser')

    title = bs.find_all('h1')
    for final in title:
        k = str(final)
        pp = re.search('(?<=>).+(?=<)', k)
        pp = str(pp.group()).strip()
        print(pp)
