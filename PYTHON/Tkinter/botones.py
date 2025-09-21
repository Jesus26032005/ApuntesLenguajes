"""
Ejemplo de creación de botones en Tkinter
----------------------------------------
- Puedes usar tkinter.Button (estilo clásico) o ttk.Button (estilo moderno).
- Argumentos principales:
    - master: ventana o frame donde se coloca el botón.
    - text: texto mostrado en el botón.
    - command: función a ejecutar al hacer clic.
    - state: 'normal' o 'disabled'.
    - width, padding, etc.
- ttk.Button hereda de tkinter.Button pero tiene mejor apariencia y más integración con temas.
- Para mostrar el botón, usa un gestor de geometría como pack(), grid() o place().

Argumentos disponibles para tkinter.Button:
------------------------------------------
- master: ventana o frame contenedor (obligatorio como primer argumento)
- text: texto mostrado en el botón
- command: función a ejecutar al hacer clic
- state: 'normal', 'disabled', 'active'
- width, height: tamaño del botón (en caracteres)
- bg, fg: color de fondo y de texto
- font: tipo y tamaño de letra
- image: imagen a mostrar en el botón (PhotoImage o BitmapImage)
- compound: posición de la imagen respecto al texto ('top', 'bottom', 'left', 'right', 'center', 'none')
- cursor: tipo de cursor al pasar el mouse
- relief: estilo del borde ('flat', 'raised', 'sunken', 'groove', 'ridge')
- padx, pady: espacio interno horizontal y vertical
- anchor: alineación del texto ('n', 's', 'e', 'w', 'center', etc.)
- activebackground, activeforeground: colores cuando el botón está activo
- disabledforeground: color del texto cuando está deshabilitado
- highlightbackground, highlightcolor, highlightthickness: opciones de resaltado
- justify: alineación del texto si es multilínea ('left', 'center', 'right')
- wraplength: longitud máxima antes de hacer salto de línea

Argumentos disponibles para ttk.Button:
----------------------------------------
- master: ventana o frame contenedor (obligatorio como primer argumento)
- text: texto mostrado en el botón
- command: función a ejecutar al hacer clic
- state: 'normal', 'disabled', 'active'
- width: ancho del botón (en caracteres)
- takefocus: si el botón puede recibir foco (True/False)
- style: nombre del estilo ttk a aplicar
- image: imagen a mostrar en el botón (PhotoImage o BitmapImage)
- compound: posición de la imagen respecto al texto ('top', 'bottom', 'left', 'right', 'center', 'none')
- cursor: tipo de cursor al pasar el mouse
- textvariable: variable tk.StringVar para cambiar el texto dinámicamente
- underline: índice del carácter subrayado en el texto
- default: si el botón es el predeterminado ('normal', 'active', 'disabled')
- padding: espacio interno (puede ser int o tupla)
- bootstyle: (en ttkbootstrap) para estilos avanzados

Notas:
- tkinter.Button permite personalizar colores y fuentes directamente con bg, fg, font, etc.
- ttk.Button no admite bg, fg, font directamente; se usan estilos con ttk.Style.
- Algunos argumentos como image, compound, cursor, textvariable, etc. son comunes a ambos.
"""

import tkinter
from tkinter import ttk

ventana= tkinter.Tk()
ventana.geometry("600x400")
ventana.title("Botones")

# Crear un botón básico con ttk
boton1 = ttk.Button(ventana, text="Botón 1")
boton1.pack() 

# Crear un botón deshabilitado
boton3 = ttk.Button(ventana, text="Deshabilitado", state="disabled")
boton3.pack()

# Crear varios botones en un bucle
for i in range(3):
    ttk.Button(ventana, text=f"Botón {i+2}").pack()

# Crear un botón con función asociada, su sintaxis seria añadir el argumento "command" y la funcion a 
def saludar():
    print("¡Hola!")

def sumar(x,y):
    print(f"La suma de {x} y {y} es {x+y}")


def anadirBoton():
    ttk.Button(ventana, text="Nuevo Botón").pack()

boton2 = ttk.Button(ventana, text="Saludar", command=saludar)
boton2.pack()

boton4= ttk.Button(ventana, text="Sumar",  command= lambda: sumar(5, 10)) #Para añadir funciones con argumentos se tiene que hacer uso de funciones lambda para que seejecute solo al hacer clcik pues si la colocamos directo se hara en automaitico
boton4.pack()

boton5 = ttk.Button(ventana, text="Añadir Botón", command=anadirBoton)
boton5.pack()

#Cambiar texto de un boton
boton2.config(text="Se sumo")

# Creacion botones usando tkinter, esto hace q se cree un botton mas claisco 
boton6 = tkinter.Button(ventana, text="Botón Tkinter")
boton6.pack()

# Configurar propiedades del botón sencillas, se puede realizar usando tkinter
boton7 = tkinter.Button(ventana, text="Botón Tkinter 2", bg="lightblue", fg="black", activebackground="blue", activeforeground="white")
boton7.pack()

ventana.mainloop()