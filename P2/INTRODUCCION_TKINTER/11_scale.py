from tkinter import *

ventana=Tk()
ventana.title("Scale")
ventana.geometry("500x500")

def mostrarValor():
    respuesta.config(text=f"Valor seleccionado por el usuario {valor.get()}")

valor=IntVar()
escala=Scale(ventana,from_=0,to=100,orient="horizontal",variable=valor)
escala.pack()

btn_mostrar=Button(ventana,text="Mostrar todo",command=mostrarValor)
btn_mostrar.pack()

respuesta=Label(ventana,text="")
respuesta.pack()

ventana.mainloop()