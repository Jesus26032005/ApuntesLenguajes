from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor

class Color(QWidget): #Crea un widget de color
    def __init__(self, nuevo_color):
        super().__init__()
        # Indicamos que se puede agregar un color de fondo
        self.setAutoFillBackground(True)
        paletaColores = self.palette()
        # Creamos el componente de color de fondo aplicando el nuevo color
        paletaColores.setColor(QPalette.Window, QColor(nuevo_color))
        # Aplicamos el nuevo color al componente
        self.setPalette(paletaColores)

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout vertical y horizontal")

        # Un layout en Qt (y en PySide6) es un administrador de diseño que organiza y distribuye automáticamente
        # los widgets (componentes visuales) dentro de una ventana o contenedor.
        # ¿Para qué sirve un layout?
        # - Permite que los widgets se acomoden automáticamente cuando cambias el tamaño de la ventana.
        # - Evita que tengas que calcular manualmente posiciones y tamaños.
        # - Hace que la interfaz sea flexible y adaptable a diferentes resoluciones o tamaños de ventana.
        # Tipos comunes de layouts:
        #   QVBoxLayout: Organiza los widgets en una columna vertical (uno debajo del otro).
        #   QHBoxLayout: Organiza los widgets en una fila horizontal (uno al lado del otro).
        #   QGridLayout: Organiza los widgets en una cuadrícula (filas y columnas).
        #   QFormLayout: Organiza widgets en pares etiqueta-campo, útil para formularios.
        # ¿Cómo se usa?
        # 1. Creas el layout (por ejemplo, QVBoxLayout()).
        # 2. Agregas widgets al layout con addWidget().
        # 3. Asignas el layout a un widget contenedor usando setLayout().

        # QVBoxLayout: Organiza los widgets en una columna vertical.
        layoutVertical = QVBoxLayout()  # Creamos un layout vertical
        # Agregamos componentes de color al layout vertical
        layoutVertical.addWidget(Color("Red"))
        layoutVertical.addWidget(Color("Green"))
        layoutVertical.addWidget(Color("Blue"))
        # Para poder publicar un layout necesitamos crear un componente, un layout no se puede publicar directamente
        # Creamos componente genérico
        componente = QWidget()
        componente.setLayout(layoutVertical)  # Asignamos el layout al componente

        # QHBoxLayout: Organiza los widgets en una fila horizontal.
        layoutHorizontal = QHBoxLayout()  # Creamos un layout horizontal
        layoutHorizontal.addWidget(Color("Cyan"))
        layoutHorizontal.addWidget(Color("Magenta"))
        layoutHorizontal.addWidget(Color("Yellow"))
        #componente.setLayout(layoutHorizontal)

        # Métodos principales de QVBoxLayout/QHBoxLayout (heredan de QLayout):
        # addWidget(widget: QWidget, stretch: int = 0, alignment: Qt.Alignment = 0):
        #   Añade un widget al layout. stretch controla el espacio extra, alignment la alineación.
        # addLayout(layout: QLayout, stretch: int = 0):
        #   Añade otro layout dentro de este layout.
        # insertWidget(index: int, widget: QWidget, stretch: int = 0, alignment: Qt.Alignment = 0):
        #   Inserta un widget en una posición específica.
        # setSpacing(spacing: int): Define el espacio entre widgets.
        # setContentsMargins(left: int, top: int, right: int, bottom: int): Define los márgenes del layout.
        # count() -> int: Número de widgets/layouts en el layout.
        # itemAt(index: int) -> QLayoutItem: Obtiene el elemento en la posición dada.
        # takeAt(index: int) -> QLayoutItem: Remueve y retorna el elemento en la posición dada.

        # QWidget es la clase base para todos los componentes visuales en Qt.
        # QWidget(parent: QWidget = None, flags: Qt.WindowFlags = 0)
        # Métodos principales de QWidget:
        # setLayout(layout: QLayout): Asigna un layout al widget.
        # setFixedSize(width: int, height: int): Fija el tamaño del widget.
        # setMinimumSize(width: int, height: int): Tamaño mínimo.
        # setMaximumSize(width: int, height: int): Tamaño máximo.
        # setGeometry(x: int, y: int, width: int, height: int): Posición y tamaño.
        # setWindowTitle(title: str): Cambia el título de la ventana.
        # setVisible(visible: bool): Muestra u oculta el widget.
        # show(): Muestra el widget.
        # hide(): Oculta el widget.
        # setEnabled(enabled: bool): Habilita o deshabilita el widget.
        # setStyleSheet(css: str): Aplica estilos CSS.
        # setAutoFillBackground(enabled: bool): Permite rellenar el fondo con el color de la paleta.
        # setPalette(palette: QPalette): Asigna una paleta de colores al widget.
        # setToolTip(text: str): Muestra un tooltip al pasar el mouse.

        # QWidget no tiene señales propias, pero puedes usar eventos sobreescribiendo métodos:
        # mousePressEvent, mouseReleaseEvent, mouseDoubleClickEvent, keyPressEvent, keyReleaseEvent,
        # enterEvent, leaveEvent, paintEvent, resizeEvent, closeEvent, etc.

        self.setCentralWidget(componente)
        self.show()

if __name__ == "__main__":
    app = QApplication()
    ventana = ventanaPrincipal()
    app.exec()