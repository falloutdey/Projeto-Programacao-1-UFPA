from bs4 import BeautifulSoup
from fontes_urls import urls, get_soup, palavras_chaves
import requests


class filtro:
  def filtragem():
      "Função responsável por filtrar as noticias baseada nas palavras-chaves"
      lista_links = []
      for j in urls:
          # sites que vão ser escavados
          soup = get_soup(j)  # criação do objeto beautifulSoup
          for k in palavras_chaves:
              for link in soup.find_all('a'):
                try:
                  if '' not in link.get('href'):
                    pass
                  elif (k in link.get('href')):  # inserção das palavras chaves
                    lista_links.append(
                        'https://dol.com.br' + link.get('href') + '\n')
                except:
                  pass
      return list(set(lista_links))