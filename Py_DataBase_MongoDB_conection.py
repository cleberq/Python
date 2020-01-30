#importando pymongo
from pymongo import MongoClient
conx = MongoClient('localhost', 27017)
'''ou conx = MongoClient(), quando o banco esta na mesma maquina'''
# Criar banco de dados uma instancia de conx
dbx = conx.cadastrodbx

# Criando uma colletcion (grupos de documentos)
''' coll = dbx.cadastrodbx'''
coll = dbx.posts
post1 = {"codigo": "ID-9987725",
        "prod_name": "Geladeira",
        "marcas": ["brastemp", "consul", "elecrolux"],
        "data_cadastro": '27/08/2019'}
post_id = coll.insert_one(post1)

for post in coll.find():
    print(post)
