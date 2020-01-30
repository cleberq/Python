#MATRIZ
#Sua leitura e preeenchimente deve -se ser indicad pela LINHA depois COLUNA
print("Exibindo Matriz em uma unica Linha")
matriz =[[10,20,30],
        [40,50,60],
        [70,80,90]]
print(matriz)

#usa-se o for para inprimir linha a linha
print()
print("Exibindo Matriz linha por linha")
for i in range(3):    
    print(matriz[i])
    
#inserindo dados em matrizes, em colunas definidas
print()
print("inserindo dados")
matriz [0] [0] = 1111
matriz [1] [1] = 1111
matriz [2] [2] = 1111
for i in range(3):    
    print(matriz[i])

#inserindo dados em matrizes: preenchendo toda matriz
'''print()
print("preenchendo toda matriz")
for i in range(3):
    for j in range(3):
       print ("insira o valore da linha:",i,"   coluna:",j)
       matriz [i] [j] = int(input("valor: "))       
for i in range(3):
      print(matriz[i])
'''
#Criando uma Matriz vazia
'''linhas, colunas = 3,3;
matrizB = [[0 for x in range(linhas)] for y in range(colunas)]
for i in range(3):
    for j in range(3):
       print ("insira o valore da linha:",i,"   coluna:",j)
       matrizB [i] [j] = int(input("valor: "))       
for i in range(3):
      print(matrizB[i])          
 '''     
    
matrizB = [[1]2]
for i in range(3):
      print(matrizB[i]) 


