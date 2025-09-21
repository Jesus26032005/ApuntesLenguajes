# Importar la biblioteca tkinter
import tkinter
#Creamos un objeto usando la clase TK
ventana = tkinter.Tk()
#Modificamos el tamaño de la ventana
ventana.geometry("600x400")
#Cambiar el nombre de la ventana
ventana.title("Introduccion tkinter")
#Cambiar el icono de la ventana
ventana.iconbitmap("icono.ico")
#Inicializar ventana(siempre se ejecuta al final)
ventana.mainloop()