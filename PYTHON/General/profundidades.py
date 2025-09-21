#Profundizando en sistemas de enumeracion
#Decimal, se coloca de forma normal
import math


a= 10
#Octal
b= 0o10 #, se debe poner un 0 antes del numero en forma octal
#Hexadecimal
c= 0x10 #, se debe poner un 0x antes del numero en forma hexadecimal
#Binario
d= 0b10 #, se debe poner un 0b antes del numero en forma binaria
#Imprimiendo los valores
print(f"Decimal: {a}, Octal: {b}, Hexadecimal: {c}, Binario: {d}")

#Conversion base numerica usando constuctor int(), donde se puede especificar la base pues su forma es int(valor, base)
#Nota: si no se especifica la base, por defecto se toma como decimal, ademas valor es el valor a convertir a partir de su base
a= int("10") #Decimal
b= int("11", 8) #Octal, el 8 indica que el numero es octal
c= int("F", 16) #Hexadecimal, el 16 indica que el numero es hexadecimal
d= int("01", 2) #Binario, el 2 indica que el numero es binario
print(f"Decimal: {a}, Octal: {b}, Hexadecimal: {c}, Binario: {d}")

#Profundizando en tipo float
#Decimal, se coloca de forma normal
a= 10.5
#limitar el numero de decimales
b= 10.12345678901234567890
print(f"Decimal: {a}, Limite de decimales: {b:.2f}") #, se limita a 2 decimales, se pueden cambiar los decimales a mostrar,la sintaxis seria {variable:.número de decimalesf}
#Conversion de int y str a float, se puede usar el constructor float() de la siguiente manera float(valor)
a= float(10) #, convierte un entero a float
b= float("10.5") #, convierte un string a float
print(f"Float de int: {a}, Float de str: {b}")
#Notacion exponencial, se puede usar la letra e o E para indicar la potencia de 10
e= 1.5e10 #, equivale a 1.5 * 10^10
f= 1.5E10 #, equivale a 1.5 * 10^10
l= 1.5e-3 #, equivale a 1.5 * 10^-3
print(f"Notacion exponencial: {e}, {f}, {l}")
#Nota cualquier calculo que involucra un float, el resultado sera un float, por ejemplo:
resultado= 10 + 10.5 #, el resultado sera un float
print(f"Resultado de la suma: {resultado}")

#Valores infinitos
# Se puede usar el constructor float() con la cadena "inf" o "-inf" para obtener un valor infinito positivo o negativo
positivoInfinito = float("inf")  # Infinito positivo
negativoInfinito = float("-inf")  # Infinito negativo
print(f"Positivo infinito: {positivoInfinito}, Negativo infinito: {negativoInfinito}") #Aqui se imprimen los valores infinitos
print(f'Es infinitito?: {math.isinf(positivoInfinito)}, {math.isinf(negativoInfinito)}')  #, se usa la funcion isinf() del modulo math para verificar si un numero es infinito

#Otra forma de crear un valor infinito es usando el modulo math
positivoInfinito = math.inf  # Infinito positivo
negativoInfinito = -math.inf  # Infinito negativo
print(f"Positivo infinito: {positivoInfinito}, Negativo infinito: {negativoInfinito}")  # Aqui se imprimen los valores infinitos
print(f'Es infinitito?: {math.isinf(positivoInfinito)}, {math.isinf(negativoInfinito)}')  #, se usa la funcion isinf() del modulo math para verificar si un numero es infinito

#Otra forma de crear un valor infinito es usando el modulo decimal
from decimal import Decimal
positivoInfinito = Decimal('Infinity')  # Infinito positivo
negativoInfinito = Decimal('-Infinity')  # Infinito negativo
print(f"Positivo infinito: {positivoInfinito}, Negativo infinito: {negativoInfinito}")  # Aqui se imprimen los valores infinitos
print(f'Es infinitito?: {math.isinf(positivoInfinito)}, {math.isinf(negativoInfinito)}')  #, se usa la funcion isinf() del modulo math para verificar si un numero es infinito

#Tipo NaN (Not a Number), puede ser el resultado de una operacion invalida, como dividir 0 entre 0 o tomar la raiz cuadrada de un numero negativo, como tambien resultado de operaciones que no tienen sentido matematico como con infinito, es un tipo de dato numerico especial que representa un valor indefinido o no representable.

# Se puede usar el constructor float() con la cadena "nan" o "NaN" para obtener un valor NaN
nanValue = float("nan") 
print(f"NaN Value: {nanValue}")  # Aqui se imprime el valor NaN
print(f'Es NaN?: {math.isnan(nanValue)}')  #, se usa la funcion isnan() del modulo math para verificar si un numero es NaN
#Otra forma de crear un valor NaN es usando el modulo math y tambien el modulo decimal
nanValue = math.nan  # NaN
nanValueDecimal = Decimal('NaN')  # NaN

#Profundizando en el tipo bool
#El tipo bool es un tipo de dato que puede tener dos valores: True o False, se usa para representar valores booleanos, como el resultado de una comparacion o una condicion.
#El valor de 0, cadenas vacias y None se consideran False, mientras que cualquier otro valor se considera True.
#Para crear un valor booleano, se puede usar el constructor bool() de la siguiente manera bool(valor), donde valor es el valor a convertir a booleano.
print(f"True: {True}, False: {False}")  #, se imprimen los valores booleanos
print(f"1 es True?: {bool(1)}")  #, 1 es True
print(f"0 es False?: {bool(0)}")  #, 0 es False
print(f"Cadena vacia es False?: {bool('')}")  #, cadena vacia es False
print(f"None es False?: {bool(None)}")  #, None es False
print(f"Lista vacia es False?: {bool([])}")  #, lista vacia es False
print(f"Diccionario vacio es False?: {bool({})}")  #, diccionario vacio es False
print(f"Tupla vacia es False?: {bool(())}")  #, tupla vacia es False
print(f"Set vacio es False?: {bool(set())}")  #, set vacio es False

#Sentencias de control con booleanos
#Las sentencias de control como if, while y for usan valores booleanos para determinar el flujo de ejecucion del programa.
#Por ejemplo, en una sentencia if, si la condicion es True, se ejecuta el bloque de codigo dentro del if, de lo contrario, se omite. Cuando se usa un valor que no es booleano en una sentencia de control, Python lo convierte automaticamente a un valor booleano usando las reglas mencionadas anteriormente.
x = 10
if x:  #, x es True porque es diferente de 0
    print("x es True")
