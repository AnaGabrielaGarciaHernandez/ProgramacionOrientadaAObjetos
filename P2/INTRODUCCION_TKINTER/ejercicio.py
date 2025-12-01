from tkinter import *

def mostrarContenido():
    mostrarContenido=txt_comentario.get("1.0",END).strip()
    resultado.config(text=f"Comentario: {mostrarContenido}")


ventana=Tk() 
ventana.title("Text")
ventana.geometry("800x600")

label_comentario=Label(ventana,text="Escriba su comentario: ")
label_comentario.pack()

txt_comentario=Text(ventana,width=40,height=5)
txt_comentario.pack()

boton=Button(ventana,text="Mostrar Contenido",command=mostrarContenido)
boton.pack()

resultado=Label(ventana,text="")
resultado.pack()

ventana.mainloop()
