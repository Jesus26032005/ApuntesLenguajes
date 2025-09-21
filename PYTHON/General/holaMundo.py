#hola mundo
print("hola mundo")

#Declaracion de variables
variable= 5

#formateo de cadenas
print(f'el valor de la variable es {variable}')
print("hola {}".format(variable))
cadena = "hola mundo"

# Operaciones con cadenas
print(cadena)
print(cadena.upper())       # Convertir a mayúsculas
print(cadena.lower())       # Convertir a minúsculas
print(cadena.split())       # Dividir en palabras
print(cadena.split(" "))     # Dividir en palabras usando un separador específico
print(len(cadena))          # Longitud de la cadena
print(cadena[0:4])     # Subcadena (primeros 4 caracteres)
print(cadena[-5:])         # Subcadena (últimos 5 caracteres)
print(cadena.replace("mundo", "Python"))  # Reemplazar "mundo" por "Python"
print(cadena.startswith("hola"))  # Verificar si comienza con "hola"
print(cadena.endswith("mundo"))  # Verificar si termina con "mundo"
print(cadena.find("mundo"))  # Encontrar la posición de "mundo"
print(cadena.strip())  # Eliminar espacios al inicio y al final
print(cadena.split("o"))  # Dividir usando "o" como separador, si no se encuentra el separador usae el espacio como separador

#conversion tipo de datos
numero = 10
print(str(numero))  # Convertir a cadena
print(int("20"))    # Convertir de cadena a entero
print(float("3.14"))  # Convertir de cadena a flotante
print(type(numero))  # Tipo de dato de la variable numero
print(type(str(numero)))  # Tipo de dato de la variable convertida a cadena
print(type(float("3.14")))  # Tipo de dato de la variable convertida a flotante
print(type(int("20")))  # Tipo de dato de la variable convertida a entero

# Comentarios en Python
# todo valor ingresado es un string, por eso es necesario el casteo de datos 
numero= input("Ingrese un numero: ")  # Solicitar entrada al usuario
print(f'El numero ingresado es: {numero}')  # Imprimir el numero ingresado
numero = int(numero)  # Convertir la entrada a entero

# Sentencias de desicion
if numero > 10:             # Operador de comparacion if
    print("El numero es mayor que 10")
elif numero == 10:           # Operador de comparacion elif
    print("El numero es igual a 10")
else:              # Operador de comparacion else, aqui se tiene que anadir los dos puntos
    print("El numero es menor que 10")


print("Mayor de edad") if numero >= 18 else print("Menor de edad")  # Operador ternario, permite en una sola linea hacer una condicion

match numero:  # Estructura de control match (similar a switch)
    case 0:
        print("El numero es cero")
    case 1:
        print("El numero es uno")
    case 2:
        print("El numero es dos")
    case _:
        print("El numero es mayor que dos o menor que cero")  # El guion bajo (_) actua como un comodin para cualquier otro caso, es el caso default

# Ciclos
while numero > 0:  # Ciclo while
    print(f'Numero actual: {numero}')
    numero -= 1

for i in range(5):  # Ciclo for, este empieza en 0 y termina en 4
    print(f' Vamos en la iteracion numero {i}')

controlFor=10
for valor in range (controlFor):  # Ciclo for con rango definido
    print(f'Iteracion numero {valor}')

nombre= "Zaddkiel de Jesus Martinez Alor"
for letra in nombre:  # Iterar sobre cada letra de una cadena
    print(letra)

# Listas
lista = [1, 2, 3, 4, 5] # Crear una lista
print(lista)  # Imprimir la lista
lista.append(6)  # Agregar un elemento al final de la lista
print(lista)  # Imprimir la lista actualizada
lista.remove(3)  # Eliminar un elemento de la lista
print(lista)  # Imprimir la lista actualizada
lista.insert(2, 10)  # Insertar un elemento en una posición específica
lista.extend([7, 8, 9])  # Agregar múltiples elementos al final de la lista
print(lista)  # Imprimir la lista actualizada
print(lista[0])  # Acceder al primer elemento de la lista
print(lista[-1])  # Acceder al último elemento de la lista
print(lista[1:4])  # Acceder a una sublista (elementos del índice 1 al 3)
print(len(lista))  # Longitud de la lista
print(lista.index(4))  # Encontrar el índice de un elemento en la lista
lista.sort()  # Ordenar la lista
print(lista)  # Imprimir la lista ordenada
lista.pop()  # Eliminar y retornar el último elemento de la lista, se puede añadir un índice para eliminar un elemento específico
print(lista)  # Imprimir la lista actualizada

