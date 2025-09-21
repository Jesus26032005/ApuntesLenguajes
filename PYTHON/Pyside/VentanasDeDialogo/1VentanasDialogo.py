from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventanas de dialogo")
        # Es una ventana que depende de otra ventana para interactuar con el usuario.
        self.setGeometry(100, 100, 800, 600)
        # Se construye botón
        boton = QPushButton("Abrir ventana de dialogo")
        boton.clicked.connect(self.abrirVentanaDialogo)
        self.setCentralWidget(boton)
        self.show()

    def abrirVentanaDialogo(self, estado):
        print("Abrir ventana de dialogo")
        # QDialog es una ventana secundaria para interacción temporal con el usuario.
        # QDialog(parent: QWidget = None, flags: Qt.WindowFlags = 0)
        # Argumentos:
        #   parent: widget padre (usualmente la ventana principal).
        #   flags: opciones de ventana (opcional).
        # Métodos principales de QDialog:
        # exec() -> int:
        #   Muestra el diálogo de forma modal (bloquea la ventana principal hasta que se cierre).
        # show():
        #   Muestra el diálogo de forma no modal (no bloquea la ventana principal).
        # accept():
        #   Cierra el diálogo y retorna QDialog.Accepted.
        # reject():
        #   Cierra el diálogo y retorna QDialog.Rejected.
        # setWindowTitle(title: str):
        #   Cambia el título de la ventana de diálogo.
        # setModal(modal: bool):
        #   Define si el diálogo es modal o no.
        # setGeometry(x: int, y: int, width: int, height: int):
        #   Posición y tamaño de la ventana.
        # setWindowIcon(icon: QIcon):
        #   Cambia el ícono de la ventana.
        # setWindowIconText(text: str):
        #   Texto alternativo para el ícono de la ventana.
        # Señales de QDialog:
        # accepted(): Se emite cuando se acepta el diálogo (accept()).
        # rejected(): Se emite cuando se rechaza el diálogo (reject()).
        # finished(int result): Se emite cuando el diálogo se cierra, con el resultado (Accepted/Rejected).

        dialogo = QDialog(self)
        dialogo.setWindowIconText("Soy una ventana interna pa") # Texto alternativo para el ícono de la ventana
        dialogo.exec() # Se ejecuta ventana de diálogo de forma modal (bloquea la ventana principal hasta que se cierre)

if __name__ == "__main__":
    app = QApplication()
    ventana = ventanaPrincipal()
    app.exec()