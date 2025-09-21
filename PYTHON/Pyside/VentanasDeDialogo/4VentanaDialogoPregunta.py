from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QFileDialog, QColorDialog, QFontDialog, QMessageBox, QInputDialog

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
        # QDialog es una ventana secundaria para interacción temporal con el usuario.
        # QDialog(parent: QWidget = None, flags: Qt.WindowFlags = 0)
        # Métodos principales de QDialog:
        # exec() -> int: Muestra el diálogo de forma modal (bloquea la ventana principal hasta que se cierre).
        # show(): Muestra el diálogo de forma no modal.
        # accept(): Cierra el diálogo y retorna QDialog.Accepted.
        # reject(): Cierra el diálogo y retorna QDialog.Rejected.
        # setWindowTitle(title: str): Cambia el título de la ventana de diálogo.
        # setModal(modal: bool): Define si el diálogo es modal o no.
        # setLayout(layout: QLayout): Asigna un layout al diálogo.
        # Señales de QDialog:
        # accepted(): Se emite cuando se acepta el diálogo (accept()).
        # rejected(): Se emite cuando se rechaza el diálogo (reject()).
        # finished(int result): Se emite cuando el diálogo se cierra, con el resultado (Accepted/Rejected).

        # QMessageBox es un diálogo estándar para mostrar mensajes, advertencias, preguntas, etc.
        # QMessageBox(parent: QWidget = None)
        # Métodos principales de QMessageBox:
        # setWindowTitle(title: str): Cambia el título de la ventana de mensaje.
        # setText(text: str): Cambia el texto principal del mensaje.
        # setInformativeText(text: str): Añade texto informativo adicional.
        # setDetailedText(text: str): Añade texto detallado (se puede expandir).
        # setIcon(icon: QMessageBox.Icon): Cambia el ícono del mensaje.
        #   Valores posibles: QMessageBox.Information, QMessageBox.Warning, QMessageBox.Critical, QMessageBox.Question, QMessageBox.NoIcon
        # setStandardButtons(buttons: QMessageBox.StandardButtons): Define los botones estándar.
        #   Valores posibles: QMessageBox.Ok, QMessageBox.Cancel, QMessageBox.Yes, QMessageBox.No, QMessageBox.Abort, QMessageBox.Retry, QMessageBox.Ignore, QMessageBox.Close, QMessageBox.Help, QMessageBox.Apply, QMessageBox.Reset, QMessageBox.Save, QMessageBox.Discard, QMessageBox.Open, QMessageBox.RestoreDefaults
        # setDefaultButton(button: QMessageBox.StandardButton): Define el botón por defecto.
        # setEscapeButton(button: QMessageBox.StandardButton): Define el botón que se activa al presionar Escape.
        # exec() -> int: Muestra el diálogo de forma modal y retorna el botón presionado.
        # show(): Muestra el diálogo de forma no modal.
        # Señales de QMessageBox:
        # buttonClicked(QAbstractButton): Se emite cuando se presiona un botón.
        # finished(int result): Se emite cuando el diálogo se cierra.

        dialogo = QMessageBox(self)
        dialogo.setWindowTitle("Ventana de dialogo simple")
        dialogo.setText("Es rojo.")
        dialogo.setIcon(QMessageBox.Question) # Icono del mensaje (Information, Warning, Critical, Question, NoIcon)
        dialogo.setStandardButtons(QMessageBox.Yes | QMessageBox.No) # Botones estándar (Yes y No)
        valorRetornado = dialogo.exec()
        print(f"Valor retornado: {valorRetornado}")
        if valorRetornado == QMessageBox.Yes:
            print("Se presionó el botón Yes")
        else:
            print("Se presionó el botón No")

if __name__ == "__main__":
    app = QApplication()
    ventana = ventanaPrincipal()
    app.exec()