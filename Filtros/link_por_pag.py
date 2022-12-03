from bs4 import BeautifulSoup
import requests

# Sites que serão minerados
urls = ['https://www.cnnbrasil.com.br/tudo-sobre/violencia-contra-a-mulher/']

# palavras_chaves que serão utilizadas para filtrar as noticias
palavras_chaves = ['mulheres', 'violencia-domestica',
                   'mulher', 'Mulheres', 'Feminicídio']


def get_soup(urls):
    """Função reponsável por realizar um request GET ao site e criar um objeto bs4"""
    try:
        req = requests.get(urls)
        soup = BeautifulSoup(req.text, 'html.parser')
        return soup
    except:
        print("Não foi possivel fazer o request !")


def filtragem():
    "Função responsável por filtrar as noticias baseada nas palavras-chaves"
    lista_links = []
    paginas = 1
    for j in urls:
        while paginas <= 5:
            # urls que serão mineradas
            # criação do objeto beautifulSoup
            soup = get_soup(j + 'pagina/' + str(paginas))
            for k in palavras_chaves:
                for link in soup.find_all('a'):
                    try:
                        if '' not in link.get('href'):
                            pass
                        elif (k in link.get('href')):  # inserção das palavras chaves
                            lista_links.append((link.get('href')))
                    except:
                        pass
            paginas += 1
    return list(set(lista_links))


links_filtrados = filtragem()
print(links_filtrados)
