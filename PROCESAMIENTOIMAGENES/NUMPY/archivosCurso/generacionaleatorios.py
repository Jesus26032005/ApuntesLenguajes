# Generación de arrays con valores aleatorios usando numpy
import numpy

# numpy.random.rand(d0, d1, ...)
# - d0, d1, ...: dimensiones del array
# Retorna: array de valores flotantes aleatorios en [0, 1)
# Ejemplo: matriz de 3x4
arreglo_aleatorio = numpy.random.rand(3, 4)  # Matriz 3x4 con valores aleatorios entre 0 y 1

# numpy.random.default_rng(seed).random(shape)
# - seed: semilla para reproducibilidad (opcional)
# - shape: tupla con dimensiones
# Retorna: array de valores flotantes aleatorios en [0, 1)
# Ejemplo: matriz de 3x4
arreglo_aleatorio2 = numpy.random.default_rng(2).random((3, 4))  # Matriz 3x4 con valores aleatorios

# Advertencia: default_rng es el generador recomendado desde NumPy 1.17, más seguro y reproducible.

# numpy.random.normal(loc=0.0, scale=1.0, size=None)
# - loc: media de la distribución
# - scale: desviación estándar
# - size: tupla con dimensiones
# Retorna: array de valores flotantes con distribución normal (campana)
# Ejemplo: matriz de 3x4
normal = numpy.random.normal(0, 1, (3, 4))  # Matriz 3x4 con valores de una distribución normal

# numpy.random.randint(low, high=None, size=None, dtype=int)
# - low: valor mínimo (incluido)
# - high: valor máximo (excluido)
# - size: tupla con dimensiones
# - dtype: tipo de dato (opcional)
# Retorna: array de enteros aleatorios
# Ejemplo: matriz de 3x4 con enteros entre 0 y 9
enteros = numpy.random.randint(0, 10, (3, 4))  # Matriz 3x4 con valores enteros aleatorios entre 0 y 9

# numpy.random.uniform(low=0.0, high=1.0, size=None)
# - low: valor mínimo
# - high: valor máximo
# - size: tupla con dimensiones
# Retorna: array de flotantes aleatorios en [low, high)
# Ejemplo: matriz de 3x4 con flotantes entre 0 y 10
floats = numpy.random.uniform(0, 10, (3, 4))  # Matriz 3x4 con valores flotantes aleatorios entre 0 y 10

# numpy.random.choice(a, size=None, replace=True, p=None)
# - a: array/lista de elementos posibles
# - size: tupla con dimensiones
# - replace: si True, puede repetirse el elemento
# - p: probabilidades de cada elemento (opcional)
# Retorna: array de elementos seleccionados aleatoriamente
# Ejemplo: matriz de 3x4 con letras aleatorias
letras = numpy.random.choice(['a', 'b', 'c', 'd', 'e'], (3, 4))  # Matriz 3x4 con letras aleatorias

# numpy.random.shuffle(x)
# - x: array a mezclar (modifica el array en el lugar)
# No retorna nada, solo reordena los elementos
arr = numpy.arange(12)
numpy.random.shuffle(arr)  # Mezcla los elementos de arr

# numpy.random.permutation(x)
# - x: array o entero
# Retorna: array permutado (nuevo orden)
permutado = numpy.random.permutation(arr)

# numpy.random.seed(seed)
# - seed: entero para fijar la semilla
# Permite reproducir los resultados aleatorios
numpy.random.seed(42)

# Ejemplo de reproducibilidad:
# Si usas la misma semilla, obtendrás los mismos resultados cada vez.
numpy.random.seed(123)
print(numpy.random.rand(2, 2))

# Caso de uso: simulaciones, pruebas, generación de datos sintéticos, mezclas y permutaciones.
# Advertencia: shuffle modifica el array original, permutation retorna uno nuevo.
                                                                                                                    
# USO DETALLADO DE numpy.random.default_rng
# -----------------------------------------
# Desde NumPy 1.17, se recomienda usar el generador de números aleatorios 'Generator' con default_rng.
# Ventajas:
# - Mejor control sobre el estado del generador.
# - Métodos más modernos y seguros.
# - Permite crear múltiples generadores independientes.

# Crear un generador:
rng = numpy.random.default_rng(123)  # 123 es la semilla (opcional)

# Métodos principales del generador:
# rng.random(shape): flotantes uniformes en [0, 1)
print(rng.random((2, 3)))

# rng.integers(low, high=None, size=None, dtype=int, endpoint=False): enteros aleatorios
print(rng.integers(0, 10, size=(2, 3)))

# rng.normal(loc=0.0, scale=1.0, size=None): distribución normal
print(rng.normal(0, 1, size=(2, 3)))

# rng.uniform(low=0.0, high=1.0, size=None): flotantes uniformes
print(rng.uniform(0, 10, size=(2, 3)))

# rng.choice(a, size=None, replace=True, p=None): selección aleatoria de elementos
print(rng.choice(['a', 'b', 'c'], size=(2, 3)))

# rng.shuffle(x): mezcla el array en el lugar
arr2 = numpy.arange(6)
rng.shuffle(arr2)
print(arr2)

# rng.permutation(x): retorna un array permutado
print(rng.permutation(arr2))

# Advertencia: El generador 'rng' es independiente de numpy.random.seed y de otros generadores.
# Puedes crear varios generadores con diferentes semillas para simulaciones paralelas o independientes.
