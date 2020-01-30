'''Melhor custo beneficio combustivel'''
vGas= float(input ("valor da Gasolina:  "))
vAlc= float(input ("valor do Alcool:  "))
kmLitroGas=float (input ("KM por Litro na Gasolina:  "))
kmLitroAlc=float (input ("KM por Litro no alcool:  "))

'''valorLitr/KmLitro = Valor por KM)'''
ValorKmGas = vGas / kmLitroGas
ValorKmAlc = vAlc / kmLitroAlc

if ValorKmGas < ValorKmAlc:
   print("abastecer com GAsolina!")
else:
   print("abastecer com Alcool!")
