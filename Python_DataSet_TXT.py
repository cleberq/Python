#TRABALHANDO COM ARQUIVOS
#
'''ABRINDO ARQUIVO PARA LEITURA'''
arq = open('//192.168.1.254/lab/- Monitor/PYTHON/CursoDSA_PythonParaDataScience/PythonFundamentos-master/Cap04/Notebooks/arquivos/arquivo1.txt', 'r')
print(arq.read()) #OBSERVE QUE DEVE SE UTILIZADO A BARRA / AO INVES DE \ INDICANDO O DIRETORIO
#
#
'''IR PARA UM PONTO DO ARQUVIO'''
print(arq.seek(2))
print(arq.read())#LER A PARTIR DA POSIÇÃO 2
#
#
'''Abrir para gravacao'''
#substituir o conteudo do arquivo
arq2 = open('//192.168.1.254/lab/- Monitor/PYTHON/CursoDSA_PythonParaDataScience/PythonFundamentos-master/Cap04/Notebooks/arquivos/arquivo1.txt', 'w')
arq2.write("testando gravacao")
arq2.close()
arq2 = open('//192.168.1.254/lab/- Monitor/PYTHON/CursoDSA_PythonParaDataScience/PythonFundamentos-master/Cap04/Notebooks/arquivos/arquivo1.txt', 'r')
print(arq2.read())
#
#Acrescentar conteudo no arquivo
arq2 = open('//192.168.1.254/lab/- Monitor/PYTHON/CursoDSA_PythonParaDataScience/PythonFundamentos-master/Cap04/Notebooks/arquivos/arquivo1.txt', 'a')
arq2.write(" acrescentando conteudo")
arq2.close()
arq2 = open('//192.168.1.254/lab/- Monitor/PYTHON/CursoDSA_PythonParaDataScience/PythonFundamentos-master/Cap04/Notebooks/arquivos/arquivo1.txt', 'r')
print(arq2.read())
#
#

