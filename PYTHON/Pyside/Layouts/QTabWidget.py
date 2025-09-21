from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget
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
        self.setWindowTitle("QTabWidget")
        # QTabWidget es un widget que permite organizar varios widgets en pestañas (tabs).
        # QTabWidget(parent: QWidget = None)
        tabulador = QTabWidget()

        # Métodos principales de QTabWidget:
        # addTab(widget: QWidget, label: str) -> int:
        #   Añade una nueva pestaña con el widget y el texto de la pestaña.
        # insertTab(index: int, widget: QWidget, label: str) -> int:
        #   Inserta una pestaña en la posición dada.
        # removeTab(index: int):
        #   Elimina la pestaña en la posición dada.
        # setTabText(index: int, label: str):
        #   Cambia el texto de la pestaña en la posición dada.
        # tabText(index: int) -> str:
        #   Devuelve el texto de la pestaña en la posición dada.
        # setTabIcon(index: int, icon: QIcon):
        #   Asigna un ícono a la pestaña.
        # setTabToolTip(index: int, tip: str):
        #   Asigna un tooltip a la pestaña.
        # setTabEnabled(index: int, enabled: bool):
        #   Habilita o deshabilita una pestaña.
        # setCurrentIndex(index: int):
        #   Cambia la pestaña activa.
        # currentIndex() -> int:
        #   Devuelve el índice de la pestaña activa.
        # currentWidget() -> QWidget:
        #   Devuelve el widget de la pestaña activa.
        # count() -> int:
        #   Devuelve el número de pestañas.
        # widget(index: int) -> QWidget:
        #   Devuelve el widget en la posición dada.
        # setTabPosition(position: QTabWidget.TabPosition):
        #   Cambia la posición de las pestañas (QTabWidget.North, South, West, East).
        # setMovable(movable: bool):
        #   Permite que el usuario reordene las pestañas arrastrándolas.
        # setTabsClosable(closable: bool):
        #   Muestra un botón de cerrar en cada pestaña.
        # setDocumentMode(enabled: bool):
        #   Cambia el estilo visual para parecerse a un editor de documentos.

        # Argumentos:
        # - widget: QWidget, el widget que se mostrará en la pestaña.
        # - label: str, el texto de la pestaña.
        # - index: int, la posición de la pestaña.
        # - position: QTabWidget.TabPosition, posición de las pestañas (North, South, West, East).
        # - icon: QIcon, ícono para la pestaña.
        # - tip: str, texto de ayuda (tooltip).
        # - enabled: bool, habilita o deshabilita la pestaña.
        # - movable: bool, permite mover las pestañas.
        # - closable: bool, muestra botón de cerrar.

        # Señales (signals) de QTabWidget:
        # currentChanged(int index): Se emite cuando cambia la pestaña activa.
        # tabCloseRequested(int index): Se emite cuando se solicita cerrar una pestaña (si es closable).
        # tabBarClicked(int index): Se emite cuando se hace clic en una pestaña.
        # tabBarDoubleClicked(int index): Se emite cuando se hace doble clic en una pestaña.

        # Posición de las etiquetas del tabulador
        tabulador.setTabPosition(QTabWidget.South)  # Posición de las pestañas (North, South, West, East)
        # Indicar si las etiquetas se pueden mover del tabulador
        tabulador.setMovable(True)
        #Para  que se vea similar en MAcOS
        tabulador.setDocumentMode(True)
        # Añadimos etiquetas
        tabulador.addTab(Color("Red"), "Rojo")   # Se coloca el widget y el nombre para la pestaña
        tabulador.addTab(Color("Green"), "Verde")
        tabulador.addTab(Color("Blue"), "Azul")

        # Ejemplo de conexión de señal:
        # tabulador.currentChanged.connect(self.cambioPestania)
        # def cambioPestania(self, index):
        #     print(f"Pestaña activa: {index}")

        self.setCentralWidget(tabulador) #Como es un QTabWidget, se coloca directamente
        self.show()

if __name__ == "__main__":
    app = QApplication()
    ventana = ventanaPrincipal()
    app.exec()