"""
Widget Menu en Tkinter
---------------------
- Menu es el widget de Tkinter para crear menús desplegables en la ventana principal o en menús contextuales (clic derecho).
- Permite organizar comandos, submenús y opciones de la aplicación de forma estructurada y accesible.

Sintaxis básica:
menu = tk.Menu(master, opciones)

Tipos de menús:
- Menú de barra principal (menubar): se coloca en la ventana principal con ventana.config(menu=menubar)
- Menú desplegable (submenu): se añade a la barra principal o a otros menús con add_cascade()
- Menú contextual (popup): se muestra al hacer clic derecho usando .post(x, y)

Argumentos principales de Menu:
- master: ventana o frame contenedor (obligatorio)
- tearoff: True/False, si el menú puede separarse (por defecto True)
- bg, fg: color de fondo y texto
- font: tipo y tamaño de letra
- activebackground, activeforeground: colores al pasar el mouse

Métodos principales:
- add_command(label, command): añade una opción que ejecuta una función
- add_separator(): añade una línea divisoria
- add_cascade(label, menu): añade un submenú
- add_checkbutton(...): añade una opción con check
- add_radiobutton(...): añade una opción tipo radio

Notas y buenas prácticas:
- Usa tearoff=0 para menús más profesionales (sin línea punteada).
- Puedes anidar submenús y crear menús contextuales fácilmente.
- Los menús pueden tener atajos de teclado (argumento accelerator).
- ttk no tiene su propio Menu, se usa el de tk.

Documentación oficial: https://docs.python.org/3/library/tkinter.html#tkinter.Menu
"""

import tkinter


ventana= tkinter.Tk()
ventana.geometry("600x400")
ventana.title("Menu")

def crearMenu():
    menu= tkinter.Menu(ventana)
    #añadir tearoff
    tearoff=0 #0 o False para que no se pueda separar el menu de la ventana, desacitiva dicha opcion
    menuArchivo= tkinter.Menu(menu, tearoff=tearoff) #Se coloca como master a menu porq este sera submenu
    #Agregar opcion al menuArchivo
    menuArchivo.add_command(label="Nuevo") #Añade comando
    menuArchivo.add_command(label="Abrir")
    menuArchivo.add_command(label="Guardar")
    menuArchivo.add_separator() #Añade una linea divisoria
    menuArchivo.add_command(label="Salir", command=ventana.destroy) #Añade comando y al hacer clic cierra la ventana

    menuAcerca= tkinter.Menu(menu, tearoff=tearoff)
    menuAcerca.add_command(label="Acerca de...")

    menu.add_cascade(menu=menuArchivo, label="Archivo")
    menu.add_cascade(menu=menuAcerca, label="Ayuda")
    ventana.config(menu=menu) # Configura la ventana principal para usar el menú, pues menu: asigna la barra de menú principal

crearMenu()
ventana.mainloop()

# Explicación de las funciones principales de Menu
# -----------------------------------------------
# - add_command(label, command, ...):
#   Añade una opción al menú. Cuando el usuario la selecciona, ejecuta la función indicada en command.
#   label: texto que se muestra en el menú.
#   command: función a ejecutar al hacer clic.
#   accelerator: texto para mostrar atajo de teclado (solo visual).
#   Ejemplo: menu.add_command(label="Guardar", command=guardar)
#
# - add_separator():
#   Añade una línea divisoria horizontal para separar grupos de opciones.
#   No recibe argumentos.
#   Ejemplo: menu.add_separator()
#
# - add_cascade(label, menu, ...):
#   Añade un submenú desplegable dentro del menú principal.
#   label: texto del submenú.
#   menu: objeto Menu que será el submenú.
#   Ejemplo: menubar.add_cascade(label="Archivo", menu=archivo)
#
# - add_checkbutton(label, variable, ...):
#   Añade una opción con casilla de verificación (checkbox).
#   variable: tk.BooleanVar o similar para guardar el estado.
#   Ejemplo: menu.add_checkbutton(label="Opción", variable=var)
#
# - add_radiobutton(label, variable, value, ...):
#   Añade una opción tipo radio (solo una puede estar activa en el grupo).
#   variable: tk.StringVar o tk.IntVar para guardar el valor seleccionado.
#   value: valor asociado a esa opción.
#   Ejemplo: menu.add_radiobutton(label="Rojo", variable=color, value="rojo")
#
# - post(x, y):
#   Muestra el menú en la posición (x, y) de la pantalla (usado para menús contextuales).
#   Ejemplo: menu_popup.post(event.x_root, event.y_root)
#
# Estas funciones permiten construir menús flexibles y personalizados en tus aplicaciones Tkinter.

# Metodo cerrar ventana
# metodo quit: cierra la ventana actual
# metodo destroy: destruye la ventana y finaliza la aplicación
# metodo sys.exit: cierra la aplicación de forma forzada