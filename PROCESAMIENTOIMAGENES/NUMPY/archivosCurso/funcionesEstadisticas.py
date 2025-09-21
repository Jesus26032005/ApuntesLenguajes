import numpy

# Crear un generador de números aleatorios
# numpy.random.default_rng(seed)
# - seed: semilla para reproducibilidad (opcional)
regenerador = numpy.random.default_rng(42)

# Generar un arreglo de enteros aleatorios
# regenerador.integers(low, high, size=None, dtype=int, endpoint=False)
# - low: valor mínimo (incluido)
# - high: valor máximo (excluido)
# - size: cantidad de elementos o tupla de dimensiones
# - dtype: tipo de dato (opcional)
# - endpoint: si True, incluye el valor máximo
arregloNormal = regenerador.integers(0, 100, size=20)

# Obtener el valor máximo
# ndarray.max(axis=None)
# - axis: sobre qué eje calcular el máximo (opcional)
maximo = arregloNormal.max()

# Obtener el valor mínimo
# ndarray.min(axis=None)
# - axis: sobre qué eje calcular el mínimo (opcional)
minimo = arregloNormal.min()

# Obtener la media
# ndarray.mean(axis=None)
# - axis: sobre qué eje calcular la media (opcional)
media = arregloNormal.mean()

# Obtener la mediana
# numpy.median(a, axis=None)
# - a: array
# - axis: sobre qué eje calcular la mediana (opcional)
mediana = numpy.median(arregloNormal)

# Obtener la desviación estándar
# numpy.std(a, axis=None)
# - a: array
# - axis: sobre qué eje calcular la desviación estándar (opcional)
estandar = numpy.std(arregloNormal)

# Obtener suma
# ndarray.sum(axis=None)
# - axis: sobre qué eje calcular la suma (opcional)
suma = arregloNormal.sum()

# Obtener la varianza
# numpy.var(a, axis=None)
# - a: array
# - axis: sobre qué eje calcular la varianza (opcional)
varianza = numpy.var(arregloNormal)

"""
En NumPy, el parámetro axis indica sobre qué dimensión se realiza una operación en un array multidimensional.
axis=0: Operación a lo largo de las filas (por columnas).
axis=1: Operación a lo largo de las columnas (por filas).
En arrays de más dimensiones, el número de axis corresponde a la dimensión (axis=2 para profundidad, etc).
"""

# Ejemplo con arrays 2D
# Para usar axis, el array debe tener más de una dimensión:
matriz = regenerador.integers(0, 100, size=(4, 5))

# Obtener mínimo de cada columna
minimos_columnas = matriz.min(axis=0)  # Devuelve array de mínimos por columna
# Obtener máximo de cada columna
maximos_columnas = matriz.max(axis=0)  # Devuelve array de máximos por columna
# Obtener mínimo de cada fila
minimos_filas = matriz.min(axis=1)     # Devuelve array de mínimos por fila
# Obtener máximo de cada fila
maximos_filas = matriz.max(axis=1)     # Devuelve array de máximos por fila

# Obtener valores únicos
# numpy.unique(a)
# - a: array
# Retorna: array de valores únicos ordenados
valores_unicos = numpy.unique(arregloNormal)

# Obtener valores por filtro (condición booleana)
# arreglo[condición]
# Retorna: array con los valores que cumplen la condición
valores_filtrados = arregloNormal[arregloNormal > 50]

# Apilar arreglos
# numpy.stack(arrays, axis=0)
# - arrays: tupla/lista de arrays
# - axis: eje sobre el que se apilan (0 = filas, 1 = columnas)
arreglo_apilado = numpy.stack((arregloNormal, arregloNormal), axis=0)

# numpy.hstack(arrays)
# - arrays: tupla/lista de arrays
# Retorna: array apilado horizontalmente (por columnas)
arreglo_apilado_horizontal = numpy.hstack((arregloNormal, arregloNormal))

# numpy.vstack(arrays)
# - arrays: tupla/lista de arrays
# Retorna: array apilado verticalmente (por filas)
arreglo_apilado_vertical = numpy.vstack((arregloNormal, arregloNormal))