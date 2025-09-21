import psycopg2

# try:
# #variable de conexion, literal es el puente entre nuestra base de datos y python
#     conexion = psycopg2.connect(
#         user= "postgres",
#         password= "ezio1969+",
#         host= "localhost",
#         port= "5432",
#         database= "test_db"
#     )

#     with conexion:
#         with conexion.cursor() as cursor:
#         #Cursor= Objeto que permite ejecutar sentencias en sql
#             sentencia= "select * from persona order by id_persona ASC"
#             #Se ejecuta sentencia
#             cursor.execute(sentencia)
#             #Se obtiene resultado de la sentencia
#             resultado= cursor.fetchall()
#             print(resultado)
# except Exception as e:
#     print("Ocurrio un error al conectarse a la base de datos")
# finally:
#     conexion.close()

# Otra forma de hacerlo
import psycopg2  # Importamos la librería para conectarnos a PostgreSQL
try:
    # El primer 'with' abre la conexión a la base de datos.
    # Esto llama automáticamente al método __enter__ de la conexión,
    # y cuando termina el bloque (o si hay error), se ejecuta __exit__,
    # lo que garantiza que la conexión se cierre correctamente.
    with psycopg2.connect(
        dbname="test_db",         # nombre de la base de datos
        user="postgres",        # nombre de usuario de PostgreSQL
        password="ezio1969+", # contraseña del usuario
        host="localhost",         # dirección del servidor (localhost si es local)
        port="5432"               # puerto por defecto de PostgreSQL
    ) as conexion:
        # El segundo 'with' abre un cursor para ejecutar consultas SQL.
        # También se asegura de que el cursor se cierre automáticamente,
        # incluso si ocurre un error dentro del bloque.
        # 🔎 ¿Qué es el cursor?
        # El cursor es un objeto que permite ejecutar comandos SQL (como SELECT, INSERT, etc.)
        # y acceder a los resultados. Funciona como un "controlador" que se mueve
        # por los datos que devuelve la base de datos.
        with conexion.cursor() as cursor:
            # Ejecutamos una consulta SQL (en este caso, obtener todos los registros)
            cursor.execute("SELECT * FROM persona;")
            # Obtenemos los resultados de la consulta como una lista de tuplas
            resultados = cursor.fetchall()

            # Mostramos los resultados fila por fila
            for fila in resultados:
                print(fila)

# Si ocurre cualquier error durante la conexión o la consulta, se captura aquí
except Exception as e:
    print("Error al conectar o consultar la base de datos:", e)
