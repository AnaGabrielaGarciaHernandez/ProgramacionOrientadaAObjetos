from tkinter import *

def hazClick():
    label_titulo.config(
        text="Poo con Python",
        bg="green",#color de fondo
        fg="red",#color d eletra
        width=50,#ancho
        height=4,#altura
        font=("Arial",30,"bold"),#tipo de letra
        border=2,#borde
        relief=GROOVE #relieve
)
    
def regresarClick():
    label_titulo.config(
        text="Bienvenidos a Tkinter",
        bg="lightblue",#color de fondo
        fg="darkblue",#color d eletra
        width=50,#ancho
        height=4,#altura
        font=("Helvetica",30,"italic"),#tipo de letra
        border=2,#borde
        relief=GROOVE#relieve
)

ventana=Tk() 
ventana.title("Personalizar Widgets")
ventana.geometry("500x500")

label_titulo=Label(ventana, text="Bienvenidos a Tkinter")
label_titulo.config(
    bg="lightblue",#color de fondo
    fg="darkblue",#color d eletra
    width=50,#ancho
    height=4,#altura
    font=("Helvetica",30,"italic"),#tipo de letra
    border=2,#borde
    relief=GROOVE#relieve
)
label_titulo.pack(pady=50)

boton_click=Button(ventana,text="Haz clic aqui",command=hazClick)
boton_click.config(
    fg="white",
    activeforeground="yellow",
    width=15,
    font=("Arial",20,"bold")
)

boton_click.pack(pady=5)

boton_regresar=Button(ventana,text="Regresa clic aqui",command=regresarClick)
boton_regresar.config(
    fg="black",
    activeforeground="red",
    width=15,
    font=("Arial",20,"bold")
)
boton_regresar.pack(pady=5)

ventana.mainloop()
