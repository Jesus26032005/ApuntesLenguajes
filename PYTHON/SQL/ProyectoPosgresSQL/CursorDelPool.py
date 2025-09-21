from Conexion import Conexion
from loogerBase import log

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None
    
    def __enter__(self):
        if self._conexion is None:
            self._conexion = Conexion.obtenerConexion()
        if self._cursor is None:
            self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self._conexion.rollback()
        else:
            self._conexion.commit()
        if self._cursor is not None:
            self._cursor.close()
        if self._conexion is not None:
            Conexion.liberarConexion(self._conexion)

    