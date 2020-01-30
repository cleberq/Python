# Trabalhando com Vetores/Listas atraves do objeto list
# Com o Objeto list é mais facil trabalhar com listas, pois possui diversos recursos

# Metodo para inserir dados
list =[4,3,2,1]
print(list)
list.append(input("insira novo valor: "))
list.append(input("insira novo valor: "))
print(list)

# Herdando metodos do objeto list
itens =['laranja','maca','banana']
print(itens)
itens.append(input("insira novo valor: "))
itens.append(input("insira novo valor: "))
print(itens)

#Metodo para contar quantidade de vezes que um valor aparece 
itens =['laranja','maca','banana','maca']
print(itens)
print(itens.count('maca'))

# exibir valor em uma posicao
itens =['laranja','maca','banana','maca']
print(itens)
print(itens.pop(3))

# remover um item
itens =['laranja','maca','banana','maca']
print(itens)
print(itens.remove('maca'))
print(itens)


#classificar em ordem alfabetica e numerica
itens =['laranja','maca','banana','maca']
valorKilo=[1.98, 2.00,4.00,2.00]
print(itens)
print(valorKilo)
itens.sort()
valorKilo.sort()
print(itens)
print(valorKilo)

# inserir dados em determinada posicao
itens =['laranja','maca','banana','maca']
print(itens)
itens.insert(1,'uva')
print(itens)


