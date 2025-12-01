from tkinter import *

def mostrarEstado():
    if opcion.get()==1:
        resultado.config(text="Se activaron las notificaicones")
    else:
        resultado.config(text="Se desactivaron las notificaciones")
    

ventana=Tk()
ventana.title("CheckButton")
ventana.geometry("500x500")

opcion=IntVar()
check_notificacion=Checkbutton(ventana,text="¿Desea recibir notificaciones?",variable=opcion,onvalue=1,offvalue=0)
check_notificacion.pack()

btn_confirmar=Button(ventana,text="Confirmar", command=mostrarEstado)
btn_confirmar.pack()

resultado=Label(ventana,text="")
resultado.pack()



ventana.mainloop()