# Tuplas
tupla = (1, 2, 3, 4, 5)  # Crear una tupla, son inmutables
print(tupla)  # Imprimir la tupla
print(tupla[0])  # Acceder al primer elemento de la tupla
print(tupla[-1])  # Acceder al último elemento de la tupla
print(tupla[1:4])  # Acceder a una subtupla (elementos del índice 1 al 3)
print(len(tupla))  # Longitud de la tupla
print(tupla.index(3))  # Encontrar el índice de un elemento en la tupla
print(tupla.count(2))  # Contar cuántas veces aparece un elemento en la tupla
print(tupla + (6, 7))  # Concatenar tuplas

# Conjuntos
conjunto = {1, 2, 3, 4, 5}  # Crear un conjunto, los conjuntos no permiten duplicados
print(conjunto)  # Imprimir el conjunto
print(3 in conjunto)  # Verificar si un elemento está en el conjunto
print(len(conjunto))  # Longitud del conjunto
print(conjunto.union({6, 7}))  # Unión de conjuntos
print(conjunto.intersection({3, 4, 5, 6}))  # Intersección de conjuntos
print(conjunto.difference({4, 5}))  # Diferencia de conjuntos
print(conjunto.add(6))  # Agregar un elemento al conjunto
print(conjunto.remove(2))  # Eliminar un elemento del conjunto, da error si el elemento no existe
conjunto.discard(3)  # Eliminar un elemento del conjunto sin error si no existe
print(conjunto)  # Imprimir el conjunto actualizado
print(conjunto.pop())  # Eliminar y retornar un elemento aleatorio del conjunto
print(conjunto)  # Imprimir el conjunto actualizado
conjunto.add(8)  # Agregar un elemento al conjunto
print(conjunto)  # Imprimir el conjunto actualizado
conjunto.update({9, 10})  # Actualizar el conjunto con múltiples elementos

# Diccionarios
diccionario = {
    "nombre": "Zaddkiel",
    "edad": 25,
    "lenguajes": ["Python", "JavaScript", "C++"]
}  # Crear un diccionario

print(diccionario)  # Imprimir el diccionario
print(diccionario["nombre"])  # Acceder al valor de una clave específica
print(diccionario.get("edad"))  # Obtener el valor de una clave con get
print(diccionario.get("direccion", "No disponible"))  # Obtener el valor de una clave con get y valor por defecto si no existe
print(diccionario.keys())  # Obtener las claves del diccionario
print(diccionario.values())  # Obtener los valores del diccionario
print(diccionario.items())  # Obtener los pares clave-valor del diccionario
diccionario["pais"] = "Mexico"  # Agregar una nueva clave-valor al diccionario
print(diccionario)  # Imprimir el diccionario actualizado
diccionario["edad"] = 26  # Actualizar el valor de una clave existente
print(diccionario)  # Imprimir el diccionario actualizado
diccionario.pop("lenguajes")  # Eliminar una clave-valor del diccionario
print(diccionario)  # Imprimir el diccionario actualizado
diccionario.clear()  # Limpiar el diccionario
print(diccionario)  # Imprimir el diccionario vacío

# Crear colecciones con funciones set(), list(), dict() y tuple()
cadenaAuxiliar= "Jesus Martinez Alor"
coleccion_lista = list((1, 2, 3, 4, 5))  # Crear una lista a partir de una tupla
coleccion_conjunto = set([1, 2, 3, 4, 5])  # Crear un conjunto a partir de una lista
coleccion_diccionario = dict(nombre="Zaddkiel", edad=25)  # Crear un diccionario a partir de pares clave-valor
coleccion_tupla = tuple((1, 2, 3, 4, 5))  # Crear una tupla a partir de una lista
coleccion_de_string= tuple(cadenaAuxiliar.split())  # Crear una tupla a partir de una cadena, separando por espacios
print(coleccion_lista)  # Imprimir la lista
print(coleccion_conjunto)  # Imprimir el conjunto
print(coleccion_diccionario)  # Imprimir el diccionario


