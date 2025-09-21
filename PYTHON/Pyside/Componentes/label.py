from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt

# Un componente es un elemento que se va a visualizar en la interfaz gráfica.
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Label")
        self.setGeometry(100, 100, 600, 400)

        # Crear componente de tipo etiqueta (QLabel)
        label = QLabel("Hola, PySide6!")  # QLabel(texto: str = '', parent: QWidget = None)
        # Métodos principales de QLabel:
        #   setText(texto: str): Cambia el texto mostrado.
        #   text(): Devuelve el texto actual.
        #   setFont(fuente: QFont): Cambia la fuente del texto.
        #   font(): Devuelve el QFont actual.
        #   setAlignment(alineacion: Qt.Alignment): Cambia la alineación del texto.
        #   alignment(): Devuelve la alineación actual.
        #   setStyleSheet(css: str): Aplica estilos CSS.
        #   setPixmap(pixmap: QPixmap("url Imagen")): Muestra una imagen en vez de texto.
        #   setWordWrap(bool): Permite que el texto se ajuste en varias líneas.
        #   setTextFormat(Qt.PlainText, Qt.RichText, Qt.AutoText): Define el formato del texto.
        #   setBuddy(widget: QWidget): Asocia la etiqueta a otro widget (accesibilidad).
        #   setMargin(margen: int): Define el margen alrededor del texto.
        #   setIndent(espacio: int): Define la sangría del texto.
        #   setOpenExternalLinks(bool): Permite abrir enlaces externos si el texto es HTML.

        # Modificar texto inicial
        label.setText("Hola, PySide6! Modificado")  # Cambia el texto de la etiqueta

        # Modificar la fuente
        fuente = label.font()  # Se obtiene la fuente actual (QFont)
        fuente.setPointSize(25)  # Cambiar tamaño letra, el valor por default es 12
        fuente.setFamily("Arial")  # Cambia la familia de la fuente
        label.setFont(fuente)  # Aplica la fuente modificada

        # Modificar alineación
        label.setAlignment(Qt.AlignCenter)  # Centra el texto horizontal y verticalmente
        # Otras opciones de alineación:
        #   Qt.AlignLeft, Qt.AlignRight, Qt.AlignHCenter, Qt.AlignJustify
        #   Qt.AlignTop, Qt.AlignBottom, Qt.AlignVCenter
        #   Se pueden combinar con el operador |, por ejemplo: Qt.AlignHCenter | Qt.AlignVCenter

        # Señales y disparadores (eventos) de QLabel:
        # QLabel NO tiene señales propias (como clicked, textChanged, etc).
        # Pero puedes reaccionar a eventos sobreescribiendo métodos de evento:
        # - mousePressEvent(self, event): Se dispara al presionar el mouse sobre la etiqueta.
        # - mouseReleaseEvent(self, event): Se dispara al soltar el mouse sobre la etiqueta.
        # - mouseDoubleClickEvent(self, event): Se dispara al hacer doble clic.
        # - enterEvent(self, event): Se dispara cuando el mouse entra en el área del label.
        # - leaveEvent(self, event): Se dispara cuando el mouse sale del área del label.
        # - contextMenuEvent(self, event): Se dispara al hacer clic derecho (menú contextual).
        # Para usar estos eventos, debes crear una subclase de QLabel y sobreescribir los métodos.

        # Ejemplo de subclase con evento:
        # class MiLabel(QLabel):
        #     def mousePressEvent(self, event):
        #         print("¡Etiqueta presionada!")

        # Otras propiedades útiles:
        # label.setWordWrap(True)  # Permite que el texto se divida en varias líneas si es largo
        # label.setTextInteractionFlags(Qt.TextSelectableByMouse)  # Permite seleccionar el texto con el mouse
        # label.setToolTip("Esto es una etiqueta")  # Muestra un tooltip al pasar el mouse

        # Publicar este componente como widget central de la ventana
        self.setCentralWidget(label)

        # Mostrar la ventana
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    app.exec()