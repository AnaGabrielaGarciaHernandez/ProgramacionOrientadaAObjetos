from tkinter import messagebox
from model import usuario,nota
from view import vista1

class Controlador:
    @staticmethod
    def registro(nombre,apellidos,email,password):
        resultado=usuario.Usuario.registrar(nombre,apellidos,email,password)
        if resultado:
            messagebox.showinfo(icon="info",message=f"{nombre} {apellidos}, se registro correcamente con el email: {email}",title="Usuarios")
        else:
            messagebox.showerror(icon="error",message="Ocurrio un error, vuelva a intentarlo",title="Usuarios")

    @staticmethod
    def iniciar_sesion(ventana,email,password):
        registro=usuario.Usuario.iniciar_sesion(email,password)
        if registro:
            messagebox.showinfo(
                icon="info",
                message=f"{registro[1]} {registro[2]}, iniciaste sesión correctamente",
                title="Usuarios"
            )
            vista1.View.menu_notas(ventana, registro[0], registro[1], registro[2])
        else:
             messagebox.showerror(icon="error",message="Email y/o contraseña incorrectos, vuelva a intentarlo",title="Usuarios")

    @staticmethod
    def respuesta_sql(respuesta): 
        if respuesta:
            messagebox.showinfo(message="Acción realizada con éxito", icon="info")
        else:
            messagebox.showerror(message="Ocurrió un error en la operación", icon="error")

    @staticmethod
    def crear_nota(usuario_id,tutulo,descripcion):
        respuesta=nota.Nota.crear(usuario_id,tutulo,descripcion)
        Controlador.respuesta_sql(respuesta)

    @staticmethod
    def mostrar_notas(usuario_id):
        registro=nota.Nota.mostrar(usuario_id)
        return registro
    
    @staticmethod
    def eliminar_nota(id):
        respuesta=nota.Nota.eliminar(id)
        Controlador.respuesta_sql(respuesta)
       
    @staticmethod
    def cambiar_nota(id,titulo,descripcion):
        cambio=nota.Nota.actualizar(id,titulo,descripcion)
        Controlador.respuesta_sql(cambio)