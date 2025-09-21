from time import sleep, time
import tkinter as tk
from tkinter import ttk, scrolledtext
from tkinter import messagebox

# ----------------------------------------------------------------------
# ScrolledText en Tkinter
# -----------------------
# El widget ScrolledText proporciona un área de texto con barra de desplazamiento
# automática (scroll), ideal para mostrar o editar textos largos.
#
# scrolledtext.ScrolledText:
# --------------------------
# - Sintaxis: scrolledtext.ScrolledText(parent, **opciones)
# - Argumentos principales y sus valores:
#     - parent: widget contenedor (ej. ventana, frame, etc.)
#     - width: ancho en caracteres (int, por defecto 20)
#     - height: alto en líneas (int, por defecto 10)
#     - wrap: control de ajuste de línea:
#         - tk.WORD: ajusta por palabra (no corta palabras)
#         - tk.CHAR: ajusta por carácter (puede cortar palabras)
#         - tk.NONE: sin ajuste, el texto puede desbordar horizontalmente
#     - font: tipo y tamaño de fuente (ej. ("Arial", 12))
#     - state: estado del widget:
#         - 'normal': editable
#         - 'disabled': solo lectura
#     - bg: color de fondo (ej. "white")
#     - fg: color del texto (ej. "black")
#
# Métodos principales de ScrolledText:
#   - insert(index, text): inserta texto en la posición indicada.
#       - index: posición ('1.0' = inicio, tk.INSERT = cursor, 'end' = final)
#   - get(start, end): obtiene el texto entre dos posiciones.
#   - delete(start, end): elimina texto entre dos posiciones.
#   - see(index): desplaza el scroll para mostrar la posición indicada.
#   - configure(**options): cambia opciones del widget.
#   - pack(), grid(), place(): métodos para posicionar el widget.
#
# Ejemplo de uso de insert():
#   scroll.insert(tk.INSERT, "Texto a mostrar")
#   - tk.INSERT: inserta en la posición actual del cursor.
#   - '1.0': inserta al inicio (línea 1, carácter 0).
#   - 'end': inserta al final del texto.
#
# Esto permite mostrar, editar y desplazar textos largos fácilmente en la interfaz.
# ------------------------------------------------------------
#Scrolltext

ventana = tk.Tk()
ventana.title("Componentes adicionales")
ventana.geometry("600x400")

controlTabulador = ttk.Notebook(ventana)
tabulador1 = ttk.Frame(controlTabulador)
controlTabulador.add(tabulador1, text="Tabulador 1")

contenido= "hola we soy contenido de scrill text"
scroll= scrolledtext.ScrolledText(tabulador1, width= 15 , height= 10, wrap=tk.WORD)
scroll.insert(tk.INSERT, contenido)
scroll.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# ----------------------------------------------------------------------
# Combobox en Tkinter
# -------------------
# El widget Combobox permite seleccionar un valor de una lista desplegable.
# Es útil para ofrecer opciones predefinidas al usuario.
#
# ttk.Combobox:
# -------------
# - Sintaxis: ttk.Combobox(parent, **opciones)
# - Argumentos principales:
#     - parent: widget contenedor (ej. ventana, frame, etc.)
#     - values: lista de valores que se mostrarán en el desplegable (puede ser lista, tupla)
#     - state: estado del widget:
#         - 'normal': editable y seleccionable
#         - 'readonly': solo seleccionable, no editable
#         - 'disabled': deshabilitado
#     - width: ancho del combobox en caracteres
#     - font: tipo y tamaño de fuente (ej. ("Arial", 12))
#
# Métodos principales de Combobox:
#   - get():
#       Devuelve el valor actualmente seleccionado o escrito en el combobox.
#       No recibe argumentos.
#
#   - set(value):
#       Establece el valor mostrado en el combobox.
#       value: cualquier valor que quieras mostrar (debe estar en 'values' si el estado es 'readonly').
#
#   - current(index):
#       Selecciona el valor por índice (posición en la lista de 'values').
#       index: entero, posición del elemento a seleccionar (empieza en 0).
#
#   - configure(**options):
#       Cambia opciones del widget en tiempo de ejecución.
#       options: cualquier argumento válido del constructor (ej. state, values, width, etc.).
#
#   - bind(event, callback):
#       Asocia una función a un evento del combobox.
#       event: cadena que representa el evento (ej. '<<ComboboxSelected>>' para detectar selección).
#       callback: función a ejecutar cuando ocurre el evento.
#
#   - pack(), grid(), place():
#       Métodos para posicionar el widget en el contenedor.
#
# Ejemplo de uso:
#   combobox = ttk.Combobox(parent, values=[1,2,3], state='readonly')
#   combobox.current(0)  # Selecciona el primer valor por defecto
#   valor = combobox.get()  # Obtiene el valor seleccionado
#
# Valores de argumentos:
#   - values: lista o tupla de opciones a mostrar.
#   - state:
#       - 'normal': el usuario puede escribir y seleccionar.
#       - 'readonly': solo puede seleccionar de la lista.
#       - 'disabled': no interactivo.
#   - width: ancho visible en caracteres.
# ----------------------------------------------------------------------

