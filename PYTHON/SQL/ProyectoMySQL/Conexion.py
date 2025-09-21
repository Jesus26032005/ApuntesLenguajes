import sys
from mysql.connector import pooling

class Conexion:
    # Parámetros de configuración para la conexión y el pool
    _HOST = "localhost"
    _DATABASE = "proyectocurso"
    _USERNAME = "root"
    _PASSWORD = "ezio1969+"
    _DB_PORT = 3308
    _POOL_NAME = "Pool_Proyecto"
    _POOL_SIZE = 5

    # Variable de clase que contendrá la instancia del pool de conexiones
    pool = None

    @classmethod
    def obtenerPool(cls):
        if cls.pool is None:
            try:
                cls.pool = pooling.MySQLConnectionPool( #Se usa el objeto poooling y su metodo MySQLConnectionPool para crear el pool
                    pool_name=cls._POOL_NAME,
                    pool_size=cls._POOL_SIZE,
                    host=cls._HOST,
                    port=cls._DB_PORT,
                    database=cls._DATABASE,
                    user=cls._USERNAME,
                    password=cls._PASSWORD
                )
                print(f"✅ Pool '{cls._POOL_NAME}' creado con tamaño {cls._POOL_SIZE}.")
            except Exception as e:
                print(f"❌ Error creando pool: {e}")
                sys.exit()
        else:
            print(f"⚠️ Pool '{cls._POOL_NAME}' ya existe, reutilizando.")

    @classmethod
    def obtenerConexion(cls):
        if cls.pool is None:
            cls.obtenerPool()
        try:
            conexion = cls.pool.get_connection()
            print("✅ Conexión obtenida del pool.")
            return conexion
        except Exception as e:
            print(f"❌ Error obteniendo conexión: {e}")
            sys.exit()

    @classmethod
    def cerrarConexion(cls, conexion):
        if conexion is not None:
            conexion.close()
            print("✅ Conexión cerrada y retornada al pool.")
        else:
            print("⚠️ No hay conexión para cerrar.")
    
        
        