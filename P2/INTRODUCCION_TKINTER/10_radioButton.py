from tkinter import *
#No recomendable para mas de 4 opciones, normalmente solo en 2, solo se elige una opcion

def mostrarSeleccion():
    respuesta.config(text=f"Opcion seleccionada: {opcion.get()}")

ventana=Tk()
ventana.title("RadioButton")
ventana.geometry("500x500")

opcion=StringVar()
opcion1=Radiobutton(ventana,text="Opcion 1",variable=opcion,value="opcion1")
opcion1.pack()

opcion2=Radiobutton(ventana,text="Opcion 2",variable=opcion,value="opcion2")
opcion2.pack()

opcion3=Radiobutton(ventana,text="Opcion 3",variable=opcion,value="opcion3")
opcion3.pack()

boton=Button(ventana,text="Mostrar Seleccion",command=mostrarSeleccion)
boton.pack()

respuesta=Label(ventana,text="")
respuesta.pack()

ventana.mainloop()