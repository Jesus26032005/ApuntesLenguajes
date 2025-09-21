import numpy as numpy

# Generar un arreglo de enteros aleatorios
# numpy.random.default_rng(seed).integers(low, high, size=None, dtype=int, endpoint=False)
# - seed: semilla para reproducibilidad (opcional)
# - low: valor mínimo (incluido)
# - high: valor máximo (excluido)
# - size: cantidad de elementos o tupla de dimensiones
# - dtype: tipo de dato (opcional)
# - endpoint: si True, incluye el valor máximo
enteros = numpy.random.default_rng(42).integers(0, 100, size=20)

# Seleccionar elementos por condición booleana
# arreglo[condición]
# - condición: expresión booleana sobre el arreglo
# Retorna: array con los elementos que cumplen la condición
# Ejemplo: seleccionar los mayores a 50
elementos_seleccionados = enteros[enteros > 50]

# Slicing (rebanado) de arrays
# arreglo[inicio:fin]
# - inicio: índice inicial (incluido)
# - fin: índice final (excluido)
# Retorna: subarray desde inicio hasta fin-1
elementos_sliced = enteros[5:15]  # Elementos del índice 5 al 14

# Slicing con paso
# arreglo[inicio:fin:paso]
# - paso: salto entre elementos
elementos_sliced2 = enteros[::2]  # Cada segundo elemento (índices pares)
elementos_sliced3 = enteros[:10]   # Primeros 10 elementos (índices 0 a 9)

# Slicing con paso específico
elementos_sliced4 = enteros[0:6:2]  # Elementos en índices 0, 2, 4

# Slicing con paso inverso
elementos_sliced5 = enteros[5:0:-1]  # Elementos del índice 5 al 1 en orden inverso

# Selección en arreglos multidimensionales
# ndarray.reshape(new_shape)
# - new_shape: tupla con nueva forma
arreglo_2d = enteros.reshape(4, 5)  # Convertir a matriz 4x5

# Seleccionar un elemento específico
# arreglo_2d[fila, columna]
elemento = arreglo_2d[2, 3]  # Elemento en fila 2, columna 3

# Seleccionar submatriz
# arreglo_2d[fila_inicio:fila_fin, columna_inicio:columna_fin]
elementos_2d = arreglo_2d[1:3, 2:4]  # Filas 1 y 2, columnas 2 y 3

# Selección con slicing avanzado
# arreglo_2d[fila_inicio:fila_fin:paso]
elementos246 = arreglo_2d[0:1:2]  # Selecciona la fila 0 (por paso 2, solo la primera)