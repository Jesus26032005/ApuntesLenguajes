
# Importar la biblioteca OpenCV
import cv2 as openCv  # OpenCV: procesamiento de imágenes y video

## Leer una imagen en color
# openCv.imread(ruta, bandera)
# - ruta: string, ruta del archivo de imagen
# - bandera: especifica cómo leer la imagen (opcional):
#     openCv.IMREAD_COLOR (1): lee en color (por defecto)
#     openCv.IMREAD_GRAYSCALE (0): lee en escala de grises
#     openCv.IMREAD_UNCHANGED (-1): lee la imagen tal cual (incluye canal alfa si existe)
#     openCv.IMREAD_ANYCOLOR: lee cualquier formato de color
#     openCv.IMREAD_ANYDEPTH: lee cualquier profundidad de bits
#     openCv.IMREAD_REDUCED_COLOR_2, _4, _8: lee imagen reducida en color (por factores 2, 4, 8)
#     openCv.IMREAD_REDUCED_GRAYSCALE_2, _4, _8: lee imagen reducida en grises
# Devuelve: un array numpy con la imagen cargada, o None si la ruta es incorrecta
imagen = openCv.imread('ProcesamientoImagenes/openCv/imagen.png')
imagengrises = openCv.imread('ProcesamientoImagenes/openCv/imagen.png', openCv.IMREAD_GRAYSCALE)

# Crear una ventana personalizada
# openCv.namedWindow(nombre_ventana, bandera)
# - nombre_ventana: string, nombre de la ventana
# - bandera: especifica el tipo de ventana (opcional):
#     openCv.WINDOW_NORMAL: permite cambiar el tamaño de la ventana
#     openCv.WINDOW_AUTOSIZE: tamaño fijo según la imagen
#     openCv.WINDOW_FULLSCREEN: ventana en modo pantalla completa
#     openCv.WND_PROP_FULLSCREEN: también se puede pasar como bandera para crear la ventana directamente en modo pantalla completa
#     openCv.WINDOW_FREERATIO: permite cambiar la relación de aspecto
#     openCv.WINDOW_KEEPRATIO: mantiene la relación de aspecto
#     openCv.WINDOW_OPENGL: usa OpenGL para renderizado
# No devuelve nada. Permite controlar propiedades de la ventana antes de mostrar la imagen.

# openCv.setWindowProperty(nombre_ventana, propiedad, valor)
# - nombre_ventana: string, nombre de la ventana a modificar
# - propiedad: tipo de propiedad a cambiar:
#     openCv.WND_PROP_FULLSCREEN: modo pantalla completa
#     openCv.WND_PROP_AUTOSIZE: modo autosize
#     openCv.WND_PROP_ASPECT_RATIO: relación de aspecto
#     openCv.WND_PROP_OPENGL: renderizado OpenGL
# - valor: nuevo valor para la propiedad:
#     openCv.WINDOW_FULLSCREEN (1): activa pantalla completa
#     openCv.WINDOW_NORMAL (0): ventana normal
#     openCv.WINDOW_AUTOSIZE (1): activa autosize
#     openCv.WINDOW_FREERATIO (0): relación libre
#     openCv.WINDOW_KEEPRATIO (1): mantiene relación
# Sirve para modificar dinámicamente propiedades de la ventana, como activar/desactivar pantalla completa, cambiar tamaño, etc.

openCv.namedWindow("ventana", openCv.WINDOW_NORMAL)
# Bucle principal para mostrar imágenes según la tecla presionada
while True:
        # Espera indefinida por una tecla
        # openCv.waitKey(delay)
        # - delay: int, tiempo en milisegundos que espera por una tecla:
        #     0: espera indefinida
        #     >0: espera ese número de milisegundos
        # Devuelve: el código ASCII de la tecla presionada, o -1 si no se presiona ninguna
    key = openCv.waitKey()
    # ord(caracter)
    # - caracter: string de un solo carácter
    # Devuelve: el valor numérico (código ASCII/Unicode) del carácter dado
    # Se usa para comparar el valor de la tecla presionada con el código correspondiente
    if key == ord("4"): 
        # Mostrar imagen en color en la ventana
            # openCv.imshow(nombre_ventana, imagen)
            # - nombre_ventana: string, nombre de la ventana
            # - imagen: array numpy, imagen a mostrar
            # No devuelve nada. Si la ventana ya existe, la actualiza rápidamente.
        openCv.imshow("ventana", imagen)
    elif key == ord("5"):
        # Mostrar imagen en escala de grises en la ventana
        openCv.imshow("ventana", imagengrises)
    else:
        # Si se presiona cualquier otra tecla, sale del bucle
        break

## Cerrar todas las ventanas abiertas por OpenCV
# openCv.destroyAllWindows()
# No recibe parámetros, cierra todas las ventanas creadas por imshow
# No devuelve nada.
openCv.destroyAllWindows()