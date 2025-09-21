from PySide6.QtWidgets import QApplication, QMainWindow, QSlider
from PySide6.QtCore import Qt

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slider")
        self.setGeometry(100, 100, 600, 400)
        # QSlider es un widget para seleccionar valores numéricos enteros mediante una barra deslizante.
        # QSlider(orientation: Qt.Orientation, parent: QWidget = None)
        # orientation: Qt.Horizontal o Qt.Vertical (por defecto es vertical si no se especifica)
        slider = QSlider(Qt.Horizontal)  # Barra horizontal

        # Métodos principales de QSlider y sus argumentos:
        # setMinimum(minimum: int): Establece el valor mínimo permitido.
        # setMaximum(maximum: int): Establece el valor máximo permitido.
        # setRange(minimum: int, maximum: int): Establece el rango de valores permitidos.
        # setValue(value: int): Establece el valor actual del slider.
        # value() -> int: Devuelve el valor actual.
        # setSingleStep(step: int): Define el incremento/decremento con las teclas de flecha (por defecto es 1).
        # singleStep() -> int: Devuelve el valor del paso.
        # setPageStep(step: int): Define el incremento/decremento con PageUp/PageDown (por defecto es 10).
        # pageStep() -> int: Devuelve el valor del paso de página.
        # setTickInterval(ticks: int): Define el intervalo entre marcas de la barra.
        # tickInterval() -> int: Devuelve el intervalo de marcas.
        # setTickPosition(position: QSlider.TickPosition): Define la posición de las marcas (NoTicks, TicksAbove, TicksBelow, TicksBothSides).
        # tickPosition() -> QSlider.TickPosition: Devuelve la posición de las marcas.
        # setOrientation(orientation: Qt.Orientation): Cambia la orientación (Qt.Horizontal o Qt.Vertical).
        # setInvertedAppearance(invert: bool): Invierte la dirección visual del slider.
        # setInvertedControls(invert: bool): Invierte el comportamiento de las teclas.
        # setTracking(enable: bool): Si es True (por defecto), valueChanged se emite mientras se mueve el slider; si es False, solo al soltar.
        # setStyleSheet(css: str): Aplica estilos CSS.

        # Ejemplo de configuración adicional:
        # slider.setSingleStep(5)  # Cambia el valor de a 5 en 5 con flechas
        # slider.setPageStep(20)   # Cambia el valor de a 20 en 20 con PageUp/PageDown
        # slider.setTickInterval(10)  # Marcas cada 10 unidades
        # slider.setTickPosition(QSlider.TicksBelow)  # Marcas debajo de la barra
        # slider.setInvertedAppearance(True)  # Invierte la dirección visual
        # slider.setInvertedControls(True)    # Invierte el control de teclas
        # slider.setTracking(False)           # valueChanged solo al soltar el slider

        # Señales (signals) de QSlider:
        # valueChanged(int value): Se emite cada vez que cambia el valor (por usuario o por código).
        # sliderMoved(int position): Se emite solo cuando el usuario mueve el slider manualmente.
        # sliderPressed(): Se emite cuando el usuario comienza a arrastrar el slider.
        # sliderReleased(): Se emite cuando el usuario suelta el slider.
        # rangeChanged(int min, int max): Se emite cuando cambia el rango de valores.

        # Conexión de señales:
        slider.valueChanged.connect(self.valorCambiado)      # Se emite siempre que cambia el valor
        slider.sliderMoved.connect(self.sliderMovido)        # Solo cuando el usuario mueve el slider
        slider.sliderPressed.connect(self.sliderPresionado)  # Cuando el usuario presiona el slider
        slider.sliderReleased.connect(self.sliderLiberado)   # Cuando el usuario suelta el slider

        self.setCentralWidget(slider)
        self.show()

    def valorCambiado(self, valor):
        print(f"Nuevo valor del slider: {valor}")

    def sliderMovido(self, posicion):
        print(f"Slider movido a la posición: {posicion}")

    def sliderPresionado(self):
        print("Slider presionado")

    def sliderLiberado(self):
        print("Slider liberado")

if __name__ == "__main__":
    app = QApplication([])
    ventana = ventanaPrincipal()
    app.exec()