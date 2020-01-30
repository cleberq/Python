import pandas as pd 
#import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show
import easygui
import string as st

xfile = easygui.fileopenbox()
print(xfile)
#print(xfile[62:])verificando posiçao da palavra
indice= xfile.index('-')
print(indice)

# gerou um dataframe correto
xpath = pd.read_excel(xfile, sheet_name='Bal. Patrim.', encoding="utf-8", skiprows=1, index_col=0)
namepath=input('nome da empresa:___     ')
corlinha=input('cor da linha:__')
## gerou uma series
xdf = xpath.loc['Ativo Total']

# funcao
def numx (arg):
    arg = int(arg /10000)
    return arg

## X o indicador e y são os valores 
## convertendo em datetime
dfx = pd.to_datetime(xdf.index)
print(dfx)

dfy = list(map(numx,xdf.values))
print(dfy)

output_file('//192.168.1.254/softwares/cleber/PYTHON/BalancosEmpresas/'+xfile[indice:]+'.html')

##com Bokeh
p = figure(title="Patrimonio Liquido - "+namepath, x_axis_label='Trimestre', y_axis_label='Bilhoes R$', x_axis_type="datetime", plot_width=800, plot_height=350, background_fill_color="#4A92AE")
p.line(dfx,dfy, color=corlinha, legend="Valor R$.", line_width=2)
show(p)

# com matplotlib
'''
plt.plot(dfx,dfy)
plt.show()
'''