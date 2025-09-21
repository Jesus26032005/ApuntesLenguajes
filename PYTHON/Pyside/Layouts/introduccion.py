from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette

class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        # QWidget es la clase base para todos los componentes visuales en Qt.
        # QWidget(parent: QWidget = None, flags: Qt.WindowFlags = 0)
        # parent: el widget padre (opcional).
        # flags: opciones de ventana (opcional), por ejemplo Qt.Window, Qt.Dialog, etc.

        # Métodos principales de QWidget y sus argumentos:
        # setAutoFillBackground(enabled: bool): Si es True, el fondo se rellena automáticamente con el color de la paleta.
        # palette() -> QPalette: Devuelve la paleta de colores actual del widget.
        # setPalette(palette: QPalette): Asigna una paleta de colores al widget.
        # setStyleSheet(styleSheet: str): Aplica estilos CSS al widget.
        # setFixedSize(width: int, height: int): Fija el tamaño del widget.
        # setMinimumSize(width: int, height: int): Establece el tamaño mínimo.
        # setMaximumSize(width: int, height: int): Establece el tamaño máximo.
        # setGeometry(x: int, y: int, width: int, height: int): Establece la posición y tamaño.
        # setWindowTitle(title: str): Cambia el título de la ventana (si el widget es una ventana).
        # setVisible(visible: bool): Muestra u oculta el widget.
        # show(): Muestra el widget.
        # hide(): Oculta el widget.
        # update(): Solicita una actualización/redibujado del widget.
        # setEnabled(enabled: bool): Habilita o deshabilita el widget.
        # setLayout(layout: QLayout): Asigna un layout para organizar widgets hijos.
        # setCursor(cursor: QCursor): Cambia el cursor cuando está sobre el widget.
        # setToolTip(text: str): Muestra un tooltip al pasar el mouse.

        # Señales (signals) de QWidget:
        # QWidget no tiene señales propias, pero puedes usar eventos sobreescribiendo métodos:
        # - mousePressEvent(self, event): Al presionar el mouse.
        # - mouseReleaseEvent(self, event): Al soltar el mouse.
        # - mouseDoubleClickEvent(self, event): Al hacer doble clic.
        # - keyPressEvent(self, event): Al presionar una tecla.
        # - keyReleaseEvent(self, event): Al soltar una tecla.
        # - enterEvent(self, event): Cuando el mouse entra en el área del widget.
        # - leaveEvent(self, event): Cuando el mouse sale del área del widget.
        # - paintEvent(self, event): Para personalizar el dibujo del widget.
        # - resizeEvent(self, event): Cuando cambia el tamaño del widget.
        # - closeEvent(self, event): Cuando se cierra el widget.

        # Indicamos que se puede agregar un color de fondo
        self.setAutoFillBackground(True)  # Habilitamos el llenado automático del fondo
        paleta = self.palette()  # Obtenemos la paleta de colores del widget
        # Creamos el componente de color de fondo aplicando nuevo color
        paleta.setColor(QPalette.Window, color)  # Creamos el componente de color de fondo aplicando nuevo color
        # Aplicamos el color al componente
        


        self.setPalette(paleta)  # Aplicamos el color al componente

        # QPalette es una clase que gestiona los colores usados por los widgets.
        # QPalette([color]): Crea una paleta de colores. Puedes pasar un color base o usar los métodos para personalizar.
        # Métodos principales de QPalette:
        # setColor(role: QPalette.ColorRole, color: QColor | Qt.GlobalColor | str):
        #   Asigna un color a un "rol" específico (por ejemplo, QPalette.Window, QPalette.WindowText, QPalette.Base, etc.).
        # color(role: QPalette.ColorRole) -> QColor:
        #   Devuelve el color asignado a un rol.
                #   - role: Especifica qué parte de la interfaz se va a colorear. Ejemplos:
        #       QPalette.Window         -> Fondo del widget
        #       QPalette.WindowText     -> Texto de la ventana
        #       QPalette.Base           -> Fondo de campos de entrada
        #       QPalette.Text           -> Texto en campos de entrada
        #       QPalette.Button         -> Fondo de botones
        #       QPalette.ButtonText     -> Texto de botones
        #       QPalette.Highlight      -> Color de selección
        #       QPalette.HighlightedText-> Texto seleccionado
        #   - color: Puede ser un QColor, un color global de Qt (ej: Qt.red), o un string ("red", "#FF0000", etc).
        #   Ejemplo:
        #       paleta.setColor(QPalette.Window, Qt.yellow)
        #       paleta.setColor(QPalette.WindowText, "blue")
        #       paleta.setColor(QPalette.Base, "#00FF00")



        # setBrush(role: QPalette.ColorRole, brush: QBrush):
        #   Asigna un pincel (brush) a un rol.
        # brush(role: QPalette.ColorRole) -> QBrush:
        #   Devuelve el pincel asignado a un rol.
        # isCopyOf(other: QPalette) -> bool:
        #   Indica si la paleta es copia de otra.
        # currentColorGroup() -> QPalette.ColorGroup:
        #   Devuelve el grupo de color actual (Active, Inactive, Disabled).

        # Roles de color comunes en QPalette:
        # QPalette.Window: Fondo del widget.
        # QPalette.WindowText: Texto de la ventana.
        # QPalette.Base: Fondo de campos de entrada.
        # QPalette.Text: Texto en campos de entrada.
        # QPalette.Button: Fondo de botones.
        # QPalette.ButtonText: Texto de botones.
        # QPalette.Highlight: Color de selección.
        # QPalette.HighlightedText: Texto seleccionado.

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Componentes Básicos")
        componenteConColor= Color("red")
        # El componente se expande para cubrir el tamaño disponible
        self.setCentralWidget(componenteConColor)
        self.show()

if __name__ == "__main__":
    app = QApplication()
    ventana = ventanaPrincipal()
    app.exec()