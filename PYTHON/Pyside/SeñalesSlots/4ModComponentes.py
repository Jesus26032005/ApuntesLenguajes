# ? Señales o eventos:
#   Son notificaciones que emiten los widgets cuando ocurre una acción (ej: clic, cambio de estado).
# ? Slots:
#   Son funciones que responden a esas señales. Se pueden conectar varias señales a un mismo slot y viceversa.

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QAction
from PySide6.QtCore import QSize

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        # ? setWindowTitle(str): Establece el título de la ventana.
        self.setWindowTitle("Almacenar estado")
        # ? setFixedSize(QSize(ancho, alto)): Fija el tamaño de la ventana.
        self.setFixedSize(QSize(400, 300))
        # !Todo elemento tiene señales que envia
        # ? QPushButton(str): Crea un botón con el texto indicado.
        self.boton = QPushButton("Haz Click Aquí")
        # ? Señales principales de QPushButton:
        # ? - clicked: Se emite cuando el botón es presionado. Si el botón es checkable, pasa un bool indicando el estado (True si está presionado, False si no).
        # ?   Conexión: self.boton.clicked.connect(self.miFuncion)   # Recibe: (checked: bool) si es checkable, nada si no.
        # ? - pressed: Se emite cuando el botón es presionado (sin soltar).
        # ?   Conexión: self.boton.pressed.connect(self.miFuncion)   # No recibe argumentos.
        # ? - released: Se emite cuando se suelta el botón.
        # ?   Conexión: self.boton.released.connect(self.miFuncion)  # No recibe argumentos.
        # ? - toggled: Se emite cuando cambia el estado checkable. Pasa un bool (True/False).
        # ?   Conexión: self.boton.toggled.connect(self.miFuncion)   # Recibe: (checked: bool)

        # ? Asociar la señal clicked a un slot (función que responde al evento)
        self.boton.clicked.connect(self._eventoClick)

        # ? setCentralWidget(widget): Coloca el widget en el área central de la ventana principal.
        self.setCentralWidget(self.boton)

        # ? QMainWindow también tiene señales propias, como:
        # ? - windowTitleChanged: Se emite cuando cambia el título de la ventana. Pasa el nuevo título (str) como argumento.
        # ?   Conexión: self.windowTitleChanged.connect(self.miFuncion)   # Recibe: (nuevoTitulo: str)
        # ? - windowIconChanged: Se emite cuando cambia el ícono de la ventana.
        # ?   Conexión: self.windowIconChanged.connect(self.miFuncion)    # Recibe: (nuevoIcono: QIcon)
        self.windowTitleChanged.connect(self._cambioTitulo)

        self.show()

    def _eventoClick(self):
        # ? Cambiar texto del botón usando setText(str)
        self.boton.setText("Nuevo texto")
        # ? setEnabled(bool): Habilita o deshabilita el botón. False lo deshabilita.
        self.boton.setEnabled(False)
        # ? Cambiar el título de la ventana con setWindowTitle(str)
        self.setWindowTitle("Almacenar estado titulo new")
        # ? Otras acciones posibles:
        # ? self.boton.setCheckable(True)  # Permite que el botón tenga dos estados (toggle)
        # ? self.boton.setChecked(True)    # Marca el botón como presionado si es checkable

    def _cambioTitulo(self, nuevoTitulo):
        # ? Este slot recibe el nuevo título como argumento (str)
        print("Se cambió el título de la ventana")
        print(f'Nuevo título: {nuevoTitulo}')

if __name__ == "__main__":
    # ? QApplication([]): Inicializa la aplicación y el ciclo de eventos.
    app = QApplication([])
    ventana = VentanaPrincipal()
    # ? app.exec(): Ejecuta el bucle principal de la aplicación.
    app.exec()

