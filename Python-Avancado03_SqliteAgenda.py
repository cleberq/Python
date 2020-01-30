import sqlite3, time
varconectar = sqlite3.connect(r'C:\Sqlite\aula\agenda.db')
c = varconectar.cursor()

def criar_db():
    c.execute('CREATE TABLE IF NOT EXISTS cadastro (nome text, telefone varchar, email text, data text)')
try: #tratamento de erro ou seja tenta se erro except
    criar_db()
except:
    print('Erro ao criar o banco de dados')
else:
    print('banco de dados criado com sucesso!!!!!!')
    
'''    
def inserir(n, t, e):
    d = time.strftime('%d/%m/%y')
    c.execute('INSERT INTO cadastro VALUES(?, ?, ?, ?)',(n, t, e, d))
    varconectar.commit()
fc = int (input('1 - Cadastrar \n 2- Pesquisar \n o que vc deseja fazer?'))
if fc ==1:
    try:
        print('Cadastro da agenda')
        time.sleep(2)
        n = str(input('digite nome: '))
        t = str(input('Digite um telefone:  '))
        e = str(input('digite um email:  '))
        inserir(n, t, e)
    except:
        print('Erro ao Cadastrar!')
    else:
        print('Cadastrado com sucesso!')
elif fc ==2 :
    print('Aguarde!')
else:
    print('...')
'''    
    
        
        
              
              
              
    