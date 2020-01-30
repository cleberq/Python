#conexao Cliente 
from socket import *

#dados do cliente para conexao com servidor

serverHost='127.0.0.1'
serverPort= 11000
mensagem = [b'Ola dem vindo !']

#criar objeto socket e conectar com servidor
objconex = socket(AF_INET, SOCK_STREAM)
objconex.connect((serverHost,serverPort))#conect para acessar o servidor

for linha in mensagem:#percorera as linhas da variavel mensagem
    objconex.send(linha)
    #Resposata do servidor
    data = objconex.recv(1024)
    print('Cliente recebeu')
objconex.close()    

