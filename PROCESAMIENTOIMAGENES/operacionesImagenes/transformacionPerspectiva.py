"""
TRANSFORMACION DE PERSPECTIVA
Producto de la matriz de transformacion con modificaciones en el espacio (0,1), (1,0) y el vector de posicion del pixel
Las matrices de transformacion de perspectiva son:
[[1, Sv, 0], 
[0, 1, 0], 
[0, 0, 1]] la vertical (cada fila se desplaza horizontalmente) desplaza cada fila horizontal hacia la derecha o izquierda, proporcional a su altura.
Original:
█
█
█

Cizallamiento vertical:
  █
 █
█


y la horizontal (cada columna se desplaza verticalmente, desplaza cada columna vertical hacia arriba o abajo, proporcional a su posición horizontal.) es
[[1, 0, 0], 
[Sh, 1, 0], 
[0, 0, 1]]
"""

import numpy as np
import cv2 as openCv  

imagen= openCv.imread("procesamientoImagenes/operacionesImagenes/imagen.png")
alto, ancho, canales = imagen.shape
matrizTransformacionVertical = np.array([[1,0,0], [2,1,0],[0,0,1]])
matrizResultante= np.zeros((alto*5, ancho*4, canales), np.uint8)

for altura in range(alto):
    for anchura in range(ancho):
        pixel = imagen[altura, anchura]
        vectorPosicion = np.array([anchura, altura, 1])
        resultadoMultiplicacion = np.dot(matrizTransformacionVertical, vectorPosicion)
        matrizResultante[int(resultadoMultiplicacion[1]), int(resultadoMultiplicacion[0])] = pixel

openCv.imshow("Transformacion Vertical", matrizResultante)
openCv.waitKey(0)
openCv.destroyAllWindows()