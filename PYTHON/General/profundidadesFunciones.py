#Funciones anidadas
#Las funciones anidadas son aquellas que se definen dentro de otra función. Esto permite encapsular la lógica y crear funciones que solo son relevantes en el contexto de la función externa.
def funcion_externa(x):
    def funcion_interna(y):
        return y + 1
    return funcion_interna(x)
#Lo que pasa aquí es que la función interna puede acceder a las variables de la función externa, incluso después de que esta haya terminado de ejecutarse, en este caso la funcion interna puede acceder a la variable x de la funcion externa, por lo que en este ejemplo la funcion interna usa x

# Ejemplo de uso usando argumentos de la funcion externa
def funcion_externa_con_argumento(x):
    def funcion_interna():
        return x + 1 # Aqui se esta accediendo a x
    return funcion_interna()

#Ejemplo sin usar return
def funcion_externa_sin_return():
    def funcion_interna():
        print("Hola desde la función interna")
    funcion_interna() #Se puede llamar a la funcion interna despues de definirla

#Ejemplo funcion que retorna funcion
def crearMultiplicador(n):
    def multiplicar(x):
        return x * n
    return multiplicar  #Devuelve la función multiplicar

#Ejemplo con sentencias de desicion
def operacion(tipo):
    if tipo == "suma":
        def hacer(x, y):
            return x + y
    else:
        def hacer(x, y):
            return x * y
    return hacer

#Ejemplo que tengran bucles o listas
def crear_funciones():
    funciones = []
    for i in range(3):
        def f(x, i=i):  # Aqui lo que pasa es que i ya se va pasando al momento de crear la funcion
            return x + i
        funciones.append(f)
    return funciones

#Resultados de las funciones
print(funcion_externa(5))  # 6
print(funcion_externa_con_argumento(5))  # 6
funcion_externa_sin_return()
por5 = crearMultiplicador(5)
print(por5(10))  # 50
f= operacion("suma")
print(f(5, 3))  # 8
fs = crear_funciones()
print([f(10) for f in fs])  # [10, 11, 12]

#Alcance de variables (Scope)
variable_global = "Soy una variable global" #Se puede acceder a ella desde cualquier parte del código
def funcion():
    #Si queremos modificar una variable global, debemos usar la palabra clave 'global' y posteriormente el nombre de la variable todo esto antes de usarla, por lo tanto recomendablemente es al inicio de donde se esta usando si no es en el aspecto global
    global variable_global
    variable_global = "He sido modificada"

    variable_local = "Soy una variable local" # Solo se puede acceder a ella dentro de esta función, su bloque de código límite
    print(variable_local) # Imprime la variable local
    print(variable_global) # Imprime la variable global
    def funcion_interna():
       global variable_global # Si se quiere modificar la variable global dentro de una funcion interna tambien se debe usar global
       variable_local2 = "Soy una variable local 2"
       variable_global = "He sido modificada dentro de la funcion interna" # Modifica la variable global , es igual necesario usar global para que no se cree una nueva instancia local y no se use la original
       print(variable_global)
       print(variable_local2) # Imprime la variable local 2
    funcion_interna()

funcion()  # Llama a la función que imprime las variables

# Uso de nonlocal, se usa para modificar una variable en un ámbito no local, es decir, en una función externa pero no global
def funcion_con_nonlocal():
    variable = "Soy una variable"
    def funcion_interna():
        nonlocal variable
        variable ="hola we" #Si se hace esto sin nonlocal lo que pasara es que se creara una nueva variable local en la funcion interna, por lo que para que no pase esto se usa nonlocal
        print(variable)
    funcion_interna()
    print(variable)

# Ejercicio alcance variables
contador=0
def mostrarContador():
    print(contador) #Imprime la variable global contador
    def incrementarContador():
        global contador #Se usa global para modificar la variable global contador
        contador += 1
    incrementarContador()
    
mostrarContador()
mostrarContador()

# Funciones y sus distintos usos
# First class citizens

#Definicion funcion
def saludar(nombre):
    print(f"Hola, {nombre}!")

#1. Asignar una funcion a una variable
saludo = saludar #Se coloca la referencia de la funcion a la variable
saludo("Juan") #Se puede llamar a la funcion a traves de la variable

#2. Pasar una funcion como argumento
def ejecutar_funcion(funcion, argumento):
    funcion(argumento) #Se pasa funcion y se usa como fuera su uso comun

