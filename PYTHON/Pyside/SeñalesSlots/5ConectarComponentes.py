from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget
from PySide6.QtGui import QAction
from PySide6.QtCore import QSize

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conectar Componentes")
        self.setMinimumSize(QSize(400, 300))
        # Crear label y campo de texto
        self.etiqueta = QLabel()
        self.entradaTexto = QLineEdit()
        # Conectar la señal textChanged del QLineEdit al slot setText del QLabel
        # Esto hace que cada vez que el texto cambie en la caja de texto, el label se actualice automáticamente
        self.entradaTexto.textChanged.connect(self.etiqueta.setText)
        
        # Crear un layout vertical (QVBoxLayout) para organizar los widgets de arriba hacia abajo
        layout = QVBoxLayout()
        layout.addWidget(self.entradaTexto)  # Añade el QLineEdit al layout
        layout.addWidget(self.etiqueta)      # Añade el QLabel al layout

        # En QMainWindow, no se puede asignar un layout directamente,
        # por eso se debe crear un QWidget contenedor, asignarle el layout,
        # y luego establecer ese QWidget como el centralWidget de la ventana principal.
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)  # Establece el contenedor como widget central

        # self.show() se puede llamar aquí o en el main, muestra la ventana

        # --- QVBoxLayout ---
        # QVBoxLayout es un layout que organiza widgets verticalmente.
        # Métodos útiles:
        #   addWidget(widget, stretch=0, alignment=0): añade un widget al layout.
        #   addLayout(layout, stretch=0): añade otro layout.
        #   insertWidget(index, widget, stretch=0, alignment=0): inserta widget en posición específica.
        #   setSpacing(espacio): define el espacio entre widgets.
        #   setContentsMargins(left, top, right, bottom): define los márgenes del layout.
        #   count(): número de widgets/layouts en el layout.
        #   itemAt(index): obtiene el QLayoutItem en la posición dada.
        #   takeAt(index): remueve y retorna el QLayoutItem en la posición dada.

        # --- QWidget ---
        # QWidget es la clase base de todos los objetos visuales.
        # Métodos útiles:
        #   setLayout(layout): asigna un layout al widget.
        #   setFixedSize(ancho, alto): fija el tamaño del widget.
        #   setMinimumSize(ancho, alto): tamaño mínimo.
        #   setMaximumSize(ancho, alto): tamaño máximo.
        #   setStyleSheet("css"): aplica estilos CSS.
        #   show(): muestra el widget.
        #   hide(): oculta el widget.

        # --- QMainWindow ---
        # QMainWindow es una ventana principal con soporte para menús, barras de herramientas, barra de estado, etc.
        # Métodos útiles:
        #   setCentralWidget(widget): define el widget central.
        #   addToolBar(toolbar): añade una barra de herramientas.
        #   statusBar(): retorna la barra de estado.
        #   menuBar(): retorna la barra de menús.
        #   setWindowTitle(titulo): define el título de la ventana.
        #   setMinimumSize(QSize): define el tamaño mínimo.
        #   resize(ancho, alto): cambia el tamaño de la ventana.

        # --- Argumentos de QVBoxLayout ---
        # QVBoxLayout(parent: QWidget = None)
        # parent: el widget padre del layout (opcional).

        # --- Argumentos de setCentralWidget ---
        # setCentralWidget(widget: QWidget)
        # widget: el widget que será el contenido principal de la ventana.

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    app.exec()