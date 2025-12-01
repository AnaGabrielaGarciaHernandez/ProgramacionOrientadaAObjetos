"""
    Tkinter trabaja a traves de interfaces, es una biblioteca de Python que
    permite crear aplicaciones en python para escritorio
"""

#from tkinter import *

import tkinter as tk

ventana=tk.Tk()
ventana.title("Mi primer App Grafica en Tkinter con Pythhon")
ventana.geometry("800x600")
ventana.resizable(False,False)#que no se modificque el tamaño de la pantalla
ventana.mainloop() #Metodo que permite tener la ventana abierta e interactuar con ella