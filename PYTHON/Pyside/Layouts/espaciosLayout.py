from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor

class Color(QWidget): #Crea un widget de color
    def __init__(self, nuevo_color):
        super().__init__()
        self.setAutoFillBackground(True)
        paletaColores = self.palette()
        paletaColores.setColor(QPalette.Window, QColor(nuevo_color))
        self.setPalette(paletaColores)

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Espacios entre layouts")
        layoutHorizontal = QHBoxLayout()
        layoutVertical = QVBoxLayout()

        # --- Métodos para espaciar y margenes en layouts ---
        # setContentsMargins(left: int, top: int, right: int, bottom: int):
        #   Define el espacio interno entre el borde del layout y sus widgets hijos.
        #   Es equivalente a 'padding' en CSS, pero NO afecta el tamaño total del layout como lo haría 'box-sizing: border-box'.
        # setSpacing(espacio: int):
        #   Define el espacio entre los widgets hijos dentro del layout.
        #   Es equivalente a 'gap' en CSS para flexbox/grid.
        # addSpacing(espacio: int):
        #   Añade un espacio fijo entre widgets, como un margin puntual en CSS.
        # addStretch(stretch: int = 0):
        #   Añade espacio flexible que se expande, similar a 'flex-grow' en CSS.
        # setAlignment(widget, alignment: Qt.Alignment):
        #   Alinea un widget específico dentro del layout.

        #Agregamos margen en el layout vertical
        layoutVertical.setContentsMargins(2,5,2,3) #Funciona como un padding pero sin box sizing como en web
        #Agregamos espacios dentro del layout vertical
        layoutVertical.setSpacing(20) #Se agrega un espacio de 20 entre cada elemento , funciona como gap en web
        #Agregamos margen en layout horizontal
        layoutHorizontal.setContentsMargins(2,5,2,3) #Funciona como un padding pero sin box sizing como en web
        layoutHorizontal.setSpacing(20) #Se agrega un espacio de 20 entre cada elemento , funciona como gap en web

        layoutVertical.addWidget(Color("red"))
        layoutVertical.addWidget(Color("blue"))
        layoutVertical.addWidget(Color("cyan"))

        layoutHorizontal.addLayout(layoutVertical)
        layoutHorizontal.addWidget(Color("Green"))
        layoutHorizontal.addWidget(Color("Yellow"))

        componente = QWidget()
        componente.setLayout(layoutHorizontal)
        self.setCentralWidget(componente)
        self.show()

        # ¿Se puede hacer un margin como en web con box-sizing?
        # No directamente. En Qt, los márgenes de layout (setContentsMargins) solo afectan el espacio interno del layout,
        # no el tamaño total del widget como 'box-sizing: border-box' en CSS.
        # Si quieres un "margin externo" (como el margin de CSS), puedes:
        # - Usar addSpacing() entre layouts o widgets.
        # - Encapsular tu widget en otro QWidget y aplicar padding/margen al contenedor.
        # - Usar setStyleSheet("margin: ...") en widgets individuales, pero esto solo afecta algunos widgets y no layouts.
        # En resumen: Qt no tiene un equivalente exacto a 'margin' con 'box-sizing: border-box' de CSS para layouts.

if __name__ == "__main__":
    app = QApplication()
    ventana = ventanaPrincipal()
    app.exec()