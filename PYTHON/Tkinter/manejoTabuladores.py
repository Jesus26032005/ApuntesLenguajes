# ----------------------------------------------------------------------
# Tabuladores (Notebook) en Tkinter
# ---------------------------------
# Los tabuladores permiten organizar la interfaz gráfica en diferentes
# pestañas, facilitando la navegación entre secciones de la aplicación.
#
# En Tkinter, los tabuladores se implementan usando el widget ttk.Notebook.
# Cada pestaña es un Frame independiente donde puedes colocar widgets.
#
# ttk.Notebook:
# -------------
# - Es el widget principal para crear tabuladores.
# - Sintaxis: notebook = ttk.Notebook(parent, **opciones)
# - Argumentos principales:
#     - parent: widget contenedor (ej. ventana principal o un frame)
#     - width, height: tamaño inicial del área de pestañas (opcional)
#     - style: estilo visual (opcional)
#
# Métodos principales de Notebook:
#   - add(child, **options): agrega una pestaña (child debe ser un Frame)
#       - options: text (nombre de la pestaña), image, compound, state, sticky, etc.
#   - insert(pos, child, **options): inserta una pestaña en una posición específica
#   - forget(child): elimina una pestaña
#   - select([tab_id]): selecciona o devuelve la pestaña activa
#   - tabs(): devuelve una lista de los IDs de las pestañas
#   - tab(tab_id, option=None, **kw): obtiene o configura opciones de una pestaña
#   - index(tab_id): devuelve el índice de una pestaña
#
# ttk.Frame:
# ----------
# - Es el contenedor que se usa como contenido de cada pestaña.
# - Sintaxis: frame = ttk.Frame(parent, **opciones)
# - Argumentos principales:
#     - parent: widget contenedor (ej. Notebook)
#     - width, height: tamaño del frame (opcional)
#     - relief: tipo de borde (opcional)
#     - padding: espacio interno (opcional)
#
# Métodos principales de Frame:
#   - pack(), grid(), place(): métodos para posicionar el frame en el contenedor
#   - config(**options): cambiar opciones del frame
#
# Método pack():
# --------------
# - Es un gestor de geometría que organiza widgets en bloques antes o después de otros widgets.
# - Sintaxis: widget.pack(**opciones)
# - Argumentos principales:
#     - side: lado donde se coloca el widget ('top', 'bottom', 'left', 'right')
#     - fill: expande el widget para llenar el espacio disponible ('x', 'y', 'both', 'none')
#     - expand: (bool) si el widget debe expandirse para ocupar espacio extra
#     - padx, pady: espacio externo horizontal y vertical (en píxeles)
# - pack() es útil para layouts simples y para apilar widgets vertical u horizontalmente.
#
#
# Esto permite mostrar diferentes contenidos en cada pestaña de la interfaz.
# ----------------------------------------------------------------------

import tkinter as tk
from tkinter import ttk, messagebox
#Tabuladores

ventana = tk.Tk()
ventana.title("Manejo de Tabuladores en Tkinter")
ventana.geometry("600x400")
ventana.resizable(False, False)

def crearTabulador1(control_tabulador):
    tabulador1 = ttk.Frame(control_tabulador)
    control_tabulador.add(tabulador1, text="Tabulador 1")
    return tabulador1

def crearTabulador2(control_tabulador):
    tabulador2 = ttk.Frame(control_tabulador)
    control_tabulador.add(tabulador2, text="Tabulador 2")
    return tabulador2

def crear_tabuladores():
    control_tabulador = ttk.Notebook(ventana) #Permite crear un tabulador

    #Agregamos un marco(frame) para agregar dentro del tab y organizar los elementos
    tabulador1= crearTabulador1(control_tabulador)

    #Agregamos el tabulador al control de tabuladores
    control_tabulador.add(tabulador1, text="Tabulador 1")
    control_tabulador.pack(expand=1, fill="both")

    # Creamos un segundo tabulador
    tabulador2 = crearTabulador2(control_tabulador)

    # Agregamos contenido a los tabuladores
    label1 = ttk.Label(tabulador1, text="Contenido del Tabulador 1")
    label1.pack(padx=10, pady=10)

    label2 = ttk.Label(tabulador2, text="Contenido del Tabulador 2")
    label2.pack(padx=10, pady=10)

crear_tabuladores()

ventana.mainloop()