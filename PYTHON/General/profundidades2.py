#FUNCION Zip
#Permite combinar dos o más iterables (listas, tuplas, etc.) en un solo iterable de tuplas.
lista1 = [1, 2, 3]
lista2 = [4,5,6,10,20]
# La sintaxis de zip es:
# zip(iterable1, iterable2, ...), que devuelve un objeto zip. Cada elemento del objeto zip es una tupla que contiene un elemento de cada iterable. Siendo que el número de elementos en el objeto zip es igual al número de elementos del iterable más corto.
# Si los iterables tienen diferentes longitudes, zip se detiene cuando el más corto se agota.
resultado = zip(lista1, lista2)
print(resultado)  # Muestra un objeto zip
# Para ver el contenido, se puede convertir a una lista o iterar sobre él.
print(list(resultado))  # Muestra el contenido como una lista de tuplas
# Una vez que se ha convertido a una lista, el objeto zip ya no se puede reutilizar, ya que se agota al ser iterado. Por lo tanto, si se quiere reutilizar, se debe crear de nuevo.


#Ireración con zip
# Se puede usar zip en un bucle for para iterar sobre varios iterables al mismo tiempo, en paralelo
for a,b in zip(lista1, lista2):
    print(a, b)  # Imprime los elementos de ambas listas en paralelo

# Si se quiere iterar sobre listas de diferentes longitudes, zip solo tomará hasta el más corto
# Por ejemplo, si lista1 tiene 3 elementos y lista2 tiene 5, solo se iterará sobre los primeros 3 elementos de lista2

# Crearlista con zip y iteración
# Se puede crear una nueva lista combinando elementos de varias listas usando zip
nuevaLista=[]
for a, b in zip(lista1, lista2):
    nuevaLista.append(f'{a}-{b}')  # Agrega una tupla con los elementos de ambas listas
print(nuevaLista)  # Muestra la nueva lista con tuplas de elementos combinados


# Proceso unzip
# Para deshacer el zip, se puede usar la función zip con el operador de desempaquetado (*)
mezclaProcesada = [(1, 4), (2, 5), (3, 6)]
desempaquetada1, desempaquetada2 = zip(*mezclaProcesada) # Desempaqueta las tuplas en dos listas separadas, porque zip procesa cada tupla como un iterable
print(desempaquetada1)  # (1, 2, 3)
print(desempaquetada2)  # (4, 5, 6)


# Ordenar un zip
letras = ['c', 'd', 'b']
numeros = [3, 1, 2]
# Se puede ordenar un zip combinando los elementos de dos listas
mezcla= zip(letras, numeros)
# Ordenar el zip por la letra, lo que devuelve una lista de tuplas ordenadas por el primer iterable que se envio, o mejor dicjo tambien, el primer elemento de cada tupla
mezcla_ordenada = sorted(mezcla) # Si no se especifica una clave, se ordena por el primer elemento de cada tupla
# Mostrar el resultado
print(mezcla_ordenada)  # [('a', 1), ('b', 2), ('c', 3)]


# Crear un diccionario con zip
# Se puede crear un diccionario combinando dos listas con zip
# Por ejemplo, si se tiene una lista de claves y una lista de valores, se puede crear un diccionario donde cada clave se asocia a su valor correspondiente.
llaves = ['a', 'b', 'c']
valores = [1, 2, 3]
diccionario = dict(zip(llaves, valores))  # Crea un diccionario a partir de las listas
print(diccionario)  # {'a': 1, 'b': 2, 'c': 3}

# Actualizar un elemento en un diccionario con zip
# Si se quiere actualizar un elemento en un diccionario, se puede usar zip para combinar las claves y valores, y luego actualizar el diccionario con el nuevo valor.
llave= ['b']  #Se define la llave a actualizar como iterable, tiene que ser igual a la clave del diccionario ya que se busca y luego se sustituye el valor si es que existe sino se agrega como nuevo elemento
valor_nuevo = [10]  # Se define el nuevo valor
diccionario.update(zip(llave, valor_nuevo)) # Se actualiza ya que zip devuelve un iterable en forma de tupla, por lo que se puede usar directamente en el método update del diccionario pues este metodo espera un iterable o otro diccionario

# Listas por comprensión
# Una forma concisa y elegante de crear listas en Python, basada en un iterable y una expresión.
# ✅ ¿Qué es una lista por comprensión?
# Es una forma compacta y elegante de construir listas en una sola línea,
# basada en un iterable y una expresión.

# ---------------------------------------
# 📌 SINTAXIS BÁSICA
# [expresión for variable in iterable]
# ---------------------------------------

# 🎯 EJEMPLO 1: Elevar al cuadrado los números del 0 al 4

