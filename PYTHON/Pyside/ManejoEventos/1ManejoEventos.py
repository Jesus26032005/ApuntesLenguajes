from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manejo eventos")
        self.setGeometry(100, 100, 800, 600)
        # Se usa self.etiqueta como atributo para poder modificar su texto desde los métodos de eventos.
        self.etiqueta = QLabel("click en la ventana")
        self.setCentralWidget(self.etiqueta)
        self.show()
        # Métodos usados:
        # setWindowTitle(title: str): Cambia el título de la ventana.
        # setGeometry(x: int, y: int, width: int, height: int): Define la posición y tamaño de la ventana.
        # QLabel(text: str): Widget para mostrar texto.
        # setCentralWidget(widget: QWidget): Coloca el widget como contenido central de la ventana principal.
        # show(): Muestra la ventana.

    # La variable evento contiene información como detalles de la posición del mouse o el botón que se presionó.
    # Los siguientes métodos son eventos especiales de QWidget/QMainWindow que se pueden sobreescribir
    # para manejar la interacción del usuario con el mouse.

    def mouseMoveEvent(self, event):  # Se genera cuando se mueve el mouse sobre la ventana.
        # event: objeto QMouseEvent con información sobre la posición y estado de los botones del mouse.
        print("Evento mouseMoveEvent")
        # Métodos útiles de event:
        # event.pos(): Devuelve la posición del mouse relativa al widget.
        # event.globalPos(): Devuelve la posición global del mouse en la pantalla.
        # event.buttons(): Devuelve los botones del mouse que están presionados.

    def mousePressEvent(self, event):  # Se genera cuando se presiona un botón del mouse.
        # event.button(): Devuelve el botón presionado (Qt.LeftButton, Qt.RightButton, Qt.MiddleButton).
        if event.button() == Qt.LeftButton:  # Verifica si el botón izquierdo del mouse fue presionado
            self.etiqueta.setText("Botón izquierdo presionado")
        if event.button() == Qt.RightButton:  # Verifica si el botón derecho del mouse fue presionado
            self.etiqueta.setText("Botón derecho presionado")
        if event.button() == Qt.MiddleButton:  # Verifica si el botón central del mouse fue presionado
            self.etiqueta.setText("Botón central presionado")
        print("Evento mousePressEvent")
        # Qt.LeftButton, Qt.RightButton, Qt.MiddleButton son constantes de Qt para identificar los botones del mouse.

    def mouseReleaseEvent(self, event):  # Se genera cuando se suelta un botón del mouse.
        print("Evento mouseReleaseEvent")

    def mouseDoubleClickEvent(self, event):  # Se genera cuando se hace doble clic con el mouse.
        print("Evento mouseDoubleClickEvent")

    # Los métodos mouseMoveEvent, mousePressEvent, mouseReleaseEvent y mouseDoubleClickEvent
    # se sobreescriben para personalizar el comportamiento de la ventana ante eventos del mouse.
    # Se usan atributos como self.etiqueta para poder modificar el contenido del widget desde cualquier método.

if __name__ == "__main__":
    app = QApplication()
    ventana = ventanaPrincipal()
    app.exec()
    # QApplication(): Inicializa la aplicación Qt.
    # app.exec(): Inicia el bucle de eventos de la aplicación.