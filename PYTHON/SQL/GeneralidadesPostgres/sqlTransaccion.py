import psycopg2


#Con el with cuando sucede un error, se hace rollback automaticamente por lo tanto para verlo de forma natural
try:
    with psycopg2.connect(
        user="postgres",
        password="ezio1969+",
        host="localhost",
        port="5432",
        database="test_db"
    ) as conexion:
        with conexion.cursor() as cursor:
            print("Conexión exitosa a la base de datos.")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")


conexion = psycopg2.connect(
        user="postgres",
        password="ezio1969+",
        host="localhost",
        port="5432",
        database="test_db"
    )
try:
    conexion.autocommit = False  # Deshabilita el autocommit por lo tanto no se guardan los cambios hasta que se haga commit
    #Si se coloca en true, se guardan los cambios automaticamente al ejecutar la consulta
    cursor= conexion.cursor()

    # Inicia una transacción
    sentencia = "INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)"
    valoresEntrada= ('Juan', 'Pérez', 'juan.perez@example.com')

    sentenciaUpdate = "UPDATE persona SET nombre = %s WHERE nombre = %s"
    valoresUpdate = ('Juanito', 'Juan')

    cursor.execute(sentencia, valoresEntrada)
    cursor.execute(sentenciaUpdate, valoresUpdate)
    #Fin transacción, se hace commit para guardar los cambios
    conexion.commit()  # Guarda los cambios en la base de datos
    print("Termina la transacción")
except Exception as e:
    conexion.rollback() # Deshace los cambios realizados en la transacción
    # Si ocurre un error, se hace rollback para deshacer los cambios
    print(f"Error al insertar datos, se hizo rollback de la transacción: {e}")
    print(f"Error al ejecutar la consulta: {e}")
finally:
    cursor.close()
