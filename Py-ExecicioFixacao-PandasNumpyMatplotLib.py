# exercicio de fixacao modulo 8

'''
    Usar o Pandas para dividir o arquivo cvm.csv em 2 com dados patrimonio e lucroliquido
    Usar Numpy para adicionar uma coluna media
    Usar Matplot Lib para gerar grafico para cada ume e mostrarar ambos em paralelo
'''

import numpy as np
import pandas as pd
import matplotlib as mtp
arq = ("C:/Users/Administrador.unip-PC/downloads/dre_cia_aberta_2019/dre_cia_aberta_con_2019.csv")
dataframe = pd.read_csv(arq,encoding ='IBM860')#erro ao decodificar em utf-8 então tive que colocar na lingua protugesa ibm860
print(dataframe.head())
    
