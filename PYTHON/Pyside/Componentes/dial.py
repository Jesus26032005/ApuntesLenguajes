from PySide6.QtWidgets import QApplication, QMainWindow, QDial
from PySide6.QtCore import Qt

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dial")
        self.setGeometry(100, 100, 600, 400)
        # QDial es un widget circular (rueda) para seleccionar valores numéricos enteros dentro de un rango.
        # QDial(parent: QWidget = None)
        dial = QDial()

        # Métodos principales de QDial y sus argumentos:
        # setMinimum(minimum: int): Establece el valor mínimo permitido.
        # setMaximum(maximum: int): Establece el valor máximo permitido.
        # setRange(minimum: int, maximum: int): Establece el rango de valores permitidos.
        # setValue(value: int): Establece el valor actual del dial.
        # value() -> int: Devuelve el valor actual.
        # setSingleStep(step: int): Define el incremento/decremento con las teclas de flecha (por defecto es 1).
        # setPageStep(step: int): Define el incremento/decremento con PageUp/PageDown (por defecto es 10).
        # setNotchesVisible(visible: bool): Muestra u oculta las marcas en la rueda.
        # setWrapping(wrap: bool): Si es True, al pasar el máximo vuelve al mínimo y viceversa.
        # setInvertedAppearance(invert: bool): Invierte la dirección visual del dial.
        # setInvertedControls(invert: bool): Invierte el comportamiento de las teclas.
        # setTracking(enable: bool): Si es True (por defecto), valueChanged se emite mientras se mueve el dial; si es False, solo al soltar.
        # setStyleSheet(css: str): Aplica estilos CSS.

        # Ejemplo de configuración:
        dial.setRange(0, 100)         # Rango de valores permitidos (int, int)
        dial.setValue(50)             # Valor inicial (int)
        # dial.setSingleStep(5)       # Paso de incremento/decremento (int)
        # dial.setPageStep(20)        # Paso de página (int)
        # dial.setNotchesVisible(True) # Muestra las marcas en la rueda
        # dial.setWrapping(True)      # Permite que el valor "gire"
        # dial.setInvertedAppearance(True)  # Invierte la dirección visual
        # dial.setInvertedControls(True)    # Invierte el control de teclas
        # dial.setTracking(False)           # valueChanged solo al soltar el dial

        # Señales (signals) de QDial:
        # valueChanged(int value): Se emite cada vez que cambia el valor (por usuario o por código).
        # sliderMoved(int position): Se emite solo cuando el usuario mueve el dial manualmente.
        # sliderPressed(): Se emite cuando el usuario comienza a arrastrar el dial.
        # sliderReleased(): Se emite cuando el usuario suelta el dial.
        # rangeChanged(int min, int max): Se emite cuando cambia el rango de valores.

        # Ejemplo de conexión de señales:
        # dial.valueChanged.connect(self.valorCambiado)
        # dial.sliderMoved.connect(self.dialMovido)
        # dial.sliderPressed.connect(self.dialPresionado)
        # dial.sliderReleased.connect(self.dialLiberado)

        self.setCentralWidget(dial)
        self.show()

    # def valorCambiado(self, valor):
    #     print(f"Nuevo valor del dial: {valor}")

    # def dialMovido(self, posicion):
    #     print(f"Dial movido a la posición: {posicion}")

    # def dialPresionado(self):
    #     print("Dial presionado")

    # def dialLiberado(self):
    #     print("Dial liberado")

if __name__ == "__main__":
    app = QApplication([])
    ventana = ventanaPrincipal()
    app.exec()