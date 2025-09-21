from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QFileDialog, QColorDialog, QFontDialog, QMessageBox, QInputDialog

class VentanaDialogo(QDialog):
    def __init__(self, padre= None):
        super().__init__(padre) #Se pasa referencia de objeto padre
        self.setWindowTitle("Ventana de dialogo parte 2")
        # QDialog es una ventana secundaria para interacción temporal con el usuario.
        # Métodos principales de QDialog:
        # exec() -> int: Muestra el diálogo de forma modal (bloquea la ventana principal hasta que se cierre).
        # show(): Muestra el diálogo de forma no modal.
        # accept(): Cierra el diálogo y retorna QDialog.Accepted.
        # reject(): Cierra el diálogo y retorna QDialog.Rejected.
        # setWindowTitle(title: str): Cambia el título de la ventana de diálogo.
        # setModal(modal: bool): Define si el diálogo es modal o no.
        # setLayout(layout: QLayout): Asigna un layout al diálogo.
        # Señales de QDialog:
        # accepted(): Se emite cuando se acepta el diálogo (accept()).
        # rejected(): Se emite cuando se rechaza el diálogo (reject()).
        # finished(int result): Se emite cuando el diálogo se cierra, con el resultado (Accepted/Rejected).

        # QDialogButtonBox es un widget que agrupa botones estándar para diálogos (OK, Cancel, Yes, No, etc).
        # Métodos principales de QDialogButtonBox:
        # addButton(button: QAbstractButton, role: QDialogButtonBox.ButtonRole): Añade un botón personalizado.
        # setStandardButtons(buttons: QDialogButtonBox.StandardButtons): Define los botones estándar.
        # button(role: QDialogButtonBox.ButtonRole) -> QAbstractButton: Devuelve el botón para un rol específico.
        # setOrientation(orientation: Qt.Orientation): Cambia la orientación de los botones.
        # clear(): Elimina todos los botones.
        # Señales de QDialogButtonBox:
        # accepted(): Se emite cuando se acepta.
        # rejected(): Se emite cuando se rechaza.

        # Agregamos botones estándar OK y Cancel
                # Botones estándar de QDialogButtonBox:
        # QDialogButtonBox.Ok            # Botón OK (Aceptar)
        # QDialogButtonBox.Cancel        # Botón Cancelar
        # QDialogButtonBox.Yes           # Botón Sí
        # QDialogButtonBox.No            # Botón No
        # QDialogButtonBox.Abort         # Botón Abort (Abortar)
        # QDialogButtonBox.Retry         # Botón Reintentar
        # QDialogButtonBox.Ignore        # Botón Ignorar
        # QDialogButtonBox.Close         # Botón Cerrar
        # QDialogButtonBox.Help          # Botón Ayuda
        # QDialogButtonBox.Apply         # Botón Aplicar cambios
        # QDialogButtonBox.Reset         # Botón Restablecer valores
        # QDialogButtonBox.Save          # Botón Guardar
        # QDialogButtonBox.Discard       # Botón Descartar cambios
        # QDialogButtonBox.Open          # Botón Abrir
        # QDialogButtonBox.RestoreDefaults # Botón Restaurar valores por defecto

        # Puedes combinarlos usando el operador | (OR), por ejemplo:
        # QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        botones = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self._botonesDialogo = QDialogButtonBox(botones)
        self._botonesDialogo.accepted.connect(self.accept)
        self._botonesDialogo.rejected.connect(self.reject)

        # Creamos layout para poder publicar los botones
        self._layout= QVBoxLayout()
        mensaje= QLabel("Presiona alguno de los botones")
        self._layout.addWidget(mensaje)
        self._layout.addWidget(self._botonesDialogo)
        self.setLayout(self._layout)

        # Clases hijas útiles de QDialog y sus métodos principales:
        # QFileDialog: Diálogo para abrir/guardar archivos.
        #   - getOpenFileName(parent, caption, dir, filter): Abre diálogo para seleccionar un archivo.
        #   - getSaveFileName(parent, caption, dir, filter): Abre diálogo para guardar un archivo.
        #   - setFileMode(mode): Define el modo de selección (archivo, carpeta, etc).
        #   - setNameFilter(filter): Define los tipos de archivos permitidos.
        # QColorDialog: Diálogo para seleccionar colores.
        #   - getColor(initial, parent): Abre diálogo para seleccionar un color.
        #   - setCurrentColor(color): Define el color inicial.
        #   - selectedColor(): Devuelve el color seleccionado.
        # QFontDialog: Diálogo para seleccionar fuentes.
        #   - getFont(parent): Abre diálogo para seleccionar una fuente.
        #   - setCurrentFont(font): Define la fuente inicial.
        #   - selectedFont(): Devuelve la fuente seleccionada.
        # QMessageBox: Diálogo para mostrar mensajes, advertencias, preguntas, etc.
        #   - information(parent, title, text): Muestra un mensaje informativo.
        #   - warning(parent, title, text): Muestra una advertencia.
        #   - question(parent, title, text): Muestra una pregunta (sí/no).
        #   - critical(parent, title, text): Muestra un mensaje crítico.
        #   - setText(text): Cambia el texto del mensaje.
        #   - setIcon(icon): Cambia el ícono del mensaje.
        # QInputDialog: Diálogo para pedir un valor simple al usuario.
        #   - getText(parent, title, label): Pide un texto.
        #   - getInt(parent, title, label): Pide un número entero.
        #   - getDouble(parent, title, label): Pide un número decimal.
        #   - getItem(parent, title, label, items): Pide seleccionar un elemento de una lista.

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventanas de dialogo")
        # Es una ventana que depende de otra ventana para interactuar con el usuario
        self.setGeometry(100, 100, 800, 600)
        # Se construye boton
        boton = QPushButton("Abrir ventana de dialogo")
        boton.clicked.connect(self.abrirVentanaDialogo)
        self.setCentralWidget(boton)
        self.show()

    def abrirVentanaDialogo(self, estado):
        print("Abrir ventana de dialogo")
        # Aquí se abriría la ventana de diálogo personalizada
        dialogo= VentanaDialogo(self)
        valorretornado= dialogo.exec()
        print(f"Valor retornado: {valorretornado}")

if __name__ == "__main__":
    app = QApplication()
    ventana = ventanaPrincipal()
    app.exec()