else:
    print("x es False")
y = 5
while y:
    print("y es True")
    y -= 1  #, se decrementa y para evitar un bucle infinito
for i in "golang":  #, la cadena "golang" es True porque no es una cadena vacia
    print(i)


# Manejo de cadenas
# Concatenacion de cadenas, forma 1
cadena1 = "Hola"
cadena2 = "Mundo"
cadena_concatenada = cadena1 + " " + cadena2  #, se concatenan las cadenas con un espacio entre ellas
print(f"Cadenas concatenadas: {cadena_concatenada}")

# Concatenacion de cadenas, forma 2
cadena_concatenada = f"{cadena1} {cadena2}"  #, se usa f-string para concatenar las cadenas
print(f"Cadenas concatenadas con f-string: {cadena_concatenada}")

# Concatenacion de cadenas, forma 3, separadas por espacios
cadena_concatenada = "hola" "mundo" + "variable"  #Se pueden concatenar cadenas sin usar el operador +, solo separandolas por espacios sin embargo si hay variables involucradas, se debe usar el operador +
print(f"Cadenas concatenadas sin operador +: {cadena_concatenada}")

# Concatenacion de cadenas, forma 4, usando join
lista_cadenas = ["Hola", "Mundo", "Python"]
cadena_concatenada = " ".join(lista_cadenas)  #, se usa el metodo join() para concatenar las cadenas de una lista con un espacio entre ellas

# Metodo help, el metodo help() se usa para obtener informacion sobre un objeto, metodo o atributo en python
#help(cadena_concatenada)  #, se usa el metodo help() para obtener información sobre la cadena concatenada
#help(str)

# Uso de docstrings, los docstrings son cadenas de documentacion que se usan para documentar funciones, clases y modulos en python, se colocan al inicio de la funcion, clase o modulo y se pueden acceder usando el atributo __doc__
class MiClase:
    """Esta es una clase de ejemplo para demostrar el uso de docstrings."""
    
    def mi_metodo(self):
        """Este es un metodo de ejemplo que no hace nada en particular."""
        pass

# Accediendo al docstring de la clase y el metodo
#print(MiClase.__doc__)  #, se imprime el docstring de la clase
#print(MiClase.mi_metodo.__doc__)  #, se imprime el docstring del metodo
#help(MiClase)  #, se usa el metodo help() para obtener información sobre la clase, incluyendo su docstring

# Ste son inmutables
# Una vez creada una cadena, no se puede modificar, pero se pueden crear nuevas cadenas a partir de las existentes
cadena_original = "Hola Mundo"
cadena_modificada = cadena_original.replace("Mundo", "Python")  #, se crea una nueva cadena reemplazando "Mundo" por "Python"
print(f"Cadena original: {cadena_original} {id(cadena_original)}")  #, se imprime la cadena original
print(f"Cadena modificada: {cadena_modificada} {id(cadena_modificada)}")  #, se imprime la cadena modificada


#Metodo join de cadenas
# El metodo join() se usa para concatenar una lista de cadenas en una sola cadena, usando un separador especifico
#Concatenar una cadena que se encuentra en una lista, la documentacion oficial es: str.join( self, iterable )
#Para añadir un separador entre las cadenas, se coloca el separador antes del metodo join() y se pasa la lista de cadenas como argumento, siendo que su sintaxis seria: "separador".join(lista_cadenas)
# Devuelve una cadena que es la concatenacion de todas las cadenas en la lista, separadas por el separador especificado
lista_cadenas = ["Python", "es", "genial"]
cadena_concatenada = "-".join(lista_cadenas)
print(f"Cadena concatenada con join(): {cadena_concatenada}")

#Metodo split de cadenas
# El metodo split() se usa para dividir una cadena en una lista de cadenas, usando un separador especifico
# La documentacion oficial es: str.split( self, sep=None, maxsplit=-1 )
# Si no se especifica el separador, se usa cualquier espacio en blanco como separador
# Lo que devuelve es una lista de cadenas, donde cada cadena es una parte de la cadena original dividida por el separador
# La sintaxis seria: cadena.split(separador, maxsplit) , maxsplit es el numero maximo de divisiones que se deben hacer, si no se especifica, se divide en todas las ocurrencias del separador
cadena = "Hola Mundo"
lista_palabras = cadena.split()  #, se usa el metodo split() sin argumentos para dividir la cadena en palabras
print(f"Lista de palabras: {lista_palabras}")

# Formato de str con parametros posicionales
# El metodo format() se usa para formatear cadenas, permitiendo insertar valores en una cadena usando marcadores de posicion
# La documentacion oficial es: str.format( self, *args, **kwargs )
# La sintaxis seria: cadena.format(valor1, valor2, ...)
cadena_formateada = "Hola {}, tu numero es {}".format("Mundo", 10)  #, se usa el metodo format() para insertar valores en la cadena
#Si manejamos valores flotantes, se puede especificar el numero de decimales a mostrar usando :n.donde n es el numero de decimales, por ejemplo: cadena_formateada = "Hola {}, tu numero es {:.2f}".format("Mundo", 10.123456)

