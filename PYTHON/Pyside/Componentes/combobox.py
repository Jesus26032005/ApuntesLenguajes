from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox
from PySide6.QtCore import Qt

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ComboBox")
        self.setGeometry(100, 100, 600, 400)
        # Creamos un combo box (drop down list)
        # QComboBox(parent: QWidget = None)
        combo = QComboBox()

        # Métodos principales de QComboBox y sus argumentos:
        # addItem(text: str, userData: Any = None): Agrega un elemento al combo. userData es opcional y puede ser cualquier objeto.
        # addItems(texts: Iterable[str]): Agrega varios elementos a partir de una lista o iterable de strings.
        # insertItem(index: int, text: str, userData: Any = None): Inserta un elemento en una posición específica.
        # insertItems(index: int, texts: Iterable[str]): Inserta varios elementos en una posición específica.
        # removeItem(index: int): Elimina el elemento en la posición dada.
        # clear(): Elimina todos los elementos.
        # count() -> int: Devuelve el número de elementos.
        # itemText(index: int) -> str: Devuelve el texto del elemento en la posición dada.
        # setItemText(index: int, text: str): Cambia el texto de un elemento.
        # setCurrentIndex(index: int): Cambia el elemento seleccionado.
        # currentIndex() -> int: Devuelve el índice seleccionado.
        # currentText() -> str: Devuelve el texto seleccionado.
        # findText(text: str): Devuelve el índice del texto dado, o -1 si no existe.
        # setEditable(editable: bool): Permite que el usuario escriba texto personalizado.
        # setInsertPolicy(policy: QComboBox.InsertPolicy): Define cómo se insertan nuevos elementos cuando el usuario escribe.
        # setMaxCount(count: int): Limita el número máximo de elementos.
        # setDuplicatesEnabled(enable: bool): Permite o no elementos duplicados.
        # setIconSize(size: QSize): Cambia el tamaño de los íconos de los elementos.
        # setStyleSheet(css: str): Aplica estilos CSS.

        # Agregamos elementos con addItem
        combo.addItem("Opcion 1")
        combo.addItems(["Opcion 2", "Opcion 3", "Opcion 4"]) # Recibe una lista de strings

        # Señales (signals) de QComboBox:
        # currentIndexChanged(int index): Se emite cuando cambia el índice seleccionado.
        # currentTextChanged(str text): Se emite cuando cambia el texto seleccionado.
        # activated(int index o str text): Se emite cuando el usuario selecciona un elemento (por clic o enter).
        # highlighted(int index o str text): Se emite cuando el usuario resalta un elemento con el mouse o teclado.
        # editTextChanged(str text): Se emite cuando el texto editable cambia (si es editable).

        # Asociar señales, cambio de elemento seleccionado tanto de indice como texto
        combo.currentIndexChanged.connect(self.cambioIndice)
        combo.currentTextChanged.connect(self.cambioTexto)

        # Hacemos editable el comboBox
        combo.setEditable(True)

        # setInsertPolicy(policy: QComboBox.InsertPolicy): Define cómo se insertan nuevos elementos cuando el usuario escribe y presiona Enter.
        # Opciones de InsertPolicy:
        #   QComboBox.NoInsert: No inserta nuevos elementos, solo cambia el texto editable.
        #   QComboBox.InsertAtTop: Inserta nuevos elementos al inicio.
        #   QComboBox.InsertAtCurrent: Reemplaza el elemento actual.
        #   QComboBox.InsertAtBottom: Inserta nuevos elementos al final.
        #   QComboBox.InsertBeforeCurrent: Inserta antes del elemento actual.
        #   QComboBox.InsertAfterCurrent: Inserta después del elemento actual.
        #   QComboBox.InsertAlphabetically: Inserta en orden alfabético.

        combo.setInsertPolicy(QComboBox.NoInsert)
        combo.setInsertPolicy(QComboBox.InsertAtTop)
        combo.setInsertPolicy(QComboBox.InsertAtCurrent)
        combo.setInsertPolicy(QComboBox.InsertAtBottom)
        combo.setInsertPolicy(QComboBox.InsertBeforeCurrent)
        combo.setInsertPolicy(QComboBox.InsertAfterCurrent)
        combo.setInsertPolicy(QComboBox.InsertAlphabetically)

        # Limitar elementos a ingresar
        combo.setMaxCount(8) # Solo pueden haber 8 elementos en total

        # Publicar componente
        self.setCentralWidget(combo)
        self.show()

    def cambioIndice(self, indiceNuevo):
        print(f'Nuevo indice seleccionado {indiceNuevo}')

    def cambioTexto(self, textoNuevo):
        print(f'Nuevo texto ingresado {textoNuevo}')

if __name__ == "__main__":
    app = QApplication([])
    ventana = ventanaPrincipal()
    app.exec()