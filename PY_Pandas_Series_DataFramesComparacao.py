# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:55:03 2019

@author: Administrador
"""

import pandas as pd
from pandas import Series

# Criando uma série e especificando os índices
Obj1 = Series([67, 78, -56, 13], index = ['a', 'b', 'c', 'd'])
print('series','\n',Obj1)



var = {'valora':10,'valorB':20, 'ValorC':30}
print('\n ----dicionario--- ')
print(var)


obj2 = Series(var)
print('\n ----series----')
print(obj2)


df=pd.DataFrame(var, index=['a'])
print('\n ---- DataFrame ----')
print(df)


data = {'Valor A': [10,20,30,40],'Valor B': [100, 200, 300, 4000], 
        }
print('\n ---- DataFrame ----')
frame = pd.DataFrame(data)
print(frame)