# Funciones
def hola_mundo():  # Definir una función sin parámetros
    print("¡Hola, mundo!")  # Imprimir un mensaje

def saludar(nombre):  # Definir una función que recibe un parámetro
    print("Hola, " + nombre + "!")

def sumar(a, b):  # Definir una función que recibe dos parámetros y retorna un valor
    return a + b  # Retornar la suma de los dos parámetros

hola_mundo()  # Llamar a la función sin parámetros
saludar("Zaddkiel")  # Llamar a la función con un parámetro
print(sumar(5, 10))  # Llamar a la función con dos parámetros y almacenar el resultado

def imprimir_mensaje(mensaje="¡Hola!".lower()):  # Definir una función con un parámetro con valor por defecto
    print(mensaje)  # Imprimir el mensaje

def imprimirNombres( nombre, apellido, edad=18):  # Definir una función con múltiples parámetros y uno con valor por defecto
    print(f'Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}')  # Imprimir los valores de los parámetros

imprimir_mensaje()  # Llamar a la función sin argumentos, usará el valor por defecto
imprimirNombres(nombre="Zaddkiel",  apellido="Martinez")  # Llamar a la funcion usando argumentos por nombre, ademas de default
imprimirNombres(apellido="Martinez", nombre="Zaddkiel", edad=25)  # Llamar a la funcion usando argumentos por nombre en diferente orden

def retornarTupla():
    return (1, 2, 3)  # Retornar una tupla
def otraFormaRetornarTupla():
    return 4, 5, 6  # Retornar una tupla sin paréntesis

resultado = retornarTupla()  # Llamar a la función y almacenar el resultado
print(resultado)  # Imprimir el resultado de la función
numero3, numero4, numero5 = otraFormaRetornarTupla()  # Llamar a la función y almacenar el resultado
print(numero3, numero4, numero5)  # Imprimir el resultado de la función


def funcionConArgumentos(*args):  # Definir una función que acepta un número variable de argumentos
    for arg in args:  # Iterar sobre los argumentos
        print(arg)  # Imprimir cada argumento
funcionConArgumentos(1, 2, 3, "Hola", True)  # Llamar a la función con múltiples argumentos, si se quiere pasar una colecion se tiene que desempaquetar

def funcionConVariablesyNormales( nombre, apellido, *hoovies): #Siempre se colocan los parámetros normales antes de los variables, los valores *hoovies son opcionales pero tambien una tupla
    print(f'Nombre: {nombre}, Apellido: {apellido}')  # Imprimir los valores de los parámetros
    for hoovie in hoovies:  # Iterar sobre los argumentos adicionales
        print(f'Hoovie: {hoovie}')  # Imprimir cada argumento adicional
funcionConVariablesyNormales("Zaddkiel", "Martinez", "Hoovie1", "Hoovie2", "Hoovie3")  # Llamar a la función con múltiples argumentos, si quieremos pasar un diccionario se tiene que desempaquetar usando **

def argumentosVariablesEnDiccionario(**kwargs):  # Definir una función que acepta un número variable de argumentos como diccionario
    for key, value in kwargs.items():  # Iterar sobre los pares clave-valor
        print(f'{key}: {value}')  # Imprimir cada par clave-valor
argumentosVariablesEnDiccionario(nombre="Zaddkiel", edad=25, ciudad="Mexico")  # Llamar a la función con múltiples argumentos como diccionario

def funcionConArgumentosYVariables(*args, **kwargs):  # Definir una función que acepta un número variable de argumentos y un diccionario
    print("Argumentos:", args)  # Imprimir los argumentos
    print("Palabras clave:", kwargs)  # Imprimir el diccionario de palabras clave
funcionConArgumentosYVariables(1, 2, 3, nombre="Zaddkiel", edad=25)  # Llamar a la función con múltiples argumentos y un diccionario

def funcionCompleta(nombre, apellido, edad=18, *args, **kwargs):  # Definir una función completa con múltiples parámetros
    print(f'Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}')  # Imprimir los valores de los parámetros
    print("Argumentos adicionales:", args)  # Imprimir los argumentos adicionales
    print("Palabras clave adicionales:", kwargs)  # Imprimir el diccionario de palabras clave adicionales
