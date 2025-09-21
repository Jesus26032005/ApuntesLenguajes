from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
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
        self.setWindowTitle("GRID LAYOUT")
        # Un QGridLayout es un administrador de diseño que organiza los widgets en una cuadrícula (filas y columnas).
        # Permite colocar widgets en posiciones específicas, y no es necesario rellenar todos los espacios.
        # Es útil para interfaces tipo tabla o formularios complejos.

        # Métodos principales de QGridLayout:
        # addWidget(widget: QWidget, row: int, column: int, rowSpan: int = 1, columnSpan: int = 1, alignment: Qt.Alignment = 0):
        #   Añade un widget en la posición (fila, columna). rowSpan y columnSpan permiten que el widget ocupe varias filas o columnas.
        #   alignment permite alinear el widget dentro de su celda (Qt.AlignLeft, Qt.AlignRight, Qt.AlignCenter, etc).
        # addLayout(layout: QLayout, row: int, column: int, rowSpan: int = 1, columnSpan: int = 1):
        #   Añade otro layout en la cuadrícula.
        # setSpacing(spacing: int): Define el espacio entre widgets (equivalente a gap en CSS).
        # setContentsMargins(left: int, top: int, right: int, bottom: int): Define el espacio interno del layout (equivalente a padding en CSS).
        # setRowMinimumHeight(row: int, minSize: int): Define la altura mínima de una fila.
        # setColumnMinimumWidth(column: int, minSize: int): Define el ancho mínimo de una columna.
        # setRowStretch(row: int, stretch: int): Controla cómo se expande una fila si hay espacio extra.
        # setColumnStretch(column: int, stretch: int): Controla cómo se expande una columna si hay espacio extra.
        # itemAtPosition(row: int, column: int) -> QLayoutItem: Devuelve el elemento en la posición dada.
        # count() -> int: Número de widgets/layouts en el layout.
        # itemAt(index: int) -> QLayoutItem: Devuelve el elemento en la posición dada.
        # takeAt(index: int) -> QLayoutItem: Remueve y retorna el elemento en la posición dada.

        # Señales:
        # QGridLayout no tiene señales propias, pero los widgets que contiene sí pueden emitir señales (por ejemplo, clicked, valueChanged, etc).

        # Inicializamos layout
        layoutCuadrado = QGridLayout()

        # Añadimos widgets al layout en posiciones específicas.
        # addWidget(widget, fila, columna, [rowSpan=1], [columnSpan=1], [alignment=0])
        layoutCuadrado.addWidget(Color("Red"), 0, 0)      # Fila 0, Columna 0
        layoutCuadrado.addWidget(Color("Green"), 0, 2)    # Fila 0, Columna 2 (dejas columna 1 vacía)
        layoutCuadrado.addWidget(Color("Blue"), 1, 4)     # Fila 1, Columna 4
        layoutCuadrado.addWidget(Color("Cyan"), 1, 6)     # Fila 1, Columna 6
        layoutCuadrado.addWidget(Color("Magenta"), 2, 0)  # Fila 2, Columna 0

        # Puedes usar rowSpan y columnSpan para que un widget ocupe varias filas o columnas:
        # layoutCuadrado.addWidget(Color("Yellow"), 0, 1, 2, 2)  # Ocupa 2 filas y 2 columnas

        # Puedes ajustar el espacio entre widgets y los márgenes del layout:
        # layoutCuadrado.setSpacing(10)  # Espacio entre widgets (gap)
        # layoutCuadrado.setContentsMargins(5, 5, 5, 5)  # Márgenes internos (padding)

        # Puedes controlar el tamaño mínimo y el estiramiento de filas/columnas:
        # layoutCuadrado.setRowMinimumHeight(0, 50)      # Altura mínima de la fila 0
        # layoutCuadrado.setColumnMinimumWidth(0, 50)    # Ancho mínimo de la columna 0
        # layoutCuadrado.setRowStretch(0, 2)             # Fila 0 se expande el doble que otras
        # layoutCuadrado.setColumnStretch(0, 1)          # Columna 0 se expande

        componente = QWidget()
        componente.setLayout(layoutCuadrado)
        self.setCentralWidget(componente)
        self.show()

if __name__ == "__main__":
    app = QApplication()
    ventana = ventanaPrincipal()
    app.exec()