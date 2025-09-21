from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor

class Color(QWidget): #Crea un widget de color
    def __init__(self, nuevo_color):
        super().__init__()
        # Indicamos que se puede agregar un color de fondo
        self.setAutoFillBackground(True)
        paletaColores = self.palette()
        # Creamos el componente de color de fondo aplicando el nuevo color
        paletaColores.setColor(QPalette.Window, QColor(nuevo_color))
        # Aplicamos el nuevo color al componente
        self.setPalette(paletaColores)

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout anidados")
        #Creamos primer layout horizontal y vertical
        layoutHorizontal = QHBoxLayout()
        layoutVertical = QVBoxLayout()

        #Algunso widgets al vertical
        layoutVertical.addWidget(Color("red"))
        layoutVertical.addWidget(Color("blue"))
        layoutVertical.addWidget(Color("cyan"))

        #Agrega layour vertical dentro del horizontal, es decir, anidado, uno dentro de otro
        layoutHorizontal.addLayout(layoutVertical)
        # Añaden otros elementos
        layoutHorizontal.addWidget(Color("Green"))
        layoutHorizontal.addWidget(Color("Yellow"))

        componente = QWidget()
        #Se coloca el layout que contiene todo
        componente.setLayout(layoutHorizontal)
        self.setCentralWidget(componente)
        self.show()

if __name__ == "__main__":
    app = QApplication()
    ventana = ventanaPrincipal()
    app.exec()