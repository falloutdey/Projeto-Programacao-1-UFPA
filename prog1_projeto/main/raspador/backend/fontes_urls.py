from bs4 import BeautifulSoup
import requests

# Links das redes de notícias a serem escavadas
urls = ['https://dol.com.br/noticias/policia?d=1']

# Palavras-chaves que deverão ser filtradas
palavras_chaves = ['feminicídios', 'mulher', 'namorada']

# Criação do objeto bs4
def get_soup(urls):
    """Função reponsável por realizar um request GET ao site e criar um objeto bs4"""
    try:
        req = requests.get(urls)
        soup = BeautifulSoup(req.text, 'html.parser')
        return soup
    except:
        print("Não foi possivel fazer o request !")
