import sys
from looginInf import log
import psycopg2

class Conexion:
    _database = "test_db"
    _username = "postgres"
    _password = "ezio1969+"
    _host = "localhost"
    _port = 5432
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = psycopg2.connect(
                    database=cls._database,
                    user=cls._username,
                    password=cls._password,
                    host=cls._host,
                    port=cls._port
                )
                log.debug("Conexión a la base de datos establecida.")
                return cls._conexion
            except Exception as e:
                log.error(f"Error al conectar a la base de datos")
                cls._conexion = None
                sys.exit() # Esta línea puede ser opcional, dependiendo de cómo quieras manejar los errores de conexión, si pasa esto no se puede continuar con la ejecución del programa, lo finaliza.
        else:
            return cls._conexion
        
    @classmethod
    def obtenerCursor(cls):
        if cls._conexion is None:
            cls.obtenerConexion()
        if cls._cursor is None:
            try:
                cls._cursor = cls._conexion.cursor()
                log.debug("Cursor obtenido.")
                return cls._cursor
            except Exception as e:
                log.error(f"Error al obtener el cursor: {e}")
                cls._cursor = None
                sys.exit()
        else:
            return cls._cursor
        
    @classmethod
    def cerrarConexion(cls):
        if cls._cursor is not None:
            cls._cursor.close()
            log.debug("Cursor cerrado.")
            cls._cursor = None
        if cls._conexion is not None:
            cls._conexion.close()
            log.debug("Conexión cerrada.")
            cls._conexion = None

if __name__ == "__main__":
    Conexion.obtenerConexion()