#Podemos indicar la posicion de los valores a insertar en la cadena usando indices, por ejemplo: cadena_formateada = "Hola {0}, tu numero es {1}".format("Mundo", 10), donde {0} se refiere al primer valor y {1} al segundo valor
cadena_formateada = "Hola {0}, tu numero es {1}".format("Mundo", 10)  #, se usa el metodo format() para insertar valores en la cadena usando indices
#Tambien se pueden usar nombres de variables como marcadores de posicion, por ejemplo: cadena_formateada = "Hola {nombre}, tu numero es {numero}".format(nombre="Mundo", numero=10), donde {nombre} se refiere al valor de la variable nombre y {numero} al valor de la variable numero
cadena_formateada = "Hola {nombre}, tu numero es {numero}".format(nombre="Mundo", numero=10)  #, se usa el metodo format() para insertar valores en la cadena usando nombres de variables
#Podemos combinar ambos tipos de marcadores de posicion, por ejemplo: cadena_formateada = "Hola {0}, tu numero es {numero}".format("Mundo", numero=10), donde {0} se refiere al primer valor y {numero} al valor de la variable numero y incluso de los valores
cadena_formateada = "Hola {0}, tu numero es {numero}".format("Mundo", numero=10)  #, se usa el metodo format() para insertar valores en la cadena usando indices y nombres de variables
#Tambien se pueden usar diccionarios como argumentos, por ejemplo: cadena_formateada = "Hola {nombre}, tu numero es {numero}".format(**{"nombre": "Mundo", "numero": 10}), donde ** indica que se esta pasando un diccionario como argumento
diccionario = {"nombre": "Mundo", "numero": 10}
cadena_formateada = "Hola {nombre}, tu numero es {numero}".format(**diccionario)  #, se usa el metodo format() para insertar valores en la cadena usando un diccionario como argumento
#otra forma es
cadena_formateada = "Hola {nombre}, tu numero es {numero}".format(nombre=diccionario["nombre"], numero=diccionario["numero"])  #, se usa el metodo format() para insertar valores en la cadena usando un diccionario como argumento, pero accediendo a los valores directamente
#otra es

# Formato de str con f-strings
# Las f-strings son una forma mas reciente y eficiente de formatear cadenas, introducidas en Python 3.6
# Permiten insertar expresiones dentro de cadenas usando llaves {}
nombre = "Mundo"
numero = 10
cadena_fstring = f"Hola {nombre}, tu numero es {numero:.1f}"  #, se usa f-string para insertar valores en la cadena, donde {nombre} se refiere al valor de la variable nombre y {numero:.1f} indica que se debe mostrar el numero con un decimal



# Formato de str con el operador %
# El operador % se usa para formatear cadenas de manera similar a como se hace en C
# La documentacion oficial es: str.__mod__( self, other )
cadena_formateada = "Hola %s, tu numero es %d" % (nombre, numero) #Si solo hay un valor se puede omitir el parentesis, pero si hay mas de un valor se deben usar parentesis para agrupar los valores, los diferentes % son los siguientes:
# %s para cadenas, %d para enteros, %f.ndecimales para flotantes, %x para hexadecimales, %o para octales, %e para notacion cientifica
#Si tenemos una lista de valores, se puede usar el operador % con una tupla para formatear la cadena
valores = ("Mundo", 10)
cadena_formateada = "Hola %s, tu numero es %d" % valores
# Donde se colocaran los valores de la tupla en los marcadores de posicion correspondientes, aunque el tipo de dato no coincida, python lo convertira automaticamente al tipo de dato correspondiente, por ejemplo, si se coloca un numero flotante en un marcador de posicion %d, python lo convertira a entero
cadena_formateada = "Hola %s, tu numero es %d" % (21, 10.5)  #, el numero flotante se convierte a entero
print(f"Cadenas formateadas: {cadena_formateada}, {cadena_fstring}")
#Si vamos a estar en un for o no requerimos pasar los valores, podemos dejar la cadena con los marcadores de posicion y luego simplemente usar cadenaConPosiciones%(valores)


# Metodo prin usando un separador
# El metodo print() se usa para imprimir valores en la consola, pero tambien se puede usar para imprimir cadenas con un separador especifico
# La documentacion oficial es: print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
print("Hola", "Mundo", sep="-")  #, se usa el argumento sep para especificar el separador entre los valores a imprimir
print("Hola", "Mundo", sep=" ", end="!")  #, se usa el argumento end para especificar el final de la linea, en este caso se imprime un signo de exclamacion al final
print("Hola", "Mundo", sep=" ", end="\n")  #, se usa el argumento end para especificar el final de la linea, en este caso se imprime un salto de linea al final
print("Hola", "Mundo", sep=" ", end="")  #, se usa el argumento end para especificar que no se debe imprimir nada al final, es decir, no se imprime un salto de linea

# Multiplicacion de cadenas
# La multiplicacion de cadenas se usa para repetir una cadena un numero especifico de veces
cadena_repetida = "Hola" * 3  #, se repite la cadena "Hola" 3 veces

#Multiplicacion tuplas
cadena_repetida_tupla = ("Hola",) * 3  #, se repite la tupla ("Hola",) 3 veces, nota que se debe usar una coma para indicar que es una tupla de un solo elemento
print(f"Cadenas repetidas: {cadena_repetida}, {cadena_repetida_tupla}")

# Muliplicacion de listas
lista_repetida = ["Hola"] * 3  #, se repite la lista ["Hola"] 3 veces
print(f"Lista repetida: {lista_repetida}")

# Caractereres de escape
cadena_con_escapes = "Hola\nMundo\tPython"  #, se usa \n para salto de linea y \t para tabulacion
print(f"Cadenas con caracteres de escape: {cadena_con_escapes}")
#Los caracteres de escape son secuencias de caracteres que tienen un significado especial, por ejemplo:
# \n para salto de linea, \t para tabulacion, \\ para una barra invertida, \' para una comilla simple, \" para una comilla doble, \r para retorno de carro, \b para retroceso, \f para avance de pagina, \v para tabulacion vertical, \a para campana, \0 para caracter nulo

# Cararacteres unicode
# Los caracteres unicode son caracteres que pueden representar cualquier simbolo de cualquier idioma, se pueden usar en cadenas usando la secuencia \u seguido de 4 digitos hexadecimales o \U seguido de 8 digitos hexadecimales
cadena_unicode = "Hola \u00A9 Mundo"  #, se usa \u00A9 para el simbolo de copyright
print(f"Cadenas con caracteres unicode: {cadena_unicode}")
#Lo mas comunes son los siguientes:
# \u00A9 para el simbolo de copyright, \u00AE para el simbolo de marca registrada, \u20AC para el simbolo del euro, \u00B0 para el simbolo de grado, \u00B1 para el simbolo de mas menos, \u221E para el simbolo de infinito. Esta la noacion extendida que permite usar mas de 4 digitos hexadecimales, por ejemplo: \U0001F600 para el emoji de cara sonriente, donde 1F600 es el codigo unicode del emoji. Igual puede usarse notacion hexadecimal con el prefijo 0x, por ejemplo: "\xA9" para el simbolo de copyright, donde A9 es el codigo hexadecimal del simbolo.

