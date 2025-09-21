from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox
from PySide6.QtCore import Qt

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Checkbox")
        self.setGeometry(100, 100, 600, 400)

        # Crear componente de checkbox
        # QCheckBox(text: str = '', parent: QWidget = None)
        checkbox = QCheckBox("Este es un checbox")

        # Métodos principales de QCheckBox y sus argumentos:
        # setText(text: str): Cambia el texto mostrado junto al checkbox.
        # text() -> str: Devuelve el texto actual.
        # setChecked(checked: bool): Marca o desmarca el checkbox.
        # isChecked() -> bool: Devuelve True si está marcado.
        # setTristate(y: bool = True): Permite un tercer estado (parcialmente marcado).
        # isTristate() -> bool: Devuelve True si el checkbox está en modo tristate.
        # checkState() -> Qt.CheckState: Devuelve el estado actual (Qt.Checked, Qt.Unchecked, Qt.PartiallyChecked).
        # setCheckState(state: Qt.CheckState): Cambia el estado (Checked, Unchecked, PartiallyChecked).
        # setIcon(icon: QIcon): Asigna un ícono al checkbox.
        # setStyleSheet(css: str): Aplica estilos CSS.

        # Activar tercer estado, se tienen 3 de forma original pero por default solo hay dos
        # Qt.Unchecked (0), Qt.PartiallyChecked (1), Qt.Checked (2)
        checkbox.setTristate(True)

        # Señales (signals) de QCheckBox:
        # stateChanged(int estado): Se emite cuando cambia el estado (0, 1, 2).
        # toggled(bool checked): Se emite cuando cambia entre marcado/desmarcado (ignora el estado parcial).
        # clicked(bool checked): Se emite cuando el usuario hace clic.
        # pressed(): Se emite cuando el usuario presiona el checkbox.
        # released(): Se emite cuando el usuario suelta el checkbox.

        # Conectar señal con un slot
        checkbox.stateChanged.connect(self.mostrarEstado)

        # Publicar componente
        self.setCentralWidget(checkbox)
        self.show()
    
    def mostrarEstado(self, estado):
        # El argumento 'estado' es un int: 0 (Unchecked), 1 (PartiallyChecked), 2 (Checked)
        if estado == Qt.Checked:
            print("Checkbox marcado")
        elif estado == Qt.Unchecked:
            print("Checkbox desmarcado")
        elif estado == Qt.PartiallyChecked:
            print("Checkbox parcialmente marcado")
        else:
            print("Estado desconocido")

if __name__ == "__main__":
    app = QApplication([])
    ventana = ventanaPrincipal()
    app.exec()