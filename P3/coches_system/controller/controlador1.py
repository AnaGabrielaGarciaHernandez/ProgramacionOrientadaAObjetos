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

    @staticmethod
    def insertar_camioneta(marca, color, modelo, velocidad, caballaje, plaza,traccion,cerrada):
        respuesta=cochesBD.Camionetas.insertar(marca,color, modelo, velocidad, caballaje, plaza,traccion,cerrada)
        Controlador.respuesta_sql(respuesta)

    @staticmethod
    def consultar_camionetas():
        registro=cochesBD.Camionetas.consultar()
        return registro
    
    @staticmethod
    def cambiar_camionetas(id,marca, color, modelo, velocidad, caballaje, plaza,traccion,cerrada):
        cambio=cochesBD.Camionetas.actualizar(id,marca, color, modelo, velocidad, caballaje, plaza,traccion,cerrada)
        Controlador.respuesta_sql(cambio)

    @staticmethod
    def eliminar_camionetas(id):
        respuesta=cochesBD.Camionetas.eliminar(id)
        Controlador.respuesta_sql(respuesta)

    @staticmethod
    def buscar_camionetas(id):
        operacion=cochesBD.Camionetas.consultar_id(id)
        if operacion:
            return operacion
        else:
            messagebox.showinfo(message="No se encontró el id")

    @staticmethod
    def insertar_camiones(marca, color, modelo, velocidad, caballaje, plaza,ejes,capacidad):
        respuesta=cochesBD.Camiones.insertar(marca, color, modelo, velocidad, caballaje, plaza,ejes,capacidad)
        Controlador.respuesta_sql(respuesta)

    @staticmethod
    def consultar_camiones():
        registro=cochesBD.Camiones.consultar()
        return registro
    
    @staticmethod
    def cambiar_camiones(id,marca, color, modelo, velocidad, caballaje, plaza,ejes,capacidad):
        cambio=cochesBD.Camiones.actualizar(id,marca, color, modelo, velocidad, caballaje, plaza,ejes,capacidad)
        Controlador.respuesta_sql(cambio)

    @staticmethod
    def eliminar_camiones(id):
        respuesta=cochesBD.Camiones.eliminar(id)
        Controlador.respuesta_sql(respuesta)

    @staticmethod
    def buscar_camiones(id):
        operacion=cochesBD.Camiones.consultar_id(id)
        if operacion:
            return operacion
        else:
            messagebox.showinfo(message="No se encontró el id")


            