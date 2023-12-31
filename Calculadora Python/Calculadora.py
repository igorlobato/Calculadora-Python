from tkinter import *
from style.Style import *


#Principal
janela = Tk()
janela.title("Calculadora Python")
janela.geometry("235x310")
janela.config(bg=preto)


#Frames
FrameTela = Frame(janela, width=235, height=50, bg=azul)
FrameTela.grid(row=0, column=0)

FrameCorpo = Frame(janela, width=235, height=268)
FrameCorpo.grid(row=1, column=0)


#Label
valorTexto = StringVar()
appLabel = Label(FrameTela, textvariable=valorTexto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg = preto, fg=branco)
appLabel.place(x=0, y=0)

valorTexto.set(str(0.0))

todosValores = ''

#Funções
def entrarValores(event):
    global todosValores
    todosValores += str(event)
    valorTexto.set(todosValores)

def calcular():
    global todosValores
    try:
        resultado = eval(todosValores)
        valorTexto.set(str(resultado))
        todosValores = str(resultado)
    except:
        valorTexto.set("Error")
        todosValores = ""

def limparTela():
    global todosValores
    todosValores = ""
    valorTexto.set("")

#Botões
b1 = Button(FrameCorpo, command=limparTela, text="C", width=11, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=0,y=0)
b2 = Button(FrameCorpo,  command=lambda: entrarValores('%'), text="%", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=118,y=0)
b3 = Button(FrameCorpo, command=lambda: entrarValores('/'),  text="/", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x=177,y=0)

b4 = Button(FrameCorpo, command=lambda: entrarValores('7'),  text="7", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=0,y=52)
b5 = Button(FrameCorpo, command=lambda: entrarValores('8'),  text="8", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=59,y=52)
b6 = Button(FrameCorpo, command=lambda: entrarValores('9'),  text="9", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=118,y=52)
b7 = Button(FrameCorpo, command=lambda: entrarValores('*'),  text="*", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x=177,y=52)

b8 = Button(FrameCorpo, command=lambda: entrarValores('4'),  text="4", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=0,y=104)
b9 = Button(FrameCorpo, command=lambda: entrarValores('5'),  text="5", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=59,y=104)
b10 = Button(FrameCorpo, command=lambda: entrarValores('6'),  text="6", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=118,y=104)
b11 = Button(FrameCorpo, command=lambda: entrarValores('-'),  text="-", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x=177,y=104)

b12 = Button(FrameCorpo, command=lambda: entrarValores('1'),  text="1", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=0,y=156)
b13 = Button(FrameCorpo, command=lambda: entrarValores('2'),  text="2", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x=59,y=156)
b14 = Button(FrameCorpo, command=lambda: entrarValores('3'),  text="3", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x=118,y=156)
b15 = Button(FrameCorpo, command=lambda: entrarValores('+'),  text="+", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b15.place(x=177,y=156)

b16 = Button(FrameCorpo, command=lambda: entrarValores('0'),  text="0", width=11, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b16.place(x=0,y=208)
b17 = Button(FrameCorpo, command=lambda: entrarValores('.'),  text=".", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x=118,y=208)
b18 = Button(FrameCorpo, command=calcular,  text="=", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b18.place(x=177,y=208)






janela.mainloop()