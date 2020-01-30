'''SQLITE'''
#SQLite3 é um modulo do python que da acesso ao banco de dados sqlite3 e
#esse banco de dados é utilizado para testes e pequenos aplicativos
import sqlite3
#criando as variaveis
varpath = r'c:\Sqlite\aula' # caminho usando o atributo r para criar a pasta
varconx = sqlite3.connect(varpath+r'\testing.db')# dentro da pasta em path criar o arquivo testing se não tiver ele cria
print(varpath)

#Criando tabela
c = varconx.cursor() # variavel para guardar a classe cursor de banco de dados para conexao
'''
def create_table():
    #foi usado a  \ barra para quebra de linha
    c.execute('CREATE TABLE dados (id int, valor real, nome text, enderco text,\
              total real)')
create_table()
'''
    
#inserindo dados
'''
def inserirDados():
    c.execute("INSERT INTO dados VALUES(1, 50 , 'cleber', 'rua alpes', 38)")
    c.execute("INSERT INTO dados VALUES(2, 48 , 'cleber', 'rua alpes', 34)")
    c.execute("INSERT INTO dados VALUES(3, 50 , 'cleber', 'rua alpes', 32)")
    c.execute("INSERT INTO dados VALUES(4, 50 , 'cleber', 'rua alpes', 388)")
    varconx.commit()
inserirDados()    
'''  
#Busacando dados select
sql = 'SELECT * FROM dados WHERE nome = ?'
def ler_dados(valorbusca):
    for row in c.execute(sql, (valorbusca,)):
        print(row)        
ler_dados('cleber')
        