tabulador2= ttk.Frame(controlTabulador)
controlTabulador.add(tabulador2, text="Tabulador 2")
datos= [v+1 for v in range(10)]
combobox= ttk.Combobox(tabulador2, values=datos)
combobox.current(0) #Valor por default
combobox.pack(padx=10, pady=10, fill=tk.X, expand=True)
#Boton seleccionar opcion
ButtonSeleccionar = ttk.Button(tabulador2, text="Seleccionar Opción", command=lambda: messagebox.showinfo("Información", f"Seleccionado: {combobox.get()}"))
ButtonSeleccionar.pack(padx=10, pady=10, fill=tk.X, expand=True)

#Manejo imagenes
# ----------------------------------------------------------------------
# PhotoImage en Tkinter
# ---------------------
# El objeto PhotoImage permite manejar imágenes en formato compatible con Tkinter
# (principalmente PNG y GIF) para mostrarlas en widgets como Label o Button.
#
# tk.PhotoImage:
# --------------
# - Sintaxis: imagen = tk.PhotoImage(**opciones)
# - Argumentos principales:
#     - file: ruta al archivo de imagen (ej. "imagen.png")
#     - data: datos binarios de la imagen en base64 (opcional)
#     - format: formato de la imagen (ej. "png", "gif") si se usa 'data'
#     - width: ancho de la imagen (opcional, en píxeles)
#     - height: alto de la imagen (opcional, en píxeles)
#
# Métodos principales de PhotoImage:
#   - copy(): crea una copia de la imagen.
#   - zoom(x, y): escala la imagen por un factor entero (amplía).
#       - x, y: factores de escala horizontal y vertical (int)
#   - subsample(x, y): reduce la imagen por un factor entero.
#       - x, y: factores de reducción horizontal y vertical (int)
#   - blank(): borra la imagen (la deja vacía).
#   - write(filename, format=None): guarda la imagen en un archivo.
#       - filename: nombre del archivo de salida
#       - format: formato de salida ("png", "gif", etc.)
#   - cget(option): obtiene el valor de una opción de la imagen.
#       - option puede ser:
#           - "file": ruta del archivo de imagen cargado (si se usó 'file')
#           - "data": datos de la imagen en base64 (si se usó 'data')
#           - "format": formato de la imagen (ej. "png", "gif")
#           - "width": ancho actual de la imagen en píxeles
#           - "height": alto actual de la imagen en píxeles


# Ejemplo de uso:
#   imagen = tk.PhotoImage(file="imagen.png")
#   label = ttk.Label(parent, image=imagen)
#   label.pack()
#
# Valores de argumentos:
#   - file: ruta a la imagen (debe ser PNG o GIF para PhotoImage estándar).
#   - data: datos de imagen en base64 (útil para imágenes embebidas).
#   - format: especifica el formato si se usa 'data'.
#   - width/height: redimensionan la imagen al crearla (pueden distorsionar).
# ----------------------------------------------------------------------

tabulador3= ttk.Frame(controlTabulador)
controlTabulador.add(tabulador3, text="Tabulador 3")
imagen= tk.PhotoImage(file="Tkinter/imagen.png")  # Asegúrate de que la ruta sea correcta
bottonimagen= ttk.Button(tabulador3, image=imagen, command= lambda: print(imagen.cget("file")))
bottonimagen.pack(padx=10, pady=10)

