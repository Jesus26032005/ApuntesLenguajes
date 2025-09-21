import sys
from PySide6.QtWidgets import QApplication, QWidget

applicacion=QApplication() #Clase base para la aplicacion, se encarga de procesar eventos
#Crear un objeto ventana
ventana= QWidget() #Objeto que representa la ventana
ventana.setWindowTitle("Hola Mundo") #Titulo de la ventana
ventana.resize(400, 300) #Tamaño de la ventana (ancho, alto)
ventana.show() #Mostrar la ventana

#Se ejecuta la aplicacion
sys.exit(applicacion.exec())