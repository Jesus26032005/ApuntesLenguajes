import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ezio1969+",
        database="prueba_db",
        port=3308
    )
    cursor = conexion.cursor()
    print("Conexión establecida:", conexion)

    #Sentencia select para obtener datos de una tabla
    sentenciaSelect = "SELECT * FROM persona"
    cursor.execute(sentenciaSelect)
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)
    
    # Sentencia insert para insertar datos en una tabla
    sentenciaInsert = "INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)"
    valoresInsertar = ('Fatima', 'Guadalupe', 'fat@gmail.com')
    cursor.execute(sentenciaInsert, valoresInsertar)
    cursor.rowcount
    print(f"Registros insertados: {cursor.rowcount}")

    # Sentencia update para actualizar datos en una tabla
    sentenciaUpdate = "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE idpersona=%s"
    valoresActualizar = ('Juana', 'De Arco', 'juana@gmailcom', 4)
    cursor.execute(sentenciaUpdate, valoresActualizar)
    print(f"Registros actualizados: {cursor.rowcount}")

    # Sentencia delete para eliminar datos de una tabla
    sentenciaDelete = "DELETE FROM persona WHERE idpersona=%s"
    valorEliminar = (5,)
    cursor.execute(sentenciaDelete, valorEliminar)
    print(f"Registros eliminados: {cursor.rowcount}")

    conexion.commit()  # Confirmar los cambios en la base de datos usando commit
    cursor.close()  # Cerrar el cursor
    conexion.close()  # Cerrar la conexión

except mysql.connector.Error as err:
    print("Error al conectar a la base de datos:", err) 