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

2 DICIEMBRE
    1) INTERFACES
        1.1 insertar_camionetas()
        1.2 consultar_camionetas()
        1.3 cambiar_camionetas()
        1.4 borrar_camionetas()

        2.1 insertar_camiones()
        2.2 consultar_camiones()
        2.3 cambiar_camiones()
        2.4 borrar_camiones()

    ENTREGABLES
        Interaccion con todas las interfaces
        Nombre del Commit: "commit_02_12_25"
    
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

