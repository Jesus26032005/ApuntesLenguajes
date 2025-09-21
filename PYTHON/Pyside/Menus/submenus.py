from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPalette, QColor, QAction, QIcon

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Barra herramientas parte 2 iconos")

        # QMainWindow.menuBar() devuelve la barra de menús principal de la ventana.
        # Se usa self.menuBar() porque QMainWindow ya tiene integrada una barra de menús,
        # y este método devuelve la instancia asociada a la ventana actual.
        # Así puedes agregar menús y acciones fácilmente a la barra de menús de la ventana.

        # Métodos principales de QMenuBar:
        # addMenu(title: str | QIcon, title: str) -> QMenu:
        #   Añade un menú desplegable a la barra de menús. Puedes pasar solo el texto o un ícono y texto.
        # insertMenu(before: QAction, menu: QMenu) -> QMenu:
        #   Inserta un menú antes de una acción específica.
        # addAction(action: QAction | str) -> QAction:
        #   Añade una acción directamente a la barra de menús.
        # clear(): Elimina todos los menús y acciones.
        # setNativeMenuBar(native: bool): Usa la barra de menús nativa del sistema operativo si es posible.
        # menuAction() -> QAction: Devuelve la acción asociada al menú.
        # Señales de QMenuBar:
        # triggered(QAction): Se emite cuando se activa una acción de cualquier menú.
        # hovered(QAction): Se emite cuando el mouse pasa sobre una acción.

        menu = self.menuBar()  # Devuelve la barra de menús principal de la ventana

        # QAction representa una acción que puede ser añadida a menús, barras de herramientas, etc.
        # QAction(text: str, parent: QObject = None)
        # QAction(icon: QIcon, text: str, parent: QObject = None)
        # Métodos principales de QAction:
        # setText(text: str): Cambia el texto de la acción.
        # setIcon(icon: QIcon): Asigna un ícono a la acción.
        # setShortcut(shortcut: QKeySequence | str): Asigna un atajo de teclado.
        #   El argumento puede ser una cadena como "Ctrl+Q" o un QKeySequence.
        #   Permite que el usuario active la acción usando el teclado.
        # setStatusTip(tip: str): Texto que se muestra en la barra de estado al pasar el mouse.
        # setCheckable(checkable: bool): Permite que la acción sea tipo check (activada/desactivada).
        # setChecked(checked: bool): Marca o desmarca la acción.
        # isChecked() -> bool: Devuelve si está marcada.
        # triggered[bool].connect(función): Señal que se emite cuando se activa la acción.
        # toggled[bool].connect(función): Señal que se emite cuando cambia el estado check.
        # hovered.connect(función): Señal que se emite cuando el mouse pasa sobre la acción.

        # Ejemplo de creación de menús y submenús:
        menuArchivo = menu.addMenu("&Archivo")  # Añade un menú llamado "Archivo" (& activa el atajo Alt+A)
        botonAction = QAction(QIcon("icono.png"), "Botón de acción", self)
        menuArchivo.addAction(botonAction)
        menuArchivo.addAction("Nuevo")          # Añade acción "Nuevo"
        menuArchivo.addAction("Guardar")        # Añade acción "Guardar"
        menuArchivo.addSeparator()              # Añade una línea separadora
        botonSalir = QAction("Salir", self)

        # setShortcut(shortcut: QKeySequence | str): Asigna un atajo de teclado a la acción.
        # Ejemplo: "Ctrl+Q" permite cerrar la aplicación con Ctrl+Q.
        botonSalir.setShortcut("Ctrl+Q")        # Asigna un atajo de teclado Ctrl+Q
        # También puedes usar: botonSalir.setShortcut(Qt.ControlModifier + Qt.Key_Q) para mejor funcionalidad en sistemas operativos
        menuArchivo.addAction(botonSalir)          # Añade acción "Salir"

        # Puedes crear submenús usando addMenu sobre un menú existente:
        menuOtro = menuArchivo.addMenu("Otro")
        menuOtro.addAction("Acción 1")
        menuOtro.addAction("Acción 2")
        menuOtro.addAction("Acción 3")
        menuOtro.addSeparator()
        menuOtro.addAction("Salir")

        # Añadir menú principal "Ayuda" y submenús
        menuAyuda = menu.addMenu("&Ayuda")
        menuAyuda.addAction("Acerca de")
        menuDocumentacion = menuAyuda.addMenu("Documentación")
        menuDocumentacion.addAction("Guía del usuario")
        menuDocumentacion.addAction("API")

        # Puedes conectar señales para reaccionar a acciones:
        # menuArchivo.triggered.connect(self._clickAccion)
        # def _clickAccion(self, accion):
        #     print(f"Acción seleccionada: {accion.text()}")

        self.show()

    def _clickAccion(self, s):
        print("Botón de acción clicado")
        print(f'Estado {s}')

if __name__ == "__main__":
    app = QApplication()
    ventana = ventanaPrincipal()
    app.exec()