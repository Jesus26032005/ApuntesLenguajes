from logging import log
import sys
import psycopg2
from psycopg2 import pool

class Conexion:
    _database = "test_db"
    _username = "postgres"
    _password = "ezio1969+"
    _host = "localhost"
    _port = 5432
    _Min_Connections = 1 # Número mínimo de conexiones en el pool
    _Max_Connections = 5 # Número máximo de conexiones en el pool
    _pool = None

    @classmethod
    def inicializarPool(cls):
        if cls._pool is None:
            print("Inicializando el pool de conexiones...")
            try:
                cls._pool = pool.SimpleConnectionPool( # Inicializa el pool de conexiones, es la forma mas sencilla de crearlo
                    minconn=cls._Min_Connections,
                    maxconn=cls._Max_Connections,
                    user=cls._username,
                    password=cls._password,
                    host=cls._host,
                    port=cls._port,
                    database=cls._database
                )
            except Exception as e:
                print(f"Error al inicializar el pool de conexiones: {e}")
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        if cls._pool is None:
            cls.inicializarPool()
        try:
            return cls._pool.getconn()  # Obtiene una conexión del pool
        except Exception as e:
            print(f"Error al obtener una conexión del pool: {e}")
            sys.exit()

    @classmethod
    def liberarConexion(cls, conexion):
        if cls._pool is not None and conexion is not None:
            cls._pool.putconn(conexion) # Libera la conexión al pool
            print("Conexión liberada al pool.")
        else:
            if conexion is None:
                print("No se puede liberar una conexión nula.")
            elif cls._pool is None:
                print("El pool de conexiones no ha sido inicializado.")
            else:
                print("Error al liberar la conexión al pool.")
        
    @classmethod
    def cerrarConexiones(cls):
        if cls._pool is not None:
            cls._pool.closeall()  # Cierra todas las conexiones en el pool
            print("Todas las conexiones del pool han sido cerradas.")
        else :
            print("El pool de conexiones no ha sido inicializado, no hay conexiones que cerrar.")

if __name__ == "__main__":
    conexion1= Conexion.obtenerConexion()
    conexion2= Conexion.obtenerConexion()
    conexion3= Conexion.obtenerConexion()
    conexion4= Conexion.obtenerConexion()
    conexion5= Conexion.obtenerConexion() # Obtiene varias conexiones del pool, si se supera el número máximo de conexiones, se generará una excepción
    Conexion.liberarConexion(conexion1) # Libera una conexión al pool
    conexion6= Conexion.obtenerConexion() # Obtiene una nueva conexión del pool
    Conexion.cerrarConexiones() # Cierra todas las conexiones del pool
