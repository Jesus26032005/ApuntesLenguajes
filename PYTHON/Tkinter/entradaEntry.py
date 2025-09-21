"""
Widget Entry en Tkinter
----------------------
- Entry es el widget de Tkinter para crear campos de texto de una sola línea (input).
- Permite al usuario escribir y editar texto, útil para formularios, búsquedas, login, etc.
- Puedes obtener y modificar el contenido del Entry mediante métodos o variables asociadas.

Sintaxis básica:
entry = tk.Entry(master, opciones)

Argumentos principales de Entry:
- master: ventana o frame contenedor (obligatorio)
- textvariable: variable tk.StringVar para enlazar el contenido
- width: ancho del campo en caracteres
- show: carácter para ocultar el texto (ej: show='*' para contraseñas)
- state: 'normal', 'disabled', 'readonly'
- font: tipo y tamaño de letra
- justify: alineación del texto ('left', 'center', 'right')
- bg, fg: color de fondo y texto
- relief: estilo del borde ('flat', 'sunken', 'raised', etc.)
- exportselection: si el texto seleccionado se copia al portapapeles

Métodos útiles:
- get(): obtiene el texto actual del Entry
- insert(pos, texto): inserta texto en la posición indicada, pos es el índice donde se insertará el texto
- delete(inicio, fin): elimina texto entre posiciones
- .focus(): da foco al Entry

Notas y buenas prácticas:
- Usa textvariable para enlazar el Entry a una variable y facilitar la gestión de datos.
- Para borrar el contenido: entrada.delete(0, tk.END)
- Puedes validar la entrada usando eventos o validación de Tkinter.
- Para campos de texto multilínea, usa tk.Text en vez de Entry.
- ttk.Entry (de ttk) tiene apariencia moderna y acepta argumentos similares, pero la personalización de colores se hace con estilos.
"""

import tkinter
from tkinter import ttk

ventana= tkinter.Tk()
ventana.geometry("600x400")
ventana.title("Entrada Entry")

ventana.columnconfigure(0, weight=2)
ventana.rowconfigure(0, weight=2)

entrada= ttk.Entry(ventana, width=10 , justify="center") #width es la cantidad de caracteres
entrada.grid(row=0, column=0, padx=10, pady=10, sticky="ew") 

#Insertar un texto por defecto o en alguna posicion por defecto
entrada.insert(0, "Texto por defecto") 
#insertar texto en la posicion final
entrada.insert(tkinter.END, " Texto final")  # Inserta al final del texto actual
# Propiedad show
entrada.config(show="*")  # Oculta el texto ingresado mediante el caracter indicado
entrada.config(show="")  # Muestra el texto ingresado
# Propiedad state
entrada.config(state="readonly")  # Establece el Entry como solo lectura
entrada.config(state="disabled")  # Desactiva el Entry
entrada.config(state="normal")  # Activa el Entry nuevamente

# Captura de información desde Entry
# ----------------------------------
# Para obtener el texto que el usuario ha escrito en un Entry, se usa el método get().
# Puedes capturar la información al presionar un botón, al presionar Enter, o en cualquier evento.
# Ejemplo básico:
# def mostrar():
#     valor = entrada.get()
#     print("Texto ingresado:", valor)
# boton = ttk.Button(ventana, text="Mostrar", command=mostrar)
# boton.grid(row=1, column=0, padx=10, pady=10)
#
# Puedes usar eventos para capturar información automáticamente:
# entrada.bind('<Return>', lambda e: print("Enter presionado. Texto:", entrada.get()))
#
# Para limpiar el Entry después de capturar:
# entrada.delete(0, tkinter.END)
# Esto es útil para formularios, búsquedas, validaciones, etc.

def enviar():
    valor = entrada.get() # Obtener el texto ingresado en forma de cadena
    print("Texto ingresado:", valor)
    entrada.delete(0, tkinter.END) # Limpiar el campo de entrada
    boton.config(state="disabled", text=f'el valor enviado fue {valor}') # Deshabilitar el botón después de enviar

boton = ttk.Button(ventana, text="Enviar", command=enviar)
boton.grid(row=1, column=0, padx=10, pady=10)

# Selección de texto en Entry
# --------------------------
# Puedes seleccionar texto en un Entry de varias formas:
#
# - Seleccionar todo el texto:
#   entrada.select_range(0, tkinter.END)  # Selecciona desde el inicio hasta el final
#   entrada.icursor(tkinter.END)          # Coloca el cursor al final
#   entrada.focus()                       # Da foco al Entry para que la selección sea visible
#
# - Seleccionar una parte específica:
#   entrada.select_range(2, 5)            # Selecciona desde el índice 2 al 5
#
# - Limpiar la selección:
#   entrada.select_clear()                # Quita cualquier selección
#
# - Saber si hay texto seleccionado:
#   entrada.selection_present()           # Devuelve True si hay selección
#
# - Obtener el texto seleccionado:
#   seleccion = entrada.selection_get()   # Devuelve el texto seleccionado (si hay)
#
# Ejemplo práctico:
# entrada.select_range(0, tkinter.END)
# entrada.focus()
#
# Esto es útil para resaltar texto automáticamente, facilitar la edición o copiar/pegar.

