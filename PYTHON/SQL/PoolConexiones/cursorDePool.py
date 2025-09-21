import pool

class cursorDePool:
    def __init__(self):
        self._conexion= None
        self._cursor= None
    
    def __enter__(self): #Este metodo se llama al usar el with
        # Inicializa la conexión y el cursor
        self._conexion= pool.Conexion.obtenerConexion()
        self._cursor= self._conexion.cursor()
        return self._cursor
    
    def __exit__(self, exc_type, exc_value, traceback): ## Este metodo se llama al finalizar el with
        # Cierra el cursor y libera la conexión
        if exc_type:
            self._conexion.rollback()
        else:
            self._conexion.commit()
        self._cursor.close()
        pool.Conexion.liberarConexion(self._conexion)

if __name__ == "__main__":
    with cursorDePool() as cursor: #Al usar el with, se inicializa la conexión y el cursor
        cursor.execute("SELECT * FROM persona")  # Reemplaza 'mi_tabla' con tu tabla real
    