import cv2 as openCv, numpy as np

"""
La transformacion afin es una de las transformaciones geomtricas mas importanntes dentro del procesamiento de imagenes, podemos definirla como una combinacion de las operaciones de traslacion, rotacion, escalado y cambios de perspectiva tanto vertical como horizontal
Una vez establecido un sistema de coordenada spodemos ubicar cualquier punto ern el universo cun un vectoe  de posicion de orden 3x1

TRASLACION
Desliza un punto en el espacio una distancia finita a lo largo de una direcion vectorial dada.
La matriz de traslacion se puede expresar como:
| 1 0 tx |
| 0 1 ty |
| 0 0 1  |
Donde (tx, ty) son las distancias de traslacion en las direcciones x e y respectivamente. 
Y quedaria definida la matriz de traslacion como el producto de la matriz de traslacion y el vector a trasladar.

La aplicacion de la matriz de traslacion a un punto en el espacio se realiza mediante la multiplicacion de la matriz de traslacion por el vector de posicion del punto. Esto da como resultado un nuevo vector de posicion que representa la ubicacion del punto tras la traslacion.
"""

# Leer imagen desde disco
# openCv.imread(ruta, bandera)
# - ruta: string, ruta del archivo de imagen
# - bandera: especifica cómo leer la imagen (opcional):
#     openCv.IMREAD_COLOR (1): lee en color (por defecto)
#     openCv.IMREAD_GRAYSCALE (0): lee en escala de grises
#     openCv.IMREAD_UNCHANGED (-1): lee la imagen tal cual (incluye canal alfa si existe)
# Devuelve: array numpy con la imagen cargada, o None si la ruta es incorrecta
imagen = openCv.imread("procesamientoImagenes/operacionesImagenes/imagen.png")

# Redimensionar imagen
# openCv.resize(imagen, dsize, fx=0, fy=0, interpolation=None)
# - imagen: array numpy, imagen a redimensionar
# - dsize: tupla (ancho, alto) de la nueva imagen
# - fx, fy: escala en x e y (opcional)
# - interpolation: método de interpolación (opcional)
# Devuelve: imagen redimensionada
imagenchicaTraslado = openCv.resize(imagen, (100,100)) #Se redimensiona imagen para facilidades

# Obtener dimensiones de la imagen
# imagen.shape
# Devuelve: tupla (alto, largo, canales)
alto, largo, canales = imagenchicaTraslado.shape

# Variables de traslacion
traslacionX = 10  # Desplazamiento en x
traslacionY = 25  # Desplazamiento en y

# Definición de la matriz de traslación
# np.array(objeto_iterable, dtype=None)
# - objeto_iterable: lista de listas o tupla
# - dtype: tipo de dato (opcional)
matrizTraslacion = np.array([[1, 0, traslacionX],
                            [0, 1, traslacionY],
                            [0, 0, 1]], dtype=np.uint8)

# Crear imagen negra para recibir la traslación
# np.zeros(shape, dtype=None)
# - shape: tupla con dimensiones
# - dtype: tipo de dato (opcional)
imagenOscura = np.zeros((alto+25, largo+10, 3), dtype=np.uint8)

# FORMA 1
# for altura in range(alto):
#     for ancho in range(largo):
#         vectorPosicion = np.array([ancho, altura, 1], np.uint8) #Vector posicion por pixeles
#         matrizResultante = matrizTraslacion @ vectorPosicion #Producto de las matrices
#         x = matrizResultante[0]
#         y = matrizResultante[1]
#         print(x, y)
#         imagenOscura[y, x] = imagenchicaTraslado[altura, ancho] #Asignacion de valores de cada pixel

# FORMA 2
# Traslación directa sumando desplazamientos
for altura in range(alto):
    for ancho in range(largo):
        x = ancho + traslacionX
        y = altura + traslacionY
        imagenOscura[y, x] = imagenchicaTraslado[altura, ancho] #Asignacion de valores de cada pixel

# FORMA 3
# Utilizando la función cv2.warpAffine para aplicar la traslación de manera eficiente
# openCv.warpAffine(src, M, dsize, flags=None, borderMode=None, borderValue=None)
# - src: imagen de entrada (array numpy)
# - M: matriz de transformación 2x3 (afín)
# - dsize: tupla (ancho, alto) de la imagen de salida
# - flags: método de interpolación (opcional, ej: cv2.INTER_LINEAR, cv2.INTER_NEAREST)
# - borderMode: cómo tratar los bordes (opcional, ej: cv2.BORDER_CONSTANT, cv2.BORDER_REFLECT)
# - borderValue: valor para los bordes si BORDER_CONSTANT
# Devuelve: imagen transformada
# Ejemplo de uso:
matriz_afin = np.float32([[1, 0, traslacionX], [0, 1, traslacionY]])  # Matriz 2x3 para traslación
imagen_trasladada = openCv.warpAffine(imagenchicaTraslado, matriz_afin, (largo+10, alto+25), flags=openCv.INTER_LINEAR, borderMode=openCv.BORDER_CONSTANT, borderValue=0)
# - matriz_afin: [[1, 0, tx], [0, 1, ty]] para solo traslación
# - (largo+10, alto+25): tamaño de la imagen de salida
# - flags: interpolación (por defecto INTER_LINEAR)
# - borderMode: por defecto BORDER_CONSTANT
# - borderValue: valor de relleno en los bordes (0 = negro)
# Mostrar el resultado
openCv.imshow("ventana_forma3", imagen_trasladada)
openCv.waitKey()
openCv.destroyAllWindows()

# Crear ventana para mostrar imagen
# openCv.namedWindow(nombre_ventana, bandera)
# - nombre_ventana: string, nombre de la ventana
# - bandera: tipo de ventana (opcional):
#     openCv.WINDOW_NORMAL: permite cambiar el tamaño de la ventana
#     openCv.WINDOW_AUTOSIZE: tamaño fijo según la imagen
openCv.namedWindow("ventana", openCv.WINDOW_NORMAL)

# Mostrar imagen en ventana
# openCv.imshow(nombre_ventana, imagen)
# - nombre_ventana: string, nombre de la ventana
# - imagen: array numpy, imagen a mostrar
openCv.imshow("ventana", imagenOscura)

# Esperar una tecla para cerrar la ventana
# openCv.waitKey(delay)
# - delay: int, tiempo en milisegundos que espera por una tecla (0 = espera indefinida)
# Devuelve: el código ASCII de la tecla presionada, o -1 si no se presiona ninguna
openCv.waitKey()

# Cerrar todas las ventanas abiertas por OpenCV
# openCv.destroyAllWindows()
# No recibe parámetros, cierra todas las ventanas creadas por imshow
openCv.destroyAllWindows()