# ? Información adicional:
# ? - Se pueden conectar señales a funciones lambda, métodos de otras clases o funciones normales.
# ? - Los slots pueden recibir argumentos si la señal los emite.
# ? - Para botones no checkables, clicked no pasa argumentos; si es checkable, pasa un bool.
# ? - Otras señales útiles de QPushButton:
# ?   - pressed: No recibe argumentos. Se emite al presionar el botón.
# ?     Conexión: self.boton.pressed.connect(self.miFuncion)
# ?   - released: No recibe argumentos. Se emite al soltar el botón.
# ?     Conexión: self.boton.released.connect(self.miFuncion)
# ?   - toggled(bool): Recibe un bool indicando el nuevo estado (solo si el botón es checkable).
# ?     Conexión: self.boton.toggled.connect(self.miFuncion)
# ? - Señales de QMainWindow:
# ?   - windowTitleChanged(str): Nuevo título como argumento.
# ?     Conexión: self.windowTitleChanged.connect(self.miFuncion)
# ?   - windowIconChanged(QIcon): Nuevo ícono como argumento.
# ?     Conexión: self.windowIconChanged.connect(self.miFuncion)
# ? - Métodos de QPushButton:
# ?   - setText(str): Cambia el texto del botón.
# ?   - setEnabled(bool): Habilita/deshabilita el botón.
# ?   - setCheckable(bool): Permite que el botón tenga dos estados (toggle).
# ?   - setChecked(bool): Cambia el estado del botón si es checkable.
# ?   - isChecked(): Devuelve True si el botón está presionado (checkable).
# ? - Métodos de QMainWindow:
# ?   - setWindowTitle(str): Cambia el título de la ventana.
# ?   - setCentralWidget(widget): Coloca un widget en el área central.
# ? - Alternativas:
# ?   - Puedes conectar varias señales a un mismo slot, o una señal a varios slots.
# ?   - Puedes usar funciones lambda para lógica simple en la conexión de señales.
# ?   - Puedes crear tus propias señales personalizadas usando Signal de PySide6.QtCore.

# ----------------------------------------------------------
# ? SEÑALES MÁS COMUNES DE WIDGETS EN PySide6 (NO SOLO DEL CÓDIGO)
# ----------------------------------------------------------

# ? QPushButton (y QAbstractButton):
# ?   - clicked([checked: bool])         # Se emite al hacer clic. Si es checkable, pasa el estado.
# ?     Conexión: boton.clicked.connect(funcion)         # Recibe: (checked: bool) si es checkable, nada si no.
# ?   - pressed()                        # Se emite al presionar el botón.
# ?     Conexión: boton.pressed.connect(funcion)         # No recibe argumentos.
# ?   - released()                       # Se emite al soltar el botón.
# ?     Conexión: boton.released.connect(funcion)        # No recibe argumentos.
# ?   - toggled(checked: bool)           # Se emite al cambiar el estado checkable.
# ?     Conexión: boton.toggled.connect(funcion)         # Recibe: (checked: bool)

# ? QLineEdit:
# ?   - textChanged(str)                 # Se emite cuando cambia el texto.
# ?     Conexión: lineedit.textChanged.connect(funcion)  # Recibe: (texto: str)
# ?   - editingFinished()                # Se emite al terminar la edición (Enter o perder foco).
# ?     Conexión: lineedit.editingFinished.connect(funcion) # No recibe argumentos.
# ?   - returnPressed()                  # Se emite al presionar Enter.
# ?     Conexión: lineedit.returnPressed.connect(funcion)   # No recibe argumentos.
# ?   - selectionChanged()               # Se emite al cambiar la selección de texto.
# ?     Conexión: lineedit.selectionChanged.connect(funcion) # No recibe argumentos.

# ? QTextEdit:
# ?   - textChanged()                    # Se emite cuando cambia el texto.
# ?     Conexión: textedit.textChanged.connect(funcion)      # No recibe argumentos.
# ?   - cursorPositionChanged()          # Se emite al mover el cursor.
# ?     Conexión: textedit.cursorPositionChanged.connect(funcion) # No recibe argumentos.

# ? QCheckBox:
# ?   - stateChanged(int)                # Se emite al cambiar el estado (0: desmarcado, 2: marcado).
# ?     Conexión: checkbox.stateChanged.connect(funcion)     # Recibe: (estado: int)
# ?   - toggled(bool)                    # Se emite al cambiar el estado (True/False).
# ?     Conexión: checkbox.toggled.connect(funcion)          # Recibe: (checked: bool)

