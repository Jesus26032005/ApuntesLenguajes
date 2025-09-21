import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.colors import BoundaryNorm
import matplotlib.colors as mcolors
from matplotlib.colors import ListedColormap, BoundaryNorm
import mapa as mp


class interfaz(tk.Tk):
    colorTerreno = {
        0: "#5E5A59", #Montaña
        1: "#4682B4", #Agua
        2: "#228B22", #Bosque
        3: "#F8E268", #Arena
        4: "#F5D198" #Tierra
    }
    colorTerreno.setdefault(-1, "#FFFFFF") #Color para valores no definidos en el mapa

    def __init__(self):
        self.configurarBase()
        self.crearLabelsEntradasBotones()
        self.mainloop()

    def configurarBase(self):
        #Inicializacion de la ventana
        super().__init__()
        self.title("Practica 1 - Fundamentos de IA")
        self.geometry("1250x600")
        self.resizable(False, False)

        #Configuracion de la cuadrícula
        for i in range(10):
            self.columnconfigure(i, weight=1)
        for i in range(14):
            self.rowconfigure(i, weight=1)

    def crearLabelsEntradasBotones(self):
        # Creacion etiquetas bases de la interfaz
        self.labelEntradA=tk.Label(self,text="Interfaz de usuario - Mapa", justify="center", font=("Arial", 16, "bold"))
        self.labelEntradA.grid(row=0, column=0, ipadx=5, ipady=5, sticky="nsew", columnspan=2)
        self.labelOpciones= tk.Label(self,text="Funciones disponibles", justify="center", font=("Arial", 14, "bold"))
        self.labelOpciones.grid(row=2, column=0, ipadx=5, ipady=5, sticky="nsew", columnspan=2)

        #Creacion boton de cargar mapa
        self.boton=tk.Button(self, text="Cargar Mapa", command=self.cargarMapa)
        self.boton.grid(row=1, column=0, ipadx=80, ipady=2,sticky="ns")

        self.botonValAdicional=tk.Button(self, text="Cargar Valores Adicionales", command=lambda: self.cargarArchivoAdicional(modo="adicional"))
        self.botonValAdicional.grid(row=1, column=1, ipadx=40, ipady=2,sticky="ns")

        # Creacion de diferentes secciones de la interfaz
        self.CoordenadasGUI()
        self.ModificarGUI()

    def CoordenadasGUI(self):
        #Creacion de labels
        self.labeltituloF1=tk.Label(self, text="Obtener valor de una coordenada", font=("Arial", 12, "bold"))
        self.labeltituloF1.grid(row=3, column=0, ipadx=5, ipady=5, sticky="nsew", columnspan=2)
        self.labelCoordenadaXF1=tk.Label(self, text="Coordenada X:", font=("Arial", 10))
        self.labelCoordenadaYF1=tk.Label(self, text="Coordenada Y:", font=("Arial", 10))
        self.labelResultadoF1=tk.Label(self, text="Valor:", font=("Arial", 10))

        #Creacion entradas y botones
        self.entradaCoordenadaXF1=tk.Entry(self)
        self.entradaCoordenadaXF1.insert(0, "0")
        self.entradaCoordenadaYF1=tk.Entry(self)
        self.entradaCoordenadaYF1.insert(0, "0")

        self.botonObtenerF1=tk.Button(self, text="Obtener valor", command= self.obtenerValorCoordenada)
        
        #Posicionamiento labels, entradas y botones en la cuadrícula
        self.labelCoordenadaXF1.grid(row=4, column=0, ipadx=5, ipady=5, sticky="nsew")
        self.labelCoordenadaYF1.grid(row=5, column=0, ipadx=5, ipady=5, sticky="nsew")
        self.labelResultadoF1.grid(row=6, column=0, ipadx=5, ipady=5, columnspan=2, sticky="nsew")

        self.entradaCoordenadaXF1.grid(row=4, column=1, ipadx=5, ipady=10, sticky="w")
        self.entradaCoordenadaYF1.grid(row=5, column=1, ipadx=5, ipady=10, sticky="w")
        self.botonObtenerF1.grid(row=7, column=0, columnspan=2, ipadx=120, ipady=2, sticky="ns")

    def ModificarGUI(self):
        #Creacion de labels
        self.labeltituloF2=tk.Label(self, text="Modificar valor de una coordenada", font=("Arial", 12, "bold"))
        self.labeltituloF2.grid(row=8, column=0, ipadx=5, ipady=5, sticky="nsew", columnspan=2)
        self.labelCoordenadaXF2=tk.Label(self, text="Coordenada X:", font=("Arial", 10))
        self.labelCoordenadaYF2=tk.Label(self, text="Coordenada Y:", font=("Arial", 10))
        self.labelNuevoValorF2=tk.Label(self, text="Nuevo valor:", font=("Arial", 10))

        #Creacion entradas y botones
        self.entradaCoordenadaXF2=tk.Entry(self)
        self.entradaCoordenadaXF2.insert(0, "0")
        self.entradaCoordenadaYF2=tk.Entry(self)
        self.entradaCoordenadaYF2.insert(0, "0")
        self.entradaNuevoValorF2=tk.Entry(self)
        self.entradaNuevoValorF2.insert(0, "5")

        self.botonObtenerF2=tk.Button(self, text="Modificar valor", command= self.modificarValorCoordenada)

        #Posicionamiento labels, entradas y botones en la cuadrícula
        self.labelCoordenadaXF2.grid(row=9, column=0, ipadx=5, ipady=5, sticky="nsew")
        self.labelCoordenadaYF2.grid(row=10, column=0, ipadx=5, ipady=5, sticky="nsew")
        self.labelNuevoValorF2.grid(row=11, column=0, ipadx=5, ipady=5, sticky="nsew")
        self.entradaCoordenadaXF2.grid(row=9, column=1, ipadx=5, ipady=10, sticky="w")
        self.entradaCoordenadaYF2.grid(row=10, column=1, ipadx=5, ipady=10, sticky="w")
        self.entradaNuevoValorF2.grid(row=11, column=1, ipadx=5, ipady=10, sticky="w")
        self.botonObtenerF2.grid(row=12, column=0, columnspan=2, ipadx=120, ipady=4, pady=5, sticky="ns")

    def cargarArchivoAdicional(self, modo="adicional"):
        if hasattr(self, "mapa"):
            bandera= self.cargarArchivo(modo="adicional")
            if bandera == True:
                self.dibujarMapa()
        else:
            messagebox.showinfo("Error", "No se ha cargado ningún mapa base. Por favor, cargue un mapa base primero.")

    def cargarArchivo(self, modo="base"):
        # Carga de archivo mediante un cuadro de dialogo
        archivo= filedialog.askopenfilename(title="Seleccione el archivo", filetypes= [
            ("Archivos de texto y csv", "*.txt; *.csv"),
            ("Archivos de texto", "*.txt"),
            ("Archivos CSV", "*.csv")])
        if not archivo: return False
        else: 
            # Creacion o modificacion del mapa segun el modo que se este realizandp
            if modo=="base":
                self.mapa= mp.Mapa(archivo)
            elif modo=="adicional":
                self.mapa.leerArchivo(archivo, modo="adicional")
            return True

    def cargarMapa(self):
        # Bucle para cargar el mapa base y los valores adicionales
        for i in range(2):
            if i==0:
                respuesta = messagebox.askokcancel("Instrucciones", "Desea cargar un archivo para el mapa base?")
                if respuesta == False: break
                else:
                    #Si no se carga el mapa base, no se puede cargar el adicional por lo tanto se rompe el ciclo 
                    bandera= self.cargarArchivo(modo="base")
                    if bandera == False: break
            elif i==1:
                #Si no se cargo el mapa base, no se puede cargar el adicional
                if len(self.mapa.matriz) == 0: break
                else:
                    respuesta = messagebox.askquestion("Instrucciones", "Desea cargar un archivo para los valores adicionales?")
                    if respuesta == "no": break
                    else: self.cargarArchivo(modo="adicional")

        if hasattr(self,"mapa") and len(self.mapa.matriz) != 0:
            self.dibujarMapa()

    def dibujarMapa(self):
        if hasattr(self.mapa, 'matriz'):
            matrizTerreno = self.mapa.crearMatrizTerreno()
            print(matrizTerreno)
            matrizTexto= self.mapa.crearMatrizValorAdicional()
            # Creacion la figura y el eje para el gráfico
            fig, ax = plt.subplots(figsize=(5, 6))
            # Dibujo de la matriz del terreno usando pcolormesh
            # Obtencion de los colores
            # Creacion de colormap para los valores del terreno, asociando cada valor con un color especifico
            mapaColores = ListedColormap(list(self.colorTerreno.values()))
            
            # Establecimiento de los intervalos de los colores para que sean discretos
            # # boundaries define los intervalos de tus valores reales
            boundaries = [i - 0.5 for i in range(len(self.colorTerreno)+1)]
            # Creacion de un objeto BoundaryNorm para normalizar los colores, establece los limites de la asignacion de cada color
            # BoundaryNorm toma los boundaries y el numero de colores en el colormap para crear una normalizacion adecuada
            intervaloNormalizado = BoundaryNorm(boundaries, mapaColores.N)
            
            # Dibujar matriz con norm incluido
            ax.pcolormesh(
                matrizTerreno, 
                cmap=mapaColores,
                norm=intervaloNormalizado,
                edgecolors='black'
            )
            # pcolormesh recibe la matriz.
            # Usa el norm para saber qué índice le corresponde a cada valor de la matriz.
            # Usa el cmap (tu ListedColormap) para traducir ese índice en un color exacto

            for i in range(self.mapa.alto):
                for j in range(self.mapa.ancho):
                    if matrizTexto[i][j] != "":
                        ax.text(j+0.5, i+0.5, #Alineacion con las coordenadas en el sistema de datos de ax
                                matrizTexto[i][j], #Texto a mostrar
                                ha='center', #Configuraciones adicionales de estilo
                                va='center', 
                                color="black", 
                                fontsize=10,
                                fontweight='bold',
                                fontfamily='Arial')
            
            ax.set_title("Mapa de Terreno") #Configuracion titulo de la grafica
            ax.set_xticks(range(self.mapa.ancho)) # Configuracion las marcas de x a aparecer
            ax.set_yticks(range(self.mapa.alto)) # Configuracion las marcas de y a aparecer
            ax.invert_yaxis()  # Inverticion del eje y para que el origen esté en la esquina superior izquierda
            fig.subplots_adjust(right=0.75)  # Ajuste del espacio para la leyenda, dejando un margen a la derecha de 0.25
            
            leyendaColores = [
                mpatches.Patch(color=color, label=nombre) #Creacion parches para la leyenda con lista por comprension
                for nombre, color in zip(['0 Montaña', '1 Agua', '2 Bosque', '3 Arena', '4 Tierra'], self.colorTerreno.values()) #Genera un zip con los nombres y colores del terreno y con ello crea los parches
            ]
            ax.legend(handles=leyendaColores, bbox_to_anchor=(1.3, 1)) #Configuracion la leyenda en la grafica

            # Integracion de la figura de Matplotlib en la interfaz de Tkinter
            canvas = FigureCanvasTkAgg(fig, master=self)
            # Dibujo del canvas y lo coloca en la cuadrícula
            canvas.draw()
            canvas.get_tk_widget().grid(row=0, column=2, rowspan=14, columnspan=8, sticky="nsew")

    def obtenerValorCoordenada(self):
        if hasattr(self, 'mapa'):
            # Obtencion de las coordenadas ingresadas por el usuario
            coordenaaX= self.entradaCoordenadaXF1.get()
            coordenadaY= self.entradaCoordenadaYF1.get()
            # Obtencion de la etiqueta de resultado
            labelResultado= self.labelResultadoF1
            try:
                # Intento de conversion de las coordenadas a enteros y obtencion del valor de la coordenada en el mapa
                x= int(coordenaaX)
                y= int(coordenadaY)
                valorCoordenada= self.mapa.pedirCoordenada(x, y)
                # Actualizacion de la etiqueta de resultado
                labelResultado.config(text=valorCoordenada)
            except ValueError:
                messagebox.showinfo("Error", "Las coordenadas deben ser valores enteros.")
            except IndexError:
                messagebox.showinfo("Error", "Las coordenadas están fuera de los límites del mapa.")
            except Exception as e:
                messagebox.showinfo("Error", f"{e}")
        else:
            messagebox.showinfo("Error", "No se ha cargado ningún mapa. Por favor, cargue un mapa primero.")

    def modificarValorCoordenada(self):
        if hasattr(self, 'mapa'):
            coordenadaXmodificar = self.entradaCoordenadaXF2.get()
            coordenadaYmodificar = self.entradaCoordenadaYF2.get()
            nuevoValor= self.entradaNuevoValorF2.get()
            try:
                x= int(coordenadaXmodificar)
                y= int(coordenadaYmodificar)
                valorCoordenada= self.mapa.pedirCoordenada(x, y).valor
                if int(nuevoValor) < 0 or int(nuevoValor) > 4:
                    raise ValueError("El nuevo valor debe estar entre 0 y 4.")
                self.mapa.pedirCoordenada(x, y).valor= int(nuevoValor)
                messagebox.showinfo("Exito", f"El valor de la coordenada [{x},{y}] ha sido modificado de {valorCoordenada} a {nuevoValor}.")
                self.dibujarMapa()
            except ValueError as e:
                messagebox.showinfo("Error", f"{e}")
            except IndexError:
                messagebox.showinfo("Error", "Las coordenadas están fuera de los límites del mapa.")
            except Exception as e:
                messagebox.showinfo("Error", f"{e}")
        else:
            messagebox.showinfo("Error", "No se ha cargado ningún mapa. Por favor, cargue un mapa primero.")

if __name__ == "__main__":
    app = interfaz()