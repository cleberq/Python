import pandas as pd
#import urllib as url
import urllib.request
from bs4 import BeautifulSoup
# Aqui eu trago todo codigo do site
#site = url.request.urlopen('http://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/empresas-listadas.htm?codigo=9512')

#Aqui eu procuro tabelas para trazer
#df = pd.read_html('http://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/empresas-listadas.htm?codigo=9512')

with urllib.request.urlopen('http://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/empresas-listadas.htm?codigo=9512') as url:
    page = url.read()
soup = BeautifulSoup(page, "html.parser")
tb = soup.find_all("table")
print(tb)
df = pd.read_html(str(tb))
print(df)