cuadrados = [i ** 2 for i in range(5)]
print("Cuadrados:", cuadrados)  # [0, 1, 4, 9, 16]

# 🎯 EJEMPLO 2: Crear una lista de pares del 0 al 9

pares = [i for i in range(10) if i % 2 == 0]
print("Pares:", pares)  # [0, 2, 4, 6, 8]

# 🎯 EJEMPLO 3: Aplicar condicional ternario dentro de la lista

valores = [i if i % 2 == 0 else -i for i in range(5)]
print("Condicional if-else:", valores)  # [0, -1, 2, -3, 4]

# 🎯 EJEMPLO 4: Transformar strings a mayúsculas

nombres = ["ana", "luis", "eva"]
nombres_mayus = [nombre.upper() for nombre in nombres]
print("Nombres en mayúsculas:", nombres_mayus)  # ['ANA', 'LUIS', 'EVA']

# 🎯 EJEMPLO 5: Combinar dos listas con zip

edades = [25, 30, 22]
combinados = [f"{n}-{e}" for n, e in zip(nombres, edades)]
print("Combinados:", combinados)  # ['ana-25', 'luis-30', 'eva-22']

# ---------------------------------------
# 🧠 ¿Por qué usar listas por comprensión?
# ---------------------------------------
# ✅ Más conciso que un bucle for tradicional
# ✅ Más legible cuando la transformación es simple
# ✅ Más rápido que usar append en un bucle

# 🎯 EJEMPLO 6: Equivalencia con bucle for

# Modo tradicional
cuadrados_tradicional = []
for i in range(5):
    cuadrados_tradicional.append(i ** 2)

# Modo con comprensión
cuadrados_comprension = [i ** 2 for i in range(5)]

print("¿Son iguales?", cuadrados_tradicional == cuadrados_comprension)  # True

# ---------------------------------------
# 💡 Nota: También existen sets y diccionarios por comprensión
# ---------------------------------------

# 🎯 Set por comprensión (elimina duplicados)
numeros = [1, 2, 2, 3, 3, 4]
conjunto = {x for x in numeros}
print("Set:", conjunto)  # {1, 2, 3, 4}

# 🎯 Diccionario por comprensión
claves = ["a", "b", "c"]
valores = [1, 2, 3]
diccionario = {k: v for k, v in zip(claves, valores)}
print("Diccionario:", diccionario)  # {'a': 1, 'b': 2, 'c': 3}


# PROFUNDIZANDO EN TUPLAS
# Las tuplas son colecciones inmutables de elementos, lo que significa que no se pueden modificar una vez creadas.

# Declarar variables con tuplas
a, b = 'hola', 'mundo'  # Asignación múltiple, esto porque se genere unpacking

# swap( intercambio de valores)
a, b = b, a  # Intercambia los valores de a y b, esto es posible porque las tuplas son inmutables y se pueden desempaquetar directamente en variables

# Regresar multiples valores desde una función
def sumar_y_restar(x, y):
    return x + y, x - y  # Devuelve una tupla con la suma y la resta
resultado_suma, resultado_resta = sumar_y_restar(10, 5)  # Desempaqueta los resultados en dos variables porque se devuelve una tupla

# Regresar la suma de una tupla
resultado = sum((1, 2, 3, 4))  # Suma los elementos de la tupla
print(resultado)  # 10

# PROFUNDIZANDO EN SETS
# Los sets son colecciones desordenadas de elementos únicos, lo que significa que no pueden contener duplicados y no tienen un orden específico.

# Crear un set, un set solo puede contener elementos únicos, por lo que si se intenta agregar un elemento duplicado, no se añadirá y mandara un mensaje de error
mi_set = {1, 2, 3, 4, 5}
#mi_set = {[1,2]} # Esto no es válido, ya que los sets no pueden contener listas u otros sets mutables

# Generar un set vacío
mi_set_vacio = set()  # Crea un set vacío, se debe usar set() para crear un set vacío, no se puede usar {} porque eso crea un diccionario vacío

# Generar un set a partir de una lista
lista = [1, 2, 2, 3, 4, 5]
mi_set_desde_lista = set(lista)  # Convierte la lista en un set, eliminando duplicados

# Agregar elementos a un set
mi_set.add(6)  # Agrega un elemento al set, si ya existe no se añadirá
mi_set.update([7, 8])  # Agrega varios elementos al set, si ya existen no se añadiran, estos se tienen que añadir en forma de un iterable ya sea lista, tupla o otro set

# Eliminar elementos de un set
mi_set.remove(2)  # Elimina un elemento del set, si no existe lanzará un KeyError
mi_set.discard(3)  # Elimina un elemento del set, si no existe no lanzará un error
mi_set.pop()  # Elimina y devuelve un elemento aleatorio del set, si el set está vacío lanzará un KeyError

