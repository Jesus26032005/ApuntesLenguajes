from Conexion import ConexionBase
from configuracionLoogin import log
import sys

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None
    
    def __enter__(self):
        if self._conexion is None:
            self._conexion = ConexionBase.obtenerConexion()
        if self._cursor is None:
            try:
                self._cursor = self._conexion.cursor()
            except Exception as e:
                log.warning(f"Error al crear el cursor, las caracteristicas son {e}")
                sys.exit()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self._conexion.rollback()
        else:
            self._conexion.commit()
        if self._cursor is not None:
            self._cursor.close()
        if self._conexion is not None:
            ConexionBase.liberarConexion(self._conexion)

    