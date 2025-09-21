import psycopg2

try:
    with psycopg2.connect(
        user="postgres",
        password="ezio1969+",
        host="localhost",
        port="5432",
        database="test_db"
    ) as conexion:
        with conexion.cursor() as cursor:
            # Obtencion de datos de una tabla
            sentencia= "SELECT * FROM persona WHERE id_persona = %s" #Se pueden usar parámetros para evitar inyecciones SQL o si los tenemos
            sentencia2= "SELECT * FROM PERSONA WHERE id_persona IN %s"
            
            # Entrada de usuario para el parámetro de tupla
            entrada_usuario = input("Introduce los IDs de persona separados por comas: ")
            # Convertir la entrada del usuario en una tupla de enteros
            ids_persona = (tuple(entrada_usuario.split(',')),)

            #fetchall() obtiene todas las filas(registros) de la consulta, devuelve una lista de tupla
            #fetchone() obtiene una sola fila(registro) de la consulta, devuelve una tupla
            cursor.execute(sentencia, (1,)) #Se añade el parámetro/s como una tupla, mientras que en la sentencia se usa los %s
            fila = cursor.fetchone()
            cursor.execute(sentencia2, ids_persona) # Se usa una tupla de tuplas para el IN porque se desempaqueta la tupla y se requiere la otra tupla para el IN
            filas = cursor.fetchall()

            print(f"Filas obtenidas: {filas}")
            print(f"Fila obtenida: {fila}")


            # Inseración de datos en una tabla
            sentencia_insert = "INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)"
            entrada_usuario_insert = input("Introduce el nombre, apellido y email separados por comas: ")
            tuplaAenviar= tuple(entrada_usuario_insert.split(','))

            cursor.execute(sentencia_insert, tuplaAenviar)
            # Como se esta haciendo una insercion, se requiere hacer commit para guardar los cambios en la base de datos
            #conexion.commit(), como se usa el with, no es necesario hacer commit ya que se hace automaticamente al salir del bloque with
            registros_afectados = cursor.rowcount # Al hacer una inserción, se puede obtener el número de registros afectados, lo que nos dice si se ha insertado correctamente
            print(f"Registros insertados: {registros_afectados}")

            #Insertar varios registros a la vez
            sentencia_insert_varios = "INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)"
            registrosIngresar= (
                ('Ana', 'García', 'ana.garcia@example.com'),
                ('Luis', 'Martínez', 'luis.martinez@example.com'),
                ('Marta', 'López', 'marta.lopez@example.com')
            )
            #executemany() permite insertar varios registros a la vez, recibe la sentencia y una lista o tupla de tuplas con los datos a insertar
            cursor.executemany(sentencia_insert_varios, registrosIngresar) 
            print(f"Registros insertados (varios): {cursor.rowcount}")
            
            # Nota: Cuando hacemos una insersion y no se realiza por algun error, este lanza una excepcion, y si no se captura, el commit no se realiza
            # Podemos de psycopg2 import errores y capturar la excepcion especifica de integridad (violacion de llave primaria, llave unica, etc)
            # Algunas excepciones comunes son:
            # from psycopg2 import errors
            # except errors.UniqueViolation as e: #Error de violacion de llave unica
            # except errors.ForeignKeyViolation as e: #Error de violacion de llave foranea
            # except errors.NotNullViolation as e: #Error de violacion de restriccion
            # except errors.CheckViolation as e: #Error de violacion de restriccion CHECK
            # except errors.SyntaxError as e: #Error de sintaxis en la consulta SQL
            # except errors.UndefinedTable as e: #Error de tabla no definida
            # except errors.UndefinedColumn as e: #Error de columna no definida

            # Actualización de datos en una tabla
            sentencia_update = "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s"
            cambiosEntrada = ('Zaddkiel', 'Alor', 'jesus@gmail.com', 1)
            cursor.execute(sentencia_update, cambiosEntrada)
            print(f"Registros actualizados: {cursor.rowcount}")

            # Actualización de varios registros a la vez
            sentencia_update_varios = "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s"
            cambiosEntrada_varios = (
                ('Ana', 'García', 'ana.garcia@example.com', 5),
                ('Luis', 'Martínez', 'luis.martinez@example.com', 6),
                ('Marta', 'López', 'marta.lopez@example.com', 7)
            )
            cursor.executemany(sentencia_update_varios, cambiosEntrada_varios) #Recuerda que se envia una tupla de tuplas o lista de tuplas
            print(f"Registros actualizados (varios): {cursor.rowcount}")

            # Eliminación de datos en una tabla
            sentencia_delete = "DELETE FROM persona WHERE id_persona=%s"
            idEliminar = (7,)
            cursor.execute(sentencia_delete, idEliminar)
            print(f"Registros eliminados: {cursor.rowcount}")   

            # Eliminación de varios registros a la vez
            sentencia_delete_varios = "DELETE FROM persona WHERE id_persona IN %s"
            idsEliminar = (tuple([6,7,8]),)  # Se debe enviar una tupla de tuplas para el IN
            cursor.execute(sentencia_delete_varios, idsEliminar)
            print(f"Registros eliminados (varios): {cursor.rowcount}")
except Exception as e:
    print("Error al conectar o consultar la base de datos:", e)
