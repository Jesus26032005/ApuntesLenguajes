# Señales o eventos:
#   Son notificaciones que emiten los widgets cuando ocurre una acción (ej: clic, cambio de estado).
# Slots:
#   Son funciones que responden a esas señales. Se pueden conectar varias señales a un mismo slot y viceversa.

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QAction
from PySide6.QtCore import QSize

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        # setWindowTitle(str): Establece el título de la ventana.
        self.setWindowTitle("Almacenar estado")
        # setFixedSize(QSize(ancho, alto)): Fija el tamaño de la ventana.
        self.setFixedSize(QSize(400, 300))

        # QPushButton(str): Crea un botón con el texto indicado.
        boton = QPushButton("Haz Click Aquí")
        # setCheckable(bool): Permite que el botón tenga dos estados (chequeado y deschequeado).
        # True: el botón puede permanecer presionado (toggle), False: comportamiento normal (momentáneo).
        boton.setCheckable(True)

        # clicked: Señal que emite el botón al ser presionado.
        # connect(slot): Conecta la señal a una función (slot).
        # Se pueden conectar varias funciones a la misma señal.
        # Si el botón es checkable, la señal clicked pasa un argumento booleano indicando el estado.
        boton.clicked.connect(self._checarEstado)  # Recibe el estado (True/False) como argumento.
        boton.clicked.connect(self._eventoClick)   # No recibe argumentos.

        # setCentralWidget(widget): Coloca el widget en el área central de la ventana principal.
        self.setCentralWidget(boton)

        self.show()

    def _eventoClick(self):
        # Slot que se ejecuta cada vez que se hace clic en el botón.
        print("Botón clickeado!")
        print(f"Estado actual del botón: {self.estado_boton}")


    def _checarEstado(self, estado):
        # Slot que recibe el estado del botón (True si está chequeado, False si no).
        # estado: bool
        # TODO: Se pueden guardar estados en la clase
        self.estado_boton = estado
        print(f"Estado del botón guardado: {self.estado_boton}")

        # Alternativamente, se puede consultar el estado del botón usando isChecked():
        # estado_actual = self.centralWidget().isChecked()
        # print(f"Estado actual: {estado_actual}")

        # También se pueden conectar otras señales como pressed, released, toggled, etc.

if __name__ == "__main__":
    # QApplication([]): Inicializa la aplicación y el ciclo de eventos.
    app = QApplication([])
    ventana = VentanaPrincipal()
    # app.exec(): Ejecuta el bucle principal de la aplicación.
    app.exec()

# Información adicional:
# - Se pueden conectar señales a funciones lambda o métodos de otras clases.
# - Los slots pueden recibir argumentos si la señal los emite.
# - Para botones no checkables, clicked no pasa argumentos.
# - Otras señales útiles: pressed (cuando se presiona), released (cuando se suelta), toggled (cuando cambia el estado checkable).
# - En PySide6, los widgets pueden emitir señales personalizadas usando Signal.