# Caracteres ASCII
# Los caracteres ASCII son un subconjunto de caracteres unicode que representan los primeros 128 caracteres, incluyendo letras, numeros y simbolos comunes, para usarlos en cadenas, se pueden usar los codigos ASCII correspondientes, por ejemplo:
cadena_ascii = "Hola \x41\x42\x43"  #, se usa \x41 para la letra A, \x42 para la letra B y \x43 para la letra C
# o el metodo chr() que recibe un numero entero y devuelve el caracter correspondiente, por ejemplo:
cadena_ascii = "Hola " + chr(65) + chr(66) + chr(67)  #, se usa chr(65) para la letra A, chr(66) para la letra B y chr(67) para la letra C
print(f"Cadenas con caracteres ASCII: {cadena_ascii}")

# Manejo literales de tipo bytes
# Son caracteres generalmente unicode pero cuando queremos trabajar con archivos binarios o datos que no son texto, se usan los literales de tipo bytes, que son una secuencia de bytes, se crean usando el prefijo b antes de la cadena, por ejemplo:
cadena_bytes = b"Hola Mundo"  #, se crea un literal de tipo bytes
print(f"Cadenas de bytes: {cadena_bytes}")  #, se imprime el literal de tipo bytes
print(f"Tipo de dato: {type(cadena_bytes)}")  #, se imprime el tipo de dato del literal de tipo bytes
# Acceder a los bytes individuales de un literal de tipo bytes es similar a acceder a los caracteres de una cadena, pero se devuelve un entero que representa el valor del byte, por ejemplo:
print(f"Primer byte: {cadena_bytes[0]}")  #, se imprime el primer byte del literal de tipo bytes
# Para saber el valor del byte si corresponde a un caracter, se puede usar la funcion chr() para convertir el valor del byte a un caracter, por ejemplo:
print(f"Primer byte como caracter: {chr(cadena_bytes[0])}")  #, se imprime el primer byte del literal de tipo bytes como caracter

# Se pueden usar los metodos de las cadenas en los literales de tipo bytes, pero se debe tener en cuenta que los metodos devuelven un literal de tipo bytes, por ejemplo:
print(f"Longitud del literal de tipo bytes: {len(cadena_bytes)}")  #, se imprime la longitud del literal de tipo bytes
print(f"Literal de tipo bytes en mayusculas: {cadena_bytes.upper()}")  #, se imprime el literal de tipo bytes en mayusculas
print(f"Literal de tipo bytes en minusculas: {cadena_bytes.lower()}")  #, se imprime el literal de tipo bytes en minusculas

"""
Los literales bytes (b"texto" o b"\x00\x01") sirven para manejar datos binarios de manera eficiente y explícita en Python, lo cual es esencial en contextos donde:
no se trabaja con texto (como en archivos, redes, criptografía, compresión, multimedia, web , etc.),
se necesita compatibilidad con otros lenguajes o sistemas que esperan datos binarios.
"""


#Convertir cadenas a bytes y viceversa
# Para convertir una cadena a bytes, se usa el metodo encode() de la cadena, que toma un argumento opcional que especifica la codificacion a usar, por defecto es utf-8
cadena = "Hola Mundo"
cadena_bytes = cadena.encode()  #, se convierte la cadena a bytes, de manera opcional se puede especificar la codificacion, por ejemplo: cadena.encode("utf-8"), cadena.encode("ascii"), cadena.encode("latin-1"), etc.
print(f"Cadena original: {cadena}")
print(f"Cadena en bytes: {cadena_bytes}")
# Para convertir de bytes a cadena, se usa el metodo decode() de los bytes, que toma un argumento opcional que especifica la codificacion a usar, por defecto es utf-8
cadena_decodificada = cadena_bytes.decode()  #, se convierte los bytes a cadena, de manera opcional se puede especificar la codificacion, por ejemplo: cadena_bytes.decode("utf-8"), cadena_bytes.decode("ascii"), cadena_bytes.decode("latin-1"), etc.
print(f"Cadena decodificada: {cadena_decodificada}")

# Leer archivos online en bytes
from urllib.request import urlopen #  , se importa la funcion urlopen del modulo urllib.request para abrir URLs
url = "https://www.example.com"  #, se define la URL a abrir
with urlopen(url) as response:  #, se abre la URL y se guarda la respuesta en la variable response
    contenido_bytes = response.read()  #, se lee el contenido de la respuesta en bytes
    print(f"Contenido en bytes: {contenido_bytes[:100]}")  #, se imprime los primeros 100 bytes del contenido
    contenido_bytes = contenido_bytes.decode('utf-8')  #, se decodifica el contenido de bytes a cadena usando utf-8
    print(f"Contenido decodificado: {contenido_bytes[:100]}")  #, se imprime los primeros 100 caracteres del contenido


# Leer linea por linea de un archivo online en bytes
from urllib.request import urlopen  #, se importa la funcion urlopen del modulo urllib.request
url = "https://www.example.com"  #, se define la URL a abrir
with urlopen(url) as response:  #, se abre la URL y se guarda la respuesta en la variable response
    for linea in response:  #, se itera sobre cada linea de la respuesta
        linea_bytes = linea.strip()  #, se elimina el salto de linea al final de cada linea
        print(f"Linea en bytes: {linea_bytes}")
        linea_decodificada = linea_bytes.decode('utf-8')  #, se decodifica la linea de bytes a cadena usando utf-8
        print(f"Linea decodificada: {linea_decodificada}")  #, se imprime la linea decodificada

# Leer archivos locales en bytes
# Para leer un archivo local en bytes, se usa el modo 'rb' al abrir el archivo, que indica que se debe abrir el archivo en modo lectura binaria
# with open("archivo.txt", "rb") as file:  #, se abre el archivo en modo lectura binaria
#     contenido_bytes = file.read()  #, se lee el contenido del archivo en bytes
#     print(f"Contenido en bytes: {contenido_bytes[:100]}")  #, se imprime los primeros 100 bytes del contenido
#     contenido_bytes = contenido_bytes.decode('utf-8')  #, se decodifica el contenido de bytes a cadena usando utf-8
#     print(f"Contenido decodificado: {contenido_bytes[:100]}")  #, se imprime los primeros 100 caracteres del contenido


