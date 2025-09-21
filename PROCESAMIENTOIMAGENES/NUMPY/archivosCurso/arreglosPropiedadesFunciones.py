

# Importar el módulo numpy
# Se recomienda importar como 'np' para facilitar la sintaxis: import numpy as np
# Ejemplo:
# import numpy as np
import numpy


# CREAR ARREGLO
# numpy.array(objeto_iterable, dtype=None, copy=True, order='K', subok=False, ndmin=0)
# - objeto_iterable: lista, tupla, o cualquier objeto iterable
# - dtype: tipo de dato (opcional, ej: int, float, np.int32, np.float64, bool, complex)
# - copy: si True, copia los datos (por defecto True)
# - order: 'C' (fila mayor), 'F' (columna mayor), 'A', 'K' (por defecto 'K')
# - subok: si True, subclases son permitidas (por defecto False)
# - ndmin: número mínimo de dimensiones (por defecto 0)
# Retorna: ndarray
# Ejemplos:
arreglo1 = numpy.array([1, 2, 3, 4, 5])  # Unidimensional
arreglo2 = numpy.array([[1, 2, 3], [4, 5, 6]])  # Bidimensional
lista = [1, 2, 3, 4, 5]
lista2 = [[1, 2, 3], [4, 5, 6]]
arreglo3 = numpy.array(lista2)  # Desde lista de listas
arreglo4 = numpy.array([[1, 2, 3], [4, 5, 6]])
arreglo5 = numpy.array([1, 2, 3], dtype=float)  # Especificando tipo de dato
# Advertencia: Si el tipo de dato no es compatible con los valores, se produce un error o truncamiento.



# CREAR MATRICES VACÍAS, la sintaxis de las tuplas es (filas, columnas)
# numpy.empty(shape, dtype=float, order='C')
# - shape: tupla con dimensiones (ej: (filas, columnas))
# - dtype: tipo de dato (opcional, ej: int, float)
# - order: 'C' (por filas), 'F' (por columnas)
# Retorna: ndarray sin inicializar (valores aleatorios en memoria)
matriz_vacia1 = numpy.empty((2, 3))  # Matriz vacía

# numpy.zeros(shape, dtype=float, order='C')
# - shape: tupla con dimensiones
# - dtype: tipo de dato (opcional)
# - order: 'C' o 'F'
# Retorna: ndarray inicializado en ceros
matriz_vacia2 = numpy.zeros((2, 3))  # Matriz de ceros

# numpy.ones(shape, dtype=None, order='C')
# - shape: tupla con dimensiones
# - dtype: tipo de dato (opcional)
# - order: 'C' o 'F'
# Retorna: ndarray inicializado en unos
matriz_vacia3 = numpy.ones((2, 3))   # Matriz de unos



# CREAR ARREGLOS A PARTIR DE UNA SECUENCIA
# numpy.arange(start, stop, step, dtype=None)
# - start: valor inicial
# - stop: valor final (no incluido)
# - step: incremento (por defecto 1)
# - dtype: tipo de dato (opcional)
# Retorna: ndarray con valores en el rango
arreglo6 = numpy.arange(1, 10, 2)  # [1, 3, 5, 7, 9]

# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
# - start: valor inicial
# - stop: valor final
# - num: cantidad de valores (por defecto 50)
# - endpoint: si True incluye el valor final
# - retstep: si True retorna el paso
# - dtype: tipo de dato (opcional)
# Retorna: ndarray con valores equidistantes
arreglo7 = numpy.linspace(0, 1, 5)  # [0., 0.25, 0.5, 0.75, 1.]

# numpy.arange(...).reshape(new_shape)
# - new_shape: tupla con nueva forma (ej: (3, 3))
# Retorna: ndarray con la forma indicada
arreglo8 = numpy.arange(1, 10).reshape((3, 3))  # [[1,2,3],[4,5,6],[7,8,9]]



# RESHAPE
# ndarray.reshape(new_shape, order='C')
# - new_shape: tupla con nueva forma (ej: (3, 3))
# - order: 'C' (por filas), 'F' (por columnas)
# Retorna: nuevo array con la forma indicada
# Advertencia: El número de elementos debe coincidir con el producto de las dimensiones
arreglo8 = arreglo6.reshape((3, 3))



# PROPIEDADES DE LOS ARREGLOS
# .shape: tupla con dimensiones (filas, columnas, ...)
# Retorna: tupla de enteros
print(arreglo3.shape)  # Ejemplo: (2, 3)

# .ndim: número de dimensiones
# Retorna: entero
print(arreglo3.ndim)  # Ejemplo: 2

# .dtype: tipo de dato de los elementos
# Retorna: objeto dtype
print(arreglo3.dtype)  # Ejemplo: int32, float64

# .size: número total de elementos
# Retorna: entero
print(arreglo3.size)  # Ejemplo: 6

# .itemsize: tamaño en bytes de cada elemento
# Retorna: entero
print(arreglo3.itemsize)  # Ejemplo: 4 (para int32)

