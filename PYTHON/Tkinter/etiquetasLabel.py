"""
Widget Label en Tkinter
----------------------
- Label es el widget de Tkinter para mostrar texto o imágenes en la interfaz.
- Se usa para títulos, instrucciones, resultados, mensajes, etc.
- No es interactivo (no recibe clics ni edición por el usuario).

Sintaxis básica:
etiqueta = tk.Label(master, opciones)

Argumentos principales de Label:
- master: ventana o frame contenedor (obligatorio)
- text: texto a mostrar (string)
- image: imagen a mostrar (PhotoImage o BitmapImage)
- textvariable: variable tk.StringVar para mostrar texto dinámico
- font: tipo y tamaño de letra (ej: ("Arial", 14, "bold"))
- bg, fg: color de fondo y texto
- width, height: tamaño en caracteres
- anchor: alineación del texto ('n', 's', 'e', 'w', 'center', etc.)
- justify: alineación del texto si es multilínea ('left', 'center', 'right')
- relief: estilo del borde ('flat', 'sunken', 'raised', etc.)
- padx, pady: espacio interno horizontal y vertical
- wraplength: longitud máxima antes de hacer salto de línea

Métodos útiles:
- .config(): cambiar opciones después de crear la etiqueta
- .cget("opcion"): obtener el valor de una opción

Notas y buenas prácticas:
- Usa textvariable para actualizar el texto automáticamente.
- Puedes mostrar imágenes con image=PhotoImage(file="imagen.png").
- ttk.Label (de ttk) tiene apariencia moderna y acepta argumentos similares, pero la personalización de colores se hace con estilos.
- Para mostrar resultados o mensajes que cambian, usa StringVar y .set().

"""

# Labels
import tkinter


ventana= tkinter.Tk()
ventana.geometry("600x400")
ventana.title("Etiqueta Label")
etiqueta= tkinter.Label(ventana, text="Etiqueta de texto")
entrada= tkinter.Entry(ventana, width=20)
boton= tkinter.Button(ventana, text="Botón", command= lambda: etiqueta.config(text=entrada.get()))
etiqueta.pack()
entrada.pack()
boton.pack()
ventana.mainloop()