funcionCompleta("Zaddkiel", "Martinez", 25, "Hoovie1", "Hoovie2", ciudad="Mexico", pais="Mexico")  # Llamar a la función con múltiples argumentos y un diccionario

def funcionEspecifica(nombre: str, edad: int) -> str:  # Definir una función con tipos de datos específicos y un tipo de retorno, es opcional
    return f'Nombre: {nombre}, Edad: {edad}'  # Retornar una cadena formateada
print(funcionEspecifica("Zaddkiel", "jesus"))  # Llamar a la función con tipos de datos específicos

# Clases y Objetos
class Persona:
    # Atributo de clase (compartido por todas las instancias), estos atributos son comunes a todas las instancias de la clase, se puede siempre acceder a ellos con el nombre de la clase
    especie = "Humano"

    def __init__(self, nombre="", apellido="", edad=0): #Metodo constructor, que inicializa los atributos, en caso de que nom se agregen
        # Atributos de instancia (propios de cada objeto)
        #Estos atributos son únicos para cada instancia de la clase, se inicializan en el constructor __init__
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self._nombrePila = "Zaddkiel"      # Protegido
        self.__curp = "ZADJ850101HDFRRL09" # Privado

    def __str__(self): # Método especial para representar el objeto como cadena
        return f'Persona({self.nombre}, {self.apellido}, {self.edad})' #Se manda a llamar cuando se imprime el objeto

    def saludar(self): # Método de instancia
        print(f'Hola, soy {self.nombre} {self.apellido} y tengo {self.edad} años.')

    @classmethod # Decorador para definir un método de clase
    def cambiar_especie(cls, nueva_especie): # Método de clase para cambiar el atributo de clase, se usa cls para referirse a la clase misma
        cls.especie = nueva_especie

    @staticmethod # Decorador para definir un método estático
    def info_especie(): # Método estático que no depende de la instancia o clase, no requiere el argunebnto self o cls
        return "La especie de este objeto es Humano."

    """
    Característica	@staticmethod	@classmethod
    Primer parámetro	❌ No recibe ni self ni cls	||✅ Recibe cls (la clase)
    Acceso a atributos	❌ No puede acceder a la clase ni instancia	||✅ Puede acceder a atributos de clase
    Para qué sirve	Función que no depende de la clase ni instancia	||Función que trabaja con la clase como argumento
    ¿Crea instancias?	❌ No	✅ Usualmente sí (método factory)
    """
    """
    @staticmethod → para funciones utilitarias
    Sirve para definir funciones que no necesitan saber nada de la clase ni de sus objetos, pero que lógicamente pertenecen a la clase porque están relacionadas con ella.
    
    @classmethod → para trabajar con la clase como objeto
    Sirve cuando quieres acceder o modificar atributos de clase, o cuando necesitas una forma alternativa de crear instancias (constructor alternativo o factory method).
    """

    @property # Decorador para acceder al atributo privado como si fuera público 
    def curp(self): #El nombre del método debe ser el mismo que el atributo privado
        return self.__curp

    @curp.setter # Decorador para permitir modificar el atributo privado
    def curp(self, curp): #Esto se usa para que se pueda modificar el atributo privado
        self.__curp = curp

    @property # Decorador para acceder al atributo protegido como si fuera público
    def nombrePila(self): #El nombre del método debe ser el mismo que el atributo protegido
        return self._nombrePila

    @nombrePila.setter # Decorador para permitir modificar el atributo protegido
    def nombrePila(self, nombrePila):
        self._nombrePila = nombrePila

    """""
    El encapsulamiento es uno de los pilares fundamentales de la programación orientada a objetos (POO). 
    Su propósito principal es proteger y ocultar los datos internos de un objeto para evitar que otras partes del programa 
    accedan o los modifiquen directamente de forma indebida. En lugar de acceder directamente a los atributos de un objeto, 
    el encapsulamiento promueve el uso de métodos específicos (getters y setters) que controlan cómo se obtiene o modifica 
    la información. Esto permite tener un mayor control sobre el comportamiento interno de las clases, facilita el mantenimiento 
    del código y mejora la seguridad lógica del programa.
    En lenguajes como Java o C++, existen modificadores de acceso como public, private y protected que determinan explícitamente 
    el nivel de acceso permitido para los atributos y métodos. Sin embargo, en Python, el encapsulamiento se maneja de manera más 
    flexible a través de convenciones de nombres. Aunque no hay un mecanismo estricto para restringir el acceso, se utilizan guiones 
    bajos para indicar la intención del programador: un atributo que comienza con un guion bajo (_atributo) indica que no debe ser 
    accedido desde fuera de la clase (es decir, es "protegido"), y si empieza con doble guion bajo (__atributo), Python realiza un
    proceso llamado name mangling para hacer más difícil su acceso directo, lo que simula un atributo "privado".
    El encapsulamiento tiene varios beneficios clave. En primer lugar, ayuda a prevenir errores accidentales, ya que limita el 
    acceso directo a los datos sensibles del objeto. En segundo lugar, favorece la modularidad, permitiendo que el funcionamiento 
    interno de una clase pueda cambiar sin afectar a otras partes del programa, siempre y cuando su interfaz pública se mantenga. 
    También refuerza la lógica del programa, asegurando que ciertas reglas o validaciones se apliquen cada vez que se interactúe con
    los datos del objeto, algo que no es posible si se accede directamente a sus atributos.
    En Python, el encapsulamiento se puede complementar con el uso de propiedades mediante los decoradores @property y @setter. 
    Esto permite definir un comportamiento personalizado al acceder o modificar un atributo, como por ejemplo realizar validaciones, cálculos o emitir advertencias. Aunque a primera vista el acceso parece directo (obj.atributo), internamente se está utilizando un método, lo que conserva la seguridad y flexibilidad del diseño orientado a objetos.
    """

    
