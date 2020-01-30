'''
===== SERIES =====================================

import pandas as pd
from pandas import Series

# Criando uma série e especificando os índices
Obj1 = Series([67, 78, -56, 13], index = ['a', 'b', 'c', 'd'])
print(Obj1)

# alterando valor pelo indice
Obj1['b'] = 79 #alterar valor do indice b
print(Obj1)

# imprimindo valores e indices separados
print(Obj1.values)
print(Obj1.index)

# imprimindo a partir de criterio (slice and dice)
print(Obj1[Obj1 > 3])# posicoes cujo valores maiores que 3

# imprimindo uma posicao

print(Obj1['b'])
# verificando se um indice existe na serie
print('d' in Obj1)

# Criando uma série de dados passando um dicionário como parâmetro
dict = {'Futebol':5200, 'Tenis': 120, 'Natação':698, 'Volleyball':1550}
Obj2 = Series(dict)
print(Obj2)


# Criando uma serie e usando uma lista(vetor) como índice
lista = ['Futebol', 'Tenis', 'Natação', 'Basktetball']
Obj3 = Series(dict, index=lista)
print(Obj3)

'''

'''
==== DATA FRAMES ====================================
'''
import pandas as pd
from pandas import DataFrame
data = {'Estado': ['Santa Catarina', 'Paraná', 'Goiás', 'Bahia', 'Minas Gerais'], 
        'Ano': [2002, 2003, 2004, 2005, 2006], 
        'População': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
print(frame)
    #
    # classificar colunas
print(DataFrame(data, columns=['Ano', 'Estado', 'População']))
    
    # Criando outro dataframe com os mesmo dados anteriores mas adicionando uma coluna
frame2 = DataFrame(data, columns = ['Ano', 'Estado', 'População', 'Débito'], 
                   index = ['um', 'dois', 'três', 'quatro', 'cinco'])
print(frame2)
    
    # Imprimindo apenas uma coluna do Dataframe
print(frame2['Estado'])
print(frame2.Ano)#o nome da coluna tem de ser identico inclusive tamanho da letra
print(frame2[:2])
    
    #conhecendo o tipo de dados das colunas
print(frame2.dtypes)


    #Localizando Registros Dentro do Dataframe
print(frame2.loc['dois'])#pesquisando pelo NOME do indice
print(frame2.iloc[2])#pesquisando pelo indice (lembrando que comeca por zero)

'''deu erto
import pandas as pd
from pandas import DataFrame
fonte = pd.read_json('C:/Users/Administrador.unip-PC/Desktop/coins.json')
frame = DataFrame(fonte, columns = ['Aion','Monero'])
print(frame)



data = {'Estado': ['Santa Catarina', 'Paraná', 'Goiás', 'Bahia', 'Minas Gerais'], 
        'Ano': [2002, 2003, 2004, 2005, 2006], 
        'População': [1.5, 1.7, 3.6, 2.4, 2.9]}
'''



'''


DataFrame(dict, columns=['Coins'])

# Criando outro dataframe com os mesmo dados anteriores mas adicionando uma coluna
frame2 = DataFrame(data, columns = ['Ano', 'Estado', 'População', 'Débito'], 
                   index = ['um', 'dois', 'três', 'quatro', 'cinco'])


# Gerar grafico a apartir de CSV

import pandas as pd

import pandas as pd
file_name= ("C:/Users/Adm/Desktop/arquivos/binary.csv")
df = pd.read_csv(file_name)
print(df.head())






# Gerar grafico a apartir de TXT

import pandas as pd






# Gerar grafico a apartir de JSON

import pandas as pd








# Gerar grafico a apartir de URL





import pandas as pd
'''
