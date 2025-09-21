# Importar bibliotecas
import cv2 as openCv  # OpenCV: procesamiento de imágenes y video
import numpy as np    # Numpy: manejo de arreglos y matrices
import matplotlib.pyplot as plt  # Matplotlib: visualización de datos e imágenes

# Leer una imagen usando OpenCV
# openCv.imread(ruta, bandera)
# - ruta: string, ruta del archivo de imagen
# - bandera: (opcional) especifica cómo leer la imagen:
#     cv2.IMREAD_COLOR (1, por defecto): lee en color
#     cv2.IMREAD_GRAYSCALE (0): lee en escala de grises
#     cv2.IMREAD_UNCHANGED (-1): lee la imagen tal cual (incluye canal alfa si existe)
# Devuelve: un array numpy con la imagen cargada, o None si la ruta es incorrecta
imagen = openCv.imread('ProcesamientoImagenes/openCv/imagen.png')

# Mostrar la imagen en una ventana
# openCv.imshow(nombre_ventana, imagen)
# - nombre_ventana: string, nombre de la ventana que se mostrará
# - imagen: array, imagen a mostrar (debe ser tipo numpy array)
# No devuelve nada. Muestra la imagen en una ventana emergente.
openCv.imshow('Imagen Original', imagen)

# Esperar una tecla para cerrar la ventana
# openCv.waitKey(delay)
# - delay: int, tiempo en milisegundos que espera por una tecla (0 = espera indefinida)
# Devuelve: el código ASCII de la tecla presionada, o -1 si no se presiona ninguna
openCv.waitKey(0)

# Cerrar todas las ventanas abiertas por OpenCV
# openCv.destroyAllWindows()
# No recibe parámetros, cierra todas las ventanas creadas por imshow
# No devuelve nada.
openCv.destroyAllWindows()

# Guardar una imagen en disco
# openCv.imwrite(ruta, imagen)
# - ruta: string, ruta donde se guardará la imagen (incluye nombre y extensión)
# - imagen: array numpy, imagen a guardar
# Devuelve: True si la imagen se guardó correctamente, False en caso contrario
openCv.imwrite('ProcesamientoImagenes/openCv/imagen_copia.png', imagen)