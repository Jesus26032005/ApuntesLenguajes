from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QAction
from PySide6.QtCore import QSize

# Clase principal que hereda de QMainWindow, la cual proporciona una ventana principal estándar
class VentanaPyside(QMainWindow):
    def __init__(self):
        super().__init__()
        # setWindowTitle(str): Establece el título de la ventana
        self.setWindowTitle("Componentes Básicos")
        # resize(ancho, alto): Permite cambiar el tamaño de la ventana libremente
        # self.resize(500, 500)
        # setFixedSize(QSize(ancho, alto)): Fija el tamaño de la ventana, impidiendo que el usuario la redimensione
        self.setFixedSize(QSize(500, 500))
        # Llama a un método privado para agregar componentes a la ventana
        self._agregarComponentes()
        # show(): Muestra la ventana en pantalla
        self.show()

    def _agregarComponentes(self):
        # --- Barra de menú ---
        # menuBar(): Devuelve la barra de menú de la ventana principal (QMenuBar).
        menu = self.menuBar()

        # addMenu(str): Crea un menú desplegable en la barra de menú.
        menuArchivo = menu.addMenu("Archivo")

        # --- Acciones del menú ---
        # QAction(str, parent): Crea una acción que puede agregarse a menús o barras de herramientas.
        accionNuevo = QAction("Nuevo", self)
        accionAbrir = QAction("Abrir", self)
        accionGuardar = QAction("Guardar", self)

        # addAction(QAction): Añade la acción al menú.
        menuArchivo.addAction(accionNuevo)
        menuArchivo.addAction(accionAbrir)
        menuArchivo.addAction(accionGuardar)

        # setStatusTip(str): Texto de ayuda que aparece en la barra de estado al pasar el mouse sobre la acción.
        accionNuevo.setStatusTip("Crear un nuevo archivo")
        accionAbrir.setStatusTip("Abrir un archivo existente")
        accionGuardar.setStatusTip("Guardar el archivo actual")

        # setShortcut(str): Permite definir atajos de teclado para las acciones (opcional).
        # accionNuevo.setShortcut("Ctrl+N")
        # accionAbrir.setShortcut("Ctrl+A")
        # accionGuardar.setShortcut("Ctrl+S")

        # triggered.connect(función): Conecta la acción a una función que se ejecuta al seleccionarla.
        # accionNuevo.triggered.connect(self.funcion_nuevo)

        # --- Barra de estado ---
        # statusBar(): Devuelve la barra de estado (QStatusBar) de la ventana principal.
        # showMessage(str): Muestra un mensaje temporal en la barra de estado.
        self.statusBar().showMessage("Información de la barra de estado")

        # --- Widget central ---
        # QPushButton(str, parent): Crea un botón con texto y lo asocia a la ventana principal.
        boton = QPushButton("Click Me", self)

        # clicked.connect(función): Conecta el clic del botón a una función.
        # boton.clicked.connect(self.funcion_boton)

        # setCentralWidget(widget): Coloca el widget dado en el área central de la ventana principal.
        self.setCentralWidget(boton)

        # --- Separador y acción de salir ---
        # addSeparator(): Agrega una línea separadora en el menú.
        menuArchivo.addSeparator()

        # addAction(str): Agrega una acción simple al menú (en este caso, "Salir").
        # Esto crea una acción básica, pero no permite conectar señales fácilmente.
        menuArchivo.addAction("Salir")
        # Alternativamente, se puede crear una QAction para "Salir" y conectarla a una función:
        # accionSalir = QAction("Salir", self)
        # accionSalir.triggered.connect(self.close)  # Cierra la ventana
        # menuArchivo.addAction(accionSalir)

        # Otras alternativas y widgets:
        # - Para agregar más de un widget central, se recomienda usar layouts (QVBoxLayout, QHBoxLayout, etc.)
        # - Se pueden agregar atajos de teclado a las acciones con setShortcut("Ctrl+N")
        # - Para conectar señales (como clicked) a funciones, usar: boton.clicked.connect(self.mi_funcion)
        # - Otros widgets útiles: QLabel, QLineEdit, QTextEdit, QCheckBox, QRadioButton, QComboBox, QListWidget, QTableWidget, QSlider, QProgressBar, etc.
        # - QWidget es el componente base para todos los widgets; puedes crear tus propios widgets personalizados heredando de QWidget.

if __name__ == "__main__":
    import sys
    # QApplication(sys.argv): Inicializa la aplicación y gestiona el ciclo de eventos
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPyside()
    # sys.exit(app.exec()): Ejecuta el bucle principal de la aplicación y asegura una salida limpia
    sys.exit(aplicacion.exec())



# Métodos principales del objeto menuBar() (QMenuBar):
# - addMenu(title: str | QMenu): Agrega un menú desplegable.
# - addAction(action: QAction | str): Agrega una acción al menú o barra de menú.
# - addSeparator(): Agrega un separador visual.
# - clear(): Elimina todos los menús y acciones.
# - insertMenu(before: QAction, menu: QMenu): Inserta un menú antes de una acción dada.
# - insertSeparator(before: QAction): Inserta un separador antes de una acción dada.
# - insertAction(before: QAction, action: QAction): Inserta una acción antes de otra.
# - removeAction(action: QAction): Elimina una acción.
# - findChild(type, name): Busca un hijo por tipo y nombre.
# - setNativeMenuBar(bool): Define si se usa la barra de menú nativa del sistema operativo.
# - isNativeMenuBar(): Retorna si se está usando la barra de menú nativa.

# Es mejor usar QAction en vez de addAction(str) porque:
# - QAction permite conectar señales (como triggered) a funciones fácilmente.
# - Puedes personalizar la acción: agregar iconos, atajos de teclado (setShortcut), descripciones (setStatusTip), habilitar/deshabilitar, etc.
# - addAction(str) solo agrega una acción simple, sin posibilidad de personalización ni conexión directa a eventos.

# Ejemplo recomendado:
# accionSalir = QAction("Salir", self)
# accionSalir.setStatusTip("Cerrar la aplicación")
# accionSalir.triggered.connect(self.close)
# menuArchivo.addAction(accionSalir)

# Ejemplo NO recomendado:
# menuArchivo.addAction("Salir")  # No se puede conectar a una función ni personalizar
