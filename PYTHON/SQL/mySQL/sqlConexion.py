import mysql.connector

conexion= mysql.connector.connect(
    host="localhost",
    user="root",
    password="ezio1969+",
    database="prueba_db",
    port=3308
)
cursor= conexion.cursor()
print(conexion)
print(cursor)