# .nbytes: tamaño total en bytes del arreglo
# Retorna: entero
print(arreglo3.nbytes)  # Ejemplo: 24 (6 elementos x 4 bytes)

# .T: Transpuesta del arreglo
# Retorna: ndarray transpuesto
print(arreglo3.T)

# .real: parte real del arreglo (para números complejos)
# Retorna: ndarray con la parte real
print(arreglo3.real)

# .imag: parte imaginaria del arreglo (para números complejos)
# Retorna: ndarray con la parte imaginaria
print(arreglo3.imag)

# .conj: Conjugado del arreglo (para números complejos)
# Retorna: ndarray conjugado
print(arreglo3.conj())



# CONSTANTES DE NUMPY
# numpy.pi: valor de pi (3.14159...)
# numpy.e: valor de e (2.71828...)
numpy.pi
numpy.e


# FUNCIONES DE MATEMÁTICAS
# Todas estas funciones aceptan arrays y/o valores escalares, espera los valroes en radianos
# numpy.sin(x): seno
# numpy.cos(x): coseno
# numpy.tan(x): tangente
# numpy.arcsin(x): arcoseno
# numpy.arccos(x): arcocoseno
# numpy.arctan(x): arcotangente
# numpy.sinh(x): seno hiperbólico
# numpy.cosh(x): coseno hiperbólico
# numpy.tanh(x): tangente hiperbólica
# numpy.arcsinh(x): arcoseno hiperbólico
# numpy.arccosh(x): arcocoseno hiperbólico
# numpy.arctanh(x): arcotangente hiperbólica
# numpy.exp(x): exponencial
# numpy.log(x): logaritmo natural
# numpy.log10(x): logaritmo base 10
# numpy.log2(x): logaritmo base 2
# numpy.sqrt(x): raíz cuadrada
# numpy.cbrt(x): raíz cúbica
# numpy.power(x, y): x elevado a y
# numpy.square(x): x al cuadrado
# numpy.abs(x): valor absoluto
# numpy.fabs(x): valor absoluto (float)
# numpy.around(x, decimals=0): redondeo
# - decimals: número de decimales (por defecto 0)
# Si tienes valores en grados, primero debes convertirlos a radianes usando numpy.radians.
grados = numpy.array([0, 30, 45, 60, 90])
radianes = numpy.radians(grados)
resultado = numpy.sin(radianes)


# Operaciones de arreglos
# numpy.add(x1, x2): suma elemento a elemento
# numpy.subtract(x1, x2): resta elemento a elemento
# numpy.multiply(x1, x2): multiplicación elemento a elemento
# numpy.divide(x1, x2): división elemento a elemento
# numpy.floor_divide(x1, x2): división entera
# numpy.mod(x1, x2): módulo
# numpy.power(x1, x2): potencia
# numpy.sqrt(x): raíz cuadrada
# numpy.exp(x): exponencial
# numpy.log(x): logaritmo natural
# numpy.log10(x): logaritmo base 10
# numpy.log2(x): logaritmo base 2


# Operaciones de arreglos con arreglos
# Todas las funciones admiten arrays de igual forma o broadcasting
# numpy.greater(x1, x2): mayor que
# numpy.greater_equal(x1, x2): mayor o igual que
# numpy.less(x1, x2): menor que
# numpy.less_equal(x1, x2): menor o igual que
# numpy.equal(x1, x2): igual que
# numpy.not_equal(x1, x2): diferente de
# También se pueden usar operadores:
# +, -, *, / para suma, resta, multiplicación y división elemento a elemento
arreglo3 + arreglo4  # Suma elemento a elemento
arreglo3 - arreglo4  # Resta elemento a elemento
arreglo3 * arreglo4  # Multiplicación elemento a elemento
arreglo3 / arreglo4  # División elemento a elemento

# Multiplicacion de matrices
# numpy.matmul(a, b) o a @ b
numpy.matmul(arreglo3, arreglo4)  # Multiplicación de matrices
arreglo3 @ arreglo4  # Multiplicación de matrices

# Inversa
numpy.linalg.inv(arreglo3)  # Inversa de una matriz

# Concatenación de arreglos
# numpy.concatenate((a1, a2, ...), axis=0)
# - axis: eje sobre el que se concatena (0 = filas, 1 = columnas)
numpy.concatenate((arreglo3, arreglo4), axis=0)  # Concatenar a lo largo de la primera dimensión
numpy.concatenate((arreglo3, arreglo4), axis=1)  # Concatenar a lo largo de la segunda dimensión

# Ordenar arreglos
# numpy.sort(a, axis=-1, kind='quicksort', order=None)
# - axis: eje sobre el que se ordena (por defecto -1, última dimensión)
# - kind: método de ordenamiento ('quicksort', 'mergesort', 'heapsort', 'stable')
# - order: para arrays estructurados
numpy.sort(arreglo3)  # Ordenar arreglo3
numpy.sort(arreglo4)  # Ordenar arreglo4

