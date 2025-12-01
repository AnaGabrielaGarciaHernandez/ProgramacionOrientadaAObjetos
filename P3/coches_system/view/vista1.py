from tkinter import *
from tkinter import messagebox


class View:
    def __init__(self,ventana):
        self.ventana=ventana
        ventana.title("Coches System")
        ventana.geometry("800x600")
        ventana.resizable(False,False)
        self.menu_principal(ventana)

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def menu_principal(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="::: Menu Principal :::",justify="center")
        lbl_titulo.pack(pady=10)

        lbl_opcion=Label(ventana,text="Elige una opcion...",justify="center")
        lbl_opcion.pack(pady=10)

        btn_autos=Button(ventana,text="Autos",command=lambda:View.menu_acciones(ventana,"Autos"),justify="center")
        btn_autos.pack(pady=10)

        btn_camionetas=Button(ventana,text="Camionetas",command=lambda:View.menu_acciones(ventana,"Camionetas"),justify="center")
        btn_camionetas.pack(pady=10)

        btn_camiones=Button(ventana,text="Camiones",command=lambda:View.menu_acciones(ventana,"Camiones"),justify="center")
        btn_camiones.pack(pady=10)

        btn_salir=Button(ventana,text="Salir",command=ventana.quit,justify="center")
        btn_salir.pack(pady=10)

    @staticmethod
    def menu_acciones(ventana,tipo):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=f".: Menu de {tipo} :.",justify="center")
        lbl_titulo.pack(pady=10)

        lbl_opcion=Label(ventana,text="Elige una opcion...",justify="center")
        lbl_opcion.pack(pady=10)

        btn_insertar=Button(ventana,text="Insertar",command=lambda: View.insertar_autos(ventana),justify="center")
        btn_insertar.pack(pady=10)

        btn_consultar=Button(ventana,text="Consultar",command=lambda:View.consultar_autos(ventana),justify="center")
        btn_consultar.pack(pady=10)

        btn_actualizar=Button(ventana,text="Actualizar",command=lambda:View.buscar_id(ventana,"cambiar"),justify="center")
        btn_actualizar.pack(pady=10)

        btn_eliminar=Button(ventana,text="Eliminar",command=lambda:View.buscar_id(ventana,"borrar"),justify="center")
        btn_eliminar.pack(pady=10)

        btn_regresar=Button(ventana,text="Regresar",command=lambda:View.menu_principal(ventana),justify="center")
        btn_regresar.pack(pady=10)

    @staticmethod
    def insertar_autos(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=f".: Ingresar los datos del vehiculo :.",justify="center")
        lbl_titulo.pack(pady=10)

        lbl_marca=Label(ventana,text="Marca: ",justify="center")
        lbl_marca.pack(pady=5)
        txt_marca=Entry(ventana)
        txt_marca.focus()
        txt_marca.pack(pady=5)

        lbl_color=Label(ventana,text="Color: ",justify="center")
        lbl_color.pack(pady=5)
        txt_color=Entry(ventana)
        txt_color.pack(pady=5)

        lbl_modelo=Label(ventana,text="Modelo: ",justify="center")
        lbl_modelo.pack(pady=5)
        txt_modelo=Entry(ventana)
        txt_modelo.pack(pady=5)

        lbl_velocidad=Label(ventana,text="Velocidad: ",justify="center")
        lbl_velocidad.pack(pady=5)
        txt_velocidad=Entry(ventana)
        txt_velocidad.pack(pady=5)

        lbl_potencia=Label(ventana,text="Potencia: ",justify="center")
        lbl_potencia.pack(pady=5)
        txt_potencia=Entry(ventana)
        txt_potencia.pack(pady=5)

        lbl_plazas=Label(ventana,text="No. Plazas: ",justify="center")
        lbl_plazas.pack(pady=5)
        txt_plazas=Entry(ventana)
        txt_plazas.pack(pady=5)

        btn_guardar=Button(ventana,text="Guardar",command=lambda:"",justify="center")
        btn_guardar.pack(pady=10)

        btn_regresar=Button(ventana,text="Regresar",command=lambda:View.menu_acciones(ventana,"Autos"),justify="center")
        btn_regresar.pack(pady=10)

    @staticmethod
    def consultar_autos(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=".: Mostrar Coches :.",justify="center")
        lbl_titulo.pack(pady=10)

        filas=""
        registros=[(1,"Nissan","rojo",2015,123,321,3)]
        num_registro=1
        if len(registros)>0:
            for fila in registros:
                filas=filas+f"Auto: {num_registro} \n ID: {fila[0]} \n Marca: {fila[1]} \n Color: {fila[2]} \n Modelo: {fila[3]} \n Velocidad: {fila[4]} \n Potencia: {fila[5]} \n No Plazas: {fila[6]}"
                num_registro+=1
        else:
            messagebox.showwarning(icon="warning",message="No existen registros...")

        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)
        btn_regresar=Button(ventana,text="Regresar",command=lambda:View.menu_acciones(ventana,"Autos"),justify="center")
        btn_regresar.pack(pady=10)
        
    @staticmethod
    def cambiar_auto(ventana):
        registro=""
        if registro is None:
            messagebox.showinfo(icon="info",message="No existe esta operacion en la BD")
        else:
            View.borrarPantalla(ventana)
            lbl_1=Label(ventana,text=".:: Cambiar una Autos ::.")
            lbl_1.pack(pady=10)

            lbl_id=Label(ventana,text="ID del coche: ")
            lbl_id.pack(pady=5)
            id=IntVar()
            txt_id=Entry(ventana,textvariable=id,width=5,justify="right",state="readonly")
            txt_id.focus()
            txt_id.pack(pady=5)
            
            lbl_marca=Label(ventana,text="Marca: ",justify="center")
            lbl_marca.pack(pady=5)
            txt_marca=Entry(ventana)
            txt_marca.pack(pady=5)

            lbl_color=Label(ventana,text="Color: ",justify="center")
            lbl_color.pack(pady=5)
            txt_color=Entry(ventana)
            txt_color.pack(pady=5)

            lbl_modelo=Label(ventana,text="Modelo: ",justify="center")
            lbl_modelo.pack(pady=5)
            txt_modelo=Entry(ventana)
            txt_modelo.pack(pady=5)

            lbl_velocidad=Label(ventana,text="Velocidad: ",justify="center")
            lbl_velocidad.pack(pady=5)
            txt_velocidad=Entry(ventana)
            txt_velocidad.pack(pady=5)

            lbl_potencia=Label(ventana,text="Potencia: ",justify="center")
            lbl_potencia.pack(pady=5)
            txt_potencia=Entry(ventana)
            txt_potencia.pack(pady=5)

            lbl_plazas=Label(ventana,text="No. Plazas: ",justify="center")
            lbl_plazas.pack(pady=5)
            txt_plazas=Entry(ventana)
            txt_plazas.pack(pady=5)

            btn_guardar=Button(ventana,text="Guardar",command=lambda:"",justify="center")
            btn_guardar.pack(pady=10)

            btn_regresar=Button(ventana,text="Regresar",command=lambda:View.menu_acciones(ventana,"Autos"),justify="center")
            btn_regresar.pack(pady=10)

    @staticmethod
    def eliminar_auto(ventana):
        registro=""
        if registro is None:
            messagebox.showinfo(icon="info",message="No existen esta registros la BD")
        else:
            View.borrarPantalla(ventana)
            lbl_1=Label(ventana,text="..:: Eliminar un Registro ::..")
            lbl_1.pack(pady=10)

            lbl_2=Label(ventana,text="ID del Auto: ")
            lbl_2.pack(pady=5)
            id=IntVar()

            txt_id_eliminar=Entry(ventana,textvariable=id,width=5)
            txt_id_eliminar.focus()
            txt_id_eliminar.pack(pady=5)

            btn_eliminar=Button(ventana,text="Eliminar",command=lambda:"",justify="center")
            btn_eliminar.pack(pady=10)

            btn_regresar=Button(ventana,text="Regresar",command=lambda:View.menu_acciones(ventana,"Autos"),justify="center")
            btn_regresar.pack(pady=10)

    @staticmethod
    def buscar_id(ventana,tipo):
        View.borrarPantalla(ventana)
     
        lbl_1=Label(ventana,text=".:: Buscar un Coche ::.")
        lbl_1.pack(pady=10)
       
        lbl_id=Label(ventana,text="ID del coche a buscar: ")
        lbl_id.pack(pady=5)
        id=IntVar()
        txt_id=Entry(ventana,textvariable=id,width=5,justify="right")
        txt_id.focus()
        txt_id.pack(pady=5)
        
        if tipo=="cambiar":
            Button(ventana,text="Buscar",command=lambda: View.cambiar_auto(ventana)).pack(pady=5)
        elif tipo=="borrar":
            Button(ventana,text="Buscar",command=lambda: View.eliminar_auto(ventana)).pack(pady=5)
        


