# NUMPY es una biblioteca de Python que se utiliza para trabajar con arreglos y matrices multidimensionales. Proporciona una amplia gama de funciones para realizar operaciones matemáticas, estadísticas y de álgebra lineal en estos arreglos. Es eficaz para manejar grandes cantidades de datos y es ampliamente utilizado en ciencia de datos, aprendizaje automático y análisis numérico siendo que es una de las bibliotecas más populares en el ecosistema de Python para el análisis de datos.

import numpy as np
# Crear un arreglo unidimensional, es similar a una lista pero con funcionalidades adicionales y mejor rendimiento para operaciones matemáticas.
arreglo_unidimensional = np.array([1, 2, 3, 4, 5])
# Algo a mencionar es que los arreglos de Numpy son homogéneos, lo que significa que todos los elementos deben ser del mismo tipo de datos. Esto permite una mayor eficiencia en términos de memoria y rendimiento en comparación con las listas de Python, que pueden contener elementos de diferentes tipos.

print("Arreglo unidimensional:", arreglo_unidimensional)

# Acceso a elementos: Puedes acceder a los elementos de un arreglo unidimensional utilizando índices, al igual que con las listas de Python. Los índices comienzan en 0.
print("Primer elemento:", arreglo_unidimensional[0])  # Accede al primer elemento
print("Tercer elemento:", arreglo_unidimensional[2])  # Accede al tercer elemento

# si checamos el tipo de dato del arreglo, veremos que es un arreglo de enteros (int64 en este caso).
print("Tipo de dato del arreglo:", arreglo_unidimensional.dtype)
# Si lo checamos con type vemos que es un objeto de tipo numpy.ndarray, que es la clase principal para los arreglos en Numpy.
print("Tipo del objeto:", type(arreglo_unidimensional))

# Atributos
arreglo_unidimensional.size  # Devuelve el número total de elementos en el arreglo
arreglo_unidimensional.shape  # Devuelve una tupla que representa las dimensiones del arreglo
arreglo_unidimensional.ndim  # Devuelve el número de dimensiones del arreglo
arreglo_unidimensional.dtype  # Devuelve el tipo de datos de los elementos en el arreglo

# INDEXACIÓN Y SLICING
# Para modificar un elemento específico, puedes asignar un nuevo valor utilizando su índice. Por ejemplo, para cambiar el segundo elemento del arreglo a 10, puedes hacer lo siguiente:
arreglo_unidimensional[1] = 10
print("Arreglo después de modificar el segundo elemento:", arreglo_unidimensional)

# También puedes utilizar slicing para modificar un rango de elementos. Por ejemplo, para cambiar los primeros tres elementos a 0, puedes hacer lo siguiente:
arreglo_unidimensional[0:3] = 0
print("Arreglo después de modificar los primeros tres elementos:", arreglo_unidimensional)

# Para crear un nuevo arreglo usando slicing, puedes hacer lo siguiente:
nuevo_arreglo = arreglo_unidimensional[1:4]  # Esto crea un nuevo arreglo con los elementos desde el índice 1 hasta el índice 3 (excluyendo el índice 4)
print("Nuevo arreglo creado con slicing:", nuevo_arreglo)

# Puedes usar índices negativos para acceder a los elementos desde el final del arreglo. Por ejemplo, para acceder al último elemento del arreglo, puedes usar el índice -1:
print("Último elemento del arreglo:", arreglo_unidimensional[-1])  # Accede al último elemento

# Podemos asignar varios valores a un rango de elementos utilizando slicing. Por ejemplo, para cambiar los últimos dos elementos del arreglo a 5, puedes hacer lo siguiente:
arreglo_unidimensional[-2:] = 5
print("Arreglo después de modificar los últimos dos elementos:", arreglo_unidimensional)

# Tambien para mas de dos valores puedes hacer lo siguiente:
arreglo_unidimensional[0:3] = [1, 2, 3]  # Cambia los primeros tres elementos a 1, 2 y 3 respectivamente
print("Arreglo después de modificar los primeros tres elementos con una lista:", arreglo_unidimensional)
# igual se puede hacer sin necesidad de usar una lista, simplemente asignando un valor escalar a un rango de elementos:
arreglo_unidimensional[0:3] = 1,2,3
print("Arreglo después de modificar los primeros tres elementos con valores escalares:", arreglo_unidimensional)


# OPERACIONES
# SUMA Y RESTA 
arreglo1 = np.array([1, 2, 3])
arreglo2 = np.array([4, 5, 6])
suma = arreglo1 + arreglo2  # Suma elemento por elemento
resta = arreglo1 - arreglo2  # Resta elemento por elemento
print("Suma de los arreglos:", suma)
print("Resta de los arreglos:", resta)