ejecutar_funcion(saludar, "Pedro") #Se pasa la funcion saludar y el argumento "Pedro", es decir se pasa su referencia y no se ejecuta inmediatamente
# NOTA: Cuando se coloca el nombre de una funcion sin parentesis se pasa su referencia mientras que cuando si hau parentesis se manda a ejecutar

# 3. Retornar una funcion desde otra
def crear_saludo(saludo):
    def saludar(nombre):
        print(f"{saludo}, {nombre}!")
    return saludar

saludo_morning = crear_saludo("Buenos días")
saludo_morning("Juan")

#Funciones lambda o funciones anonimas, son aquellas que no tienen un nombre definido y se utilizan para tareas pequeñas y específicas. Se definen utilizando la palabra clave 'lambda'.
"""
Normales:Se usa para funciones con varias líneas, más complejas.	Lambda: Se usa para funciones pequeñas y rápidas, de una sola línea.
NormaleS: Tiene un nombre propio (def nombre)	Lambda: Puede ser anónima, o asignarse a una variable.
"""

#Funcion normal
def sumar(a, b): #No se puede asignar a una variable
    return a + b

#Funcion lambda, no se necesita return pero si debe regresar algo valido, no se necesita parentesis para los parametros, y son de una sola linea, su sintaxis es lambda parametro1, parametro2 : accion que se realiza
# el valor de la única expresión es automáticamente el valor retornado.
suma= lambda a, b: a + b  #Crea una referencia y posteriormente se guarda para pder usarla
print(suma(5, 3))  # 8

#Funcion lambda que no recibe argumentos (debemos regresar una expresion valida)
impresion= lambda: print("Hola desde la función lambda")  # Se puede devolver desde una funcion como print hasta algun valor
impresionString= lambda: "Hola desde la función lambda"
impresion()  # Llama a la función lambda
print(impresionString())  # Llama a la función lambda y imprime el valor retornado

# Funcion lambda con parametros por defualt
saludo= lambda nombre="Juan": print(f"Hola, {nombre}!") #Se asignan los valores por defualt como cuando se define una funcion normal
saludo()  # Llama a la función lambda sin argumentos
saludo("Pedro")  # Llama a la función lambda con un argumento

# Funcion lambda con parametros *args y **kwargs
saludos = lambda *args, **kwargs: print(f"Hola, {' '.join(args)}! {kwargs.get('mensaje', '')}")
nombres= ["Juan", "Pedro", "Maria"]
mensaje= {"mensaje": "¿Cómo están?", "mensaje2": "¡Espero que bien!"}
saludos(*nombres, **mensaje)

# Funcion lambda con argumentos, argumentos variables y valores por default
funcion = lambda x, y=10, *args, **kwargs: (x + y + len(args)+len(kwargs))  # Suma x, y, la cantidad de args y la cantidad de kwargs
print(funcion(5, 3, 1, 2, clave1="valor1", clave2="valor2"))  # 15


#Closure funciones closure
# Es una funcion que a su vez encapsula otra funcion pero ademas mantiene el estado de las variables locales definidas en la funcion principal aunque despues de que la funcion extenra haya terminado de ejecutarse. Es decir que una funcion de tipo closure  es aquella que "recuerda" el entorno en el que fue creada, las variables externas a la funcion se mantienen en memoria.
"""
Variables locales de la función externa (aunque ya haya terminado).
Valores que la función interna necesita para funcionar. (Las locales externas y las que dentro de la anidada son necesarias para su chamba)
"""

def crear_contador():
    contador = 0
    def incrementar_contador():
        nonlocal contador 
        contador += 1
        return contador #Guarda contador porque es local y ademas es necesaria
    return incrementar_contador

def saludar(nombre):
    mensaje = f"Hola, {nombre}" #Guarda mensaje porq es necesario para el prin de decir hola
    def decir_hola():
        print(mensaje)
    return decir_hola

contador1 = crear_contador()
print(contador1())  # 1 #Aqui recuerda el valor de la variable contador
print(contador1())  # 2
print(contador1())  # 3

mi_saludo = saludar("Ana")  #Aqui se crea una nueva función que recuerda el mensaje
mi_saludo()  # Imprime: Hola, Ana

