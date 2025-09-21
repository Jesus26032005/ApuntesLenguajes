from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget
from PySide6.QtCore import Qt

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("listWidget")
        self.setGeometry(100, 100, 600, 400)
        # QListWidget es un widget que muestra una lista de elementos (tipo texto o QListWidgetItem).
        # Permite seleccionar uno o varios elementos, y muestra todos los elementos a la vez.
        # QListWidget(parent: QWidget = None)
        listaWidget = QListWidget()

        # Métodos principales de QListWidget y sus argumentos:
        # addItem(item: str | QListWidgetItem): Agrega un elemento (texto o QListWidgetItem) a la lista.
        # addItems(items: Iterable[str]): Agrega varios elementos a partir de una lista o iterable de strings.
        # insertItem(row: int, item: str | QListWidgetItem): Inserta un elemento en la posición dada.
        # insertItems(row: int, items: Iterable[str]): Inserta varios elementos en la posición dada.
        # takeItem(row: int) -> QListWidgetItem: Elimina y retorna el elemento en la posición dada.
        # clear(): Elimina todos los elementos.
        # count() -> int: Devuelve el número de elementos.
        # item(row: int) -> QListWidgetItem: Devuelve el elemento en la posición dada.
        # currentItem() -> QListWidgetItem: Devuelve el elemento actualmente seleccionado.
        # setCurrentItem(item: QListWidgetItem): Selecciona el elemento dado.
        # setSelectionMode(mode: QAbstractItemView.SelectionMode): Define el modo de selección.
        #   Modos: SingleSelection, MultiSelection, ExtendedSelection, NoSelection.
        # selectedItems() -> list[QListWidgetItem]: Devuelve una lista de los elementos seleccionados.
        # setSortingEnabled(enable: bool): Habilita/deshabilita el ordenamiento automático de los elementos.
        # setItemWidget(item: QListWidgetItem, widget: QWidget): Permite mostrar un widget personalizado en un elemento.

        # Agregar elementos
        listaWidget.addItem("Elemento 1")
        listaWidget.addItems(["Elemento 2", "Elemento 3", "Elemento 4"])

        # Señales (signals) de QListWidget:
        # currentItemChanged(current: QListWidgetItem, previous: QListWidgetItem): Se emite cuando cambia el elemento seleccionado.
        # currentTextChanged(text: str): Se emite cuando cambia el texto del elemento seleccionado.
        # itemClicked(item: QListWidgetItem): Se emite cuando se hace clic en un elemento.
        # itemDoubleClicked(item: QListWidgetItem): Se emite cuando se hace doble clic en un elemento.
        # itemSelectionChanged(): Se emite cuando cambia la selección (útil para selección múltiple).
        # itemActivated(item: QListWidgetItem): Se emite cuando se activa un elemento (doble clic o enter).
        # itemEntered(item: QListWidgetItem): Se emite cuando el mouse entra en un elemento (si está habilitado el tracking).

        # Ejemplo de selección múltiple:
        # listaWidget.setSelectionMode(QListWidget.MultiSelection)

        # Conectar señales de cambio de elemento seleccionado
        listaWidget.currentItemChanged.connect(self.cambioElemento)
        # Cambio texto seleccionado
        listaWidget.currentTextChanged.connect(self.cambioElemento)

        self.setCentralWidget(listaWidget)
        self.show()
        
    def cambioElemento(self, item):
        # El argumento 'item' puede ser un QListWidgetItem o un str (para currentTextChanged)
        # Si es un QListWidgetItem, accede al texto con item.text()
        if hasattr(item, "text"):
            print(f"Elemento seleccionado: {item.text()}")
        elif isinstance(item, str):
            print(f"Texto seleccionado: {item}")
        else:
            print("No hay elemento seleccionado")

if __name__ == "__main__":
    app = QApplication([])
    ventana = ventanaPrincipal()
    app.exec()