# Multiplicacion por escalar
escalar = 2
multiplicacion_escalar = arreglo1 * escalar  # Multiplica cada elemento del arreglo por el escalar
print("Multiplicación por escalar:", multiplicacion_escalar)

# Multiplicación elemento por elemento, los arreglos deben tener la misma forma para realizar esta operación. Si los arreglos tienen formas diferentes, se producirá un error. En este caso, ambos arreglos tienen la misma forma (3 elementos), por lo que la multiplicación elemento por elemento se realiza sin problemas.
z= arreglo1 * arreglo2  # Multiplica elemento por elemento (producto Hadamard)
print("Multiplicación de los arreglos (producto Hadamard):", z)


# PARA ESTAS PRIMERAS 4 OPERACIONES (SUMA, RESTA, MULTIPLICACION Y DIVISION EXISTEN LAS FUNCIONES UNIVERSALES DE NUMPY, QUE SON FUNCIONES OPTIMIZADAS PARA REALIZAR OPERACIONES ELEMENTO POR ELEMENTO EN ARREGLOS DE NUMPY. ESTAS FUNCIONES SON MÁS RÁPIDAS QUE LAS OPERACIONES DE PYTHON PURO Y SON LA FORMA RECOMENDADA DE REALIZAR ESTAS OPERACIONES EN ARREGLOS DE NUMPY.)
from numpy import add, subtract, multiply, divide
suma_funcion = add(arreglo1, arreglo2)  # Suma elemento por elemento utilizando la función universal add
resta_funcion = subtract(arreglo1, arreglo2)  # Resta elemento por elemento utilizando la función universal subtract
multiplicacion_funcion = multiply(arreglo1, arreglo2)  # Multiplica elemento por elemento utilizando la función universal multiply      
division_funcion = divide(arreglo1, arreglo2)  # Divide elemento por elemento utilizando la función universal divide
print("Suma de los arreglos utilizando la función universal add:", suma_funcion)
print("Resta de los arreglos utilizando la función universal subtract:", resta_funcion)
print("Multiplicación de los arreglos utilizando la función universal multiply:", multiplicacion_funcion)
print("División de los arreglos utilizando la función universal divide:", division_funcion)



# producto punto
producto_punto = np.dot(arreglo1, arreglo2)  # Calcula el producto punto de los dos arreglos
print("Producto punto de los arreglos:", producto_punto)


# division elemento por elemento
division = arreglo1 / arreglo2  # Divide elemento por elemento
print("División de los arreglos:", division)


# Sumar constante a cada elemento del arreglo
constante = 3
suma_constante = arreglo1 + constante  # Suma la constante a cada elemento del arreglo
print("Suma de una constante a cada elemento del arreglo:", suma_constante)

# Funciones universales
a = np.array([1, 2, 3])
#mean: Calcula el valor promedio de los elementos en el arreglo.
promedio = np.mean(a)
print("Promedio del arreglo:", promedio)

# max: Devuelve el valor máximo en el arreglo.
maximo = np.max(a)
print("Valor máximo del arreglo:", maximo)

# min: Devuelve el valor mínimo en el arreglo.
minimo = np.min(a)
print("Valor mínimo del arreglo:", minimo)

# std: Calcula la desviación estándar de los elementos en el arreglo, que es una medida de la dispersión de los datos.
desviacion_estandar = np.std(a)
print("Desviación estándar del arreglo:", desviacion_estandar)

# Acceder a pi y e
pi = np.pi  # Valor de pi
e = np.e    # Valor de e
print("Valor de pi:", pi)
print("Valor de e:", e)

# funciones trigonométricas
angulo = np.array([0, np.pi/4, np.pi/2])  # Arreglo de ángulos en radianes
seno = np.sin(angulo)  # Calcula el seno de cada ángulo
coseno = np.cos(angulo)
print("Seno de los ángulos:", seno)
print("Coseno de los ángulos:", coseno)

#linspace: Genera un arreglo de números igualmente espaciados entre un rango especificado. Por ejemplo, para generar 5 números entre 0 y 1, puedes hacer lo siguiente:
arreglo = np.linspace(0, 1, 5)  # Genera 5 números entre 0 y 1
print("Arreglo generado con linspace:", arreglo)


# GRAFICAR FUNCIONES DE PYTHON
import matplotlib.pyplot as plt
# Generar un arreglo de valores de x entre -10 y 10
x = np.linspace(-10, 10, 100)
y = np.sin(x)  # Calcular el seno de cada valor de x

# Crear un gráfico de la función seno
plt.plot(x, y)
plt.title("Gráfico de la función seno")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid()
plt.show()  # Mostrar el gráfico