from PySide6.QtWidgets import QApplication, QMainWindow, QDoubleSpinBox
from PySide6.QtCore import Qt

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("doubleSpinBox")
        self.setGeometry(100, 100, 600, 400)
        # QDoubleSpinBox es un widget para seleccionar valores numéricos decimales (float) dentro de un rango.
        # QDoubleSpinBox(parent: QWidget = None)
        doubleSpin = QDoubleSpinBox()

        # Métodos principales de QDoubleSpinBox y sus argumentos:
        # setMinimum(minimum: float): Establece el valor mínimo permitido.
        # setMaximum(maximum: float): Establece el valor máximo permitido.
        # setRange(minimum: float, maximum: float): Establece el rango de valores permitidos.
        # setValue(value: float): Establece el valor actual del spinbox.
        # value() -> float: Devuelve el valor actual.
        # setSingleStep(step: float): Define el incremento/decremento al usar las flechas (por defecto es 1.0).
        # singleStep() -> float: Devuelve el valor del paso.
        # setDecimals(decimals: int): Define la cantidad de decimales mostrados (por defecto es 2).
        # decimals() -> int: Devuelve la cantidad de decimales.
        # setSuffix(suffix: str): Añade un texto al final del número (ejemplo: " kg", " m").
        # setPrefix(prefix: str): Añade un texto al inicio del número (ejemplo: "$", "Valor: ").
        # setWrapping(wrap: bool): Si es True, al pasar el máximo vuelve al mínimo y viceversa.
        # setAlignment(alignment: Qt.Alignment): Alinea el texto (Qt.AlignLeft, Qt.AlignRight, Qt.AlignCenter).
        # setReadOnly(readOnly: bool): Si es True, el usuario no puede escribir manualmente.
        # setKeyboardTracking(enable: bool): Si es False, solo se emite valueChanged cuando se confirma el valor.
        # setStyleSheet(css: str): Aplica estilos CSS.

        # Ejemplo de configuración:
        doubleSpin.setRange(-100.0, 100.0)   # Rango de valores permitidos (float, float)
        doubleSpin.setValue(0.0)             # Valor inicial (float)
        doubleSpin.setSingleStep(0.5)        # Paso de incremento/decremento (float)
        doubleSpin.setDecimals(3)            # Número de decimales mostrados (int)
        doubleSpin.setSuffix(" m")           # Sufijo (str)
        doubleSpin.setPrefix("Distancia: ")  # Prefijo (str)
        # doubleSpin.setWrapping(True)       # Permite que el valor "gire" al llegar al máximo/mínimo
        # doubleSpin.setAlignment(Qt.AlignCenter)  # Centra el texto
        # doubleSpin.setReadOnly(True)       # Solo permite cambiar con las flechas, no escribir

        # Señales (signals) de QDoubleSpinBox:
        # valueChanged(float value): Se emite cuando cambia el valor (por flechas o escritura).
        # textChanged(str text): Se emite cuando cambia el texto mostrado.
        # editingFinished(): Se emite cuando el usuario termina de editar (pierde el foco o presiona Enter).
        # textChanged(str text): Se emite cuando cambia el texto (incluyendo prefijo/sufijo).
        # textEdited(str text): Se emite cuando el usuario edita el texto manualmente.

        # Ejemplo de conexión de señal:
        # doubleSpin.valueChanged.connect(self.valorCambiado)

        self.setCentralWidget(doubleSpin)
        self.show()

    # def valorCambiado(self, valor):
    #     print(f"Nuevo valor seleccionado: {valor}")

if __name__ == "__main__":
    app = QApplication([])
    ventana = ventanaPrincipal()
    app.exec()