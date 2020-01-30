import pandas as pd 
from bokeh.plotting import figure, output_file, show
from bokeh.transform import factor_cmap
from bokeh.palettes import Spectral6
from bokeh.models import ColumnDataSource
import easygui


'''Abrir Data Set
'''
vpath ='//192.168.1.254/softwares/cleber/Python/DataSets/VendaCarros.xlsx'
#vpath = easygui.fileopenbox() #Exibe janela abrir arquivo, apos abrir o arquivo sra armezando o caminho do mesmo na string
#print(vpath)

'''Local de salvamento
'''
output_file(vpath+'.html')


'''Gerar um dataframe 
'''
v_dframe = pd.read_excel(vpath, sheet_name='VendaCarros', encoding="utf-8", index_col=0)
#print(v_dframe)
#print(v_dframe[:2]) #linhas com indice
#print(v_dframe.values) #todos valores sem o nome das colunas
#print(v_dframe['Fabricante']) #uma coluna com o indice
#print(v_dframe.Estado) #uma coluna com o indice
#print(v_dframe[['Fabricante','Estado']])#mais de uma coluna com indice


'''# Gerar uma series do DataFrame pelo metodo groupby
'''
vseries = v_dframe.groupby('Estado').size()#agrupar e contar as unidades vendidas por ano
print(vseries)


'''# Definindo os indicadores X 
   # Definindo os Valores Y  
'''
dfx = list(map(str,(vseries.index)))
print(type(dfx))
print(dfx)

dfy = list(vseries.values)
print(dfy)

''' #Grafico Geo Map simples 
'''
# versao1
from bokeh.io import show
from bokeh.models import LogColorMapper
from bokeh.palettes import Viridis6 as palette
from bokeh.plotting import figure

from bokeh.sampledata.world_cities import data as counties
from bokeh.sampledata.unemployment import data as unemployment

palette.reverse()

counties = {
    code: county for code, county in counties.items() if county["state"] == "tx"
}

county_xs = [county["lons"] for county in counties.values()]
county_ys = [county["lats"] for county in counties.values()]

county_names = [county['name'] for county in counties.values()]
county_rates = [unemployment[county_id] for county_id in counties]
color_mapper = LogColorMapper(palette=palette)

data=dict(
    x=county_xs,
    y=county_ys,
    name=county_names,
    rate=county_rates,
)

TOOLS = "pan,wheel_zoom,reset,hover,save"

p = figure(
    title="Texas Unemployment, 2009", tools=TOOLS,
    x_axis_location=None, y_axis_location=None,
    tooltips=[
        ("Name", "@name"), ("Unemployment rate)", "@rate%"), ("(Long, Lat)", "($x, $y)")
    ])
p.grid.grid_line_color = None
p.hover.point_policy = "follow_mouse"

p.patches('x', 'y', source=data,
          fill_color={'field': 'rate', 'transform': color_mapper},
          fill_alpha=0.7, line_color="white", line_width=0.5)

show(p)