#Barra de progreso
# ----------------------------------------------------------------------
# Progressbar en Tkinter
# ----------------------
# El widget Progressbar muestra una barra de progreso visual, útil para indicar
# el avance de tareas o procesos en la interfaz gráfica.
#
# ttk.Progressbar:
# ----------------
# - Sintaxis: ttk.Progressbar(parent, **opciones)
# - Argumentos principales:
#     - parent: widget contenedor (ej. ventana, frame, etc.)
#     - orient: orientación de la barra ('horizontal' o 'vertical')
#         - tk.HORIZONTAL: barra horizontal (valor por defecto)
#         - tk.VERTICAL: barra vertical
#     - length: longitud de la barra en píxeles (int)
#     - mode: modo de funcionamiento:
#         - 'determinate': muestra progreso definido (valor conocido)
#         - 'indeterminate': muestra animación de progreso indefinido
#     - maximum: valor máximo de la barra (por defecto 100)
#     - value: valor actual de la barra (por defecto 0)
#
# Métodos principales de Progressbar:
#   - start(interval=50): inicia la animación (solo en modo 'indeterminate').
#       - interval: tiempo en milisegundos entre actualizaciones (por defecto 50 ms)
#   - stop(): detiene la animación.
#   - step(amount=1): incrementa el valor de la barra en la cantidad indicada.
#       - amount: valor a incrementar (por defecto 1)
#   - configure(**options): cambia opciones del widget en tiempo de ejecución.
#   - cget(option): obtiene el valor de una opción.
#   - update(): fuerza la actualización visual inmediata del widget (útil en bucles).
#   - pack(), grid(), place(): métodos para posicionar el widget.
#
# Ejemplo de uso:
#   barra = ttk.Progressbar(parent, orient=tk.HORIZONTAL, length=200, mode='determinate')
#   barra['maximum'] = 100
#   barra['value'] = 0
#   barra.pack()
#   barra.step(10)  # Avanza 10 unidades
#   barra.start(20) # Inicia animación (modo indeterminado)
#   barra.stop()    # Detiene animación
#   barra.update()  # Actualiza visualmente la barra inmediatamente
#
# Valores de argumentos:
#   - orient: tk.HORIZONTAL (horizontal) o tk.VERTICAL (vertical)
#   - length: longitud de la barra en píxeles
#   - mode: 'determinate' (progreso definido) o 'indeterminate' (progreso indefinido)
#   - maximum: valor máximo de la barra (int)
#   - value: valor actual de la barra (int)
# ----------------------------------------------------------------------

tabulador4= ttk.Frame(controlTabulador)
controlTabulador.add(tabulador4, text="Tabulador 4")
barraProgreso= ttk.Progressbar(tabulador4, orient=tk.HORIZONTAL, length=100, mode="determinate")
barraProgreso.pack(padx=10, pady=10, fill=tk.X, expand=True)

#Botones para controlar barra

def controlarBarra():
        barraProgreso['maximum'] = 100
        for valor in range(101):
            # Mandamos a esperar un poco antes de continuar con la ejecución de la barra
            sleep(0.05)
                # Incrementamos nuestra barra de progreso
            barraProgreso['value'] = valor
                # Actualizamos la barra de progreso
            barraProgreso.update()
        barraProgreso['value'] = 0

barraProgreso["maximum"] = 100  # Establece el valor máximo de la barra
bottonInicio= ttk.Button(tabulador4, text="Inicio", command= controlarBarra)
bottonInicio.pack(padx=10, pady=10)

#Boton ciclo
bottonCiclo= ttk.Button(tabulador4, text="Ciclo", command=lambda: barraProgreso.start(10))
bottonCiclo.pack(padx=10, pady=10)

#Boton finalizar
bottonFinalizar= ttk.Button(tabulador4, text="Finalizar", command=lambda: barraProgreso.stop())
bottonFinalizar.pack(padx=10, pady=10)

#Boton finalizar despues
bottonFinalizarDespues= ttk.Button(tabulador4, text="Finalizar Después", command=lambda: ventana.after(5000, barraProgreso.stop))
bottonFinalizarDespues.pack(padx=10, pady=10)


controlTabulador.pack(expand=1, fill="both")
ventana.mainloop()