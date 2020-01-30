'''
CLASSE TIME()

#primeiro deve-se importar a classe time
#Essa clase é um vetor, que em sua lista traz: semana,mes,dia,hora,min,seg,ano

import time

#em seguida construir o codigo
#comando time.asctime() traz a data e hora exemplo: Fri Jun 21 08:26:57 2019
t = time.localtime()

#para ver a estrutura
print (time.localtime())

#chamando uma posição
print (t[1])

#Comando sleep() execulta uma pausa pre definida
print (time.asctime())
print("pausa 5 segundos")
time.sleep(5)
print (time.asctime())

'''

'''classe WINSOUND'''
#winsound.Beep(frequencia hz,segundos em milisegundos)
#O arquivo deve-ser .wav e estar dentro da mesma pasta onde esta o codugo python
import winsound
winsound.Beep(300,2000)
winsound.PlaySound('music.wav',winsound.SND_FILENAME)
#para adicionar outra função pode acrescentala usando o PIP | ou MAIS +
#No exemplo abaixo eu quero que ele fique em loop
winsound.PlaySound('music.wav',winsound.SND_FILENAME|winsound.SND_LOOP+winsound.SND_ASYNC)
print('usando async para deixar como musica de fundo enquando o restante do programa funciona')
