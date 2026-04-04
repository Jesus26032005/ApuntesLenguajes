import numpy as np

# Los arreglos bidimensionales son matrices que tienen dos dimensiones, es decir, filas y columnas. En NumPy, puedes crear un arreglo bidimensional utilizando la función np.array() y pasando una lista de listas como argumento. Aquí tienes un ejemplo de cómo crear un arreglo bidimensional:

# Crear un arreglo bidimensional
arreglo_bidimensional = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Arreglo bidimensional:")
print(arreglo_bidimensional)

# Se puede obtener el metodo ndim para saber el numero de dimensiones del arreglo, en este caso es 2 porque es un arreglo bidimensional.
print("Número de dimensiones del arreglo:", arreglo_bidimensional.ndim)

# Para acceder a los elementos de un arreglo bidimensional, puedes usar índices para especificar la fila y la columna. Por ejemplo, para acceder al elemento en la segunda fila y tercera columna, puedes hacer lo siguiente:
print("Elemento en la segunda fila y tercera columna:", arreglo_bidimensional[1, 2])  # Accede al elemento en la segunda fila (índice 1) y tercera columna (índice 2)

# COn shape puedes obtener las dimensiones del arreglo, en este caso es (3, 3) porque tiene 3 filas y 3 columnas.
print("Dimensiones del arreglo:", arreglo_bidimensional.shape)


# Con el atributo size puedes obtener el número total de elementos en el arreglo, en este caso es 9 porque hay 9 elementos en total (3 filas x 3 columnas).
print("Número total de elementos en el arreglo:", arreglo_bidimensional.size)

# Se puede acceder y modificar elementos específicos utilizando índices. Por ejemplo, para cambiar el elemento en la primera fila y segunda columna a 10, puedes hacer lo siguiente:
arreglo_bidimensional[0, 1] = 10
print("Arreglo después de modificar el elemento en la primera fila y segunda columna:")
print(arreglo_bidimensional)

# También puedes utilizar slicing para modificar un rango de elementos. Por ejemplo, para cambiar los elementos en la primera fila a 0, puedes hacer lo siguiente:
arreglo_bidimensional[0, :] = 0  # Cambia todos los elementos de la primera fila a 0
print("Arreglo después de modificar la primera fila:")
print(arreglo_bidimensional)

# para obtener un nuevo arreglo con una parte del arreglo original, puedes usar slicing. Por ejemplo, para obtener un nuevo arreglo con las dos primeras filas y las dos primeras columnas, puedes hacer lo siguiente:
nuevo_arreglo = arreglo_bidimensional[0:2, 0:2]  #
print("Nuevo arreglo creado con slicing:")
print(nuevo_arreglo)


# Operaciones 

# Se pueden realizar operaciones elementales como suma, resta, multiplicación y división entre arreglos bidimensionales. Por ejemplo, para sumar dos arreglos bidimensionales, puedes hacer lo siguiente:
arreglo1 = np.array([[1, 2], [3, 4]])
arreglo2 = np.array([[5, 6], [7, 8]])
suma = arreglo1 + arreglo2  # Suma elemento por elemento
print("Suma de los arreglos bidimensionales:")
print(suma)

resta = arreglo1 - arreglo2  # Resta elemento por elemento
print("Resta de los arreglos bidimensionales:")
print(resta)

multiplicacion = arreglo1 * arreglo2  # Multiplicación elemento por elemento
print("Multiplicación de los arreglos bidimensionales:")
print(multiplicacion)

division = arreglo1 / arreglo2  # División elemento por elemento
print("División de los arreglos bidimensionales:", division)

# También puedes realizar operaciones con un escalar. Por ejemplo, para multiplicar un arreglo bidimensional por un escalar, puedes hacer lo siguiente:
escalar = 2
multiplicacion_escalar = arreglo1 * escalar  # Multiplica cada elemento del arreglo
print("Multiplicación del arreglo bidimensional por un escalar:")
print(multiplicacion_escalar)

# Sumar un escalar a un arreglo bidimensional también es posible. Por ejemplo, para sumar 3 a cada elemento del arreglo, puedes hacer lo siguiente:
suma_escalar = arreglo1 + 3  # Suma 3 a cada elemento del arreglo
print("Suma de un escalar al arreglo bidimensional:", suma_escalar)

# También puedes realizar operaciones entre arreglos bidimensionales de diferentes formas, como la multiplicación de matrices utilizando la función np.dot() o el operador @. Por ejemplo, para multiplicar dos arreglos bidimensionales utilizando np.dot(), puedes hacer lo siguiente:
arreglo3 = np.array([[1, 2], [3, 4]])
arreglo4 = np.array([[5, 6], [7, 8]])
producto_matrices = np.dot(arreglo3, arreglo4)  # Multiplicación de matrices
print("Producto de matrices utilizando np.dot():")
print(producto_matrices)

# También puedes usar el operador @ para realizar la multiplicación de matrices de manera más concisa. Por ejemplo:
producto_matrices_operador = arreglo3 @ arreglo4  # Multiplicación de matrices utilizando el operador @
print("Producto de matrices utilizando el operador @:")
print(producto_matrices_operador)
# tambien se puede usar la función np.matmul() para realizar la multiplicación de matrices. Por ejemplo:
producto_matrices_matmul = np.matmul(arreglo3, arreglo4)  # Multiplicación de matrices utilizando np.matmul()
print("Producto de matrices utilizando np.matmul():")
print(producto_matrices_matmul)

# Recordemos que para realizar la multiplicación de matrices, el número de columnas del primer arreglo debe ser igual al número de filas del segundo arreglo. En este caso, ambos arreglos tienen la forma (2, 2), por lo que la multiplicación de matrices se realiza sin problemas.

# Para obtener la transpuesta de un arreglo bidimensional, puedes usar el atributo .T. Por ejemplo, para obtener la transpuesta del arreglo3, puedes hacer lo siguiente:
transpuesta = arreglo3.T  # Transpuesta del arreglo3
print("Transpuesta del arreglo3:")
print(transpuesta)


# FUncion reshape para cambiar la forma de un arreglo bidimensional. Por ejemplo, para cambiar la forma del arreglo3 a (4, 1), puedes hacer lo siguiente:
nuevo_arreglo_reshape = arreglo3.reshape(4, 1)  # Cambia la forma del arreglo3 a (4, 1)
print("Nuevo arreglo con forma (4, 1) utilizando reshape:")
print(nuevo_arreglo_reshape)