
# ================= SERIES =====================================

import pandas as pd
from pandas import Series
'''
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
#==================== DATA FRAMES ====================================

import pandas as pd
from pandas import DataFrame

# Usando informacoes de um dicionario como Dataset(conjunto de dados)
data = {'Estado': ['Santa Catarina', 'Paraná', 'Goiás', 'Bahia', 'Minas Gerais'], 
        'Ano': [2002, 2003, 2004, 2005, 2006], 
        'População': [1.5, 1.7, 3.6, 2.4, 2.9]}
vframe = DataFrame(data)
print(vframe)

# classificar colunas
print(DataFrame(data, columns=['Ano', 'Estado', 'População']))

#imprimindo O Data Frame em partes
print(vframe[:2]) #linhas com indice 
print(vframe.values)#todos valores sem o nome das colunas
print(vframe['Ano']) #uma coluna com o indice
print(vframe.Estado) #uma coluna com o indice
print(vframe[['Estado','População']])#mais de uma coluna com indice


    
# Criando outro dataframe com os mesmo dados anteriores mas adicionando uma coluna
'''
frame2 = DataFrame(data, columns = ['Ano', 'Estado', 'População', 'Débito'], index = ['um', 'dois', 'três', 'quatro', 'cinco'])
print(frame2)
print('-----------------------------------')
'''

# Imprimindo apenas uma coluna do Dataframe
'''
print(frame2['Estado'])
print(frame2.Ano)#o nome da coluna tem de ser identico inclusive tamanho da letra
print(frame2[:2])
'''

#conhecendo o tipo de dados das colunas
'''
print(frame2.dtypes)
'''

#Localizando Registros Dentro do Dataframe
'''
print(frame2.loc['dois'])#pesquisando pelo NOME do indice
print('-----------------------------------')
print(frame2.iloc[2])#pesquisando pelo indice (lembrando que comeca por zero)

#Para imprimir uma linha específica, temos 2 metodos no pandas
#loc - Ele só recebe rótulo, ou seja, nome da coluna ou Recursos
#Como usar para linha específica loc
df.loc[row,column]
#Para a primeira linha e todas as colunas
df.loc[0,:]
#Para a primeira linha e alguma coluna específica
df.loc[0,'column_name']


#iloc - Aqui eu represento número inteiro, na verdade número da linha
#Para a primeira linha e todas as colunas
df.iloc[0,:]
Para a primeira linha e alguma coluna específica, ou seja, as três primeiras colunas

df.iloc[0,0:3]


ix - É uma mistura de rótulo e número inteiro




#usando  as Colunas como Índices
print(frame.set_index('Estado'))
#
#Converter DataFrame em SCV pra poseteriormente salva-lo como outro arquivo
import sys
output= frame
output.to_csv(sys.stdout, sep = '|')
print('-----------------')

## Criando um array a partir da data
dates = pd.date_range('20180101', periods = 10)
print(dates)
print('-----------------')

# quick data summary
print(frame.describe())
print('-----------------')

# Merge de Dataframes
left = pd.DataFrame({'chave': ['chave1', 'chave2'], 'coluna1': [1, 2]})
print(left)
right = pd.DataFrame({'chave': ['chave1', 'chave2'], 'coluna2': [4, 5]})
print('--------------')
print(right)
print('--------------')
print(pd.merge(left, right, on='chave'))

# Usando métodos/funcoes de outros modulos ou criados - para aplicar uma funcao ao data frame
#use o metodo .apply(nome da função)
def mult2(arg):
    valor = arg*2
    return valor

outFrame = frame['População'].apply(mult2)
# teste Frames = DataFrame(InputCSV_TB, columns = ['admit','gre','gpa',var])
print(outFrame)

# Adicionando um elemento ao Dataframe
data = {'Estado': 'Sao Paulo', 
        'Ano': 2019, 
        'População': 4.1}
outframe= frame.append(data, ignore_index=True)
print(outframe)
'''
