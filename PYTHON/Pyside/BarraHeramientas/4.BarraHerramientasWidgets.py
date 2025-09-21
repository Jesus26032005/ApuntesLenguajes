from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPalette, QColor, QAction, QIcon

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Barra herramientas widgets")
        # Publicamos etiqueta barra
        label = QLabel("Barra de herramientas", self)
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        # QToolBar es un widget para crear barras de herramientas con botones, menús, etc.
        # QToolBar(title: str = '', parent: QWidget = None)
        # Métodos principales de QToolBar:
        # addAction(action: QAction): Añade una acción (botón) a la barra.
        # addWidget(widget: QWidget): Añade un widget personalizado a la barra.
        # addSeparator(): Añade un separador visual.
        # insertAction(before: QAction, action: QAction): Inserta una acción antes de otra.
        # removeAction(action: QAction): Elimina una acción de la barra.
        # setMovable(movable: bool): Permite mover la barra (por defecto True).
        # setFloatable(floatable: bool): Permite desacoplar la barra (por defecto True).
        # setOrientation(orientation: Qt.Orientation): Cambia la orientación (Qt.Horizontal o Qt.Vertical).
        # setAllowedAreas(areas: Qt.ToolBarAreas): Define en qué áreas se puede colocar la barra.
        # setIconSize(size: QSize): Define el tamaño de los íconos en la barra.
        # setToolButtonStyle(style: Qt.ToolButtonStyle): Cambia el estilo de los botones (icono, texto, ambos, etc).
        # clear(): Elimina todas las acciones y widgets de la barra.
        # Señales de QToolBar:
        # actionTriggered(QAction): Se emite cuando se activa una acción de la barra.

        barraHerramientas = QToolBar("Barra de herramientas")
        barraHerramientas.setIconSize(QSize(16, 16))  # Tamaño de los íconos (ancho, alto)
        # setToolButtonStyle(style: Qt.ToolButtonStyle): Cambia el estilo de los botones de la barra.
        # Valores posibles:
        #   Qt.ToolButtonFollowStyle: Usa el estilo por defecto del sistema operativo.
        #   Qt.ToolButtonTextOnly: Solo muestra texto.
        #   Qt.ToolButtonIconOnly: Solo muestra icono.
        #   Qt.ToolButtonTextBesideIcon: Texto a la derecha del icono.
        #   Qt.ToolButtonTextUnderIcon: Texto debajo del icono.
        barraHerramientas.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        barraHerramientas.setToolButtonStyle(Qt.ToolButtonTextOnly)
        barraHerramientas.setToolButtonStyle(Qt.ToolButtonIconOnly)
        barraHerramientas.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        barraHerramientas.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(barraHerramientas)

        # QAction representa una acción que puede ser añadida a menús, barras de herramientas, etc.
        # QAction(icon: QIcon, text: str, parent: QObject = None)
        # Métodos principales de QAction:
        # setText(text: str): Cambia el texto de la acción.
        # setIcon(icon: QIcon): Asigna un ícono a la acción.
        # setShortcut(shortcut: QKeySequence | str): Asigna un atajo de teclado.
        # setStatusTip(tip: str): Texto que se muestra en la barra de estado al pasar el mouse.
        # setCheckable(checkable: bool): Permite que la acción sea tipo check (activada/desactivada).
        # setChecked(checked: bool): Marca o desmarca la acción.
        # isChecked() -> bool: Devuelve si está marcada.
        # triggered[bool].connect(función): Señal que se emite cuando se activa la acción.
        # toggled[bool].connect(función): Señal que se emite cuando cambia el estado check.
        # hovered.connect(función): Señal que se emite cuando el mouse pasa sobre la acción.

        # QIcon es una clase para manejar íconos en Qt.
        # QIcon(filename: str)  # Crea un ícono a partir de un archivo de imagen.
        # Métodos principales de QIcon:
        # addFile(filename: str, size: QSize = QSize(), mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off):
        #   Añade una imagen al ícono para diferentes tamaños, modos y estados.
        # isNull() -> bool: Devuelve True si el ícono está vacío.
        # pixmap(size: QSize, mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off) -> QPixmap:
        #   Devuelve un QPixmap del ícono en el tamaño y modo especificados.

        botonAccion = QAction(QIcon("Pyside/BarraHeramientasMenus/imagen.png"), "Botón de acción", self)
        barraHerramientas.addAction(botonAccion)

        # QStatusBar es una barra en la parte inferior de la ventana para mostrar mensajes de estado.
        # QStatusBar(parent: QWidget = None)
        # Métodos principales de QStatusBar:
        # showMessage(message: str, timeout: int = 0): Muestra un mensaje por un tiempo (ms), 0 = indefinido.
        # clearMessage(): Borra el mensaje actual.
        # addWidget(widget: QWidget, stretch: int = 0): Añade un widget a la barra.
        # addPermanentWidget(widget: QWidget, stretch: int = 0): Añade un widget permanente.
        # currentMessage() -> str: Devuelve el mensaje actual.
        # Señales de QStatusBar:
        # messageChanged(str): Se emite cuando cambia el mensaje.

        self.setStatusBar(QStatusBar(self))
        # setStatusTip(tip: str): El texto se muestra en la barra de estado cuando el mouse pasa sobre la acción.
        botonAccion.setStatusTip("Nuevo")
        # triggered[bool].connect(función): Señal que se emite cuando se activa la acción.
        botonAccion.triggered.connect(self._clickAccion)
        # setCheckable(checkable: bool): Permite que la acción sea tipo check (activada/desactivada).
        botonAccion.setCheckable(True)

        self.show()

    def _clickAccion(self, s):
        print("Botón de acción clicado")
        print(f'Estado {s}')

if __name__ == "__main__":
    app = QApplication()
    ventana = ventanaPrincipal()
    app.exec()