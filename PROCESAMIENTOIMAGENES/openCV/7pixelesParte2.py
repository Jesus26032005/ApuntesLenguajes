
# Importar las bibliotecas necesarias
# cv2: procesamiento de imágenes y video
# numpy: manejo de arreglos y matrices multidimensionales
# random: generación de números aleatorios (no usado en este script)
import cv2 as openCv, numpy as np, random


# Leer una imagen desde disco
# openCv.imread(ruta, bandera)
# - ruta: string, ruta del archivo de imagen
# - bandera: especifica cómo leer la imagen (opcional):
#     openCv.IMREAD_COLOR (1): lee en color (por defecto)
#     openCv.IMREAD_GRAYSCALE (0): lee en escala de grises
#     openCv.IMREAD_UNCHANGED (-1): lee la imagen tal cual (incluye canal alfa si existe)
# Devuelve: un array numpy con la imagen cargada, o None si la ruta es incorrecta
imagen = openCv.imread("procesamientoimagenes/opencv/candados.jpg")

# Obtener las dimensiones de la imagen
# imagen.shape
# Devuelve: tupla (alto, largo, canales)
alto, largo, capas = imagen.shape


# Extraer regiones de la imagen usando slicing
# imagen[fila_inicio:fila_fin, columna_inicio:columna_fin]
# Devuelve: submatriz (subimagen) de la imagen original
# En este caso, se divide la imagen en dos partes verticales
candado1 = imagen[0:alto, 0:int(largo/2)]      # Primera mitad (izquierda)
candado2 = imagen[0:alto, int(largo/2):largo]  # Segunda mitad (derecha)


# Mostrar imágenes en ventanas
# openCv.imshow(nombre_ventana, imagen)
# - nombre_ventana: string, nombre de la ventana
# - imagen: array numpy, imagen a mostrar
# No devuelve nada. Muestra la imagen en una ventana emergente.
openCv.imshow("candado completo", imagen)
openCv.imshow("candado1", candado1)
openCv.imshow("candado2", candado2)


# Crear una imagen vacía (negra) con las mismas dimensiones que la original
# np.zeros(shape, dtype)
# - shape: tupla con dimensiones (alto, largo, canales)
# - dtype: tipo de dato de los elementos (np.uint8 para imágenes de 8 bits por canal)
# Devuelve: array numpy lleno de ceros
imagenInversa = np.zeros((alto, largo, capas), np.uint8)

# Intercambiar las mitades de la imagen
# Asignar submatrices a regiones de la imagen destino
# No devuelve nada, modifica el array en memoria
imagenInversa[0:alto, 0:int(largo/2)] = candado2
imagenInversa[0:alto, int(largo/2):largo] = candado1


# Mostrar la imagen con las mitades intercambiadas
openCv.imshow("candadoInverso", imagenInversa)

# Esperar una tecla para cerrar las ventanas
# openCv.waitKey(delay)
# - delay: int, tiempo en milisegundos que espera por una tecla (0 = espera indefinida)
# Devuelve: el código ASCII de la tecla presionada, o -1 si no se presiona ninguna
openCv.waitKey()

# Cerrar todas las ventanas abiertas por OpenCV
# openCv.destroyAllWindows()
# No recibe parámetros, cierra todas las ventanas creadas por imshow
# No devuelve nada.
openCv.destroyAllWindows()