#LLamar a a funcion regresada al vuelo
def operacion(a,b):
    def suma():
        return a + b #Se guardan los valores de a y b porq son necesarios para la funcion
    return suma

print(operacion(5,3)()) #Lo que pasa es que primero Esto crea una función suma() con acceso a los valores a = 5 y b = 3 (gracias a la closure), y devuelve esa función suma (¡sin ejecutarla todavía!). Y posteriormente se esta llamando a la funcion que fue devuelta es decir ejecuta suma(),

#Closure y funciones lamba
def operacion(a,b):
    #1. Funcion lambda interna o anidada y se retorna en automatico
    return lambda: a + b #Se almacenan los valores de a y b, devuelve una funcion que ya tiene estos datos precargados

operacion_lambda = operacion(5, 3)  # Crea una función lambda que suma 5 y 3
print(operacion_lambda())  # Imprime: 8
print(operacion(5, 3)())  # Imprime: 8

#Decoradores en python
# Es una forma de modificar o extender el comportamiento de una función sin cambiar su código. Se utilizan comúnmente para agregar funcionalidades adicionales, como la autenticación, el registro o la medición del tiempo de ejecución. Consiste en que una función recibe otra función como argumento y la envuelve para agregarle comportamiento adicional.Un decorador es una función que recibe otra función como argumento y devuelve una nueva función con comportamiento modificado. Generalmente se le añade comportamiento a la funcion decorada al inicio o al final
# Un decorador sirve para: Ejecutar código antes o después de la función original, Modificar sus argumentos, Alterar o reemplazar su valor de retorno, Registrar, verificar, validar, medir tiempo, manejar permisos, etc, Controlar el flujo de ejecución (cancelar, repetir, condicionar)


#1. Funcion decorador
def funcion_decorador(funcion):
    def nueva_funcion(): #3 Funcion decorada
        print("Antes de llamar a la función.")
        funcion() #Se mantiene el comportamiento original
        print("Después de llamar a la función.")
    return nueva_funcion
#2. Funcion a decorar
@funcion_decorador
def mostrar_mensaje():
    print("Este es un mensaje decorado.")

mostrar_mensaje()  # Llama a la función decorada

#Decorador con argumentos, si la funcion recibe argumentos, el decorador debe de recibir *args y **kwargs
# --- CASO 1: Decorador simple para función con argumentos variables ---
def decorador_simple(func):
    # El wrapper acepta cualquier número de argumentos (*args, **kwargs)
    def wrapper(*args, **kwargs):
        print("Antes de la función")
        resultado = func(*args, **kwargs)  # Se pasan todos los argumentos a la función original
        print("Después de la función")
        return resultado
    return wrapper

@decorador_simple
def suma(a, b):
    return a + b

print(suma(3, 4))  # Imprime: Antes, Después, y resultado 7


# --- CASO 2: Decorador donde el wrapper espera MÁS argumentos que la función original ---
def decorador_con_extra(func):
    # El wrapper recibe 3 argumentos, pero la función solo necesita 2
    def wrapper(a, b, c):
        print("Antes de la función")
        resultado = func(a, b)  # El tercero (c) no se pasa a la función
        print(f"Usando argumento extra solo en el decorador: {c}")
        print("Después de la función")
        return resultado
    return wrapper

@decorador_con_extra
def suma2(x, y):
    return x + y

print(suma2(1, 2, "Extra!"))  # 1 y 2 van a la función, "Extra!" solo el decorador lo usa


# --- CASO 3: Decorador que recibe argumentos propios (decorador parametrizado) ---
def decorador_parametrizado(param1, param2):
    # Esta función externa recibe parámetros solo para configurar el decorador
    def decorador(func):
        def wrapper(*args, **kwargs):
            print(f"[Decorador parametrizado] Param1: {param1}, Param2: {param2}")
            resultado = func(*args, **kwargs)
            print("Después de ejecutar la función decorada")
            return resultado
        return wrapper
    return decorador

@decorador_parametrizado("modo_debug", True)
def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("Juan")


# --- CASO 4: Decorador que usa *args para capturar argumentos extra por posición ---
def decorador_por_posicion(func):
    def wrapper(*args):
        # Supongamos que los dos primeros son para la función
        a, b = args[:2]
        # Y el tercero es un valor extra solo para el decorador
        extra = args[2] if len(args) > 2 else None

        print("Ejecutando decorador con posición fija")
        print(f"Valor extra (solo decorador): {extra}")
        resultado = func(a, b)
        return resultado
    return wrapper