# Contar ocurrencias de un caracter en una cadena
# Para contar las ocurrencias de un caracter en una cadena, se usa el metodo count()
cadena = "Hola Mundo"
contador = cadena.count("o")  #, se cuenta las ocurrencias de "o" en la cadena
print(f"Ocurrencias de 'o': {contador}")

# Alinear cadenas
# Para alinear cadenas, se pueden usar los metodos ljust(), rjust() y center(), los argumentos de estos metodos son el ancho total de la cadena resultante y el caracter de relleno opcional (por defecto es un espacio), siendo su sintaxis:
# cadena.ljust(ancho, caracter_de_relleno), cadena.rjust(ancho, caracter_de_relleno) y cadena.center(ancho, caracter_de_relleno)
# El numero que se coloque en ancho es el numero total de caracteres que debe tener la cadena resultante, incluyendo los espacios de relleno y el contenido que ya trae, si la cadena original es mas larga que el ancho especificado, no se truncara, simplemente se dejara como esta.

cadena = "Hola"
print(f"Cadena original: '{cadena}'")
print(f"Alineada a la izquierda: '{cadena.ljust(10, '+')}'") # Se colocan 6 espacios a la derecha de la cadena original, rellenando con el caracter '+'. debido a que la cadena original tiene 4 caracteres, se colocan 6 espacios a la derecha.
print(f"Alineada a la derecha: '{cadena.rjust(10, '-')}'") # Se colocan 6 espacios a la izquierda de la cadena original, rellenando con el caracter '-'. debido a que la cadena original tiene 4 caracteres, se colocan 6 espacios a la izquierda.
print(f"Centrada: '{cadena.center(10, '*')}'") # Se colocan 3 espacios a cada lado de la cadena original, rellenando con el caracter '*'. debido a que la cadena original tiene 4 caracteres, se colocan 3 espacios a cada lado.

#Si quisieramos agregar el numero especifico de elementos sin tener que contar los caracteres, podemos usar una combiacion entre las funciones mas el metodo len, siendo la siguiente forma
cadena="zaddkiel"
print(f'Alineando a la la izquierda: {cadena.ljust(len(cadena)+10, "+")}')

# Metodos strip y replace
# El metodo strip() se usa para eliminar espacios en blanco al inicio y al final de una cadena, mientras que el metodo replace() se usa para reemplazar una subcadena por otra
cadena = "   Hola Mundo   "
print(f"Cadena original: '{cadena}'")
print(f"Cadena sin espacios: '{cadena.strip()}'")  #, se eliminan los espacios al inicio y al final de la cadena
#El metodo replace() se usa para reemplazar una subcadena por otra, su sintaxis es cadena.replace(subcadena_a_reemplazar, subcadena_nueva), donde subcadena_a_reemplazar es la subcadena que se desea reemplazar y subcadena_nueva es la nueva subcadena que se desea insertar en su lugar
print(f"Cadena con espacios reemplazados: '{cadena.replace(' ', '-')}'")  #, se reemplazan los espacios por guiones

#Metodo lstrip y rstrip
# El metodo lstrip() se usa para eliminar espacios en blanco al inicio de una cadena, mientras que el metodo rstrip() se usa para eliminar espacios en blanco al final de una cadena, tambien se pueden eliminar ciertos caracterees especificos añadiendo como argumento el caractera a eliminar
cadena = "   Hola Mundo   "
print(f"Cadena original: '{cadena}'")
print(f"Cadena sin espacios al inicio: '{cadena.lstrip()}'")  #, se eliminan los espacios al inicio de la cadena
print(f"Cadena sin espacios al final: '{cadena.rstrip()}'")  #, se eliminan los espacios al final de la cadena
cadena_con_caracteres = "###Hola Mundo###"
print(f"Cadena con caracteres al inicio y al final: '{cadena_con_caracteres}'")
print(f'Cadena sin caracteres al inicio: {cadena_con_caracteres.lstrip("#")}') 
print(f'Cadena sin caracteres al final: {cadena_con_caracteres.rstrip("#")}') 

# USO DE REPL Read-Evaluate-Print Loop
# El REPL es un entorno interactivo de Python que permite ejecutar codigo de manera interactiva
# Se puede acceder al REPL abriendo una terminal y escribiendo python o python3, dependiendo de la version instalada
# En el REPL, se pueden escribir expresiones y ver su resultado inmediatamente, por ejemplo:
# >>> 2 + 2
# 4
# >>> print("Hola Mundo")
# Hola Mundo
# >>> cadena = "Hola Mundo"
# >>> print(cadena)

#Se puede usar RPLN en la terminal de vs escribiendo python o python3, dependiendo de la version instalada

# Tipo NONE
# El tipo None es un tipo de dato especial que representa la ausencia de valor o un valor nulo
# Se usa para indicar que una variable no tiene un valor asignado o que una funcion no devuelve ningun valor
# Se puede crear una variable de tipo None asignando el valor None a la variable, por ejemplo:
variable_nula = None  #, se crea una variable de tipo None
#Una variable nula se considera False
print(f"Variable nula: {variable_nula}, Tipo: {type(variable_nula)}")  #, se imprime el valor y el tipo de la variable nula

# Unpacking en python
# El unpacking es una tecnica que permite asignar los valores de una coleccion (como una lista o una tupla) a variables individuales de manera sencilla
# Se puede hacer de la siguiente manera:
a,b,c= 1,2,3  #, se asignan los valores 1, 2 y 3 a las variables a, b y c respectivamente dela tupla
print(f"Unpacking: a={a}, b={b}, c={c}")  #, se imprime el valor de las variables a, b y c
elementos = [4, 5, 6]  #, se crea una lista con los valores 4, 5 y 6
a, b, c = elementos  #, se asignan los valores de la lista a las variables a, b y c
print(f"Unpacking de lista: a={a}, b={b}, c={c}")  #, se imprime el valor de las variables a, b y c

#Si queremos que un valor no se tome en cuenta, podemos usar el caracter de subrayado _, que se usa como una variable temporal que no se usara mas adelante, por ejemplo:
a, _, c = 1, 2, 3  #, se asignan los valores 1, 2 y 3 a las variables a y c, y se ignora el valor 2
print(f"Unpacking con subrayado: a={a}, c={c}")

