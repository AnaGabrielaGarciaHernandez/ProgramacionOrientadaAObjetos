from tkinter import *
def mensaje(tipo):
    resultado.config(text=f"{tipo}")

ventana=Tk()
ventana.title("Menu")
ventana.geometry("500x500")

menuBar=Menu(ventana)
ventana.config(menu=menuBar)

archivoMenu=Menu(menuBar,tearoff=1)
menuBar.add_cascade(label="Archivo" , menu=archivoMenu)
archivoMenu.add_command(label="Nuevo Archivo",command=lambda: mensaje("Nuevo Archivo"))#Lambda es para poder mandar parametros
archivoMenu.add_command(label="Guardar Archivo",command=lambda: mensaje("Guardar Archivo"))
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir",command=ventana.quit)#Quita todo

edicionMenu=Menu(menuBar,tearoff=1)
menuBar.add_cascade(label="Archivo" , menu=edicionMenu)
edicionMenu.add_command(label="Copiar",command=lambda: mensaje("Copiar Archivo"))#Lambda es para poder mandar parametros
edicionMenu.add_command(label="Recortar",command=lambda: mensaje("Recortar Archivo"))
edicionMenu.add_separator()
edicionMenu.add_command(label="Salir",command=ventana.destroy)#Quita lo que quieras

resultado=Label(ventana,text="")
resultado.pack()

ventana.mainloop()

#Tarea: complementar