from psycopg2 import pool
from loogerBase import log

class Conexion:
    _DATABASE = 'proyectoCurso'
    _USERNAME = 'postgres'
    _PASSWORD = 'ezio1969+'
    _HOST = 'localhost'
    _PORT = '5432'
    _MIN_CONNS = 1
    _MAX_CONNS = 5
    _pool = None

    @classmethod
    def inicializarPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CONNS,
                    cls._MAX_CONNS,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    host=cls._HOST,
                    port=cls._PORT,
                    database=cls._DATABASE
                )
                log.debug("Pool de conexiones inicializado correctamente.")
            except Exception as e:
                log.error(f"Error al inicializar el pool de conexiones: {e}")
        else:
            log.debug("El pool de conexiones ya está inicializado.")

    @classmethod
    def obtenerConexion(cls):
        if cls._pool is None:
            cls.inicializarPool()
        try:
            conexion = cls._pool.getconn()
            log.debug("Conexión obtenida del pool.")
            return conexion
        except Exception as e:
            log.error(f"Error al obtener conexión del pool: {e}")
            return None
    @classmethod
    def liberarConexion(cls, conexion):
        if cls._pool is not None and conexion is not None:
            cls._pool.putconn(conexion)
            log.debug("Conexión liberada al pool.")
        else:
            if conexion is None:
                log.warning("No se puede liberar una conexión nula.")
            elif cls._pool is None:
                log.warning("El pool de conexiones no ha sido inicializado.")
            else:
                log.error("Error al liberar la conexión al pool.")

    @classmethod
    def cerrarConexiones(cls):
        if cls._pool is not None:
            cls._pool.closeall()
            log.debug("Todas las conexiones del pool han sido cerradas.")
        else:
            log.warning("El pool de conexiones no ha sido inicializado.")