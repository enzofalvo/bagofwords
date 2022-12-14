# Enzo Falvo

# a) A página web (url) deve apontar para uma página web em inglês contendo, não menos que 1000 palavras.
from bs4 import BeautifulSoup
import requests
import spacy
import pandas as pd
from collections import defaultdict

sentenca = ''

lista_sentencas1 = []
lista_sentencas2 = []
lista_sentencas3 = []
lista_sentencas4 = []
lista_sentencas5 = []


url1 = "https://coldplay.fandom.com/wiki/Coldplay"
url2 = "https://www.britannica.com/biography/Freddie-Mercury"
url3 = "https://bible.fandom.com/wiki/Jesus_Christ"
url4 = "https://java.fandom.com/wiki/Java"
url5 = "https://t2informatik.de/en/smartpedia/clean-code/#:~:text=Smartpedia%3A%20Clean%20code%20refers%20to,and%20practices%20of%20software%20development."


informacoes_pagina1 = requests.get(url1)
informacoes_pagina2 = requests.get(url2)
informacoes_pagina3 = requests.get(url3)
informacoes_pagina4 = requests.get(url4)
informacoes_pagina5 = requests.get(url5)

html1 = BeautifulSoup(informacoes_pagina1.text, 'html.parser')
html2 = BeautifulSoup(informacoes_pagina2.text, 'html.parser')
html3 = BeautifulSoup(informacoes_pagina3.text, 'html.parser')
html4 = BeautifulSoup(informacoes_pagina4.text, 'html.parser')
html5 = BeautifulSoup(informacoes_pagina5.text, 'html.parser')

from pandas.core.indexes.datetimelike import DatetimeIndexOpsMixin

# Enzo Falvo
# b) O texto desta página deverá ser transformado em um array de senteças.
dicts = spacy.load('en_core_web_sm')


def get_sentencas(lista_sentencas, html):
    for sentenca in html.find_all("p"):
        # if not str(dicts(sentenca.get_text())).startswith("\n", 0, 2):
        lista_sentencas.append(dicts(sentenca.get_text()))
        sentencas = dicts(sentenca.get_text())

    lista_sentenca.append(lista_sentencas)
    return lista_sentencas


lista_sentenca = []
lista_sentencas1 = get_sentencas(lista_sentencas1, html1)
lista_sentencas2 = get_sentencas(lista_sentencas2, html2)
lista_sentencas3 = get_sentencas(lista_sentencas3, html3)
lista_sentencas4 = get_sentencas(lista_sentencas4, html4)
lista_sentencas5 = get_sentencas(lista_sentencas5, html5)



# d) O  resultado  esperado  será  uma  matriz  termo  documento  criada  a  partir  da  aplicação da técnica bag of Words em todo o corpus.

# Bag of Words
palavras_utilizadas = {}

bagOfWords = []
for sentenca in lista_sentenca:
  if not (str(sentenca).startswith("\n", 0, 2) and str(sentenca).startswith(",", 0, 1) and str(sentenca).startswith(".", 0, 1) and
            str(sentenca).strip() == "" and str(sentenca) == " "):
    for subtermo in sentenca:
      if not (str(subtermo).startswith("\n", 0, 2) and str(subtermo).startswith(",", 0, 1) and str(subtermo).startswith(".", 0, 1) and
              str(subtermo) == "" and str(subtermo) == " "):
        bagOfWords.append(subtermo)



for sentenca in bagOfWords:
  for subtermo in sentenca:
    if not (str(subtermo).startswith("\n", 0, 2) and str(subtermo).startswith(",", 0, 1) and str(subtermo).startswith(".", 0, 1) and
            str(subtermo).strip() == "" and str(subtermo) == " "):
      if subtermo in palavras_utilizadas.keys():
        palavras_utilizadas[subtermo] += 1
      else:
        palavras_utilizadas[subtermo] = 1

palavras_utilizadas = sorted(palavras_utilizadas.items(), key=lambda x:x[1])

dados = pd.DataFrame(palavras_utilizadas)
display(dados)






