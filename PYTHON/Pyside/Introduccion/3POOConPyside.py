import sys
from PySide6.QtWidgets import QApplication, QMainWindow

# class ventanaPyside(QApplication):
#     def __init__():
#         self.ventana= QMainWindow()
#         self.ventana.setWindowTitle("POO con PySide")
#         self.ventana.resize(500, 500)
#         self.ventana.show()

# if __name__ == "__main__":
#     aplicacion=QApplication()
#     ventana=ventanaPyside()
#     sys.exit(aplicacion.exec())


#Version mejorada
class ventanaPyside(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("POO con PySide")
        self.resize(500, 500)
        self.show()

if __name__ == "__main__":
    aplicacion=QApplication()
    ventana=ventanaPyside()
    sys.exit(aplicacion.exec())