'''
Sintaxe do modulo open arquivos
'''
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
''' ========= ===============================================================
    metodo     modo de abertura de arquivo(deve sempre ser especificado)
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
   ========= =============================================================== '''

#
'''TRABALHANDO COM ARQUIVOS CSV'''
#
#
#
##### Usando funcoes built in() ############################################
##### modulo io
##### problema não é possivel editar um iten especifico ####################
#
#
# Abrir/Ler
'''
DataSet = open('//192.168.1.254/lab/- Monitor/PYTHON/salarios.csv', 'r') #OBSERVE QUE DEVE SE UTILIZADO A BARRA / AO INVES DE \ 
Ler = DataSet.read() 
LerLinhas = Ler.split('\n')#funcção \n que assemelha ao enter do teclado
print(type(DataSet))
print(LerLinhas)
print(Ler.title())
'''


# EDITAR/SALVAR
# Acrescenta
'''
DataSet = open('//192.168.1.254/lab/- Monitor/PYTHON/salarios.csv', 'a')
Edit = DataSet.write('\n"moreira, Cleberson",analista, CPD Paulista, $2.000,00')
DataSet.close()#fechar a a conexao e salvar o arquivo
'''
# Altera
'''
não sei como se faz ainda
'''


#Ler
'''
DataSet = open('//192.168.1.254/lab/- Monitor/PYTHON/salarios.csv', 'r')  
Ler = DataSet.read() 
LerLinhas = Ler.split('\n')
print(type(DataSet))
print(LerLinhas)
print(Ler.title())
print(DataSet.seek(4,1))
print(Ler.title())
print(type(Ler))
'''      




################ Usando Modulo CSV ########################################
######## problema não soluciona linhas em branco ##########################
import csv

# Abrir /Ler
'''
with open('//192.168.1.254/lab/- Monitor/PYTHON/salarios.csv','r') as DataSet:
    Leitor = csv.reader(DataSet)
    
    #exibir todos itens
    print(list(Leitor))
    
    #exibir Todos itens organizado
    for x in Leitor:
        print(x)
    #exibir um item especifico    
    Ler = list(Leitor)
    print(Ler[2][3])

    #exibir a partir de um ponto
    for x in Ler[1:]:
        print (x)
'''
def menu():
    menu = int(input('O que deseja fazer  : 1- criar / 2-Editar / 3- Ler / 4- fechar:  '))
    return menu

option=menu()
while option != 4:
    if option == 1 :
    # Editar/Alterar todos valores(excluido todos itens anteriores
        with open('//192.168.1.254/lab/- Monitor/PYTHON/salarios.csv', 'w') as DataSet:
            Edit = csv.writer(DataSet)
            Edit.writerow(('cleberson','Suport io','Paulista','$1500.00'))
            Edit.writerow(('cleberson','Suport 2','Paulista','$1500.00'))
            option=menu()
               

    elif option == 2:    
    # Editar/Alterar iten especifico
        Abrir = open('//192.168.1.254/lab/- Monitor/PYTHON/salarios.csv', 'r')
        with Abrir :
            Abrir_List = list(csv.reader(Abrir))
            #print('antes da edicao:',Abrir_List)
            Abrir_List[0][1]='Suport 01'
            Text = ['cleber','Suport3','CPD','$2000.00']
            Abrir_List.append(Text)
            #print('depos da edicao:  ', Abrir_List)

        Edit = open('//192.168.1.254/lab/- Monitor/PYTHON/salarios.csv', 'w')
        with Edit :
            writer = csv.writer(Edit)
            writer.writerows(Abrir_List)
            option=menu()
       
    else :        
    #Ler
        with open('//192.168.1.254/lab/- Monitor/PYTHON/salarios.csv', 'r', encoding='utf8', newline = '\r\n') as DataSet:
                #codigo acima remove linhas em branco   
            Leitor = csv.reader(DataSet)
            for x in Leitor :
                print(x)
        # aqui sai linhas em branco mesmo assim    
            option=menu() 