@decorador_por_posicion
def multiplicar(x, y):
    return x * y

print(multiplicar(2, 5, "dato extra"))  # El "dato extra" solo lo usa el decorador


# --- CASO 5: Decorador que usa **kwargs para capturar claves extras para el decorador ---
def decorador_con_kwargs(func):
    def wrapper(*args, **kwargs):
        # Se extrae 'extra' si se pasó como keyword argument
        extra = kwargs.pop("extra", None)  # Lo sacamos para que no llegue a la función
        print("Decorador con kwargs")
        if extra:
            print(f"Argumento extra solo para el decorador: {extra}")
        return func(*args, **kwargs)  # Se pasa solo lo que la función espera
    return wrapper

@decorador_con_kwargs
def mostrar_mensaje(mensaje):
    print(f"Mensaje: {mensaje}")

mostrar_mensaje(mensaje="Hola mundo", extra="secreto decorador")


# ======================
# RESUMEN FINAL:
# - Si usas *args: debes saber el orden de los argumentos.
# - Si usas **kwargs: debes saber qué claves vas a usar para el decorador y separarlas con .pop().
# - No debes pasarle a la función decorada argumentos que no espera, o dará error.
# - Siempre puedes usar *args y **kwargs para hacer decoradores genéricos y seguros.
# ======================

#Ejemplo adicional
def requiere_admin(func):
    def wrapper(*args, **kwargs):
        if not kwargs.get('es_admin', False):
            print("Acceso denegado")
            return
        return func(*args, **kwargs)
    return wrapper

@requiere_admin
def eliminar_usuario(usuario, **kwargs):
    print(f"Usuario {usuario} eliminado")

# GENERADORES, es una funcion que permite devolver valores de forma paulatina, Un generador en Python es una forma especial de función que produce valores uno por uno, en lugar de calcular y devolver todos los valores a la vez como lo hace una función normal. Usa la palabra clave yield en lugar de return. Suspende su ejecución después de cada yield y la retoma desde ahí la próxima vez que se le llame. Produce una secuencia de valores, ideal para manejar grandes cantidades de datos sin consumir mucha memoria.

#Nota al entrar en pausa El generador mantiene un estado interno que incluye la posición del código y el contexto de variables locales.
def generador_ejemplo():
    yield 1
    yield 2
    yield 3

print(f'Primera generacion: {next(generador_ejemplo())}') #Para hacer una llamada y devuelva un valor se requiere la funcion next y luego la funcion generadora, si se pasa de next se genera un StopIteration por lo tanto es recomendable encapsular en un try/except

for valor in generador_ejemplo(): # Tambien si no se quiere usar next, en un bucle for se puede hacer uso de la funcion generadora
    print(f"Valor del generador: {valor}") #En el caso de for se detiene hasta el ultimo yield

#Ejemplo de generadores
def generadorNumeros(limite):
    for i in range(limite):
        yield i

print(type(generadorNumeros(5))) #Una funcion generadora se puede asocialr a una variable siendo q es un objeto de tipo generator

for numero in generadorNumeros(5):
    print(f"Numero generado: {numero}")

generador= generadorNumeros(5)
try:
    while True:
        print(f"Numero generado: {next(generador)}")
except StopIteration:
    pass

#Expresiones generadoras 
#Consiste en generar un generador anonimo en uan sola linea de codigo, su sisntaxis es (expr for item in iterable if condición) expr es la expresión que genera cada valor. Se usa paréntesis en lugar de corchetes (que serían para listas por comprensión).

generador= (i for i in range(5))
print(type(generador))  # <class 'generator'>
print(next(generador))  # Imprime 0

#Tambien se puede pasar una expresion generadora a una funcion
import math
suma= sum(i for i in range(5))

def funcion_con_generador(generador):
    for valor in generador:
        print(f"Valor del generador: {valor}")

# Tambien podemos usar una lista o cualquier otro iterador
lista = ["juan", "perez"]
generador= (print(i) for i in lista) #Generador que imprime cada elemento de la lista
for valor in generador:
    pass  # Ejecuta el generador, imprime "juan" y "perez"

#Crear un string a partir de un generador creador a partir de una lista
listaAyuda = ['hola', 'mundo']
contador=0
def incrementar_contador():
    global contador
    contador += 1
    return contador
