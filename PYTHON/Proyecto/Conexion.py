from psycopg2 import pool
from configuracionLoogin import log
import sys

class ConexionBase:
    _DATABASE= 'ProyectoIris'
    _USERNAME= 'postgres'
    _PASSWORD= 'ezio1969+'
    _HOST= 'localhost'
    _PORT= '5432'
    _MIN_CONNS= 1
    _MAX_CONNS= 5
    _pool= None

    @classmethod
    def inicializarPool(cls):
        if cls._pool is None:
            try:
                cls._pool= pool.SimpleConnectionPool(
                    cls._MIN_CONNS,
                    cls._MAX_CONNS,
                    user= cls._USERNAME,
                    password= cls._PASSWORD,
                    host= cls._HOST,
                    port= cls._PORT,
                    database= cls._DATABASE
                )
                log.debug("Pool de conexiones iniciado correctamente")
            except Exception as e:
                log.error(f'Ocurrio un error con las siguientes caracteristicas: {e}')
                sys.exit()
        else:
            log.debug("El pool de conexiones ya esta inicializado")

    @classmethod
    def obtenerConexion(cls):
        if cls._pool is None:
            cls.inicializarPool()
        try:
            conexion= cls._pool.getconn()
            log.debug("Conexion obtenida con el pool")
            return conexion
        except Exception as e:
            log.warning(f"Error al obtener la conexion,su descripcion es {e}")
            return None

    @classmethod
    def liberarConexion(cls, conexion):
        if cls._pool is not None and conexion is not None:
            cls._pool.putconn(conexion)
            log.debug("Conexión liberada al pool.")
        else:
            if conexion is None:
                log.warning("No se puede liberar una conexión nula.")
                sys.exit()
            elif cls._pool is None:
                log.warning("El pool de conexiones no ha sido inicializado.")
                sys.exit()
            else:
                log.error("Error al liberar la conexión al pool.")
                sys.exit()
