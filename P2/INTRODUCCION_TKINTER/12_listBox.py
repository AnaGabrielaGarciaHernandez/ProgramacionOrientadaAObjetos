from tkinter import *

def mostrarSeleccion():
    valor=lista.get(lista.curselection())
    respuesta.config(text=f"Seleccionaste: {valor}")

ventana=Tk()
ventana.title("ListBox")
ventana.geometry("500x500")


lista=Listbox(ventana,width=50,height=5,selectmode="single")
lista.pack()

opciones=["Azul","Rojo","Negro","Amarillo"]
for i in opciones:
    lista.insert(END,i)


btn_mostar=Button(ventana,text="Mostrar Seleccion del Usuario",command=mostrarSeleccion)
btn_mostar.pack()

respuesta=Label(ventana,text="")
respuesta.pack()

ventana.mainloop()