"""
1ERO DICIEMBRE:
    1) Implementacion mvc
    2) POO
    3) INTERFACES:
        3.1 menu_principal()
        3.2 menu_acciones()
        3.3 insertar_autos()
        3.4 consultar_autos()
        3.5 cambiar_autos()
        3.6 borrar_autos()

    ENTREGABLES:
        Estructura del proyecto basado en MVC
        Modulo main
        Interaccion con interfaces
        Nombre del commit: "commit_01_12_25
"""

from view import vista1
from tkinter import *

class App:
    def __init__(self,ventana):
        view=vista1.View(ventana)

if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()

