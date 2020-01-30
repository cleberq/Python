import urllib.request
import pandas as pd
'''
from bs4 import BeautifulSoup
with urllib.request.urlopen("https://www.fundamentus.com.br/detalhes.php?papel=") as url:
    page = url.read()
soup = BeautifulSoup(page, "html.parser")
tb = soup.find_all("table")
print(tb)
df = pd.read_html(str(tb))
print(df)
'''
#----------Usando Pandas para parse----------------
#não funciona
'''
lk = pd.read_html("https://www.fundamentus.com.br/detalhes.php?papel=", attrs={'id':'test1'}) 
lk2 = pd.read_html("https://www.fundamentus.com.br/detalhes.php?papel=",attrs = {'class':"par"})
'''
#gera uma list
lk = pd.read_html("https://www.fundamentus.com.br/detalhes.php?papel=")
#print(type(lk))
print(lk)
lst=list(lk)
print(lst)
#df = pd.DataFrame(lk, index='Papel')
#sr = pd.Series(df,
#print(df)
#['Papel','Nome Comercial'])