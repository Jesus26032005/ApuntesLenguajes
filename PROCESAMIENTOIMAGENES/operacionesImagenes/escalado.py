"""
ESCALADO O REDIMENSIONADO
Producto de la matriz de transformacion con modificaciones en el espacio (0,0), (1,1) y el vecto posicoon del pixel
Dicha matriz es: 
[[sx, 0, 0], 
[0, sy, 0], 
[0, 0, 1]]
"""


import cv2 as openCv  # OpenCV para procesamiento de imágenes
import numpy  # numpy para operaciones con matrices

# Leer imagen desde disco
# openCv.imread(ruta, bandera)
# - ruta: string, ruta del archivo de imagen
# - bandera: especifica cómo leer la imagen (opcional):
#     openCv.IMREAD_COLOR (1): lee en color (por defecto)
#     openCv.IMREAD_GRAYSCALE (0): lee en escala de grises
#     openCv.IMREAD_UNCHANGED (-1): lee la imagen tal cual (incluye canal alfa si existe)
# Devuelve: array numpy con la imagen cargada, o None si la ruta es incorrecta
imagen = openCv.imread("procesamientoImagenes/operacionesImagenes/imagen.png")

# Obtener dimensiones de la imagen
# imagen.shape
# Devuelve: tupla (alto, ancho, canales)
alto, ancho, canales = imagen.shape

# Factor de escala
# Puede ser float o int. Ejemplo: 2 duplica tamaño, 0.5 reduce a la mitad
escala = 2  # Duplicar tamaño

# Matriz de escalado 3x3 para transformación manual
# numpy.array(objeto_iterable, dtype=None)
# - objeto_iterable: lista de listas o tupla
# - dtype: tipo de dato (opcional)
matrizEscalado = numpy.array([[escala, 0, 0],
                             [0, escala, 0],
                             [0, 0, 1]])

# Crear imagen negra para recibir el resultado del escalado manual
# numpy.zeros(shape, dtype=None)
# - shape: tupla con dimensiones (alto, ancho, canales)
# - dtype: tipo de dato (opcional)
imagenDuplicada = numpy.zeros((alto * escala, ancho * escala, canales), numpy.uint8)

# FORMA 1: Escalado manual usando matriz de transformación
# Se calcula la nueva posición de cada pixel usando la matriz de escalado
for altura in range(alto):
    for largo in range(ancho):
        pixel = imagen[altura, largo]  # Valor del pixel original
        vectorPosicion = numpy.array([largo, altura, 1])  # Vector posición (x, y, 1)
        resultadoMulti = matrizEscalado @ vectorPosicion  # Producto de la matriz y el vector
        x, y, _ = resultadoMulti  # Nueva coordenada x, y
        imagenDuplicada[y, x] = pixel  # Asignación del pixel escalado


# FORMA 2: Escalado usando función resize de OpenCV
# openCv.resize(imagen, dsize, fx=0, fy=0, interpolation=None)
# - imagen: array numpy, imagen a redimensionar
# - dsize: tupla (ancho, alto) de la nueva imagen
# - fx, fy: escala en x e y (opcional)
# - interpolation: método de interpolación (opcional)
#   Valores posibles:
#   openCv.INTER_NEAREST: Vecino más cercano (rápido, pero puede verse pixelado)
#   openCv.INTER_LINEAR: Interpolación bilineal (por defecto, buena calidad para ampliaciones)
#   openCv.INTER_CUBIC: Interpolación bicúbica (mejor para ampliaciones grandes, más lento)
#   openCv.INTER_AREA: Interpolación por área (mejor para reducciones, preserva detalles)
#   openCv.INTER_LANCZOS4: Interpolación Lanczos (alta calidad, más lento)
#   El resultado cambia en suavidad, nitidez y velocidad según el método elegido.
# Devuelve: imagen redimensionada
imagenDuplicada = openCv.resize(imagen, (ancho * escala, alto * escala), interpolation=openCv.INTER_LINEAR)


# FORMA 3: Escalado usando matriz afín y warpAffine
# openCv.warpAffine(src, M, dsize, flags=None, borderMode=None, borderValue=None)
# - src: imagen de entrada (array numpy)
# - M: matriz de transformación 2x3 (afín, aquí de escalado)
# - dsize: tupla (ancho, alto) de la imagen de salida
# - flags: método de interpolación (opcional)
#   Valores posibles:
#   openCv.INTER_NEAREST: Vecino más cercano (rápido, pero puede verse pixelado)
#   openCv.INTER_LINEAR: Interpolación bilineal (por defecto, buena calidad para ampliaciones)
#   openCv.INTER_CUBIC: Interpolación bicúbica (mejor para ampliaciones grandes, más lento)
#   openCv.INTER_AREA: Interpolación por área (mejor para reducciones, preserva detalles)
#   openCv.INTER_LANCZOS4: Interpolación Lanczos (alta calidad, más lento)
#   El resultado cambia en suavidad, nitidez y velocidad según el método elegido.
# - borderMode: cómo tratar los bordes (opcional, ej: openCv.BORDER_CONSTANT, openCv.BORDER_REFLECT)
# - borderValue: valor para los bordes si BORDER_CONSTANT
# Devuelve: imagen transformada
matriz_escalado = numpy.float32([[escala, 0, 0],
                                 [0, escala, 0]])  # Matriz 2x3 para escalado
nuevo_ancho = int(ancho * escala)
nuevo_alto = int(alto * escala)
imagenDuplicada = openCv.warpAffine(
    imagen,
    matriz_escalado,
    (nuevo_ancho, nuevo_alto),
    flags=openCv.INTER_LINEAR,  # Cambia aquí el método de interpolación según lo que necesites
    borderMode=openCv.BORDER_CONSTANT,
    borderValue=0
)
# - matriz_escalado: [[sx, 0, 0], [0, sy, 0]] para solo escalado
# - (nuevo_ancho, nuevo_alto): tamaño de la imagen de salida
# - flags: interpolación (por defecto INTER_LINEAR)
# - borderMode: por defecto BORDER_CONSTANT
# - borderValue: valor de relleno en los bordes (0 = negro)

# Mostrar imagen escalada en ventana
# openCv.imshow(nombre_ventana, imagen)
# - nombre_ventana: string, nombre de la ventana
# - imagen: array numpy, imagen a mostrar
openCv.imshow("ventanaDuplicada", imagenDuplicada)

# Esperar una tecla para cerrar la ventana
# openCv.waitKey(delay)
# - delay: int, tiempo en milisegundos que espera por una tecla (0 = espera indefinida)
# Devuelve: el código ASCII de la tecla presionada, o -1 si no se presiona ninguna
openCv.waitKey()

# Cerrar todas las ventanas abiertas por OpenCV
# openCv.destroyAllWindows()
# No recibe parámetros, cierra todas las ventanas creadas por imshow
openCv.destroyAllWindows()
        

