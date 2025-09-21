from PySide6.QtWidgets import QApplication, QMainWindow, QTimeEdit
from PySide6.QtCore import QTime

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTimeEdit")
        self.setGeometry(100, 100, 300, 100)

        # QTimeEdit es un widget para seleccionar y mostrar horas y minutos (y opcionalmente segundos).
        # QTimeEdit(parent: QWidget = None)
        time_edit = QTimeEdit()

        # Métodos principales de QTimeEdit y sus argumentos:
        # setTime(time: QTime): Establece la hora actual del widget.
        # time() -> QTime: Devuelve la hora seleccionada.
        # setDisplayFormat(format: str): Define el formato de visualización, por ejemplo:
        #   "HH:mm" (24h), "hh:mm AP" (12h con AM/PM), "HH:mm:ss" (con segundos).
        # displayFormat() -> str: Devuelve el formato actual.
        # setMinimumTime(time: QTime): Establece la hora mínima seleccionable.
        # setMaximumTime(time: QTime): Establece la hora máxima seleccionable.
        # setTimeRange(min: QTime, max: QTime): Establece el rango de horas seleccionables.
        # setWrapping(wrap: bool): Si es True, al pasar el máximo vuelve al mínimo.
        # setReadOnly(readOnly: bool): Si es True, el usuario no puede editar manualmente.
        # setAlignment(alignment: Qt.Alignment): Alinea el texto (Qt.AlignLeft, Qt.AlignRight, Qt.AlignCenter).
        # setStyleSheet(css: str): Aplica estilos CSS.

        # Ejemplo de configuración:
        time_edit.setTime(QTime.currentTime())      # Valor inicial: hora actual
        time_edit.setDisplayFormat("HH:mm")         # Formato de visualización (24h, solo horas y minutos)
        # time_edit.setDisplayFormat("hh:mm AP")    # Formato 12h con AM/PM
        # time_edit.setDisplayFormat("HH:mm:ss")    # Incluye segundos
        # time_edit.setMinimumTime(QTime(8, 0, 0))  # Hora mínima: 08:00
        # time_edit.setMaximumTime(QTime(20, 0, 0)) # Hora máxima: 20:00
        # time_edit.setWrapping(True)               # Permite que el valor "gire"
        # time_edit.setReadOnly(True)               # Solo permite cambiar con las flechas

        # Señales (signals) de QTimeEdit:
        # timeChanged(QTime time): Se emite cuando cambia la hora seleccionada.
        # editingFinished(): Se emite cuando el usuario termina de editar (pierde el foco o presiona Enter).

        # Ejemplo de conexión de señal:
        time_edit.timeChanged.connect(self.horaCambiada)

        self.setCentralWidget(time_edit)
        self.show()

    def horaCambiada(self, hora):
        # El argumento 'hora' es un objeto QTime
        print(f"Hora seleccionada: {hora.toString('HH:mm')}")

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    app.exec()