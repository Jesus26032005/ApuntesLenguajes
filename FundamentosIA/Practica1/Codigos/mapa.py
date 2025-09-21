import re
from tkinter import messagebox
import numpy as np

class Coordenada:
    def __init__(self, valor, coordenadaX, coordenadaY, visitado=False):
        self.valor= valor
        self.coordenadaX= coordenadaX
        self.coordenadaY= coordenadaY
        self.visitado= visitado
        self.valorAdicional= None

    def __str__(self):
        return f"La coordenada [{self.coordenadaX},{self.coordenadaY}] tiene el valor de:{self.valor}"

class Mapa:
    def __init__(self, nombreArchivo= None):
        self.matriz = list()
        self.alto = 0
        self.ancho = 0
        self.leerArchivo(nombreArchivo, modo="base")

    def buscartipoCoincidencia(self, linea):
        # Expresiones regulares para identificar los diferentes formatos de linea
        # Formato base: al menos 4 valores separados por comas
        patronBase = r"([a-zA-Z0-9]+(?:,[a-zA-Z0-9]+){3,})"
        # Formato basico: al menos 4 valores separados por comas y una coma al final
        patronBasico = r"([a-zA-Z0-9]+(?:,[a-zA-Z0-9]+){3,}),"
        # Formato CSV: al menos 4 valores separados por comas y dos comas al final
        patronCSV = r"([a-zA-Z0-9]+(?:,[a-zA-Z0-9]+){3,}),,?"

        if re.fullmatch(patronBase, linea):
            return "base"
        elif re.fullmatch(patronBasico, linea):
            return "basico"
        elif re.fullmatch(patronCSV, linea):
            return "csv"
        else:
            return "ninguno"

    def procesarLinea(self, linea):
        linea = linea.strip()
        tipo = self.buscartipoCoincidencia(linea)
        match tipo:
            case "base":
                pass
            case "basico":
                linea= linea[:-1]
            case "csv":
                linea= linea[:-2]
            case "ninguno":
                raise ValueError("El archivo contiene lineas con formato incorrecto para un mapa. Cada linea debe contener al menos tres valores alfanumericos separados por comas.")
            case _:
                raise ValueError("Error inesperado al procesar la linea del archivo.")
        linea = linea.split(',')
        return linea

    def leerArchivo(self, nombreArchivo, modo="base"):
        matrizAuxiliar = list()
        try:
            with open(nombreArchivo, 'r', encoding="utf-8-sig") as archivo:
                for iteracion, linea in enumerate(archivo):
                    # Procesamiento de cada linea del archivo
                    lineaProcesada= self.procesarLinea(linea)
                    if modo == "base":
                        if iteracion > 0 and len(lineaProcesada)!= len(matrizAuxiliar[iteracion-1]):
                            raise ValueError("El archivo contiene lineas con diferente cantidad de valores, por favor verifique el formato del archivo, no se cargo el mapa.")
                    if modo == "adicional":
                        if (len(lineaProcesada)!= self.ancho or iteracion >= self.alto):
                            raise ValueError("El archivo contiene lineas con diferente cantidad de valores o mas lineas de las que tiene el mapa, por favor verifique el formato del archivo, solo se le mostrara el mapa sin valores adicionales.")
                    matrizAuxiliar.append(lineaProcesada)

                if modo=="base":
                    self.alto= len(matrizAuxiliar)
                    self.ancho= len(matrizAuxiliar[0])
                    self.matriz = [[Coordenada(int(matrizAuxiliar[y][x]), x, y) for x in range(self.ancho)] for y in range(self.alto)]
                elif modo=="adicional":
                    for y in range(len(matrizAuxiliar)):
                        for x in range(len(matrizAuxiliar[y])):
                            self.matriz[y][x].valorAdicional = matrizAuxiliar[y][x]
        except ValueError:
            messagebox.showerror("Error", "El archivo base debe cargarse con valores numericos enteros")
        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo no fue encontrado, por favor verifique la ruta del archivo")
        except Exception:
            messagebox.showerror("Error", "Algo salio mal al cargar el archivo")

    def crearMatrizTerreno(self):
        return np.array([[int(coordenada.valor) for coordenada in fila] for fila in self.matriz])

    def crearMatrizVisitados(self):
        return np.array([[coordenada.visitado for coordenada in fila] for fila in self.matriz])
    
    def crearMatrizValorAdicional(self):
        return np.array([[coordenada.valorAdicional for coordenada in fila] for fila in self.matriz])

    def pedirCoordenada(self, x, y):
        if (x<0) or (y<0) or (x>=self.ancho) or (y>=self.alto):
            raise IndexError()
        return self.matriz[y][x]
if __name__ == "__main__":
    documento = Mapa()
