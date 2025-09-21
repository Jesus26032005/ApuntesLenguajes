import tkinter as tk

# Función para actualizar el texto de la etiqueta
def actualizar_etiqueta():
    etiqueta.config(text="¡El texto ha sido actualizado!")

# Crear ventana
ventana = tk.Tk()
ventana.geometry("400x300")
ventana.title("Actualizar Componente")

# Crear etiqueta
etiqueta = tk.Label(ventana, text="Texto inicial")
etiqueta.pack(pady=10)

# Crear botón que actualiza la etiqueta
boton_actualizar = tk.Button(ventana, text="Actualizar", command=actualizar_etiqueta)
boton_actualizar.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
