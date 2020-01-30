#############
## TRABALHANDO COM ARQUIVOS .JSON
#############
#
#
'''criando um dicionario'''
dict = {'nome': 'cleber', 'Rua':'alpes','logradouro':[34,'colinas','cotia']}
for k, v in dict.items():
    print(k, v)
'''
#
#importando o modulo JSON
import json
#
#convertendo um dicionario para json
json.dumps(dict)
#
#criando arquivo JSON
with open('C:/Users/Adm/Desktop/arquivos/jason1.txt','w') as arquivo:
    arquivo.write(json.dumps(dict))
#Leitura
with open('C:/Users/Adm/Desktop/arquivos/jason1.txt','r') as arquivo:
    texto = arquivo.read()
    data=json.loads(texto)
print(data)
print(data['nome'])
#
#
#Abrindo arquivos da internet-----teste
import ssl
from urllib.request import urlopen
headers = {'User-Agent':'Chrome/75.0.3770.142'}
response = urlopen("https://whattomine.com/coins.json").read().decode('utf-8')
data = json.loads(response)[0]
print('coins: ', data["coins"])
#print('Simbolo:', data['tag'])
print('valorBTC:', data['btc_revenue'])

'''
                                                             
      
                                                             
                                                             
