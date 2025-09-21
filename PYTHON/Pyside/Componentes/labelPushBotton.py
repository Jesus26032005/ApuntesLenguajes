from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPushButton y QLabel")

        # QLabel es un widget para mostrar texto o imágenes.
        # QLabel(text: str = '', parent: QWidget = None, flags: Qt.WindowFlags = 0)
        # Métodos principales de QLabel:
        # setText(text: str): Cambia el texto mostrado.
        # text() -> str: Devuelve el texto actual.
        # setAlignment(alignment: Qt.Alignment): Alinea el texto (Qt.AlignLeft, Qt.AlignRight, Qt.AlignCenter, etc).
        # setFont(font: QFont): Cambia la fuente del texto.
        # setPixmap(pixmap: QPixmap): Muestra una imagen en vez de texto.
        # setStyleSheet(css: str): Aplica estilos CSS.
        # setWordWrap(on: bool): Permite que el texto se ajuste en varias líneas.
        # Señales: QLabel no tiene señales propias, pero puedes reaccionar a eventos sobreescribiendo métodos de evento.

        self.label = QLabel("Texto inicial")
        self.label.setAlignment(Qt.AlignCenter)

        # QPushButton es un botón que el usuario puede presionar.
        # QPushButton(text: str = '', parent: QWidget = None)
        # Métodos principales de QPushButton:
        # setText(text: str): Cambia el texto del botón.
        # text() -> str: Devuelve el texto actual.
        # setIcon(icon: QIcon): Asigna un ícono al botón.
        # setCheckable(checkable: bool): Permite que el botón sea tipo check (activado/desactivado).
        # setChecked(checked: bool): Marca o desmarca el botón.
        # isChecked() -> bool: Devuelve si está marcado.
        # setEnabled(enabled: bool): Habilita o deshabilita el botón.
        # setStyleSheet(css: str): Aplica estilos CSS.
        # setShortcut(shortcut: QKeySequence | str): Asigna un atajo de teclado.
        # Señales de QPushButton:
        # clicked(bool checked=False): Se emite cuando el botón es presionado.
        # pressed(): Se emite cuando el botón es presionado (antes de soltar).
        # released(): Se emite cuando el botón es soltado.
        # toggled(bool checked): Se emite cuando cambia el estado check.

        boton = QPushButton("Cambiar texto")
        boton.clicked.connect(self.cambiar_texto)  # Conectamos la señal clicked a un método

        # Layout vertical para organizar los widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(boton)

        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

    def cambiar_texto(self):
        # Cambia el texto del label al presionar el botón
        self.label.setText("¡Texto cambiado!")

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    app.exec()