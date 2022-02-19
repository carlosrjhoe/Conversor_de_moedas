from tkinter import Tk, ttk
from tkinter import *

from numpy import place

""" IMPORTANDO BIBLIOTECAS EXTERNAS """
from PIL import Image, ImageTk, ImageOps, ImageDraw

""" CORES """

cor0 = "#FFFFFF" # white
cor1 = "#333333" # black
cor2 = "#38576b" # dark blue

""" CONFIGURAÇÃO DA JANELA """

janela = Tk()
janela.geometry('300x320')
janela.title('Conversor')
janela.configure(bg=cor0)

style = ttk.Style(janela)
style.theme_use("clam")
janela.resizable(width=False, height=False)

""" DIVISÃO DA JANELA """

frame_superior = Frame(janela, width=300, height=60, padx=0, pady=0, bg=cor2, relief='flat')
frame_superior.grid(row=0, column=0, columnspan=2)

frame_inferior = Frame(janela, width=300, height=260, padx=0, pady=5, bg=cor0, relief='flat')
frame_inferior.grid(row=1, column=0, sticky=NSEW)

""" CONFIGURANDO FRAME_SUPERIOR """

icon = Image.open('./imagem/icons8-money-64.png')
icon = icon.resize((40, 40), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)
app_nome = Label(frame_superior, image=icon, compound=LEFT, text='Conversor de moeda ', height=5, pady=30, padx=13, relief='raised', anchor=CENTER, font=('Arial 16 bold'), bg=cor2, fg=cor0)
app_nome.place(x=0, y=0)

""" CONFIGURANDO FRAME_INFERIOR """

app_resultado = Label(frame_inferior, width=16, height=2, relief='solid', anchor=CENTER, font=('Ivi 15 bold'), bg=cor0, fg=cor1)
app_resultado.place(x=50, y=10)

""" LISTA DE MOEDAS """
moeda = ['AOA', 'BRL', 'EUR', 'USD']

app_DE = Label(frame_inferior, text='De:', width=12, height=1, relief='flat', anchor=NW, font=('Ivi 10 bold'), bg=cor0, fg=cor1)
app_DE.place(x=48, y=90)
combo_DE = ttk.Combobox(frame_inferior, width=8, justify=CENTER, font=('Ivi 12 bold'))
combo_DE.place(x=50, y=115)
combo_DE['values'] = (moeda)

app_PARA = Label(frame_inferior, text='Para:', width=12, height=1, relief='flat', anchor=NW, font=('Ivi 10 bold'), bg=cor0, fg=cor1)
app_PARA.place(x=158, y=90)
combo_PARA = ttk.Combobox(frame_inferior, width=8, justify=CENTER, font=('Ivi 12 bold'))
combo_PARA.place(x=160, y=115)
combo_PARA['values'] = (moeda)

valor = Entry(frame_inferior, width=22, justify=CENTER, font=('Ivi 12 bold'), relief=SOLID)
valor.place(x=50, y=155)
janela.mainloop()