#Si tenemos una lista o tupla con mas valores de los que queremos asignar, podemos usar el operador * para agrupar los valores restantes en una sola variable, por ejemplo:
a, *b = 1, 2, 3, 4, 5  #, se asigna el valor 1 a la variable a y los valores restantes (2, 3, 4, 5) a la lista b
print(f"Unpacking con operador *: a={a}, b={b}")  #, se imprime el valor de las variables a y b
#Si no se usa el operador se producira un error que nos dira que hay demasiados valores para desempaquetar

# Si queremos desempaquetar valores incluso despues de usar el operador * , se puede hacer de la siguiente manera:
a, *b, c = 1, 2, 3, 4, 5  #, se asigna el valor 1 a la variable a, los valores restantes (2, 3, 4) a la lista b y el valor 5 a la variable c
print(f"Unpacking con operador * al final: a={a}, b={b}, c={c}")  #, se imprime el valor de las variables a, b y c

#En funciones tambien se puede usar el unpacking para devolver varios valores, por ejemplo:
def sumar_y_restar(a, b):
    return a + b, a - b, a*b  #, se devuelve una tupla con la suma y la resta de los valores a y b
resultado_suma, resultado_resta, res = sumar_y_restar(10, 5)  #, se asignan los valores devueltos por la funcion a las variables resultado_suma y resultado_resta
print(f"Resultado de la suma: {resultado_suma}, Resultado de la resta: {resultado_resta}")  #, se imprime el valor de las variables resultado_suma y resultado_resta

#Si la funcion devuelve mas valores de los que queremos asignar, podemos usar el operador * para agrupar los valores restantes en una sola variable, por ejemplo:
resultado_suma, *otros_resultados = sumar_y_restar(10, 5)  #, se asigna el valor de la suma a la variable resultado_suma y los valores restantes (resta y multiplicacion) a la lista otros_resultados

#Si no quisieramos procesar varios valores devueltos se puede usar la combinacion de subrayado y el operador * para ignorar los valores que no nos interesan, por ejemplo:
x,*_ = sumar_y_restar(10, 5)  #, se asigna el valor 15 a la variable x y se ignoran los valores restantes q son la resta y la multiplicacion

#Funcion partition
# La funcion partition() se usa para dividir una cadena en tres partes: la parte antes del separador, el separador y la parte despues del separador, devuelve una tupla con las tres partes
# La sintaxis es: cadena.partition(separador), donde separador es la cadena que se usara como separador para dividir la cadena
# Si el separador no se encuentra en la cadena, la parte antes del separador sera la cadena completa, el separador sera una cadena vacia y la parte despues del separador sera una cadena vacia
# La documentacion oficial es: str.partition(sep)
cadena = "Hola Mundo Python"
parte_antes, separador, parte_despues = cadena.partition("Mundo")
print(f"Parte antes: '{parte_antes}', Separador: '{separador}', Parte despues: '{parte_despues}'")  #, se imprime las partes de la cadena dividida por el separador "Mundo"

# PROFUNDIZANDO EN LISTAS
#suma de listas, la suma de listas se hace con el operador +, que concatena dos listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_suma = lista1 + lista2  #, se suman las dos listas
print(f'suma de listas: {lista_suma}')

#Extender una lista con otra, se usa el metodo extend() de la lista, que agrega los elementos de otra lista al final de la lista original, se modifica la lista original y no se devuelve una nueva lista, su sintaxis es: lista1.extend(lista2), donde lista1 es la lista que se desea extender y lista2 es la lista cuyos elementos se agregaran a lista1
lista1.extend(lista2)  #, se extiende la lista1 con los elementos de lista2
print(f'Lista extendida: {lista1}')  #, se imprime la lista extendida

# Obtener indice de un elemento en una lista
# Para obtener el indice de un elemento en una lista, se usa el metodo index() de la lista, que devuelve el primer indice donde se encuentra el elemento, si el elemento no se encuentra en la lista, se lanza una excepcion ValueError, su sintaxis es: lista.index(elemento), donde elemento es el elemento cuyo indice se desea obtener
lista = [1, 2, 3, 4, 5]
indice = lista.index(3)  #, se obtiene el indice del elemento 3 en la lista
print(f'Indice del elemento 3: {indice}')  #, se imprime el indice

# La funcion index() tambien acepta un argumento opcional start, que indica el indice desde donde se debe comenzar a buscar el elemento, y un argumento opcional end, que indica el indice hasta donde se debe buscar el elemento, su sintaxis es: lista.index(elemento, start, end), donde start es el indice desde donde se comienza a buscar y end es el indice hasta donde se busca
indice = lista.index(3, 0, 4)  #, se obtiene el indice del elemento 3 en la lista, comenzando a buscar desde el indice 0 hasta el indice 4 (exclusivo)

#Invertir el orden de los elementos de una lista
# Para invertir el orden de los elementos de una lista, se puede usar el metodo reverse() de la lista, que modifica la lista original y no devuelve una nueva lista, su sintaxis es: lista.reverse(), donde lista es la lista cuyos elementos se desea invertir
lista = [1, 2, 3, 4, 5]
lista.reverse()  #, se invierte el orden de los elementos de la lista
print(f'Lista invertida: {lista}')  #, se imprime la lista invertida

# Ordenar una lista
# Para ordenar una lista, se puede usar el metodo sort() de la lista, que modifica la lista original y no devuelve una nueva lista, su sintaxis es: lista.sort(), donde lista es la lista que se desea ordenar
lista = [5, 3, 1, 4, 2]
lista.sort()  #, se ordena la lista
print(f'Lista ordenada: {lista}')  #, se imprime la lista ordenada

# Sort() puede aceptar dos argumentos opcionales: key y reverse, donde key es una funcion que se usa para extraer un valor de cada elemento de la lista para compararlos, y reverse es un booleano que indica si se debe ordenar la lista en orden descendente (True) o ascendente (False), por defecto es False
# La sintaxis es: lista.sort(key=None, reverse=False), donde key es la funcion que se usa para extraer un valor de cada elemento de la lista y reverse es un booleano que indica si se debe ordenar la lista en orden descendente o ascendente
lista = ["banana", "apple", "cherry"]
lista.sort(key=len)  #, se ordena la lista por la longitud de cada elemento
print(f'Lista ordenada por longitud: {lista}')  #, se imprime la lista ordenada por longitud

