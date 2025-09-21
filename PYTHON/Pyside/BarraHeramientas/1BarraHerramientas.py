from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor, QAction

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Barra herramientas parte 1")
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
        # clear(): Elimina todas las acciones y widgets de la barra.
        # Señales de QToolBar:
        # actionTriggered(QAction): Se emite cuando se activa una acción de la barra.

        # Se crea barra de herramientas
        barraHerramientas = QToolBar("Barra de herramientas")
        self.addToolBar(barraHerramientas)

        # QAction representa una acción que puede ser añadida a menús, barras de herramientas, etc.
        # QAction(text: str, parent: QObject = None)
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

        # Se añaden elemento a la barra de herramientas
        botonAccion = QAction("Botón de acción", self)
        # Agregamos botón a la barra
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

        # Barra de estado (se muestra en parte inferior para mostrar ciertas cosas)
        self.setStatusBar(QStatusBar(self))

        # Agregamos un mensaje del botón de acción
        botonAccion.setStatusTip("Este es un botón de acción")
        # Asociamos el evento click
        botonAccion.triggered.connect(self._clickAccion)
        # Hacemos checkable el botón
        botonAccion.setCheckable(True)

        self.show()

    def _clickAccion(self, s):
        print("Botón de acción clicado")
        print(f'Estado {s}')

if __name__ == "__main__":
    app = QApplication()
    ventana = ventanaPrincipal()
    app.exec()