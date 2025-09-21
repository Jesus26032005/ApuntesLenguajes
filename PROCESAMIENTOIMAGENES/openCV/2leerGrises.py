
# Importar la biblioteca OpenCV
import cv2 as openCv  # OpenCV: procesamiento de imágenes y video

# Leer una imagen en escala de grises
# openCv.imread(ruta, bandera)
# - ruta: string, ruta del archivo de imagen
# - bandera: especifica cómo leer la imagen:
#     openCv.IMREAD_COLOR (1): lee en color (por defecto)
#     openCv.IMREAD_GRAYSCALE (0): lee en escala de grises
#     openCv.IMREAD_UNCHANGED (-1): lee la imagen tal cual (incluye canal alfa si existe)
# Devuelve: un array numpy con la imagen cargada, o None si la ruta es incorrecta
imagen = openCv.imread('ProcesamientoImagenes/openCv/imagen.png', openCv.IMREAD_GRAYSCALE)

# Mostrar la imagen en una ventana
# openCv.imshow(nombre_ventana, imagen)
# - nombre_ventana: string, nombre de la ventana que se mostrará
# - imagen: array, imagen a mostrar (debe ser tipo numpy array)
# No devuelve nada. Muestra la imagen en una ventana emergente.
openCv.imshow('Imagen en Escala de Grises', imagen)

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