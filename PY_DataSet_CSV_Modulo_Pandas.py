
#==================== PANDAS ARQUIVOS CSV ====================================
import pandas as pd
from pandas import DataFrame
#Abrir CSV como STR Ler como CSV e convertendo para DF
InputCSV_STR= ('//192.168.1.254/softwares/cleber/PYTHON/binary.csv')
print(type(InputCSV_STR))

Convert = pd.read_csv(InputCSV_STR)
print(type(Convert))
      
Output_DF = DataFrame(Convert)
print(Output_DF.head())
print('-----------------')
'''
#Abrir CSV convertendo para DataFrame
InputCSV_DF = pd.read_csv('//192.168.1.254/lab/- Monitor/PYTHON/binary.csv')
print(type(InputCSV_DF))
print(InputCSV_DF.head())
print('-----------------')
#
# Abrir CSV como DataFrame usando o método read_table (permite usar argumentos)
InputCSV_TB= pd.read_table('//192.168.1.254/lab/- Monitor/PYTHON/binary.csv', sep = ',')
print(type(InputCSV_TB))
print(InputCSV_TB.head())
print('-----------------')

# Alterando o título das colunas
InputCSV_STR2= ('//192.168.1.254/lab/- Monitor/PYTHON/binary.csv')
Output_DF2 = pd.read_csv(InputCSV_STR2, names = ['a', 'b', 'c', 'd'])#isso fara com que o Pandas entenda que a primeira linha são dados e acrescenta o novo titulo
print(Output_DF2.head())
print('-----------------')

#Converter DataFrame em SCV pra poseteriormente salva-lo como outro arquivo
import sys
data = Output_DF
data.to_csv(sys.stdout, sep = '|')
print('-----------------')



'''