# La primera parte es el yield y la segunda parte es el for
generador= (f'{incrementar_contador()}.{nombre}' for nombre in listaAyuda)
listaGenerada = list(generador)  # Convierte el generador en una lista, pues estara formando cada elemento por cada llamada
StringGenerada = ','.join(listaGenerada)
print(StringGenerada)  # Imprime: 1.hola,2.mundo

#Listas de compresion: Es una forma compacta y elegante de crear listas a partir de otras listas, iterables o rangos, aplicando una expresión y opcionalmente un filtro. Su sintaxis es [nueva_expresion for item in iterable if condicion], nueva_expresion: valor o transformación que quieres poner en la lista nueva. item: variable que representa cada elemento del iterable. iterable: cualquier objeto sobre el que puedas iterar (lista, rango, string, etc). if condicion (opcional): filtra los elementos que quieres incluir.
#Compresion normal
lista = [i for i in range(5)]
print(lista)  # Imprime: [0, 1, 2, 3, 4]

#Compresion con una condicion
lista= [ i for i in range(5) if i % 2 == 0]  # Filtra solo los números pares
print(lista)  # Imprime: [0, 2, 4]

#Compresion con asignacion dependiendo de valor
lista = [ 'par' if i % 2 == 0 else 'impar' for i in range(5) ] # Crea una lista de 'par' e 'impar' dependiendo de cierta condicion
print(lista)

#Compresion con mas de dos condiciones
pares= [numero for numero in range(10) if numero % 2 == 0 if numero % 6 == 0]
print(pares)  # Imprime: [0, 6]
#La sintaxis final seria [ expresión for variable in iterable if condición1 if condición2 ... ]

#Compresion con if-else en asignacion
lista_pares= []
lista_impares= []
[lista_pares.append(i) if i % 2 == 0 else lista_impares.append(i) for i in range(5)]
print(lista_pares)  # Imprime: [0, 2, 4]
print(lista_impares)  # Imprime: [1, 3]

#Compresion con operadores logicos
#[ expresión for variable in iterable if (condición1 and condición2) or condición3 ]
pares= [numero for numero in range(10) if (numero % 2 == 0 and numero % 6 == 0) or numero % 3 == 0]
print(pares)  # Imprime: [0, 3, 6, 9]

#Listas de listas
listaDeListas= [[1,2,3],[4,5,6],[7,8,9]]
lista= [valor for sublista in listaDeListas for valor in sublista] #Lo que pasa aqui es que primero se itera por cada sublista y luego por cada valor de la sublista, normalmente se veria como for sublista in listaDeListas: for valor in sublista:, es decir, valor se ignora, y primero vamos al for despues con esa sublista hacemos el otro for donde valor sera el q se almacena y finalmente se añade
lista = [valor 
         for sublista in listaDeListas 
            for valor in sublista] 
print(lista)  # Imprime: [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Lista con numeros pares apartir de sublista
listaPares= [valor 
             for sublista in listaDeListas
                for valor in sublista if valor % 2 == 0]

#Asignacion funciones a variables
# # 1. Función normal con def asignada a variable
# def saludar():
#     print("Hola")

# mi_funcion = saludar  # Asignar función a variable
# mi_funcion()          # Ejecutar: imprime "Hola"

# # 2. Función lambda asignada a variable
# mi_lambda = lambda x: x * 2
# print(mi_lambda(5))   # Imprime 10

# # 3. Closure: función interna que recuerda entorno
# def crear_multiplicador(n):
#     def multiplicar(x):
#         return x * n
#     return multiplicar

# doblar = crear_multiplicador(2)
# print(doblar(5))      # Imprime 10

# # 4. Función generadora asignada a variable
# def generador():
#     yield 1
#     yield 2

# g = generador         # g apunta a la función generadora
# gen_obj = g()         # gen_obj es el generador (iterador)
# print(next(gen_obj))  # Imprime 1
# print(next(gen_obj))  # Imprime 2


#Palabras reservadas
import keyword #Aqui se importan las palabras reservadas
print(keyword.kwlist) #Imprime la lista de palabras reservadas

#1. No podemos utilizar un keyword como nombre de variable
#2. No podemos nombrar una función con un keyword
#3. No podemos nombrar una clase con un keyword
#4. No podemos utilizar un keyword como nombre de módulo