# Vetores/Listas
# Apos criar o vetor, deve-se chamar a posicao que esta o valor para ele trazer seu conteudo
# A posicao inicial do vetor é 0
'''
vetor=[4,3,2,1]
print(vetor[0])
print(vetor[3])
'''
# Inserindo dados no vetor funcao append()
'''
vetor=[]
vetor.append(input("insira um valor texto: "))
vetor.append(input("insira um valor texto: "))
vetor.append(input("insira um valor texto: "))
vetor.append(input("insira um valor texto: "))
print(vetor[0])
print(vetor[1])
print(vetor[2])
print(vetor[3])
'''

# Utilizando FOR para preencher vetor
'''
vetor=[]
for i in range(0,5):
    vetor.append(input("digite um texto:  "))
print(vetor)
'''
# utilizando Split() funcao que recebe texto o separa(conforme delimitador) e insere os dados em um vetor
valores = input("Digite os valores na mesma linha separado por espacos: ").split()
print(valores)
valores = input("Digite os valores na mesma linha separado por ,: ").split(",")
print(valores)



