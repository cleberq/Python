from tkinter import *
import time

#Tela 
#===============================================================
janela = Tk()
janela.title("Primeira Janela")
janela.geometry("500x500+250+50")#posição da tela Acima/Abaixo/Esquerda/Direita
janela["bg"] = "navy"

#Caixa de Texto
#===============================================================
cxtexto = Entry(janela, width =20)
cxtexto.place(x=170, y=100)#posição da caixa
cxtexto2 = Entry(janela, width =20)
cxtexto2.place(x=170, y=150)#posição da caixa

#Labels
#================================================================
lb = Label(janela, text="Texto na tela", width=65)
lb.place(x=10, y=250)


#Estanciar objeto /criar função: para usar nos botoes
#================================================================
def janela2():
    janela2 = Tk()
    janela2.title("janela 2")
    janela2.geometry("600x200+100+100")#Tamanho(l/A) X posição da tela Acima/Abaixo
    janela2["bg"] = "pink"
    lb2 = Label(janela2, text="BOTAO FUNCIONOU!!", width=65)
    lb2.place(x=10, y=10)
    janela2.mainloop()

#outra Estancia: Chama o processo de encerrar o programa
#==================================================================
def sair():
    janela.destroy()

#Botoes
#================================================================
btn = Button(janela, text="Botão1", width=20, command=janela2)
btn.place(x=155, y=200)
btn2 = Button(janela, text="Encerrar", width=20, command=sair)
btn2.place(x=155, y=300)

#Rodando todo codigo
#================================================================
janela.mainloop()




'''
def bt_oksenha():
    p1=str(passwd.get())
    lb["text"] =str("A senha digitada foi {}".format(p1))


def bt_entrar(passw1=None):
    p1=str(passwd.get())
    p2=str(confpas.get())
    if p1 == p2:
        lb["text"] = str("Login Efetuado com Sucesso")
        time.sleep(5)
        jpas.destroy()
    else:
        lb["text"] = str("Senha incorreta")




