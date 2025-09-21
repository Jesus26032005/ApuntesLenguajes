from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QMenu
from PySide6.QtGui import QAction, QIcon
from random import randint

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu contextual")
        self.setGeometry(100, 100, 800, 600)
        self.show()
        # Métodos usados:
        # setWindowTitle(title: str): Cambia el título de la ventana principal.
        # setGeometry(x: int, y: int, width: int, height: int): Define la posición y tamaño de la ventana.
        # show(): Muestra la ventana principal.

    def contextMenuEvent(self, event):
        # contextMenuEvent(event): Método especial de QWidget que se llama automáticamente
        # cuando el usuario solicita el menú contextual (normalmente clic derecho).
        # event: objeto QContextMenuEvent con información sobre la posición del mouse.
        menuContextual = QMenu(self)  # QMenu(self): Crea un menú contextual asociado a la ventana principal.

        # QAction(QIcon, texto, parent): Crea una acción con ícono y texto.
        # triggered.connect(función): Conecta la señal triggered (cuando se selecciona la acción) a una función.
        accion1 = QAction(QIcon("Pyside/ManejoEventos/imagen.png"), "Opción 1", self)
        accion1.triggered.connect(lambda: print("Opción 1 seleccionada"))
        menuContextual.addAction(accion1)

        accion2 = QAction(QIcon("Pyside/ManejoEventos/imagen.png"), "Opción 2", self)
        accion2.triggered.connect(lambda: print("Opción 2 seleccionada"))
        menuContextual.addAction(accion2)

        accion3 = QAction(QIcon("Pyside/ManejoEventos/imagen.png"), "Opción 3", self)
        accion3.triggered.connect(lambda: print("Opción 3 seleccionada"))
        menuContextual.addAction(accion3)

        # exec(pos): Muestra el menú contextual en la posición indicada (globalPos).
        menuContextual.exec(event.globalPos())

        # Métodos y constantes usados:
        # QMenu: Widget para menús contextuales o de barra de menús.
        # QAction: Representa una acción que puede estar en menús, barras de herramientas, etc.
        # triggered: Señal emitida cuando se selecciona la acción.
        # addAction(action): Añade una acción al menú.
        # exec(pos): Muestra el menú en la posición indicada.
        # event.globalPos(): Devuelve la posición global del mouse en la pantalla.
        # Se usan atributos (como self) para poder acceder a los widgets y métodos desde cualquier parte de la clase,
        # facilitando la gestión de eventos y la interacción entre componentes.

if __name__ == "__main__":
    app = QApplication()
    ventana = ventanaPrincipal()
    app.exec()
    # QApplication(): Inicializa la aplicación Qt.
    # app.exec(): Inicia el bucle de eventos de la aplicación.