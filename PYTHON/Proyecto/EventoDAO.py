from cursorPool import CursorDelPool
from configuracionLoogin import log
from Evento import Evento


class EventoDAO:
    _SELECCIONTODOS = "SELECT * FROM Evento"
    _SELECCIONACTIVOS= "SELECT * FROM Evento WHERE estado = 'activo'"
    _SELECCIONAREVENTO= "SELECT * FROM Evento WHERE dia = %s"
    _INSERTAR_EVENTO = "INSERT INTO Evento (horainicio, horafinal, nombrecontratista, telefono, colormantel, pagofinal, saldopagado, saldopendiente, dia, estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    _ACTUALIZAR_EVENTO = "UPDATE Evento SET horainicio = %s, horafinal = %s, nombrecontratista = %s, telefono = %s, colormantel = %s, pagofinal = %s, saldopagado = %s, saldopendiente = %s, dia = %s , estado = %s WHERE id = %s"
    _ELIMINAR_EVENTO = "DELETE FROM Evento WHERE id = %s"

    @staticmethod
    def crearEventoIndividual(evento):
        eventoIndividual= Evento(evento[0], evento[1], evento[2], evento[3], evento[4], evento[5], evento[6], evento[7], evento[9], evento[8])
        eventoIndividual.horaInicio = eventoIndividual.horaInicio.strftime("%H:%M:%S")
        eventoIndividual.horaFinal = eventoIndividual.horaFinal.strftime("%H:%M:%S")
        eventoIndividual.dia = eventoIndividual.dia.strftime("%Y-%m-%d")
        print(eventoIndividual)
        return eventoIndividual

    @classmethod
    def seleccionarTodos(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONTODOS)
            eventos = cursor.fetchall()
            retornoEventos = []
            for evento in eventos:
                retornoEventos.append(cls.crearEventoIndividual(evento))
            log.debug("Obtencion de todos los eventos exitosa")
            return retornoEventos
    
    @staticmethod
    def configurarValores(evento):
        return ( evento.horaInicio, evento.horaFinal, evento.nombreContratista, evento.telefono, evento.colorMantel, evento.pagoFinal, evento.saldoPagado, evento.saldoPendiente, evento.dia,"activo"
    )
 
    @classmethod
    def seleccionarActivos(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONACTIVOS)
            eventos = cursor.fetchall()
            log.debug("Obtencion de eventos activos exitosa")
            return [cls.crearEventoIndividual(evento) for evento in eventos]

    @classmethod
    def seleccionarEvento(cls, fecha):
        try:
            with CursorDelPool() as cursor:
                cursor.execute(cls._SELECCIONAREVENTO, (fecha,))
                eventosIndividuales = cursor.fetchall()
                log.debug("Busqueda de evento realizada con exito")
                return [cls.crearEventoIndividual(e) for e in eventosIndividuales]
        except Exception as e:
            log.error(f"Error al realizar busqueda de evento: {e}")
            return None

    @classmethod
    def insertarEvento(cls, evento: Evento):
        try:
            with CursorDelPool() as cursor:
                cursor.execute(cls._INSERTAR_EVENTO, cls.configurarValores(evento))
                log.debug(f"Evento insertado: { 'Evento insertado correctamente' if cursor.rowcount > 0 else 'No se insertó ningún evento' }")
        except Exception as e:
            log.error(f"Error al insertar evento: {e}")
    
    @classmethod
    def actualizarEvento(cls, fecha, id, evento):
        try:
            with CursorDelPool() as cursor:
                tuplaConFecha= (fecha,) + cls.configurarValores(evento) + (id,)
                cursor.execute(cls._ACTUALIZAR_EVENTO, tuplaConFecha)
                log.debug(f"Evento actualizado: { 'Evento actualizado correctamente' if cursor.rowcount > 0 else 'No se actualizó ningún evento' }")
        except Exception as e:
            log.error(f"Error al actualizar evento: {e}")

    @classmethod
    def eliminarEvento(cls, id):
        try:
            with CursorDelPool() as cursor:
                cursor.execute(cls._ELIMINAR_EVENTO, (id,))
                log.debug(f"Evento eliminado: { 'Evento eliminado correctamente' if cursor.rowcount > 0 else 'No se eliminó ningún evento' }")
        except Exception as e:
            log.error(f"Error al eliminar evento: {e}")

if __name__ == "__main__":
    #eventos= EventoDAO.seleccionarTodos()
    #eventos= EventoDAO.seleccionarActivos()
    #eventos = EventoDAO.seleccionarEvento("2025-08-10")
    eventos = EventoDAO.insertarEvento(Evento("10:00:00", "12:00:00", "Contratista A", "1234567890", "Rojo", 1000, 500, 500, "2025-08-10"))