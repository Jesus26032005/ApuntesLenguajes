# Importar la biblioteca OpenCV
import cv2 as openCV  # OpenCV: procesamiento de imágenes y video

# Leer una imagen desde disco
# openCV.imread(ruta, bandera)
# - ruta: string, ruta del archivo de imagen
# - bandera: especifica cómo leer la imagen (opcional):
#     openCV.IMREAD_COLOR (1): lee en color (por defecto)
#     openCV.IMREAD_GRAYSCALE (0): lee en escala de grises
#     openCV.IMREAD_UNCHANGED (-1): lee la imagen tal cual (incluye canal alfa si existe)
#     openCV.IMREAD_ANYCOLOR: lee cualquier formato de color
#     openCV.IMREAD_ANYDEPTH: lee cualquier profundidad de bits
#     openCV.IMREAD_REDUCED_COLOR_2, _4, _8: lee imagen reducida en color (por factores 2, 4, 8)
#     openCV.IMREAD_REDUCED_GRAYSCALE_2, _4, _8: lee imagen reducida en grises
# Devuelve: un array numpy con la imagen cargada, o None si la ruta es incorrecta
imagen = openCV.imread("procesamientoimagenes/opencv/imagen.png")

# Separar los canales de color BGR
# openCV.split(imagen)
# - imagen: array numpy, imagen a separar
# Devuelve: una tupla de arrays (canales), en orden B, G, R para imágenes OpenCV
MatrizBlue, MatrizGreen, MatrizRed = openCV.split(imagen) # Devuelve los canales B, G, R en matrices

# Unir canales en una sola imagen
# openCV.merge((canal1, canal2, canal3))
# - canal1, canal2, canal3: arrays numpy, canales a unir
# Devuelve: array numpy, imagen combinada
imagenCombinada = openCV.merge((MatrizBlue, MatrizGreen, MatrizRed)) # Unimos los 3 canales y guardamos la imagen resultante

# Crear ventanas para mostrar imágenes
# openCV.namedWindow(nombre_ventana, bandera)
# - nombre_ventana: string, nombre de la ventana
# - bandera: tipo de ventana (opcional):
#     openCV.WINDOW_NORMAL: permite cambiar el tamaño de la ventana
#     openCV.WINDOW_AUTOSIZE: tamaño fijo según la imagen
#     openCV.WINDOW_FULLSCREEN: ventana en modo pantalla completa
#     openCV.WND_PROP_FULLSCREEN: también se puede pasar como bandera para crear la ventana directamente en modo pantalla completa
#     openCV.WINDOW_FREERATIO: permite cambiar la relación de aspecto
#     openCV.WINDOW_KEEPRATIO: mantiene la relación de aspecto
#     openCV.WINDOW_OPENGL: usa OpenGL para renderizado
# No devuelve nada.
openCV.namedWindow("imagen", openCV.WINDOW_NORMAL)
openCV.namedWindow("imagenRoja", openCV.WINDOW_NORMAL)
openCV.namedWindow("imagenAzul", openCV.WINDOW_NORMAL)
openCV.namedWindow("imagenVerde", openCV.WINDOW_NORMAL)

# Mostrar imágenes en ventanas
# openCV.imshow(nombre_ventana, imagen)
# - nombre_ventana: string, nombre de la ventana
# - imagen: array numpy, imagen a mostrar
# No devuelve nada. Muestra la imagen en una ventana emergente.
openCV.imshow("imagen", imagenCombinada)
openCV.imshow("imagenRoja", MatrizRed)
openCV.imshow("imagenAzul", MatrizBlue)
openCV.imshow("imagenVerde", MatrizGreen)

# Convertir imagen de BGR a HSV
# openCV.cvtColor(imagen, codigo_conversion)
# - imagen: array numpy, imagen a convertir
# - codigo_conversion: especifica el tipo de conversión:
#     openCV.COLOR_BGR2HSV: de BGR a HSV
#     openCV.COLOR_BGR2RGB: de BGR a RGB
#     openCV.COLOR_RGB2GRAY: de RGB a escala de grises
#     openCV.COLOR_BGR2GRAY: de BGR a escala de grises
# Devuelve: array numpy, imagen convertida
hsv = openCV.cvtColor(imagen, openCV.COLOR_BGR2HSV)

# Separar canales HSV
# openCV.split(imagen)
# - imagen: array numpy, imagen a separar
# Devuelve: una tupla de arrays (canales), en orden H, S, V para HSV
matrizH, matrizS, matrizV = openCV.split(hsv)

# Mostrar imagen HSV y sus canales
openCV.imshow("HSV ", hsv)
openCV.imshow("matriz tono", matrizH)        # Tono (Hue)
openCV.imshow("matriz saturacion", matrizS)  # Saturación (Saturation)
openCV.imshow("matriz brillo", matrizV)      # Brillo (Value)

#  Conversion de BGR a grises
# openCV.cvtColor(imagen, openCV.COLOR_BGR2GRAY)
# - imagen: array numpy, imagen a convertir
# - openCV.COLOR_BGR2GRAY: convierte de BGR a escala de grises
# Devuelve: array numpy, imagen en escala de grises
imagenGris = openCV.cvtColor(imagen, openCV.COLOR_BGR2GRAY)
openCV.imshow("Imagen gris", imagenGris)

# Esperar una tecla para cerrar las ventanas
# openCV.waitKey(delay)
# - delay: int, tiempo en milisegundos que espera por una tecla (0 = espera indefinida)
# Devuelve: el código ASCII de la tecla presionada, o -1 si no se presiona ninguna
openCV.waitKey()

# Cerrar todas las ventanas abiertas por OpenCV
# openCV.destroyAllWindows()
# No recibe parámetros, cierra todas las ventanas creadas por imshow
# No devuelve nada.
openCV.destroyAllWindows()