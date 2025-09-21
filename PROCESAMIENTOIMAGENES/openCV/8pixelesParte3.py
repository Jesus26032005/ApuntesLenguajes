import cv2 as openCv, numpy as np, random

# Leer una imagen desde disco
# openCv.imread(ruta, bandera)
# - ruta: string, ruta del archivo de imagen
# - bandera: especifica cómo leer la imagen (opcional):
#     openCv.IMREAD_COLOR (1): lee en color (por defecto)
#     openCv.IMREAD_GRAYSCALE (0): lee en escala de grises
#     openCv.IMREAD_UNCHANGED (-1): lee la imagen tal cual (incluye canal alfa si existe)
# Devuelve: array numpy con la imagen cargada, o None si la ruta es incorrecta
imagen = openCv.imread("procesamientoimagenes/opencv/candados.jpg")

# Crear una copia de la imagen
# imagen.copy()
# Devuelve: copia independiente del array de la imagen
imagencopia = imagen.copy()

# Obtener dimensiones de la imagen
# imagen.shape
# Devuelve: tupla (alto, largo, canales)
alto, largo, canales = imagencopia.shape

# Crear una ventana para mostrar imágenes
# openCv.namedWindow(nombre_ventana, bandera)
# - nombre_ventana: string, nombre de la ventana
# - bandera: tipo de ventana (opcional):
#     openCv.WINDOW_NORMAL: permite cambiar el tamaño de la ventana
#     openCv.WINDOW_AUTOSIZE: tamaño fijo según la imagen
openCv.namedWindow("ventana", openCv.WINDOW_NORMAL)

# Seleccionar una región de interés (ROI) manualmente
# openCv.selectROI(nombre_ventana, imagen, showCrosshair=True, fromCenter=False)
# - nombre_ventana: string, ventana donde se selecciona
# - imagen: array numpy, imagen sobre la que se selecciona
# - showCrosshair: muestra cruz (opcional, por defecto True)
# - fromCenter: selecciona desde el centro (opcional, por defecto False)
# Devuelve: tupla (x, y, ancho, alto) de la región seleccionada
Roil1 = openCv.selectROI("ventana", imagen)
print(Roil1)

# Obtener dimensiones de la imagen original
alto, largo, capas = imagen.shape

# Extraer subimagen usando slicing
# imagen[y_inicio:y_fin, x_inicio:x_fin]
# Devuelve: submatriz (subimagen) de la imagen original
candado1 = imagen[int(Roil1[1]): int(Roil1[1]+Roil1[3]), int(Roil1[0]): int(Roil1[0]+Roil1[2])]
# Obtener dimensiones del candado1
alto1, largo1, _, = candado1.shape

# Seleccionar otra región de interés
Roil2 = openCv.selectROI("ventana", imagen)
candado2 = imagen[int(Roil2[1]): int(Roil2[1]+Roil2[3]), int(Roil2[0]): int(Roil2[0]+Roil2[2])]
alto2, largo2, _ = candado2.shape

# Redimensionar imágenes
# openCv.resize(imagen, dsize, fx=0, fy=0, interpolation=None)
# - imagen: array numpy, imagen a redimensionar
# - dsize: tupla (ancho, alto) de la nueva imagen
# - fx, fy: escala en x e y (opcional)
# - interpolation: método de interpolación (opcional)
# Devuelve: imagen redimensionada
newcandado1 = openCv.resize(candado1, (largo2, alto2))
newcandado2 = openCv.resize(candado2, (largo1, alto1))

# Reemplazar regiones en la copia de la imagen
# imagencopia[y_inicio:y_fin, x_inicio:x_fin] = nueva_imagen
imagencopia[int(Roil1[1]): int(Roil1[1]+Roil1[3]), int(Roil1[0]): int(Roil1[0]+Roil1[2])] = newcandado2
imagencopia[int(Roil2[1]): int(Roil2[1]+Roil2[3]), int(Roil2[0]): int(Roil2[0]+Roil2[2])] = newcandado1

# Mostrar la imagen modificada en una ventana
# openCv.imshow(nombre_ventana, imagen)
# - nombre_ventana: string, nombre de la ventana
# - imagen: array numpy, imagen a mostrar
openCv.imshow("imagencopia", imagencopia)

# Esperar una tecla para cerrar las ventanas
# openCv.waitKey(delay)
# - delay: int, tiempo en milisegundos que espera por una tecla (0 = espera indefinida)
# Devuelve: el código ASCII de la tecla presionada, o -1 si no se presiona ninguna
openCv.waitKey()

# Cerrar todas las ventanas abiertas por OpenCV
# openCv.destroyAllWindows()
# No recibe parámetros, cierra todas las ventanas creadas por imshow
openCv.destroyAllWindows()