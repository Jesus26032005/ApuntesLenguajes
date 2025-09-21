"""
APUNTE DETALLADO: Tkinter + POO + self + super()

Este archivo demuestra:
- Cómo heredar de tkinter.Tk para crear una ventana personalizada.
- Cómo funciona `super()` para inicializar la ventana base.
- Por qué usamos `self` para acceder a atributos (widgets y variables).
- Relación entre métodos, atributos y eventos de Tkinter.
"""

import tkinter       # Módulo base para interfaces gráficas en Python
from tkinter import ttk, messagebox  # ttk = widgets más modernos, messagebox = ventanas emergentes


class Login(tkinter.Tk):
    """
    Esta clase hereda de `tkinter.Tk`, lo que significa que **es** una ventana principal.
    Al heredar, la clase Login hereda todos los métodos y atributos de Tk.

    Ejemplo: ahora podemos usar `self.geometry()`, `self.title()`, etc.,
    sin tener que crear un objeto `root = Tk()` manualmente.
    """

    def __init__(self):
        """
        Constructor de la clase Login.
        Aquí inicializamos la ventana y configuramos sus propiedades básicas.
        """
        # Llamamos al constructor de la clase padre (`tkinter.Tk`) para crear
        # internamente el objeto ventana.
        super().__init__()

        # Configuración básica de la ventana
        self.geometry("600x400")     # Establece el tamaño inicial
        self.title("Login Básico")   # Título de la ventana
        self.resizable(False, False) # No permitir que se cambie el tamaño

        # Configuración del grid de la ventana (estructura de filas y columnas)
        self.columnconfigure(0, weight=1)  # Columna 0 más pequeña
        self.columnconfigure(1, weight=2)  # Columna 1 más grande
        self.rowconfigure(0, weight=1)     # Fila 0
        self.rowconfigure(1, weight=1)     # Fila 1
        self.rowconfigure(2, weight=1)     # Fila 2

        # Llamamos al método que crea los widgets
        self._crear_componentes()


    def _mostrarMensaje(self):
        """
        Método que se ejecuta al hacer clic en el botón.

        IMPORTANTE: usamos `self` para acceder a los widgets que guardamos como atributos
        en `_crear_componentes()`, ya que `self` hace referencia a la instancia actual
        de la clase y nos permite que otros métodos accedan a esos widgets.
        """
        usuario = self.entry_usuario.get()       # Obtiene el texto escrito en la caja de usuario
        contrasena = self.entry_contrasena.get() # Obtiene el texto escrito en la caja de contraseña

        # Mostramos los datos en una ventana emergente
        messagebox.showinfo(
            "Información del usuario",
            f"Usuario: {usuario}\nContraseña: {contrasena}"
        )


    def _crear_componentes(self):
        """
        Crea y coloca los widgets en la ventana.

        Aquí usamos `self.entry_usuario` y `self.entry_contrasena` en lugar
        de variables locales para que puedan ser accedidas desde otros métodos.
        """
        # Etiqueta para el campo usuario
        label_usuario = tkinter.Label(self, text="Usuario:")
        label_usuario.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        # Etiqueta para el campo contraseña
        label_contrasena = tkinter.Label(self, text="Contraseña:")
        label_contrasena.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        # Campo de entrada para usuario (guardado en self para acceder después)
        self.entry_usuario = tkinter.Entry(self)
        self.entry_usuario.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Campo de entrada para contraseña (guardado en self para acceder después)
        self.entry_contrasena = tkinter.Entry(self, show="*")
        self.entry_contrasena.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Botón de enviar (ejecuta _mostrarMensaje cuando se presiona)
        botonEnviar = ttk.Button(
            self, 
            text="Enviar", 
            command=self._mostrarMensaje  # Llamamos al método sin paréntesis para que se ejecute SOLO al hacer clic
        )
        botonEnviar.grid(row=2, column=0, columnspan=2, pady=10)


# Punto de entrada del programa
if __name__ == "__main__":
    # Creamos una instancia de Login, que automáticamente es una ventana Tkinter
    loginprueba = Login()

    # Mantenemos la ventana abierta y activa
    loginprueba.mainloop()
