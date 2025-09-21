from mysql.connector import pooling

class Conexion:
    # ---------------------------------------------
    # ¿Qué es un Pool de Conexiones?
    #
    # Un pool de conexiones es un conjunto de conexiones preestablecidas a la base de datos
    # que se mantienen abiertas y listas para usarse.
    #
    # En lugar de abrir y cerrar una conexión cada vez que se necesita acceder a la base de datos,
    # la aplicación toma una conexión disponible del pool, la usa y luego la devuelve para que
    # otra operación pueda reutilizarla.
    #
    # Beneficios principales:
    # - Mejora el rendimiento al evitar la sobrecarga de crear conexiones repetidamente.
    # - Controla y limita el número máximo de conexiones simultáneas para no saturar el servidor.
    # - Facilita la gestión eficiente de recursos en aplicaciones con múltiples accesos concurrentes.
    #
    # Esta clase implementa un pool usando mysql.connector.pooling.MySQLConnectionPool,
    # una funcionalidad nativa del conector oficial de MySQL para Python.
    # ---------------------------------------------
    
    # Parámetros de configuración para la conexión y el pool
    _HOST = "localhost"
    _DATABASE = "proyectocurso"
    _USERNAME = "root"
    _PASSWORD = "tu_contraseña"
    _DB_PORT = 3308
    _POOL_NAME = "Pool_Proyecto"
    _POOL_SIZE = 5

    # Variable de clase que contendrá la instancia del pool de conexiones
    pool = None

    @classmethod
    def obtenerPool(cls):
        """
        Este método crea el pool de conexiones si no existe y devuelve la instancia.
        El pool mantiene abiertas múltiples conexiones reutilizables para optimizar el acceso.
        """
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
                raise
        else:
            print(f"⚠️ Pool '{cls._POOL_NAME}' ya existe, reutilizando.")
        return cls.pool

    @classmethod
    def obtenerConexion(cls):
        """
        Obtiene una conexión activa del pool para ejecutar consultas.
        Si el pool no existe, se crea antes.
        """
        if cls.pool is None:
            cls.obtenerPool()
        try:
            conexion = cls.pool.get_connection()
            print("✅ Conexión obtenida del pool.")
            return conexion
        except Exception as e:
            print(f"❌ Error obteniendo conexión: {e}")
            raise

    @classmethod
    def cerrarConexion(cls, conexion):
        """
        Cierra la conexión y la devuelve al pool para que pueda ser reutilizada.
        """
        if conexion is not None:
            conexion.close()
            print("✅ Conexión cerrada y retornada al pool.")
        else:
            print("⚠️ No hay conexión para cerrar.")

# Ejemplo de uso
if __name__ == "__main__":
    try:
        conexion = Conexion.obtenerConexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM persona LIMIT 5")
        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila)
        cursor.close()
        Conexion.cerrarConexion(conexion)
    except Exception as e:
        print(f"⚠️ Error durante la operación: {e}")