# Funciones de selección en Entry: para qué sirven y argumentos
# -------------------------------------------------------------
# - select_range(start, end): Selecciona el texto desde el índice start hasta end (no inclusivo).
#   * start: índice inicial (int, 0 es el primer carácter)
#   * end: índice final (int, puede ser tkinter.END para seleccionar hasta el final)
#   * Sirve para resaltar texto automáticamente, por ejemplo al enfocar el campo.
#
# - select_clear(): Elimina cualquier selección de texto en el Entry.
#   * No recibe argumentos.
#   * Útil para limpiar la selección después de copiar/pegar o al perder el foco.
#
# - selection_present(): Devuelve True si hay texto seleccionado, False si no.
#   * No recibe argumentos.
#   * Sirve para saber si el usuario ha seleccionado algo antes de operar sobre la selección.
#
# - selection_get(): Devuelve el texto actualmente seleccionado en el Entry.
#   * No recibe argumentos.
#   * Lanza excepción si no hay selección.
#   * Útil para copiar el texto seleccionado o validarlo.
#
# - icursor(index): Coloca el cursor de inserción en la posición indicada.
#   * index: índice (int o tkinter.END)
#   * Sirve para mover el cursor al inicio, final o cualquier posición tras seleccionar texto.
#
# - focus(): Da foco al Entry para que la selección sea visible y el usuario pueda escribir.
#   * No recibe argumentos.
#   * Útil para mejorar la experiencia de usuario al abrir formularios.
#
# Ejemplo de uso combinado:
# entrada.select_range(0, tkinter.END)  # Selecciona todo
# entrada.icursor(tkinter.END)          # Cursor al final
# entrada.focus()                       # Foco al Entry

def enviarselect():
    valor = entrada.get() # Obtener el texto ingresado en forma de cadena
    print("Texto ingresado:", valor)
    entrada.select_range(0, 2)
    entrada.icursor(2)  # Coloca el cursor en la posición 2
    entrada.focus()  # Da foco al Entry para que la selección sea visible

boton10 = ttk.Button(ventana, text="Enviar", command=enviarselect)
boton10.grid(row=1, column=0, padx=10, pady=10)


"""
Uso de StringVar en Entry
------------------------
- StringVar es una clase de Tkinter que permite enlazar el contenido de un Entry (u otros widgets) a una variable Python.
- Cuando el usuario escribe en el Entry, el valor de la StringVar se actualiza automáticamente.
- Si cambias el valor de la StringVar en el código, el Entry también se actualiza.
- Es útil para obtener, modificar y rastrear el contenido de los campos de texto de forma reactiva.

Sintaxis básica:
texto = tkinter.StringVar()
entrada = ttk.Entry(ventana, textvariable=texto)

Métodos principales:
- texto.get(): obtiene el valor actual de la variable (lo que hay en el Entry)
- texto.set(valor): cambia el valor de la variable y actualiza el Entry

Notas y buenas prácticas:
- Puedes usar StringVar para enlazar varios widgets al mismo valor.
- Es útil para validaciones, formularios y cuando necesitas que el valor se actualice automáticamente en la interfaz.
- Existen otras variables similares: IntVar, DoubleVar, BooleanVar para otros tipos de datos.
- ttk.Entry y tk.Entry aceptan textvariable.

# Argumentos que acepta StringVar
# ------------------------------
# StringVar puede recibir los siguientes argumentos al crearse:
#
# - master: widget padre (opcional, normalmente la ventana principal o un frame)
#   Ejemplo: texto = tkinter.StringVar(master=ventana)
# - value: valor inicial de la variable (opcional)
#   Ejemplo: texto = tkinter.StringVar(value="Hola")
# - name: nombre interno de la variable (opcional, poco usado)
#   Ejemplo: texto = tkinter.StringVar(name="mi_var")
"""

textoUnido= tkinter.StringVar(value="Texto inicial")
entrada = ttk.Entry(ventana, textvariable=textoUnido)
entrada.grid(row=2, column=1, padx=10, pady=10)

def enviarselect2():
    valor = textoUnido.get()
    print("Texto ingresado:", valor)
    textoUnido.set("Texto modificado")

botonEnviar = ttk.Button(ventana, text="Enviar", command=enviarselect2)
botonEnviar.grid(row=2, column=0, padx=10, pady=10)

ventana.mainloop()


