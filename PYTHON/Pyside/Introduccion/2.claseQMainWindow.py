import sys
from PySide6.QtWidgets import QApplication, QMainWindow
# Se crea una instancia de QApplication.
# QApplication es la clase base para cualquier aplicación Qt.
# Se encarga de gestionar los recursos y el ciclo de eventos de la aplicación.
applicacion = QApplication()  # Si se desea usar argumentos desde linea de comandos: QApplication(sys.argv)

# PySide6 proporciona una amplia variedad de componentes (widgets) para crear interfaces gráficas.
# Algunos de los widgets más comunes incluyen:
# - QLabel: Etiquetas de texto o imágenes.
# - QPushButton: Botones interactivos.
# - QLineEdit: Campos de texto de una sola línea.
# - QTextEdit: Campos de texto multilínea.
# - QCheckBox: Casillas de verificación.
# - QRadioButton: Botones de opción.
# - QComboBox: Menús desplegables.
# - QListWidget: Listas de elementos.
# - QTableWidget: Tablas de datos.
# - QSlider: Barras deslizantes.
# - QProgressBar: Barras de progreso.
# - QMenuBar, QToolBar, QStatusBar: Componentes para menús, herramientas y barras de estado.
# - QWidget: Es el componente base para todos los widgets en PySide6. Puedes crear tus propios widgets personalizados heredando de QWidget.
# - QMainWindow: Es una ventana principal que proporciona una estructura estándar para aplicaciones, permitiendo agregar menús, barras de herramientas, barras de estado y un widget central.
# Todos estos widgets pueden agregarse a la ventana principal usando métodos como setCentralWidget()
# o añadiéndolos a layouts (QVBoxLayout, QHBoxLayout, etc.) para organizar la interfaz.

# Crear un objeto ventana principal.
# QMainWindow es una clase que proporciona una ventana principal con funcionalidades estándar,
# como barra de menús, barra de herramientas, barra de estado y área central.
ventana = QMainWindow()  # Objeto que representa la ventana principal

# Configuración de la ventana principal:
ventana.setWindowTitle("Hola Mundo")  # Establece el título de la ventana
ventana.resize(500, 500)              # Establece el tamaño de la ventana (ancho, alto)
ventana.show()                        # Muestra la ventana en pantalla

#Se ejecuta la aplicacion
sys.exit(applicacion.exec())