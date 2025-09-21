from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPalette, QColor, QAction, QIcon

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Barra herramientas parte 2 iconos")

        # QMainWindow.menuBar() devuelve el menú principal de la ventana.
        # Se usa self.menuBar() porque QMainWindow ya tiene integrado un menú principal,
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

        # QMenu representa un menú desplegable.
        # Métodos principales de QMenu:
        # addAction(text: str) -> QAction:
        #   Añade una acción al menú con el texto dado.
        # addAction(icon: QIcon, text: str) -> QAction:
        #   Añade una acción con ícono y texto.
        # addSeparator(): Añade una línea separadora.
        # addMenu(menu: QMenu): Añade un submenú.
        # insertAction(before: QAction, action: QAction): Inserta una acción antes de otra.
        # removeAction(action: QAction): Elimina una acción del menú.
        # clear(): Elimina todas las acciones del menú.
        # setTitle(title: str): Cambia el texto del menú.
        # setIcon(icon: QIcon): Cambia el ícono del menú.

        # Señales de QMenu:
        # triggered(QAction): Se emite cuando se activa una acción del menú.
        # hovered(QAction): Se emite cuando el mouse pasa sobre una acción.

        # Ejemplo de uso:
        menu = self.menuBar()  # Devuelve la barra de menús principal de la ventana
        menuArchivo = menu.addMenu("&Archivo")  # Añade un menú llamado "Archivo" (& activa el atajo Alt+A)
        menuArchivo.addAction("Nuevo")          # Añade acción "Nuevo"
        menuArchivo.addAction("Guardar")        # Añade acción "Guardar"
        menuArchivo.addSeparator()              # Añade una línea separadora
        menuArchivo.addAction("Salir")          # Añade acción "Salir"

        # Puedes conectar señales para reaccionar a acciones:
        # menuArchivo.triggered.connect(self._accionMenu)
        # def _accionMenu(self, accion):
        #     print(f"Acción seleccionada: {accion.text()}")

        self.show()

    def _clickAccion(self, s):
        print("Botón de acción clicado")
        print(f'Estado {s}')

if __name__ == "__main__":
    app = QApplication()
    ventana = ventanaPrincipal()
    app.exec()