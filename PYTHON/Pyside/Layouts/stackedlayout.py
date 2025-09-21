from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor

class Color(QWidget): #Crea un widget de color
    def __init__(self, nuevo_color):
        super().__init__()
        self.setAutoFillBackground(True)
        paletaColores = self.palette()
        paletaColores.setColor(QPalette.Window, QColor(nuevo_color))
        self.setPalette(paletaColores)

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStackedLayout")
        # QStackedLayout es un layout que apila widgets uno sobre otro, mostrando solo uno a la vez.
        # Es útil para interfaces tipo "pestañas" o "pantallas" donde solo se muestra una vista a la vez.
        # QStackedLayout(parent: QWidget = None)

        layout = QStackedLayout()

        # Métodos principales de QStackedLayout:
        # addWidget(widget: QWidget) -> int:
        #   Añade un widget a la pila y retorna su índice.
        # insertWidget(index: int, widget: QWidget) -> int:
        #   Inserta un widget en la posición dada.
        # removeWidget(widget: QWidget):
        #   Elimina el widget de la pila.
        # setCurrentIndex(index: int):
        #   Muestra el widget en la posición indicada (0 es el primero).
        # currentIndex() -> int:
        #   Devuelve el índice del widget actualmente visible.
        # setCurrentWidget(widget: QWidget):
        #   Muestra el widget dado (debe estar en la pila).
        # currentWidget() -> QWidget:
        #   Devuelve el widget actualmente visible.
        # count() -> int:
        #   Devuelve el número de widgets en la pila.
        # widget(index: int) -> QWidget:
        #   Devuelve el widget en la posición dada.

        # Argumentos:
        # - index: int, posición del widget (0 para el primero, 1 para el segundo, etc).
        # - widget: QWidget, el widget a agregar, mostrar o eliminar.

        # Señales (signals) de QStackedLayout:
        # currentChanged(int index): Se emite cuando cambia el widget visible (cuando cambias el índice actual).

        # Ejemplo de uso:
        layout.addWidget(Color("Red"))    # Por default solo se visualiza el primer widget agregado (índice 0)
        layout.addWidget(Color("Green"))  # Índice 1
        layout.addWidget(Color("Blue"))   # Índice 2

        # Para modificar el elemento mostrado se usa setCurrentIndex o setCurrentWidget
        layout.setCurrentIndex(1)  # Muestra el widget en la posición 1 (el verde)

        # Puedes conectar la señal currentChanged para reaccionar al cambio de vista:
        # layout.currentChanged.connect(self.cambioVista)
        # def cambioVista(self, index):
        #     print(f"Vista actual: {index}")

        componente = QWidget()
        componente.setLayout(layout)
        self.setCentralWidget(componente)
        self.show()

if __name__ == "__main__":
    app = QApplication()
    ventana = ventanaPrincipal()
    app.exec()