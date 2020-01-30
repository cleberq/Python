#### Exportando Arquivos #######

###### Exportando Excel ########
import os
from pandas import DataFrame
# Gerando um arquivo excel a partir de um Dataframe
data = {'Estado': ['Santa Catarina', 'Paraná', 'Goiás', 'Bahia', 'Minas Gerais'],
        'Ano': [2002, 2003, 2004, 2005, 2006],
        'População': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
print(frame)
frame.to_excel('//192.168.1.254/softwares/cleber/PYTHON/export1.xlsx', sheet_name='Sheet1')