# Ordenar una lista de objetos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f"{self.nombre} ({self.edad})"

personas = [Persona("Alice", 30), Persona("Bob", 25), Persona("Charlie", 35)]
# Para ordenar una lista de objetos, se puede usar el metodo sort() de la lista, pasando una funcion que extraiga el atributo por el cual se desea ordenar
personas.sort(key=lambda p: p.edad)  #, se ordena la lista por la edad de cada persona
print(f'Lista de personas ordenada por edad: {personas}')  #, se imprime la lista ordenada por edad


# Funcion sorted()
# La funcion sorted() se usa para ordenar una lista y devuelve una nueva lista ordenada, no modifica la lista original, su sintaxis es: sorted(iterable, key=None, reverse=False), donde iterable es la lista que se desea ordenar, key es una funcion que se usa para extraer un valor de cada elemento de la lista para compararlos y reverse es un booleano que indica si se debe ordenar la lista en orden descendente (True) o ascendente (False), por defecto es False
lista = [5, 3, 1, 4, 2]
lista_ordenada = sorted(lista)  #, se ordena la lista y se devuelve una nueva lista ordenada
print(f'Lista original: {lista}')  #, se imprime la lista original
print(f'Lista ordenada: {lista_ordenada}')  #, se imprime la lista ordenada

#Obtener el valor maximo y minimo de una lista
# Para obtener el valor maximo y minimo de una lista, se pueden usar las funciones max() y min(), que devuelven el valor maximo y minimo de la lista respectivamente
lista = [5, 3, 1, 4, 2]
maximo = max(lista)  #, se obtiene el valor maximo de la lista
minimo = min(lista)  #, se obtiene el valor minimo de la lista
# Igual que sort pueden aceptar dos argumentos opcionales: key y default, donde key es una funcion que se usa para extraer un valor de cada elemento de la lista para compararlos, y default es el valor que se devuelve si la lista esta vacia, su sintaxis es: max(lista, key=None, default=None) y min(lista, key=None, default=None)

# Copiar una lista
# Para copiar una lista, se puede usar el metodo copy() de la lista, que devuelve una copia superficial de la lista, es decir, una nueva lista con los mismos elementos que la lista original, su sintaxis es: lista.copy(), donde lista es la lista que se desea copiar. Se copia la referencia a los objetos de la lista, no los objetos en si, por lo que si los objetos son mutables y se modifican, se reflejara el cambio en ambas listas
lista = [1, 2, 3, 4, 5]
lista_copia = lista.copy()  #, se copia la lista
print(f'Lista original: {lista}')  #, se imprime la lista original
print(f'Lista copia: {lista_copia}')  #, se imprime la lista copia

# NOTA: El comparador is se usa para comparar si dos objetos son el mismo objeto en memoria, es decir, si tienen la misma direccion de memoria, mientras que el comparador == se usa para comparar si dos objetos son iguales en valor, es decir, si tienen el mismo contenido
print(f'Comparacion de listas: {lista is lista_copia}')  #, se imprime si la lista original y la copia son el mismo objeto en memoria
print(f'Comparacion de listas: {lista == lista_copia}')  #, se imprime si la lista original y la copia son iguales en valor 

# Copiar usando el constuctor de la lista
# Otra forma de copiar una lista es usando el constructor de la lista, que crea una nueva lista con los mismos elementos que la lista original, su sintaxis es: nueva_lista = list(lista), donde lista es la lista que se desea copiar, aqui se crea una nueva lista con los mismos elementos que la lista original, pero no es la misma lista en memoria, pasa lo mismo que copy(), se copia la referencia a los objetos de la lista, no los objetos en si, por lo que si los objetos son mutables y se modifican, se reflejara el cambio en ambas listas
lista_copia2 = list(lista)  #, se copia la lista usando el constructor de la lista
print(f'Lista copia 2: {lista_copia2}')  #, se imprime la lista copia 2

# Copiar usando el operador de corte 
# Otra forma de copiar una lista es usando el operador de corte, que crea una nueva lista con los mismos elementos que la lista original, su sintaxis es: nueva_lista = lista[:], donde lista es la lista que se desea copiar, aqui se crea una nueva lista con los mismos elementos que la lista original, pero no es la misma lista en memoria, pasa lo mismo que copy(), se copia la referencia a los objetos de la lista, no los objetos en si, por lo que si los objetos son mutables y se modifican, se reflejara el cambio en ambas listas
lista_copia3 = lista[:]  #, se copia la lista usando el operador de corte
print(f'Lista copia 3: {lista_copia3}')  #, se imprime la lista copia 3


# Copiar una lista usando deepcopy
# Si se desea hacer una copia profunda de una lista, es decir, una copia que no solo copie la referencia a los objetos de la lista, sino que cree nuevas instancias de los objetos, se puede usar el modulo copy y su funcion deepcopy(), que crea una copia profunda de la lista, su sintaxis es: nueva_lista = copy.deepcopy(lista), donde lista es la lista que se desea copiar
import copy  #, se importa el modulo copy
lista_copia_profunda = copy.deepcopy(lista)  #, se copia la lista usando deepcopy
print(f'Lista copia profunda: {lista_copia_profunda}')  #, se imprime la lista copia profunda

# Incluso cuando se hace multiplicacion de listas, se copia la referencia a los objetos de la lista, no los objetos en si, por lo que si los objetos son mutables y se modifican, se reflejara el cambio en ambas listas
lista_multiplicada = lista * 2  #, se multiplica la lista por 2, creando una nueva lista con los mismos elementos que la lista original, pero no es la misma lista en memoria, pasa lo mismo que copy(), se copia la referencia a los objetos de la lista, no los objetos en si, por lo que si los objetos son mutables y se modifican, se reflejara el cambio en ambas listas
print(f'Lista multiplicada: {lista_multiplicada}')  #, se imprime la lista multiplicada
(print(f'Comparacion de lista {lista_multiplicada[0] is lista[0]}'))  #, se imprime si el primer elemento de la lista multiplicada es el mismo objeto en memoria que el primer elemento de la lista original

# Matrices en python
# Las matrices en python se pueden representar como listas de listas, donde cada lista interna representa una fila de la matriz, por ejemplo:
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  #, se crea una matriz de 3x3
print(f'Matriz: {matriz}')  #, se imprime la matriz

