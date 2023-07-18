from tkinter import *

#cores
preto = "#1e1f1e"
branco = "#feffff"
azul = "#38576b"
cinza = "#ECEFF1"
laranja = "#FFAB40"

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
appLabel = Label(FrameTela, text='123456789', width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg = preto, fg=branco)
appLabel.place(x=0, y=0)

#Botões
b1 = Button(FrameCorpo, text="C", width=11, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=0,y=0)
b2 = Button(FrameCorpo, text="%", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=118,y=0)
b3 = Button(FrameCorpo, text="/", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x=177,y=0)

b4 = Button(FrameCorpo, text="7", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=0,y=52)
b5 = Button(FrameCorpo, text="8", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=59,y=52)
b6 = Button(FrameCorpo, text="9", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=118,y=52)
b7 = Button(FrameCorpo, text="*", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x=177,y=52)

b8 = Button(FrameCorpo, text="4", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=0,y=104)
b9 = Button(FrameCorpo, text="5", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=59,y=104)
b10 = Button(FrameCorpo, text="6", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=118,y=104)
b11 = Button(FrameCorpo, text="-", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x=177,y=104)

b12 = Button(FrameCorpo, text="1", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=0,y=156)
b13 = Button(FrameCorpo, text="2", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x=59,y=156)
b14 = Button(FrameCorpo, text="3", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x=118,y=156)
b15 = Button(FrameCorpo, text="+", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b15.place(x=177,y=156)

b16 = Button(FrameCorpo, text="0", width=11, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b16.place(x=0,y=208)
b17 = Button(FrameCorpo, text=".", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x=118,y=208)
b18 = Button(FrameCorpo, text="=", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b18.place(x=177,y=208)


#Funções


a =eval('9+8+2')
print(a)





janela.mainloop()