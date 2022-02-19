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
janela.mainloop()
