''' DIFERENCA ENTRE CODIGO SIMPLES, FOR E FUNCAO MAP'''

#Codigo Simples
''' não consigo aplicar o calculo em todos itens da lista
#valorReal = [250, 20, 10, 100]
valorReal = 250
dolar = int(input('valor do dolar atual:  '))
euro = int(input('valor do euro atual:  '))
vdolar = valorReal / dolar
veuro = valorReal / euro
print('valor em Dolar',vdolar, '\n','valor em euro', veuro)
'''

# Usando Funcao
'''
Não consigo aplicar a função em todos itens da lista
Porem a função é vista por todo programa
valorReal = [250, 20, 10, 100]

valorReal = 250
def dolar(valorReal):
    dolar = int(input('valor do dolar atual:  '))
    return valorReal / dolar

def euro(valorReal):
    euro = int(input('valor do euro atual:  '))
    return valorReal / euro
print('valor do dolar:  ',dolar(valorReal))
'''
# Usando FOR
'''
valorReal = [10, 20, 30, 40,50]
uss = int(input('valor do dolar atual:  '))
eu = int(input('valor do euro atual:  '))
def dolar(valorReal):
    return valorReal /uss

def euro(valorReal):
    return valorReal /eu

print('---------------------------')
print('valor em reais:  ',valorReal)
for i in valorReal: #para nao dar erro de fora de index chamar funcao pelo contador
       print('valor em dolar: ' ,dolar(i))#chamando a funcao pelo contador que tera o valor da variavel
    
print('---------------------------')
print('valor em reais:  ',valorReal)
for i in range(4):   
        print('valor em euro:  ',euro(valorReal[i]))

'''
#Usando Map
'''
valorReal = [10, 20, 30, 40,50]
uss = int(input('valor do dolar atual:  '))
eu = int(input('valor do euro atual:  '))

def dolar(valorD):
    return valorD /uss
def euro(valorE):
    return valorE /eu

print('---------------------------')
print('valor em reais:  ',valorReal)
print('valor em dolar:  ',map(dolar,valorReal)) 
print('---------------------------')
print('valor em reais:  ',valorReal)
print('valor em euro:  ',map(euro,valorReal))
'''
#Usando ListComprehension

uss = int(input('valor do dolar atual:  '))
eu = int(input('valor do euro atual:  '))

def dolar(valorD):
    return valorD /uss
def euro(valorE):
    return valorE /eu

valorReal = [10, 20, 30, 40, 50]
result=[(dolar(i)) for i in valorReal]
print('---------------------------')
print('valor em reais:  ',valorReal)
print('valor em dolar: ',result)


