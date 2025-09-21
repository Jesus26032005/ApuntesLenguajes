from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Imagen")
        self.setGeometry(100, 100, 600, 400)
        # Crear componente QLabel
        # QLabel(text: str = '', parent: QWidget = None, flags: Qt.WindowFlags = 0)
        etiqueta = QLabel("hoal we")

        # Asignar una imagen a la etiqueta usando setPixmap
        # setPixmap(pixmap: QPixmap): Muestra una imagen en vez de texto.
        # QPixmap("ruta"): Carga la imagen desde la ruta indicada.
        # Si el texto y la imagen están presentes, solo se muestra la imagen.
        etiqueta.setPixmap(QPixmap("Pyside/Componentes/imagen.png"))

        # Escalar la imagen al tamaño del QLabel
        # setScaledContents(scaled: bool): Si es True, la imagen se ajusta al tamaño del QLabel.
        # Si es False, la imagen mantiene su tamaño original.
        etiqueta.setScaledContents(True)

        # Otros métodos útiles de QLabel con imágenes:
        # setAlignment(alignment: Qt.Alignment): Alinea la imagen dentro del QLabel.
        #   alignment puede ser Qt.AlignLeft, Qt.AlignRight, Qt.AlignHCenter, Qt.AlignVCenter, etc.
        # pixmap() -> QPixmap: Devuelve el QPixmap actual.
        # setMargin(margin: int): Define el margen alrededor de la imagen.
        # setStyleSheet(css: str): Aplica estilos CSS al QLabel (bordes, fondo, etc).

        # Señales y eventos de QLabel:
        # QLabel no tiene señales propias, pero puedes reaccionar a eventos sobreescribiendo:
        # - mousePressEvent(self, event: QMouseEvent): Al presionar el mouse sobre la imagen.
        # - mouseDoubleClickEvent(self, event: QMouseEvent): Al hacer doble clic.
        # - enterEvent(self, event: QEvent): Cuando el mouse entra en el área del QLabel.
        # - leaveEvent(self, event: QEvent): Cuando el mouse sale del área del QLabel.
        # Para usar estos eventos, crea una subclase de QLabel y sobreescribe los métodos.

        # Ejemplo de alineación de imagen:
        # etiqueta.setAlignment(Qt.AlignCenter)

        # Ejemplo de margen:
        # etiqueta.setMargin(10)

        # Ejemplo de estilo:
        # etiqueta.setStyleSheet("border: 2px solid red; background: #eee;")

        # Publicar el componente como widget central de la ventana
        self.setCentralWidget(etiqueta)
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    ventana = ventanaPrincipal()
    app.exec()