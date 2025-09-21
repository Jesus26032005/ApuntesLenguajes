from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QMenu
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt
from random import randint

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu contextual")
        self.setGeometry(100, 100, 800, 600)
        # Mostrar la ventana principal
        self.show()
        # Nos conectamos a la señal de customContextMenuRequested
        # setContextMenuPolicy(Qt.CustomContextMenu): Permite definir un menú contextual personalizado.
        # Qt.CustomContextMenu es una constante que indica que el menú contextual será gestionado por el usuario.
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        # customContextMenuRequested es una señal que se emite cuando se solicita el menú contextual (clic derecho).
        # Se conecta al método mostrarMenuContextual, que recibe la posición del mouse.
        self.customContextMenuRequested.connect(self.mostrarMenuContextual)

    def mostrarMenuContextual(self, pos):  # Se recibe directamente la posición del mouse
        # QMenu(self): Crea un menú contextual asociado a la ventana principal.
        menuContextual = QMenu(self)

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

        # mapToGlobal(pos): Convierte la posición local del mouse a coordenadas globales de pantalla.
        # menuContextual.exec(globalPos): Muestra el menú contextual en la posición del mouse.
        menuContextual.exec(self.mapToGlobal(pos))

        # Métodos y constantes usados:
        # setContextMenuPolicy(policy): Define la política de menú contextual (Qt.DefaultContextMenu, Qt.CustomContextMenu, etc).
        # customContextMenuRequested: Señal emitida al solicitar el menú contextual.
        # QMenu: Widget para menús contextuales o de barra de menús.
        # QAction: Representa una acción que puede estar en menús, barras de herramientas, etc.
        # triggered: Señal emitida cuando se selecciona la acción.
        # addAction(action): Añade una acción al menú.
        # mapToGlobal(pos): Convierte coordenadas locales a globales.
        # exec(pos): Muestra el menú en la posición indicada.

        # Se usan atributos (como self) para poder acceder a los widgets y métodos desde cualquier parte de la clase,
        # facilitando la gestión de eventos y la interacción entre componentes.

if __name__ == "__main__":
    app = QApplication()
    ventana = ventanaPrincipal()
    app.exec()
    # QApplication(): Inicializa la aplicación Qt.
    # app.exec(): Inicia el bucle de eventos de la aplicación.