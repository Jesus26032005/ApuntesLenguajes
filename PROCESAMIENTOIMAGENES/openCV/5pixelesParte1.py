
# Importar las bibliotecas necesarias
# cv2: procesamiento de imágenes y video
# numpy: manejo de arreglos y matrices multidimensionales
# random: generación de números aleatorios
import cv2 as openCv, numpy as np, random


# Crear una imagen negra (oscura) de 100x100 píxeles y 3 canales (RGB)
# np.zeros(shape, dtype)
# - shape: tupla con dimensiones (alto, largo, canales)
# - dtype: tipo de dato de los elementos (np.uint8 para imágenes de 8 bits por canal)
# Devuelve: array numpy lleno de ceros
imagenOscura = np.zeros((100, 100, 3), np.uint8)

# Acceder al valor de un pixel en la posición (50, 50)
# imagenOscura[fila][columna]
# Devuelve: array con los valores de los canales en esa posición (ejemplo: [0, 0, 0])
pixel = imagenOscura[50][50]
print(pixel)


# Modificar el valor de un pixel
# imagenOscura[fila][columna] = [R, G, B]
# - R, G, B: valores enteros entre 0 y 255 para cada canal
# No devuelve nada, modifica el array en memoria
imagenOscura[50][50] = [255, 255, 255]
pixel = imagenOscura[50][50]
print(pixel)


# Obtener las dimensiones de la imagen
# imagenOscura.shape
# Devuelve: tupla (alto, largo, canales)
alto, largo, canales = imagenOscura.shape
print(alto, largo, canales)


# Asignar valores aleatorios a cada pixel de la imagen
# random.randint(a, b)
# - a: valor mínimo (incluido)
# - b: valor máximo (incluido)
# Devuelve: entero aleatorio entre a y b
# Se usa para generar colores aleatorios en cada canal de cada pixel
for i in range(alto):
    for j in range(largo):
        imagenOscura[i][j] = [random.randint(0, 225), random.randint(0, 255), random.randint(0, 255)]
        

# Mostrar la imagen generada en una ventana
# openCv.imshow(nombre_ventana, imagen)
# - nombre_ventana: string, nombre de la ventana
# - imagen: array numpy, imagen a mostrar
# No devuelve nada. Muestra la imagen en una ventana emergente.
openCv.imshow("imagen", imagenOscura)

# Esperar una tecla para cerrar la ventana
# openCv.waitKey(delay)
# - delay: int, tiempo en milisegundos que espera por una tecla (0 = espera indefinida)
# Devuelve: el código ASCII de la tecla presionada, o -1 si no se presiona ninguna
openCv.waitKey()

# Cerrar todas las ventanas abiertas por OpenCV
# openCv.destroyAllWindows()
# No recibe parámetros, cierra todas las ventanas creadas por imshow
# No devuelve nada.
openCv.destroyAllWindows()