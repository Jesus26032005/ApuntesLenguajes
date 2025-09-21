"""
Gestor de geometría grid en Tkinter
-----------------------------------
- El grid manager permite organizar widgets en una cuadrícula de filas y columnas.
- Es ideal para interfaces donde necesitas alineación precisa y estructura tabular.
- Cada widget se coloca en una celda específica usando los argumentos row (fila) y column (columna).
- No se puede usar grid y pack en el mismo contenedor (ventana o frame).

Sintaxis básica:
widget.grid(row=FILA, column=COLUMNA)

Argumentos principales de grid():
- row: número de fila (empieza en 0)
- column: número de columna (empieza en 0)
- rowspan: cuántas filas ocupa el widget (por defecto 1)
- columnspan: cuántas columnas ocupa el widget (por defecto 1)
- sticky: alinea el widget dentro de la celda ('n', 's', 'e', 'w', o combinaciones)
- padx, pady: espacio externo horizontal y vertical (en píxeles)
- ipadx, ipady: espacio interno (relleno dentro del widget)

Notas y buenas prácticas:
- Puedes usar grid_rowconfigure y grid_columnconfigure para hacer que filas/columnas se expandan con la ventana.
- Si no defines sticky, el widget se centra en la celda.
- Es útil para formularios, tableros, calculadoras, etc.
- No mezcles grid y pack en el mismo contenedor.
"""

import tkinter
from tkinter import ttk

ventana= tkinter.Tk()
ventana.geometry("600x400")
ventana.title("Gestor de Grid")

row = 5
column = 5

def eventoBoton():
    print("Botón presionado")

def eventoBoton2():
    print("Botón 2 presionado")

# Posicionar botones en el grid
# Usamos grid() en vez de pack(). Cada botón se coloca en una celda específica.
boton1 = ttk.Button(ventana, text="Botón 1 corto", command=eventoBoton)
boton1.grid(row=0, column=0)  # Fila 0, columna 0

boton2 = ttk.Button(ventana, text="Botón 2 largoooo", command=eventoBoton2)
boton2.grid(row=1, column=1)  # Fila 1, columna 1


# Propiedad sticky en grid():
# --------------------------
# - El argumento sticky controla cómo se alinea y expande un widget dentro de su celda en el grid.
# - Por defecto, el widget se centra en la celda.
# - Puedes usar las letras:
#     - 'n' (north/arriba)
#     - 's' (south/abajo)
#     - 'e' (east/derecha)
#     - 'w' (west/izquierda)
# - Puedes combinarlas para expandir el widget en varias direcciones:
#     - 'ns' (vertical), 'ew' (horizontal), 'nsew' (ocupa toda la celda)
# - Ejemplo: sticky='ew' hace que el widget se expanda horizontalmente para llenar la celda.
# - Es útil para que los widgets se ajusten al tamaño de la celda, especialmente al redimensionar la ventana.

# Ejemplo: botón que ocupa varias columnas y se expande
# boton3 = ttk.Button(ventana, text="Grande")
# boton3.grid(row=2, column=0, columnspan=2, sticky='ew', padx=10, pady=10)
# Por default los botones se acomodaran al centro
def modificarSticky():
    boton3.grid(sticky="w")

boton3= ttk.Button(ventana, text="mini", command=modificarSticky)
boton3.grid(row=2, column=2, sticky="nsew")


# Configurar grid manager
# --------------------------------------
# - Puedes usar grid_rowconfigure() y grid_columnconfigure() para controlar cómo se expanden filas y columnas al redimensionar la ventana.
# La sintaxis basica de estas funciones es (indice_fila, option=value)
#Sus argumentos pasables son:
# index: índice de la fila o columna a configurar (entero, empieza en 0).
# weight: (int) cuánto espacio extra recibe la fila/columna al expandir la ventana. Si es 0 (por defecto), no se expande.
# minsize: (int) tamaño mínimo de la fila/columna en píxeles.
# pad: (int) espacio extra alrededor de la fila/columna en píxeles.
# uniform: (str) nombre de grupo para que varias filas/columnas se expandan igual (todas con el mismo valor de uniform compartirán el espacio extra).
ventana.rowconfigure(0, weight=1)  # Fila 0 se expande al redimensionar
ventana.columnconfigure(0, weight=1)  # Columna 0 se expande al redimensionar
ventana.rowconfigure(1, weight=2)  # Fila 1 se expande al redimensionar
ventana.columnconfigure(1, weight=2)  # Columna 1 se expande al redimensionar
ventana.rowconfigure(2, weight=3)  # Fila 2 se expande al redimensionar
ventana.columnconfigure(2, weight=3)  # Columna 2 se expande al redimensionar
ventana.columnconfigure(3, weight=4)  # Columna 3 se expande al redimensionar
ventana.rowconfigure(3, weight=4)  # Fila 3 se expande al redimensionar
ventana.columnconfigure(4, weight=5)  # Columna 4 se expande al redimensionar
ventana.rowconfigure(4, weight=5)  # Fila 4 se expande al redimensionar
#Se forma una cuadricula de 4x4 pero en realidad se veria como algo de 10x10 donde se establece cual digamos entre comillas columna y cuadricula se ocupa

Button4= ttk.Button(ventana, text="Botón 4", command=eventoBoton)
Button4.grid(row=3, column=3, sticky="nsew") #Al hacer la asignacion, al ya estar configurados las columnas y filas, se expandira a como esta establecido

#Padding 
# ------------------
# - El padding controla el espacio extra alrededor de los widgets en la cuadrícula.
# - padx y pady: agregan espacio externo (horizontal y vertical) entre el widget y los bordes de la celda.
#     - padx: espacio a la izquierda y derecha (en píxeles) externa, es como el margin en web
#     - pady: espacio arriba y abajo (en píxeles) externa, es como el margin en web
# - ipadx e ipady: agregan espacio interno dentro del widget, expandiendo su área de clic.
#     - ipadx: espacio interno horizontal (en píxeles) del elemento
#     - ipady: espacio interno vertical (en píxeles) del elemento
# - Puedes usar valores enteros o tuplas (para especificar valores diferentes para cada lado).
# - El padding es útil para separar visualmente los widgets y mejorar la usabilidad.
# - Puedes combinar padding con sticky para lograr layouts más limpios y adaptables.

boton5= ttk.Button(ventana, text="Botón 5")
boton5.grid(row=4, column=4, sticky="nsew", padx=20, pady=20, ipadx=25, ipady=25)  # Padding externo e interno

#Colspan y Rowspan
# ---------------------------
# - columnspan: permite que un widget ocupe varias columnas en la cuadrícula.
#     - Por defecto es 1 (ocupa solo una columna).
#     - Ejemplo: columnspan=2 hace que el widget se extienda a lo largo de dos columnas.
# - rowspan: permite que un widget ocupe varias filas en la cuadrícula.
#     - Por defecto es 1 (ocupa solo una fila).
#     - Ejemplo: rowspan=3 hace que el widget se extienda a lo largo de tres filas.
# - Son útiles para crear layouts más complejos, como encabezados de tabla, celdas grandes, etc.
# - Puedes combinar columnspan y rowspan con sticky y padding para controlar el tamaño y la alineación del widget dentro de la celda expandida.

botonlargo= ttk.Button(ventana, text="Botón Largo")
botonlargo.grid(row=4, column=0, columnspan=3, rowspan=2, sticky='nsew')

ventana.mainloop()