# Acceder a los elementos de una matriz
# Para acceder a los elementos de una matriz, se puede usar el operador de indice, donde el primer indice representa la fila y el segundo indice representa la columna, por ejemplo:
print(f'Elemento en la fila 1, columna 2: {matriz[1][2]}')  #, se imprime el elemento en la fila 1, columna 2 de la matriz

# Recorrer una matriz
# Para recorrer una matriz, se puede usar un bucle for anidado, donde el primer bucle recorre las filas y el segundo bucle recorre las columnas, por ejemplo:
for fila in matriz:  #, se recorre cada fila de la matriz
    for columna in fila:  #, se recorre cada columna de la fila
        print(f'Elemento en la fila {matriz.index(fila)}, columna {fila.index(columna)}: {columna}')  #, se imprime el elemento en la fila y columna correspondiente

# Ordernar una matriz
# Para ordenar una matriz, se puede usar el metodo sort() de la lista, siendo que se añade una funcion key que extraiga el valor por el cual se desea ordenar, por ejemplo, para ordenar una matriz por la suma de cada fila, se puede hacer lo siguiente:
matriz.sort(key=sum)  #, se ordena la matriz por la suma de cada fila
print(f'Matriz ordenada por la suma de cada fila: {matriz}')  #, se imprime la matriz ordenada por la suma de cada fila
# Para ordenar una matriz por un elemento especifico de cada fila, se puede usar una funcion lambda que extraiga el elemento por el cual se desea ordenar, por ejemplo, para ordenar una matriz por el segundo elemento de cada fila, se puede hacer lo siguiente:
matriz.sort(key=lambda fila: fila[1])  #, se ordena la matriz por el segundo elemento de cada fila
print(f'Matriz ordenada por el segundo elemento de cada fila: {matriz}')  #, se imprime la matriz ordenada por el segundo elemento de cada fila
#Para ordenar una matriz por la cantidad de elementos en cada fila, se puede usar la funcion len() como key, por ejemplo:
matriz2 = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]  #, se crea una matriz con filas de diferente longitud
matriz2.sort(key=len)

# Funcion reversed()
# La funcion reversed() se usa para invertir el orden de los elementos de cualquier iterable y devuelve un iterador que recorre los elementos en orden inverso, no modifica la lista original, su sintaxis es: reversed(lista), donde lista es la lista que se desea invertir
lista = [1, 2, 3, 4, 5]
lista_invertida = list(reversed(lista))  #, se invierte la lista y se convierte el iterador en una lista
print(f'Lista original: {lista}')  #, se imprime la lista original
print(f'Lista invertida: {lista_invertida}')  #, se imprime la lista invertida

# Mas del operador unpacking
# El operador unpacking * se puede usar en varias situaciones, como en llamadas a funciones, en asignaciones de variables y en literales de listas y tuplas

# Desempaquetar argumentos en llamadas a funciones
# El operador * se puede usar para desempaquetar una lista o tupla de argumentos, el ejemplo mas comun es en print
numeros = [1, 2, 3, 4, 5]
print(*numeros)  #, se desempaquetan los elementos de la lista y se pasan como argumentos individuales a la funcion print
print(*numeros, sep=' - ')  #, se desempaquetan los elementos de la lista y se pasan como argumentos individuales a la funcion print, separando los elementos con ' - '

# Desempaquetar diccionarios en llamadas a funciones
# El operador ** se puede usar para desempaquetar un diccionario de argumentos, donde las claves del diccionario representan los nombres de los argumentos y los valores representan los valores de los argumentos
def suma(valor1, valor2):
    print(f'Valor 1: {valor1}, Valor 2: {valor2}')  #, se imprime el valor de los argumentos
    print(f'Suma: {valor1 + valor2}')  #, se imprime la suma de los dos valores
argumentos = {'valor1': 10, 'valor2': 20}
suma(**argumentos)  #, se desempaquetan los elementos del diccionario y se pasan como argumentos individuales a la funcion suma

# Crear listas y tuplas con el operador unpacking
# El operador * se puede usar para crear listas y tuplas a partir de otros iterables
numeros = [1, 2, 3, 4, 5]
nueva_lista = [*numeros, 6, 7, 8]  #, se crea una nueva lista a partir de la lista original que se desempaqueta y se añaden nuevos elementos
print(f'Nueva lista: {nueva_lista}')  #, se imprime la nueva lista
nueva_tupla = (*numeros, 6, 7, 8)  #, se crea una nueva tupla a partir de la tupla original y se añaden nuevos elementos
print(f'Nueva tupla: {nueva_tupla}')  #, se imprime la nueva tupla

#No es lo mismo
lista = [1, 2, 3]
lista2= [4, 5, 6]

lista3 = [*lista, *lista2]  #, se crea una nueva lista a partir de las dos listas originales que se desempaquetan
lista4 = [lista, lista2]  #, se crea una nueva lista que contiene las dos listas originales como elementos

# Unir diccionarios con el operador unpacking
# El operador ** se puede usar para unir dos o mas diccionarios, donde las claves de los diccionarios se combinan y los valores se sobrescriben si hay claves duplicadas
diccionario1 = {'a': 1, 'b': 2}
diccionario2 = {'b': 3, 'c': 4}
diccionario_unido = {**diccionario1, **diccionario2}  #, se crea un nuevo diccionario que combina los dos diccionarios originales, sobrescribiendo el valor de la clave 'b' con el valor del segundo diccionario
print(f'Diccionario unido: {diccionario_unido}')  #, se imprime el diccionario unido
# Unir diccionarios con el operador | (Python 3.9+)
# A partir de Python 3.9, se puede usar el operador | para unir dos
# o mas diccionarios, donde las claves de los diccionarios se combinan y los valores se sobrescriben si hay claves duplicadas
diccionario_unido2 = diccionario1 | diccionario2  #, se crea un nuevo diccionario que combina los dos diccionarios originales, sobrescribiendo el valor de la clave 'b' con el valor del segundo diccionario
print(f'Diccionario unido con |: {diccionario_unido2}')  #,

# Construir lista apartir de un string
lista= [*"hola mundo"]
print(f'Lista construida a partir de un string: {lista}')