# ? QRadioButton:
# ?   - toggled(bool)                    # Se emite al cambiar el estado.
# ?     Conexión: radiobutton.toggled.connect(funcion)       # Recibe: (checked: bool)

# ? QComboBox:
# ?   - currentIndexChanged(int)         # Se emite al cambiar el índice seleccionado.
# ?     Conexión: combobox.currentIndexChanged.connect(funcion) # Recibe: (index: int)
# ?   - currentTextChanged(str)          # Se emite al cambiar el texto seleccionado.
# ?     Conexión: combobox.currentTextChanged.connect(funcion)  # Recibe: (texto: str)
# ?   - activated(int)                   # Se emite al activar una opción.
# ?     Conexión: combobox.activated.connect(funcion)            # Recibe: (index: int)

# ? QListWidget:
# ?   - itemClicked(QListWidgetItem)     # Se emite al hacer clic en un ítem.
# ?     Conexión: listwidget.itemClicked.connect(funcion)       # Recibe: (item: QListWidgetItem)
# ?   - itemDoubleClicked(QListWidgetItem) # Se emite al hacer doble clic en un ítem.
# ?     Conexión: listwidget.itemDoubleClicked.connect(funcion) # Recibe: (item: QListWidgetItem)
# ?   - currentItemChanged(QListWidgetItem, QListWidgetItem) # Se emite al cambiar el ítem seleccionado.
# ?     Conexión: listwidget.currentItemChanged.connect(funcion) # Recibe: (itemActual: QListWidgetItem, itemAnterior: QListWidgetItem)

# ? QTableWidget:
# ?   - cellClicked(int, int)            # Se emite al hacer clic en una celda.
# ?     Conexión: tablewidget.cellClicked.connect(funcion)      # Recibe: (fila: int, columna: int)
# ?   - cellChanged(int, int)            # Se emite al cambiar el contenido de una celda.
# ?     Conexión: tablewidget.cellChanged.connect(funcion)      # Recibe: (fila: int, columna: int)

# ? QSlider:
# ?   - valueChanged(int)                # Se emite al cambiar el valor.
# ?     Conexión: slider.valueChanged.connect(funcion)          # Recibe: (valor: int)
# ?   - sliderPressed()                  # Se emite al presionar el slider.
# ?     Conexión: slider.sliderPressed.connect(funcion)         # No recibe argumentos.
# ?   - sliderReleased()                 # Se emite al soltar el slider.
# ?     Conexión: slider.sliderReleased.connect(funcion)        # No recibe argumentos.

# ? QMainWindow:
# ?   - windowTitleChanged(str)          # Se emite al cambiar el título.
# ?     Conexión: mainwindow.windowTitleChanged.connect(funcion) # Recibe: (nuevoTitulo: str)
# ?   - windowIconChanged(QIcon)         # Se emite al cambiar el ícono.
# ?     Conexión: mainwindow.windowIconChanged.connect(funcion)  # Recibe: (nuevoIcono: QIcon)

# ? QWidget (base de todos los widgets):
# ?   - destroyed(QObject*)              # Se emite al destruir el widget.
# ?     Conexión: widget.destroyed.connect(funcion)             # Recibe: (objeto: QObject)
# ?   - customContextMenuRequested(QPoint) # Se emite al solicitar un menú contextual.
# ?     Conexión: widget.customContextMenuRequested.connect(funcion) # Recibe: (pos: QPoint)

# ? QAction:
# ?   - triggered(bool)                  # Se emite al activar la acción.
# ?     Conexión: action.triggered.connect(funcion)             # Recibe: (checked: bool) si es checkable, nada si no.
# ?   - hovered()                        # Se emite al pasar el mouse sobre la acción.
# ?     Conexión: action.hovered.connect(funcion)               # No recibe argumentos.
# ?   - toggled(bool)                    # Se emite al cambiar el estado checkable.
# ?     Conexión: action.toggled.connect(funcion)               # Recibe: (checked: bool)

# ? Puedes consultar la documentación oficial de cada widget para ver todas sus señales y argumentos:
# ?