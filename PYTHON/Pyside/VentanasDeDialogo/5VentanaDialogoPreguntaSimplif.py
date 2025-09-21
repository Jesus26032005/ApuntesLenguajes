from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventanas de dialogo pregunta")
        # Es una ventana que depende de otra ventana para interactuar con el usuario
        self.setGeometry(100, 100, 800, 600)
        # Se construye boton
        boton = QPushButton("Abrir ventana de dialogo")
        boton.clicked.connect(self.abrirVentanaDialogo)
        self.setCentralWidget(boton)
        self.show()

    def abrirVentanaDialogo(self, estado):
        print("Abrir ventana de dialogo")
        # Métodos estáticos de QMessageBox:
        # QMessageBox.question(parent, title, text, buttons=QMessageBox.StandardButtons, defaultButton=QMessageBox.StandardButton)
        #   Muestra un diálogo de pregunta (icono de pregunta, botones Yes/No por defecto).
        # QMessageBox.information(parent, title, text, buttons=..., defaultButton=...)
        #   Muestra un mensaje informativo (icono de información, botón Ok por defecto).
        # QMessageBox.warning(parent, title, text, buttons=..., defaultButton=...)
        #   Muestra una advertencia (icono de advertencia, botón Ok por defecto).
        # QMessageBox.critical(parent, title, text, buttons=..., defaultButton=...)
        #   Muestra un mensaje de error/crítico (icono de error, botón Ok por defecto).
        # QMessageBox.about(parent, title, text)
        #   Muestra un mensaje "Acerca de" (sin botones personalizables).
        #
        # Argumentos:
        #   parent: widget padre (usualmente self).
        #   title: título de la ventana de diálogo (str).
        #   text: mensaje principal (str).
        #   buttons: botones a mostrar (QMessageBox.Ok, QMessageBox.Yes, QMessageBox.No, etc).
        #   defaultButton: botón por defecto (opcional).
        # Todos estos métodos retornan el botón presionado.

        # Ejemplo de uso de los métodos estáticos:
        dialogo = QMessageBox.question(self, "Ventana pregunta simplificada", "ola we")
        if dialogo == QMessageBox.Yes:
            print("Se presionó el botón Yes")
        else:
            print("Se presionó el botón No")

        # QMessageBox.information(self, "Título", "Mensaje informativo")
        # QMessageBox.warning(self, "Título", "Mensaje de advertencia")
        # QMessageBox.critical(self, "Título", "Mensaje de error")
        # QMessageBox.about(self, "Acerca de", "Texto acerca de la aplicación")

if __name__ == "__main__":
    app = QApplication()
    ventana = ventanaPrincipal()
    app.exec()