# Ejemplo de uso:
persona1 = Persona("Victor", "Hugo", 30)
persona2 = Persona("Zaddkiel", "Martinez", 25)

print(persona1.especie)  # Acceso al atributo de clase
print(persona2.especie)  # Acceso al atributo de clase

persona1.saludar()
persona2.saludar()

# Cambiar el atributo de clase
Persona.especie = "Homo Sapiens"
print(persona1.especie)
print(persona2.especie)

#Agregar atributos dinamicos
setattr(persona1, "nacionalidad", "Mexicana") #Solo se anade el atrbuto a dicha instancia
setattr(persona2, "nacionalidad", "Estadounidense")

persona1.cambiar_especie("Homo Sapiens")
print(persona1.especie)

# Herencia, individual y multiple
class animal:
    def __init__(self, nombre= "", edad=0):
        self.edad = edad
        self.nombre = nombre
    def hacerRuido(self):
        print("El animal hace un ruido.")

class serVivo:
    def __init__(self, planeta=""):
        self.planeta = planeta

class perro(animal, serVivo): #Se agrega entre parentesis la clase de donde se heredara
    def __init__(self, nombre="", edad=0, planeta="", raza=""):
        self.raza = raza
        animal.__init__(self,nombre, edad)  #Siempre pasar self como primer parametro de inicializador
        serVivo.__init__(self,planeta)   #Se hace la inicialiacion de cada clase de la que se hereda
                            #El polimorfismo consiste en que un mismo método puede tener diferentes implementaciones 
    def hacerRuido(self):   #La sobreescritura consiste en redefinir el comportamiento de la clase padre
        print("El perro ladra.")

perro1 = perro("Rex", 5, "Tierra", "Pastor Alemán")
perro1.hacerRuido()
print(perro1.planeta)







# Method resolution order (MRO)
print(perro.__mro__)  # Mostrar el orden de resolución de métodos (MRO) para la clase perro, que indica el orden en que se buscarán
print(perro.mro())                        # los métodos y atributos en la jerarquía de herencia, asi como el orden en que se ejecutarán si mandamos a
                        # llamar metodos de mismo nombre o cosas asi.
# MRO es importante porque define el orden en que se buscarán los métodos y atributos en la jerarquía de herencia.
# Esto es especialmente útil en casos de herencia múltiple, donde una clase puede heredar de múltiples clases base.
# El MRO garantiza que se sigan ciertas reglas para evitar ambigüedades y conflictos en la resolución de métodos.
# En Python, el MRO se puede consultar utilizando el atributo __mro__ de una clase, que devuelve una tupla con el orden de las clases en la jerarquía de herencia

