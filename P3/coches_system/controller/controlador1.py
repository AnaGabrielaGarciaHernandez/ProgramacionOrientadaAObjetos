from tkinter import messagebox
from model import cochesBD
from view import vista1

class Controlador:
    @staticmethod
    def respuesta_sql(respuesta): 
        if respuesta:
            messagebox.showinfo(message="Acción realizada con éxito", icon="info")
        else:
            messagebox.showerror(message="Ocurrió un error en la operación", icon="error")

    @staticmethod
    def insertar_autos(marca, color, modelo, velocidad, caballaje, plaza):
        respuesta=cochesBD.Autos.insertar(marca,color, modelo, velocidad, caballaje, plaza)
        Controlador.respuesta_sql(respuesta)

    @staticmethod
    def consultar_autos():
        registro=cochesBD.Autos.consultar()
        return registro
    
    @staticmethod
    def cambiar_autos(id,marca, color, modelo, velocidad, caballaje, plaza):
        cambio=cochesBD.Autos.actualizar(id,marca, color, modelo, velocidad, caballaje, plaza)
        Controlador.respuesta_sql(cambio)

    @staticmethod
    def eliminar_autos(id):
        respuesta=cochesBD.Autos.eliminar(id)
        Controlador.respuesta_sql(respuesta)

    @staticmethod
    def buscar(id):
        operacion=cochesBD.Autos.consultar_id(id)
        if operacion:
            return operacion
        else:
            messagebox.showinfo(message="No se encontró el id")
            