# Crear un set a partir de un iterable
iterable = range(10)  # Un iterable de números del 0 al 9
iterable_set = set(iterable)  # Convierte el iterable en un set, eliminando duplicados

# Copiar un set
mi_set_copia = mi_set.copy()  # Crea una copia superficial del set, usando el método copy(), es decir, se crea un nuevo set con los mismos elementos, es decir se hace una copia totlalmente con direccion de memoria diferente para todo

#Operaciones algebraicas con sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union = set_a | set_b  # Unión, lo que hace es unir los elementos de ambos sets
interseccion = set_a & set_b  # Intersección, obtiene los elementos comunes
diferencia = set_a - set_b  # Diferencia, obtiene los elementos de set_a que no están en set_b
diferenciaSimetrica = set_a ^ set_b  # Diferencia simétrica, obtiene los elementos que están en uno de los sets pero no en ambos
print("Unión:", union)
print("Intersección:", interseccion)
print("Diferencia:", diferencia)
print("Diferencia Simétrica:", diferenciaSimetrica)

#Tambien se pueden realizar usando las funciones respectivas que vienen por de
union = set_a.union(set_b) # Une los elementos de ambos set
interseccion = set_a.intersection(set_b) #Une los elementos que se repiten en ambos set
diferencia = set_a.difference(set_b) #  Obtiene los elementos del set inicial que no esten en el segundo
diferenciaSimetrica = set_a.symmetric_difference(set_b) #Une los elemementos que esten no en ambos sets
print("Unión:", union)
print("Intersección:", interseccion)
print("Diferencia:", diferencia)
print("Diferencia Simétrica:", diferenciaSimetrica)

# Funciones para preguntar subconjunto, superconjunto, desigualdad(disjoin, dos conjuntos sin nada en comun)
print("¿Es subconjunto?", set_a.issubset(set_b)) # Devuelve un valor de true si los elementos del set_a están en set_b
print("¿Es superconjunto?", set_a.issuperset(set_b)) # Devuelve un valor de true si los elementos del set_b están en set_a
print("¿Es desigualdad?", set_a.isdisjoint(set_b)) # Devuelve un valor de true si no hay elementos en común entre los dos sets

# Profundizando en diccionarios
#Los diccionarios guardan un orden ( a diferencia de los conjuntos)
diccionario= {'Nombre': 'Zadd', 'Apellido': 'Martinez'}
print(diccionario)

#Los diccionarios son mutables pero las llaves deben de ser inmutables por lo tanto no se pueden usar elementos como las listas o diccionarios pues no se pueden modificar
diccionario= {(1,2): 'Valor1'}
#diccionario[1: 'numero'] el numero es mutable por lo tanto no se puede usar como llave
print(diccionario)

#Se agrega una llave si no se encuentra un valor, es decir se añade en automatico la clave y valor, si se encuentra solo se actualiza el valor
diccionario["email"] = 'Zaddkielma@gmail.com'
print(diccionario)

#No hay valores duplicados en la llaves de un diccionario, si ya existen se reemplaza
diccionario["email"] = 'jesus@gmail.com'
print(diccionario)

# Recuperar un valor indicando una llave
#La primera forma es entre corchetes indicar la llave, si no encuentra el valor devuelve una excepcion
print(diccionario["email"]) 
#La segunda es usando get , la cual tiene como argumentos la llave y un valor por defecto si es que no se encuentra, por default dicho valor es None
print(diccionario.get("email", "No encontrado"))

# Metodo setdefault, este metodo busca la llave y si no la encuentra la crea con un valor por defecto, su sintaxis seria la siguiente setdefault(clave, valor), devuelve el valor de la llave
print(diccionario.setdefault("telefono", "No disponible"))
print(diccionario)

#Forma de imprimir un diccionario usando pprint del modulo pprint, sus sintaxis es la siguiente: pprint(diccionario)
from pprint import pprint
pprint(diccionario, sort_dicts=True, indent=4, width=80, depth=None, compact=False)
# La sintaxis de pprint es la siguiente: pprint(objeto, sort_dicts=False, indent=1, width=80, depth=None, compact=False) dichos argumentos hacen lo siguiente
# sort_dicts: Si se establece en True, los diccionarios se ordenan por clave antes de ser impresos.
# indent: Establece el número de espacios para la indentación de cada nivel.
# width: Establece el ancho máximo de la salida. Si se supera, se realiza un ajuste de línea.
# depth: Limita la profundidad de la impresión. Si se supera, se imprime '...' en su lugar.
# compact: Si se establece en True, se utiliza una representación más compacta de los objetos.