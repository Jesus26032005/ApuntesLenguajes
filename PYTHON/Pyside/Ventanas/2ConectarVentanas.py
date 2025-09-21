from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit
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
        # QVBoxLayout(): Layout vertical para organizar widgets en columna.
        # QLabel(text: str): Widget para mostrar texto.
        # addWidget(widget: QWidget): Añade un widget al layout.
        # setLayout(layout: QLayout): Asigna un layout al widget.

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        # Se usa self.NuevaVentana como atributo para poder acceder a la instancia de la ventana secundaria
        # desde cualquier método de la clase y así controlar su ciclo de vida (mostrar, ocultar, cerrar, etc).
        self.NuevaVentana = NuevaVentana()
        self.setWindowTitle("Ventanas")
        self.setGeometry(100, 100, 800, 600)
        self.boton = QPushButton("Abrir Nueva Ventana", self)
        self.boton.clicked.connect(self.abrir_nueva_ventana)
        # QPushButton(text: str, parent: QWidget): Crea un botón.
        # setCentralWidget(widget: QWidget): Coloca el widget como contenido central de la ventana principal.
        # clicked.connect(función): Conecta la señal clicked del botón a una función.

        # QLineEdit es un widget para entrada de texto de una sola línea.
        self.EntradaTexto = QLineEdit(self)
        self.EntradaTexto.textChanged.connect(self.NuevaVentana.etiqueta.setText)
        # textChanged.connect(función): Señal que se emite cuando el texto cambia.
        # Aquí se conecta directamente al método setText del QLabel de la ventana secundaria,
        # así cada vez que se escribe algo, el texto de la etiqueta en la ventana secundaria se actualiza.

        # Se crea un layout vertical para organizar los widgets en la ventana principal.
        layout = QVBoxLayout()
        layout.addWidget(self.EntradaTexto)
        layout.addWidget(self.boton)
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)
        self.show()
        # Métodos usados:
        # QVBoxLayout(): Layout vertical para organizar widgets.
        # addWidget(widget: QWidget): Añade un widget al layout.
        # setLayout(layout: QLayout): Asigna el layout al contenedor.
        # setCentralWidget(widget: QWidget): Coloca el contenedor como widget central.
        # show(): Muestra la ventana principal.

    def abrir_nueva_ventana(self):
        # Este método controla la apertura y cierre de la ventana secundaria.
        # Se usa self.NuevaVentana como atributo para mantener la referencia y evitar múltiples instancias.
        if self.NuevaVentana.isVisible():
            self.NuevaVentana.hide()  # Oculta la ventana secundaria si ya está visible.
        else:
            self.NuevaVentana.show()  # Muestra la ventana secundaria si está oculta.
        # Métodos usados:
        # isVisible(): Devuelve True si la ventana está visible.
        # hide(): Oculta la ventana secundaria.
        # show(): Muestra la ventana secundaria.

if __name__ == "__main__":
    app = QApplication()
    ventana = ventanaPrincipal()
    app.exec()
    # QApplication(): Inicializa la aplicación Qt.
    # app.exec(): Inicia el bucle de eventos de la aplicación.