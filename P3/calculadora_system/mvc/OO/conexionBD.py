import mysql.connector

try:
    conexion=mysql.connector.connect(
        port=3307,
        host="localhost",
        user="root",
        password="",
        database="bd_operaciones_basicas"
    )
    cursor=conexion.cursor(buffered=True)
except:
    print("Ocurrio un error con la BD ... Verifique")