from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor

class Color(QWidget): #Crea un widget de color
    def __init__(self, nuevo_color):
        super().__init__()
        self.setAutoFillBackground(True)
        paletaColores = self.palette()
        paletaColores.setColor(QPalette.Window, QColor(nuevo_color))
        self.setPalette(paletaColores)

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo QStackedLayout")
        layoutPrincipal = QVBoxLayout()
        layoutOpciones = QHBoxLayout()
        layoutCambiante = QStackedLayout()

        layoutPrincipal.addLayout(layoutOpciones)
        layoutPrincipal.addLayout(layoutCambiante)

        # Añadimos botones para cambiar entre vistas
        boton = QPushButton("Cambiar a Vista 1")
        boton.clicked.connect(lambda: layoutCambiante.setCurrentIndex(0))
        layoutOpciones.addWidget(boton)

        boton = QPushButton("Cambiar a Vista 2")
        boton.clicked.connect(lambda: layoutCambiante.setCurrentIndex(1))
        layoutOpciones.addWidget(boton)

        boton = QPushButton("Cambiar a Vista 3")
        boton.clicked.connect(lambda: layoutCambiante.setCurrentIndex(2))
        layoutOpciones.addWidget(boton)

        layoutCambiante.addWidget(Color("red"))
        layoutCambiante.addWidget(Color("green"))
        layoutCambiante.addWidget(Color("blue"))

        componente = QWidget()
        componente.setLayout(layoutPrincipal)
        self.setCentralWidget(componente)
        self.show()

if __name__ == "__main__":
    app = QApplication()
    ventana = ventanaPrincipal()
    app.exec()