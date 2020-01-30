import sqlite3
conx = sqlite3.Connection('C:/Users/Adm/Desktop/Sqlite/mybase2.db')
curx = conx.cursor()
'''comando para criar tabela so habilita quando for usar'''
# curx.execute('create table cadastro (nome string, cel varchar, end varchar)')

'''comando para inserir valores, so habilita quando for usar'''
# curx.execute('insert into cadastro values ("cleber1",46166367,"rua alpes 38")')

'''comando para salvar valores inseridos'''
# conx.commit()

'''comando para exibir tabela'''
curx.execute('select * from cadastro')
dados = curx.fetchall()
for linha in dados:
    print(linha)


