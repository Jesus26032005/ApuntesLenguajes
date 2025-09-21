from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel
from random import randint

class NuevaVentana(QWidget):  # Podemos usar cualquier clase que sea un componente QWidget
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nueva Ventana")
        self.setGeometry(100, 100, 400, 300)
        layout = QVBoxLayout()
        self.etiqueta = QLabel(f'Nueva ventana:{randint(0,100)}')
        layout.addWidget(self.etiqueta)
        self.setLayout(layout)
        # Métodos usados:
        # setWindowTitle(title: str): Cambia el título de la ventana.
        # setGeometry(x: int, y: int, width: int, height: int): Define la posición y tamaño de la ventana.
        # setLayout(layout: QLayout): Asigna un layout al widget.
        # QLabel(text: str): Widget para mostrar texto.
        # QVBoxLayout(): Layout vertical para organizar widgets en columna.
        # addWidget(widget: QWidget): Añade un widget al layout.

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        # Se usa self.NuevaVentana como atributo para poder acceder a la instancia de la ventana secundaria
        # desde cualquier método de la clase y así controlar su ciclo de vida (mostrar, ocultar, cerrar, etc).
        self.NuevaVentana = None
        # Si se quiere tener solo una instancia, se inicializa la ventana aquí y luego solo se muestra/oculta.
        self.setWindowTitle("Ventanas")
        self.setGeometry(100, 100, 800, 600)
        self.boton = QPushButton("Abrir Nueva Ventana", self)
        self.setCentralWidget(self.boton)
        self.boton.clicked.connect(self.abrir_nueva_ventana)
        self.show()
        # Métodos usados:
        # setWindowTitle(title: str): Cambia el título de la ventana principal.
        # setGeometry(x: int, y: int, width: int, height: int): Define la posición y tamaño de la ventana.
        # QPushButton(text: str, parent: QWidget): Crea un botón.
        # setCentralWidget(widget: QWidget): Coloca el widget como contenido central de la ventana principal.
        # clicked.connect(función): Conecta la señal clicked del botón a una función.
        # show(): Muestra la ventana.

    def abrir_nueva_ventana(self):
        # Este método controla la apertura y cierre de la ventana secundaria.
        # Se usa self.NuevaVentana como atributo para mantener la referencia y evitar múltiples instancias.
        if self.NuevaVentana is None:  # Si no se ha instanciado, se crea la ventana y se muestra
            self.NuevaVentana = NuevaVentana()
            self.NuevaVentana.show()
        else:
            self.NuevaVentana.close()  # Se cierra la ventana de forma segura
            self.NuevaVentana = None

        """
        TODO: Si se quiere tener solo una instancia, se inicializa la ventana en el __init__ y ahora se hace esto:
        if self.NuevaVentana.isVisible():
            self.NuevaVentana.hide()
        else:
            self.NuevaVentana.show()
        """
        # Métodos usados:
        # show(): Muestra la ventana secundaria.
        # close(): Cierra la ventana secundaria.
        # isVisible(): Devuelve True si la ventana está visible.
        # hide(): Oculta la ventana secundaria.

if __name__ == "__main__":
    app = QApplication()
    ventana = ventanaPrincipal()
    app.exec()
    # QApplication(): Inicializa la aplicación Qt.
    # app.exec(): Inicia el bucle de eventos de la aplicación.