"""
ROTACION
Podemos interpretar una matriz de rotacion como un operador rotacion que opera sobre un vector y convierte ese vector en uno nuevo por medio de una rotacion
La matriz de rotacion en 2D es la siguiente:
| cos(θ) -sin(θ) 0|
| sin(θ)  cos(θ) 0|
| 0      0       1|
En 3D hay diferentes casos dependiendo del eje alrededor del cual se realice la rotacion. Las matrices de rotacion en 3D son las siguientes:
Rotacion alrededor del eje X:
| 1       0        0      |
| 0  cos(θ) -sin(θ) |
| 0  sin(θ)  cos(θ) |

Rotacion alrededor del eje Y:
| cos(θ)  0  sin(θ) |
| 0       1       0      |
| -sin(θ) 0  cos(θ) |

Rotacion alrededor del eje Z:
| cos(θ) -sin(θ) 0 |
| sin(θ)  cos(θ) 0 |
| 0       0      1 |
"""


import numpy as np  # numpy: librería para operaciones numéricas y matrices
import cv2 as openCv  # cv2: OpenCV para procesamiento de imágenes

"""
ROTACIÓN DE IMÁGENES
La rotación es una transformación geométrica que gira una imagen alrededor de un punto (centro) por un ángulo específico. En procesamiento de imágenes, se puede realizar de varias formas: manualmente con matrices de rotación, usando funciones de OpenCV o librerías externas.
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

# Redimensionar imagen para facilitar la visualización
# openCv.resize(imagen, dsize, fx=0, fy=0, interpolation=None)
# - imagen: array numpy, imagen a redimensionar
# - dsize: tupla (ancho, alto) de la nueva imagen
# - fx, fy: escala en x e y (opcional)
# - interpolation: método de interpolación (opcional)
# Devuelve: imagen redimensionada
imagenMini = openCv.resize(imagen, (100, 100))

# Obtener dimensiones de la imagen
# imagen.shape
# Devuelve: tupla (alto, ancho, canales)
alto, ancho, canales = imagenMini.shape

# Variables de rotación
angulo = 0  # Ángulo de rotación en grados. Positivo: antihorario, Negativo: horario
centro = (ancho // 2, alto // 2)  # Centro de rotación (x, y). Normalmente el centro de la imagen
escala = 1  # Escala de la imagen tras rotar. 1 = igual tamaño, <1 reduce, >1 aumenta

# Definición de la matriz de rotación usando OpenCV
# openCv.getRotationMatrix2D(center, angle, scale)
# - center: tupla (x, y), centro de rotación
# - angle: float, ángulo en grados
# - scale: float, factor de escala
# Devuelve: matriz de transformación 2x3 para rotación
matrizRotacion = openCv.getRotationMatrix2D(centro, angulo, escala)

# Crear imagen negra para recibir la rotación
# np.zeros(shape, dtype=None)
# - shape: tupla con dimensiones (alto, ancho, canales)
# - dtype: tipo de dato (opcional)
imagenRotada = np.zeros((alto + 1, ancho + 1, canales), dtype=np.uint8)

# FORMA 1: Rotación manual usando la matriz de rotación de OpenCV
# Se calcula la nueva posición de cada pixel usando la matriz de rotación
# for altura in range(alto):
#     for largo in range(ancho):
#         vectorPosicion = np.array([altura, largo, 1], np.uint8) # Vector posición (y, x, 1)
#         productoPunto = np.dot(matrizRotacion, vectorPosicion) # Producto de la matriz y el vector
#         x = int(productoPunto[0]) # Nueva coordenada x
#         y = int(productoPunto[1]) # Nueva coordenada y
#         imagenRotada[y, x] = imagenMini[altura, largo] # Asignación del pixel rotado
#         print(x, y) # Imprime coordenadas nuevas

# FORMA 2: Rotación usando función warpAffine de OpenCV
# openCv.warpAffine(src, M, dsize, flags=None, borderMode=None, borderValue=None)
# - src: imagen de entrada (array numpy)
# - M: matriz de transformación 2x3 (afín, aquí de rotación)
# - dsize: tupla (ancho, alto) de la imagen de salida
# - flags: método de interpolación (opcional, ej: cv2.INTER_LINEAR, cv2.INTER_NEAREST)
# - borderMode: cómo tratar los bordes (opcional, ej: cv2.BORDER_CONSTANT, cv2.BORDER_REFLECT)
# - borderValue: valor para los bordes si BORDER_CONSTANT
# Devuelve: imagen transformada
imagenRotada = openCv.warpAffine(imagenMini, matrizRotacion, (ancho + 1, alto + 1), flags=openCv.INTER_LINEAR, borderMode=openCv.BORDER_CONSTANT, borderValue=0)
# - matrizRotacion: obtenida con getRotationMatrix2D
# - (ancho+1, alto+1): tamaño de la imagen de salida
# - flags: interpolación (por defecto INTER_LINEAR)
# - borderMode: por defecto BORDER_CONSTANT
# - borderValue: valor de relleno en los bordes (0 = negro)

# FORMA 3: Rotación usando la librería imutils
# imutils.rotate_bound(image, angle)
# - image: imagen origen (array numpy)
# - angle: ángulo en grados
# Devuelve: imagen rotada sin recorte (ajusta el tamaño para que no se pierda información)
import imutils
imagenRotada = imutils.rotate_bound(imagenMini, angulo)

# FORMA 4: Rotación manual usando matriz de rotación creada con numpy
# np.radians(angulo): convierte grados a radianes
anguloRadianes = np.radians(angulo)
# Matriz de rotación 2D (3x3)
# - np.cos, np.sin: funciones trigonométricas
# - La matriz rota el punto (x, y) alrededor del origen
matrizRotacion = np.array([
    [np.cos(anguloRadianes), -np.sin(anguloRadianes), 0],
    [np.sin(anguloRadianes), np.cos(anguloRadianes), 0],
    [0, 0, 1]
])
# Aplica la rotación a cada pixel manualmente
for altura in range(alto):
    for largo in range(ancho):
        vectorPosicion = np.array([largo, altura, 1], np.uint8) # Vector posición (x, y, 1)
        productoPunto = np.dot(matrizRotacion, vectorPosicion) # Producto de la matriz y el vector
        x = int(productoPunto[0]) # Nueva coordenada x
        y = int(productoPunto[1]) # Nueva coordenada y
        imagenRotada[y, x] = imagenMini[altura, largo] # Asignación del pixel rotado
        print(x, y) # Imprime coordenadas nuevas

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
openCv.imshow("ventana", imagenRotada)

# Esperar una tecla para cerrar la ventana
# openCv.waitKey(delay)
# - delay: int, tiempo en milisegundos que espera por una tecla (0 = espera indefinida)
# Devuelve: el código ASCII de la tecla presionada, o -1 si no se presiona ninguna
openCv.waitKey()

# Cerrar todas las ventanas abiertas por OpenCV
# openCv.destroyAllWindows()
# No recibe parámetros, cierra todas las ventanas creadas por imshow
openCv.destroyAllWindows()