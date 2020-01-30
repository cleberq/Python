#conexao Servidor 
from socket import *
meuhost='127.0.0.1'
minhaport= 11000
objconex = socket(AF_INET, SOCK_STREAM)#Usando conexão do tipo TCP, IP
objconex.bind((meuhost,minhaport))#bind para informar o host e porta ele exige 2 aspas
objconex.listen(5)#limitando o numero de conexões
#testando conexão com o servidor
while True:
    conexao, end = objconex.accept()
    print('o servidor esta conectado por', end)
    while True:
        data = conexao.recv(1024)#enquanto tiver conexao limitar a 1Mb
        if not data: #se não tiver conexao parar while
            break
        conexao.send(b'eco=>' + data)#para mostrar o que esta sendo enviado
    conexao.close()
