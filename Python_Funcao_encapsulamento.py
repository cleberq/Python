#Funcao em phyton
'''def nomeEscolhido(_lista de parâmetros_)
  suite do corpo da funcao
'''
# Funcao sem parametro
'''
def escreveCabecalhoProva ():
    print("Avaliaçao da Disciplina")
    print("Aluno:  ")
    print("Data:   ")
    
escreveCabecalhoProva ()
escreveCabecalhoProva ()
'''
# Funcao com parametro
'''
def escreveCabecalhoProva (nome, data):
    print("Avaliaçao da Disciplina")
    print("Aluno:  ", nome)
    print("Data:   ", data)
    
escreveCabecalhoProva ("joao ", "10/10/2017")
escreveCabecalhoProva ("Maria", "10/10/2017")
'''
# Função com retorno
'''
def realizaSoma (valor1, valor2):
    soma = valor1 + valor2
    return soma
    
# a variavel resultado ganha valor de soma
resultado = realizaSoma(10, 20)
print(resultado)

# a variavel resultado sera = o valor numerico passado mas o antigo valor da variavel resultado
resultado = realizaSoma (300,resultado)
print(resultado)

'''