class a: 
    @staticmethod  # Decorador para definir un método estático
    def hello():
        print("Hello from class a")
class b: 
    @staticmethod  # Decorador para definir un método estático
    def hello():
        print("Hello from class b")
class c(a):
    @staticmethod  # Decorador para definir un método estático
    def hello():
        print("Hello from class c")
class d(b, c):  # Herencia múltiple
    pass

D = d()
D.hello()  # Llamar al método estático de la clase d
print(d.__mro__)  # Mostrar el orden de resolución de métodos (MRO) para la clase d

# Clases abstractas
from abc import ABC, abstractmethod  # Importar la clase base abstracta y el decorador abstractmethod
class Animal(ABC):  # Definir una clase abstracta que hereda de ABC, para quen esta sea una clase abstracta
    @abstractmethod  # Decorador para definir un método abstracto
    def hacerRuido(self):  # Método abstracto que debe ser implementado por las subclases
        pass
class Gato(Animal):  # Definir una subclase que hereda de la clase abstracta Animal
    pass

try:
    gato = Gato()  # Intentar crear una instancia de la clase Gato
except TypeError as e:
    print(f"Error: {e}")
# Esto generará un error porque Gato no implementa el método abstracto hacerRuido

class Perro(Animal):  # Definir una subclase que hereda de la clase abstracta Animal
    def hacerRuido(self):  # Implementar el método abstracto
        print("El perro ladra.")
try:
    perro = Perro()  # Crear una instancia de la clase Perro
    perro.hacerRuido()  # Llamar al método hacerRuido
except TypeError as e:
    print(f"Error: {e}")
# Esto no generará un error porque Perro implementa el método abstracto hacerRuido


#Sobre carga de operadores
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):  # Sobrecarga del operador +       #Otro objeto debe ser de la misma clase
        return Punto(self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro):  # Sobrecarga del operador -
        return Punto(self.x - otro.x, self.y - otro.y)

    def __mul__(self, escalar):  # Sobrecarga del operador *
        return Punto(self.x * escalar, self.y * escalar)
    def __truediv__(self, escalar):  # Sobrecarga del operador /
        if escalar == 0:
            raise ValueError("No se puede dividir por cero")
        return Punto(self.x / escalar, self.y / escalar)
    
    def __eq__(self, otro):  # Sobrecarga del operador ==
        return self.x == otro.x and self.y == otro.y

    def __lt__(self, otro):  # Sobrecarga del operador <
        return (self.x, self.y) < (otro.x, otro.y)
    
    def __le__(self, otro):  # Sobrecarga del operador <=
        return (self.x, self.y) <= (otro.x, otro.y)
    def __gt__(self, otro):  # Sobrecarga del operador >
        return (self.x, self.y) > (otro.x, otro.y)
    def __ge__(self, otro):  # Sobrecarga del operador >=
        return (self.x, self.y) >= (otro.x, otro.y)
    def __str__(self):  # Método para representar el objeto como cadena
        return f'Punto({self.x}, {self.y})'
    
class Persona1:
    def __init__(self):
        self.nombre = "Zaddkiel"
        self.edad = 25
    
    def __add__(self, otro):
        return f'{self.nombre} y {otro.nombre} son amigos.' #Se pueden usar los atributos de la clase para realizar operaciones
    
    def __sub__(self, otro):
        return f'{self.nombre} y {otro.nombre} no son amigos.' #Se configura el comportamiento del operador de resta
    
persona5 = Persona1()
persona6 = Persona1()
print(persona5 + persona6)  # Llamar al método __add__
print(persona5 - persona6)  # Llamar al método __sub__

punto1 = Punto(2, 3)  # Crear una instancia de la clase Punto
punto2 = Punto(4, 5)  # Crear otra instancia de la clase
print(punto1 + punto2)  # Llamar al método __add__ para sumar dos puntos
print(punto1 - punto2)  # Llamar al método __sub__ para restar dos puntos
print(punto1 * 2)  # Llamar al método __mul__ para multiplicar un punto por un escalar

variable1 = "XD"

