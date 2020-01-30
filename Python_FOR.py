# comando FOR
# A logica sera: para <variável> de <valor-inicial> ate <valor-limite> [passo <incremento>] faca:
#   <seqüência-de-comandos>

#usando range() cria uma lista com exetenção predefinida
# range(valor inicial, valor limite)obs extenção
# range(valor inicial, valor limite, avanço) obs: extenção

for cont in range(0,5):
    print("teste")
    
    
#usando vetor[], onde i recebera uma valor baseado na quantidade de intens no vetor, não nos valores

for i in [1,0,3,4,5]:
  print("teste1")
    
#usando lens() que conta a quantidade de caracteres em uma string
teste="textos"
for cont in range(len(teste)):
    print("teste")
    
#definindo a quantidade de vezes  de execucao'''
r = int (input("quantidade de repeticao:  "))
for i in range (r):
    a = int (input("digite valor de A:   "))
    b = int (input("digite valor de B:   "))
    c = a + b
    print ("resultado:  ",c)
    
# outro exemplo, fazendo com que a variavel i mude de valor '''
for i in range (0,5):
    print(i)
    
#outro exemplo, fazendo com que a variavel i mude de valor com vetor'''
nomes = ['Pedro', 'João', 'Leticia']
for n in nomes:
    print(n)
    
#Loop usando uma string como contador, se repetira conforme cada letra'''
palavra =input("digite uma palavra:  ")
for letra in palavra:
    print(letra)
    
