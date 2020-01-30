'''USANDO MUDOLO os PARA arquvos.TXT'''
#
text = "Bussiness inteligence é mais legal que Ciencia de dados \n"
text = text +"porque é mais dinamico e visual \n"
text += "por isso tenho que entender de dashboard \n"
print(text)
import os #pacote de funcoes relacionadas ao sistema operacional(OS)
#
#Criando arquivo
file = open(os.path.join("C:/Users/Adm/Desktop/arquivos/cientista2.txt"),"w")
#
#Escrevendo dentro do arquivo.txt
for palavra in text.split(): #esse spplit vazio puxara as palavra nos espaços em branco
    file.write(palavra+'___')
file.close()
#lendo arquivo.txt
file = open(os.path.join("C:/Users/Adm/Desktop/arquivos/cientista2.txt"),"r")
conteudo = file.read()
file.close()
print(conteudo)
