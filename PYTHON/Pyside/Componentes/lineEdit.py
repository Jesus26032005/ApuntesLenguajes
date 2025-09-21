from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtCore import Qt

# Un componente es un elemento que se va a visualizar en la interfaz gráfica.
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LineEdit")
        self.setGeometry(100, 100, 600, 400)
        # QLineEdit es un widget de una sola línea para entrada de texto.
        # QLineEdit(parent: QWidget = None)
        # Permite capturar una linea de texto que el usuario ingrese
        lineaEdit = QLineEdit()

        # Métodos principales de QLineEdit y sus argumentos:
        # setText(text: str): Establece el texto del QLineEdit.
        # text() -> str: Devuelve el texto actual.
        # setMaxLength(maxLength: int): Define el número máximo de caracteres permitidos.
        # maxLength() -> int: Devuelve el máximo de caracteres.
        # setPlaceholderText(text: str): Muestra un texto de ayuda cuando está vacío.
        # placeholderText() -> str: Devuelve el texto de ayuda.
        # setReadOnly(readOnly: bool): Si es True, el usuario no puede editar el texto.
        # isReadOnly() -> bool: Devuelve si está en modo solo lectura.
        # setInputMask(mask: str): Define una máscara de entrada (ejemplo: '00-0000-0000' solo permite números en ese formato).
        # inputMask() -> str: Devuelve la máscara actual.
        # setEchoMode(mode: QLineEdit.EchoMode): Define cómo se muestra el texto (Normal, Password, NoEcho, PasswordEchoOnEdit).
        # setAlignment(alignment: Qt.Alignment): Alinea el texto (Qt.AlignLeft, Qt.AlignRight, Qt.AlignCenter).
        # setValidator(validator: QValidator): Permite validar la entrada (por ejemplo, solo números).
        # clear(): Borra el texto.
        # selectAll(): Selecciona todo el texto.
        # setSelection(start: int, length: int): Selecciona parte del texto.
        # selectedText() -> str: Devuelve el texto seleccionado.
        # cursorPosition() -> int: Devuelve la posición actual del cursor.
        # setCursorPosition(pos: int): Cambia la posición del cursor.
        # setStyleSheet(css: str): Aplica estilos CSS.

        # Establecemos el maximo de caracteres a capturar
        lineaEdit.setMaxLength(15)  # Valor: int (ejemplo: 15)

        # Establecemos un texto de ayuda
        lineaEdit.setPlaceholderText("hola we ingresa tu name:")  # Valor: str

        # Establecer solo para lectura
        lineaEdit.setReadOnly(True)   # True = solo lectura, False = editable
        lineaEdit.setReadOnly(False)  # Lo dejamos editable

        # Agregamos una validacion (mask)
        # setInputMask(mask: str): Define una máscara de entrada.
        # Ejemplos de máscaras:
        #   '000-0000-0000'   -> Solo números, formato teléfono.
        #   'AAA-AAAA'        -> Solo letras.
        #   '>AAAAA'          -> Letras en mayúsculas.
        #   '<aaaaa'          -> Letras en minúsculas.
        #   'NNNNN'           -> Letras o números.
        #   '99999'           -> Dígitos opcionales.
        #   '0000-00-00'      -> Fecha (YYYY-MM-DD).
        #   '000.000.000.000' -> IP.
        #   'NNNN@NNNN.NNN'   -> Email simple (pero para emails reales es mejor usar un QValidator personalizado).
        # Para validaciones complejas como correos electrónicos reales, se recomienda usar QRegularExpressionValidator.
        lineaEdit.setInputMask('00-0000-0000')

        # Señales (signals) de QLineEdit:
        # returnPressed(): Se emite cuando el usuario presiona Enter.
        # selectionChanged(): Se emite cuando cambia la selección de texto.
        # textChanged(str texto): Se emite cuando cambia el texto (por el usuario o por código).
        # textEdited(str texto): Se emite cuando el usuario edita el texto (no por código).
        # editingFinished(): Se emite cuando el usuario termina de editar (pierde el foco o presiona Enter).
        # cursorPositionChanged(int old, int new): Se emite cuando cambia la posición del cursor.

        # Evento enter, cambio seleccion texto (se lanza cuando se selecciona el texto), cambio texto (cuando cambia texto)
        lineaEdit.returnPressed.connect(self.enterPrsionado)
        # Evento cambio seleccion
        lineaEdit.selectionChanged.connect(self.cambioSeleccion)
        # Evento cambio texto
        lineaEdit.textChanged.connect(self.textoCamiado)

        self.setCentralWidget(lineaEdit)
        self.show()

    def enterPrsionado(self):
        print("Se presiono el enter")
        # Se usa self.centralWidget() para acceder al widget central de la ventana principal.
        # Esto es útil si necesitas manipular el widget desde cualquier método de la clase,
        # sin necesidad de guardar una referencia directa al QLineEdit como atributo.
        # Así, puedes reutilizar el mismo método aunque cambies el widget central en el futuro.
        self.centralWidget().setText("presioando")
    
    def cambioSeleccion(self):
        print("Cambio la seleccion del texto")
        # Se usa self.centralWidget() para obtener el QLineEdit actual y acceder al texto seleccionado.
        print(self.centralWidget().selectedText())

    def textoCamiado(self, nuevoTexto):
        print("Se cambio texto")
        print(f'Nuevo texto {nuevoTexto}')

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    app.exec()