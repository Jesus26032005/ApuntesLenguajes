from cursorPool import CursorDelPool
from configuracionLoogin import log
from Clase import Clase

class ClaseDAO:
    _SELECCION_TODAS = "SELECT * FROM clase"
    _SELECCION_ACTIVAS = "SELECT * FROM clase WHERE estado = 'activa'"
    _SELECCIONAR_CLASE = "SELECT * FROM clase WHERE nombreclase = %s"
    _INSERTAR_CLASE = "INSERT INTO clase (nombreclase, profesor, mensualidad, pagohecho, pagorestante, horario) VALUES (%s, %s, %s, %s, %s, %s)"
    _ACTUALIZAR_CLASE = "UPDATE clase SET profesor = %s, mensualidad = %s, pagohecho = %s, pagorestante = %s, horario = %s, estado = %s WHERE nombreclase = %s"
    _ELIMINAR_CLASE = "DELETE FROM clase WHERE nombreclase = %s"

    @staticmethod
    def crearClaseIndividual(clase):
        claseIndividual = Clase(
            clase[0],
            clase[1],
            clase[2],
            clase[3],
            clase[4],
            clase[5]
        )
        print(claseIndividual)
        return claseIndividual

    @classmethod
    def seleccionarTodas(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCION_TODAS)
            clases = cursor.fetchall()
            retornoClases = []
            for clase in clases:
                retornoClases.append(cls.crearClaseIndividual(clase))
            log.debug("Obtención de todas las clases exitosa")
            return retornoClases

    @staticmethod
    def configurarValores(clase):
        return (
            clase.nombreClase, clase.profesor, clase.mensualidad,
            clase.pagoHecho, clase.pagoRestante, clase.horario
        )

    @classmethod
    def seleccionarActivas(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCION_ACTIVAS)
            clases = cursor.fetchall()
            log.debug("Obtención de clases activas exitosa")
            return [cls.crearClaseIndividual(clase) for clase in clases]

    @classmethod
    def seleccionarClase(cls, nombreClase):
        try:
            with CursorDelPool() as cursor:
                cursor.execute(cls._SELECCIONAR_CLASE, (nombreClase,))
                clasesIndividuales = cursor.fetchall()
                log.debug("Búsqueda de clase realizada con éxito")
                return [cls.crearClaseIndividual(c) for c in clasesIndividuales]
        except Exception as e:
            log.error(f"Error al realizar búsqueda de clase: {e}")
            return None

    @classmethod
    def insertarClase(cls, clase: Clase):
        try:
            with CursorDelPool() as cursor:
                cursor.execute(cls._INSERTAR_CLASE, cls.configurarValores(clase))
                log.debug(f"Clase insertada: {'Clase insertada correctamente' if cursor.rowcount > 0 else 'No se insertó ninguna clase'}")
        except Exception as e:
            log.error(f"Error al insertar clase: {e}")

    @classmethod
    def actualizarClase(cls, clase: Clase):
        try:
            with CursorDelPool() as cursor:
                valores = (
                    clase.profesor, clase.mensualidad, clase.pagoHecho,
                    clase.pagoRestante, clase.horario, "activa", clase.nombreClase
                )
                cursor.execute(cls._ACTUALIZAR_CLASE, valores)
                log.debug(f"Clase actualizada: {'Clase actualizada correctamente' if cursor.rowcount > 0 else 'No se actualizó ninguna clase'}")
        except Exception as e:
            log.error(f"Error al actualizar clase: {e}")

    @classmethod
    def eliminarClase(cls, nombreClase):
        try:
            with CursorDelPool() as cursor:
                cursor.execute(cls._ELIMINAR_CLASE, (nombreClase,))
                log.debug(f"Clase eliminada: {'Clase eliminada correctamente' if cursor.rowcount > 0 else 'No se eliminó ninguna clase'}")
        except Exception as e:
            log.error(f"Error al eliminar clase: {e}")

if __name__ == "__main__":
    #clases = ClaseDAO.seleccionarTodas()
    #clases = ClaseDAO.seleccionarActivas()
    #clases = ClaseDAO.seleccionarClase("Matemáticas")
    clases = ClaseDAO.insertarClase(Clase("Matemáticas", "Profesor X", 800, 400, 400, "Lunes"))