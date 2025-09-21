"""
Módulo messagebox en Tkinter
---------------------------
- messagebox es un módulo de Tkinter que permite mostrar cuadros de diálogo emergentes (pop-ups) para mensajes, advertencias, errores, confirmaciones, etc.
- Es útil para informar al usuario, pedir confirmación o mostrar errores de forma sencilla y visual.

Importación:
from tkinter import messagebox

Funciones principales de messagebox:
- showinfo(title, message): muestra un mensaje informativo
- showwarning(title, message): muestra una advertencia
- showerror(title, message): muestra un mensaje de error
- askquestion(title, message): pregunta al usuario (devuelve 'yes' o 'no')
- askokcancel(title, message): pregunta si continuar (devuelve True/False)
- askyesno(title, message): pregunta sí/no (devuelve True/False)
- askretrycancel(title, message): pregunta reintentar/cancelar (devuelve True/False)

Argumentos principales:
- title: título de la ventana emergente (string)
- message: texto del mensaje a mostrar (string)

Notas y buenas prácticas:
- Los cuadros de diálogo son modales: bloquean la ventana principal hasta que el usuario responde.
- Puedes usarlos en cualquier momento para mostrar información o pedir confirmación.
- El resultado de las funciones ask* puede usarse para controlar el flujo del programa.
- messagebox funciona igual con Tk y con Toplevel.

"""

import tkinter
from tkinter import ttk, messagebox

ventana = tkinter.Tk()
ventana.geometry("600x400")
ventana.title("MessageBox")

label = ttk.Label(ventana, text="Haz clic en el botón para mostrar un mensaje")
label.pack(pady=20)

variableentrada= tkinter.StringVar()
entrada= ttk.Entry(ventana, textvariable=variableentrada, width=30)
entrada.pack(pady=10)

def enviar_mensaje():
    messagebox.showinfo("Información", variableentrada.get())
def mostrar_advertencia():
    messagebox.showwarning("Advertencia", variableentrada.get())

boton_info = ttk.Button(ventana, text="Mostrar Información", command=enviar_mensaje)
boton_info.pack(pady=5)

boton_advertencia = ttk.Button(ventana, text="Mostrar Advertencia", command=mostrar_advertencia)
boton_advertencia.pack(pady=5)

botonpregunta= ttk.Button(ventana, text="Preguntar", command=lambda: messagebox.askyesno("Pregunta", "¿Estás seguro?"))
botonpregunta.pack(pady=5)

ventana.mainloop()