# Manejo de excepciones
try:
    print(variable1 / 0)  # Intentar dividir por cero, esto generará un ValueError
except ZeroDivisionError as e:  # Capturar la excepción de división por cero, mediante el objeto de tipo ZeroDivisionError
    print("No se puede dividir por cero:")
except TypeError as e:  #Se pueden capturar otros tipos de excepciones, como TypeError si se intenta dividir un string por un número
    print(f"Error: {e}")
except Exception as e:  # Capturar cualquier otra excepción que no haya sido manejada anteriormente, generalmente se colocan las excepciones más específicas primero
    # y posteriormente las más generales como Exception
    print(f"Se produjo un error inesperado: {e}")
else:  # El bloque else se ejecuta si no ocurre ninguna excepción en el bloque try
    print("La operación se realizó correctamente")
finally:  # El bloque finally se ejecuta siempre, independientemente de si ocurrió una excepción o no
    print("Fin del manejo de excepciones")
#La forma en que se colocan los bloques try, except, else y finally es importante para el manejo adecuado de excepciones en Python.
# El bloque try contiene el código que puede generar una excepción.

# Execepciones personalizadas
class MiExcepcion(Exception):  # Definir una excepción personalizada que hereda de alguna de las excepciones base de Python, generalmente de Exception
    def __init__(self, mensaje, codigo): #El mensaje se puede personalizar o se puede dejar como para recibir un mensaje por defecto
        super().__init__(mensaje)
        self.codigo = codigo  # Atributo adicional para almacenar un código de error

def funcion_con_error():
    raise MiExcepcion("Este es un error personalizado", 404)  # la palabra raise se usa para lanzar una excepción, en este caso la personalizada MiExcepcion

try:
    funcion_con_error()  # Intentar llamar a la función que genera un error
    #Tambien puede ser directamente raise MiExcepcion("Este es un error personalizado", 404)  # Lanzar la excepción personalizada directamente
except MiExcepcion as e:  # Capturar la excepción personalizada
    print(f"Se capturó una excepción personalizada: {e}")
    print(f"Código de error: {e.codigo}")


# Manejo de archivos

#uso de with para abrir archivo
#como open puede lanzar una excepción, es recomendable usar try y except
try:
    archivo = open("archivo.txt", "w+", encoding="utf-8")  # Abrir un archivo en modo lectura, encoding especifica la codificación del archivo
    #escritura
    archivo.write("hola we\n.")  # Escribir en el archivo
    archivo.write("Hola, mundo!\n")
    
    #redireccion
    archivo.seek(0)  # Mover el cursor al inicio del archivo para poder leerlo
    
    #lectura
    archivo.read(5)  # Leer los primeros 5 caracteres del archivo
    archivo.readline()  # Leer una línea del archivo 
    archivo.readlines()  # Leer todas las líneas del archivo y devolverlas como una lista
    contenido=archivo.read()  # Leer todo el contenido del archivo

    #iterar archivo
    for linea in archivo:
        print(linea)

    print(contenido)  # Imprimir el contenido del archivo
    archivo.close()  # Cerrar el archivo
except FileNotFoundError as e:  # Capturar la excepción si el archivo no existe
    print("El archivo no fue encontrado.")
except IOError as e:  # Capturar la excepción si hay un error de entrada/salida
    print(f"Error al leer el archivo: {e}")     
finally:  # El bloque finally se ejecuta siempre, independientemente de si ocurrió una excepción o no
    print("Fin del archivo")

#Uso de with, evita estar abriendo y cerrando el archivo
with open("archivo.txt", "r+", encoding="utf8") as archivo:
    archivo.write("hola we")
    archivo.seek(0)
    print(archivo.read())

# Uso de Context Manager 
class ManejoArchivos:
    def __init__(self, nombreArchivo):
        self.nombreArchivo= nombreArchivo   
    
    def __enter__(self):
        print("Entrando al recurso")
        self.nombreArchivo = open(self.nombreArchivo, "r", encoding="utf8")
        return self.nombreArchivo
    
    def __exit__(self, tipoExepcion, valorExcepcion, trazaError):
        print("Cerramos el recurso")
        if self.nombreArchivo:
            self.nombreArchivo.close()

with ManejoArchivos("prueba.txt") as archivo:
    print("entre al archivo")