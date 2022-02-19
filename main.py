from tkinter import Tk, ttk
from tkinter import *
from turtle import width

""" CORES """
cor0 = "#FFF" # white
cor1 = "#333" # black
cor2 = "#38576b" # dark blue

""" CONFIGURAÇÃO DA JANELA """
janela = Tk()
janela.geometry("400x420")
janela.title("Cconversor")
janela.configure(bg=cor0)
style = ttk.Style(janela)
style.theme_use("clam")
janela.resizable(width=False, height=False)
janela.mainloop()