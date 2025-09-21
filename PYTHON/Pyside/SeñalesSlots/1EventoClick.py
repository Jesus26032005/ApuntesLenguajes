#Señales o eventos 
#Slot funciones que responden a las señales

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QAction
from PySide6.QtCore import QSize

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Señales y Slots")
        self.setFixedSize(QSize(400, 300))
        boton= QPushButton("Haz Click Aquí")
        #TODO: Conectar evento signal con el slot llamado eventoClick
        # clicked: Señal que emite el botón al ser presionado.
        # connect(slot): Conecta la señal a una función (slot).
        boton.clicked.connect(self._eventoClick)
        self.setCentralWidget(boton)
        self.show()

    def _eventoClick(self):
        print("Botón clickeado!")

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    # Ejecuta la aplicación
    app.exec()