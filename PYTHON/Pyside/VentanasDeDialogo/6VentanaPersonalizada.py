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
        # QMessageBox es un diálogo estándar para mostrar mensajes, advertencias, preguntas, errores, etc.
        # Se puede usar de dos formas: métodos estáticos o creando una instancia.
        #
        # Métodos estáticos principales de QMessageBox:
        # - QMessageBox.question(parent, title, text, buttons=..., defaultButton=...):
        #     Diálogo de pregunta (icono de pregunta, botones Yes/No por defecto).
        # - QMessageBox.information(parent, title, text, buttons=..., defaultButton=...):
        #     Mensaje informativo (icono de información, botón Ok por defecto).
        # - QMessageBox.warning(parent, title, text, buttons=..., defaultButton=...):
        #     Mensaje de advertencia (icono de advertencia, botón Ok por defecto).
        # - QMessageBox.critical(parent, title, text, buttons=..., defaultButton=...):
        #     Mensaje de error/crítico (icono de error, botón Ok por defecto).
        # - QMessageBox.about(parent, title, text):
        #     Mensaje "Acerca de" (sin botones personalizables).
        #
        # Argumentos:
        #   parent: widget padre (usualmente self).
        #   title: título de la ventana de diálogo (str).
        #   text: mensaje principal (str).
        #   buttons: botones a mostrar (QMessageBox.Ok, QMessageBox.Yes, QMessageBox.No, etc).
        #   defaultButton: botón por defecto (opcional).
        # Todos estos métodos retornan el botón presionado.
        #
        # Métodos de instancia de QMessageBox:
        # setWindowTitle(title: str): Cambia el título de la ventana.
        # setText(text: str): Cambia el texto principal.
        # setInformativeText(text: str): Añade texto informativo adicional.
        # setDetailedText(text: str): Añade texto detallado (expandible).
        # setIcon(icon: QMessageBox.Icon): Cambia el icono (Information, Warning, Critical, Question, NoIcon).
        # setStandardButtons(buttons: QMessageBox.StandardButtons): Define los botones estándar.
        # setDefaultButton(button: QMessageBox.StandardButton): Define el botón por defecto.
        # exec(): Muestra el diálogo de forma modal y retorna el botón presionado.
        # show(): Muestra el diálogo de forma no modal.
        #
        # Valores posibles para botones:
        # QMessageBox.Ok, QMessageBox.Cancel, QMessageBox.Yes, QMessageBox.No, QMessageBox.Abort,
        # QMessageBox.Retry, QMessageBox.Ignore, QMessageBox.Close, QMessageBox.Help, QMessageBox.Apply,
        # QMessageBox.Reset, QMessageBox.Save, QMessageBox.Discard, QMessageBox.Open, QMessageBox.RestoreDefaults
        #
        # Valores posibles para iconos:
        # QMessageBox.Information, QMessageBox.Warning, QMessageBox.Critical, QMessageBox.Question, QMessageBox.NoIcon
        #
        # Señales de QMessageBox:
        # buttonClicked(QAbstractButton): Se emite cuando se presiona un botón.
        # finished(int result): Se emite cuando el diálogo se cierra.

        dialogo = QMessageBox.critical(
            self,
            "Título",
            "Mensaje de error",
            buttons=QMessageBox.Discard | QMessageBox.Cancel | QMessageBox.Ignore | QMessageBox.Retry,
            defaultButton=QMessageBox.Cancel
        ) #Es el boton de cuando se cierra la ventana

        if dialogo == QMessageBox.Discard:
            print("Se presionó el botón Discard")
        elif dialogo == QMessageBox.Retry:
            print("Se presionó el botón Retry")
        elif dialogo == QMessageBox.Ignore:
            print("Se presionó el botón Ignore")
        else:
            print("Se presionó el botón Cancel")

if __name__ == "__main__":
    app = QApplication()
    ventana = ventanaPrincipal()
    app.exec()