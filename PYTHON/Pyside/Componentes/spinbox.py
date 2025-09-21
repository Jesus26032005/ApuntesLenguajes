from PySide6.QtWidgets import QApplication, QMainWindow, QSpinBox
from PySide6.QtCore import Qt

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("spinBox")
        self.setGeometry(100, 100, 600, 400)
        # QSpinBox es un widget para seleccionar valores numéricos enteros dentro de un rango.
        # QSpinBox(parent: QWidget = None)
        spin = QSpinBox()

        # Métodos principales de QSpinBox y sus argumentos:
        # setMinimum(minimum: int): Establece el valor mínimo permitido.
        # setMaximum(maximum: int): Establece el valor máximo permitido.
        # setRange(minimum: int, maximum: int): Establece el rango de valores permitidos.
        # setValue(value: int): Establece el valor actual del spinbox.
        # value() -> int: Devuelve el valor actual.
        # setSingleStep(step: int): Define el incremento/decremento al usar las flechas (por defecto es 1).
        # singleStep() -> int: Devuelve el valor del paso.
        # setSuffix(suffix: str): Añade un texto al final del número (ejemplo: " kg", " unidades").
        # setPrefix(prefix: str): Añade un texto al inicio del número (ejemplo: "$", "Valor: ").
        # setWrapping(wrap: bool): Si es True, al pasar el máximo vuelve al mínimo y viceversa.
        # setAlignment(alignment: Qt.Alignment): Alinea el texto (Qt.AlignLeft, Qt.AlignRight, Qt.AlignCenter).
        # setReadOnly(readOnly: bool): Si es True, el usuario no puede escribir manualmente.
        # setDisplayIntegerBase(base: int): Cambia la base numérica (por ejemplo, 2 para binario, 16 para hexadecimal).
        # setKeyboardTracking(enable: bool): Si es False, solo se emite valueChanged cuando se confirma el valor.
        # setStyleSheet(css: str): Aplica estilos CSS.

        # Establecer valor mínimo y máximo
        spin.setMaximum(100)      # Valor máximo permitido (int)
        spin.setMinimum(0)        # Valor mínimo permitido (int)
        # Otra forma de establecer rango
        spin.setRange(0, 100)     # Rango de valores permitidos (min, max)
        # Añadir valor por defecto
        spin.setValue(50)         # Valor inicial (int)
        # Añadir prefijo o sufijo
        spin.setSuffix(" unidades")   # Texto al final del número
        spin.setPrefix("Valor: ")     # Texto al inicio del número
        # Indicar incrementos o decrementos cada vez que se presiona las flechas
        spin.setSingleStep(5)     # Paso de incremento/decremento (int)
        # Otras opciones útiles:
        # spin.setWrapping(True)   # Permite que el valor "gire" al llegar al máximo/mínimo
        # spin.setAlignment(Qt.AlignCenter)  # Centra el texto
        # spin.setReadOnly(True)  # Solo permite cambiar con las flechas, no escribir

        #Eventos valuechanged y textChanged
        spin.valueChanged.connect( lambda valor: print(f"Nuevo valor seleccionado: {valor}"))
        spin.textChanged.connect( lambda texto: print(f"Nuevo texto: {texto}")) #Se recibe sufijo, numero y prefijo

        # Señales (signals) de QSpinBox:
        # valueChanged(int value): Se emite cuando cambia el valor (por flechas o escritura).
        # textChanged(str text): Se emite cuando cambia el texto mostrado.
        # editingFinished(): Se emite cuando el usuario termina de editar (pierde el foco o presiona Enter).
        # textChanged(str text): Se emite cuando cambia el texto (incluyendo prefijo/sufijo).
        # textEdited(str text): Se emite cuando el usuario edita el texto manualmente.

        # Ejemplo de conexión de señal:
        # spin.valueChanged.connect(self.valorCambiado)

        self.setCentralWidget(spin)
        self.show()

    # def valorCambiado(self, valor):
    #     print(f"Nuevo valor seleccionado: {valor}")

if __name__ == "__main__":
    app = QApplication([])
    ventana = ventanaPrincipal()
    app.exec()