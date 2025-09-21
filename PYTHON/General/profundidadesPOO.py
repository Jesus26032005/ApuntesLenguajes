#Atributos de clase y objetos
import inspect


class Persona:
    # Atributo de clase
    numeroPersona = 0 #Se puede acceder desde la clase o desde las instancias, siendo ya sea pasando como cls.numeroPersona o Persona.numeroPersona, la diferencia es que cls hace referencia a la clase actual y permite modificar el atributo de clase desde dentro de métodos de instancia y Persona se usa mas para acceder a el sin necesidad de una instancia

    def __init__(self,nombre, edad):
        # Atributos de instancia, son aquellos que pertenecen a cada objeto individualmente
        self.nombre = nombre
        self.edad = edad
        self.id = Persona.numeroPersona  # Asignar un ID único basado en el contador de personas
        Persona.numeroPersona += 1  # Incrementar el contador de personas al crear una nueva instancia


    #Nota: Nunca tener self y cls juntos pues indivualmente significan diferentes metodos

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Especie: {Persona.numeroPersona}, ID: {self.id}")

# Crear instancias de la clase
persona1 = Persona("Juan", 30)
persona2 = Persona("Maria", 25)

# Acceder a los atributos de instancia
persona1.mostrar_info()
persona2.mostrar_info()

#Modificar atributo de instancia
persona1.edad = 31
persona2.nombre = "Ana" #Funciona si son publicos

# Acceder al atributo de clase
print(Persona.numeroPersona)
print(persona1.numeroPersona) #Se puede acceder al atributo de clase usando una instancia, sin embargo para modificarlo se tiene que usar la propia clase

#Modificar atributo de clase
persona1.numeroPersona = 5 #El atributo se vuelve un atributo de instancia, por lo tanto no estamos modificando el de clase, no se añade dicho atributo a las demas instancias
print(persona1.__dict__) #Devuelve los atributos de instancia
Persona.numeroPersona = 10 #Modificando el atributo de clase directamente desde la clase, esto es valido

#Añadir atributo nuevo a instancia
persona1.direccion = "Calle Falsa 123"
print(persona1.direccion)

#Añadir atributo a una clase
Persona.especie = "Humano" #Esto añade un atributo de clase que puede ser accedido por todas las instancias, no es recomendable hacer esto ni lo de atributis
print(Persona.especie)

#Añadir metodos a una clase
def mostrar_especie(cls):
    print(f"Especie: {cls.especie}")

Persona.mostrar_especie = mostrar_especie  # Añadir el método a la clase
#Se pueden añadir decoradores a las funciones que se añadan siendo de la siguiente forma; ya sea staticmethod o classmethod
def mostrar_especie(cls):
    print(f"Especie: {cls.especie}")
Persona.mostrar_especie = staticmethod(mostrar_especie)  # Añadir el método como un método de clase


class Persona:
    contador_personas = 0

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# Mostrar los atributos de un objeto
persona1 = Persona('Juan','Perez')
print(persona1.__dict__)

# Crear un atributo al vuelo
print(persona1.contador_personas) # Accediendo al atributo de clase
# Pero no es posible modificarlo con el objeto, sino con la clase
persona1.contador_personas = 10
print(persona1.__dict__)
# El atributo anterior oculta al atributo de clase
print(Persona.contador_personas) # Atributo clase
print(persona1.contador_personas) # Atributo del objeto 1

# Un segundo objeto
persona2 = Persona('Karla', 'Gomez')
print(persona2.__dict__)
print(persona2.contador_personas)

# Asociar un atributo de clase al vuelo
Persona.contador2 = 20
print(Persona.contador2)

# Desde los objetos creados, accedemos al nuevo atributo de la clase
# Esto es posible por que los atributos de clase se comparten con todos los objetos
print(persona1.contador2)
print(persona2.contador2)


#SOBRECARGA DE CONSTRUCTORES
#Simulacion de sobrecarga de constructores, consiste en tener varios metodos classmethod que actuan como consturctores secundarios
class humano:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    @classmethod
    def crearHumanoVacio(cls):
        return cls("","") #Manda a llamar al metodo init al usar cls()

    @classmethod
    def crearHumanoConDatos(cls, nombre, apellido):
        return cls(nombre, apellido)
    
humano1= humano.crearHumanoVacio()
humano2= humano.crearHumanoConDatos("Juan", "Perez")


#REPRESENTACION DE OBJETOS 
# Metodo repr, Su objetivo principal es que al imprimir el objeto (por ejemplo, en la consola o al usar repr(obj)), devuelva una cadena que ayude a identificar el objeto y, preferiblemente, que sea una expresión válida para recrear el objeto.Es usado por desarrolladores para debugging y logging.

"""
Aspecto	__str__
epresentación amigable para usuarios (legible y bonita)
Cuando usas print(obj) o str(obj)
Texto fácil de leer y entender
Opcional (si no está, se usa __repr__)
"Persona: Ana, 30 años"	

Aspecto __repr__
Representación oficial y detallada (para desarrolladores)
Cuando usas repr(obj) o en consola interactiva (por ejemplo, al escribir solo obj)
Texto que idealmente puede usarse para recrear el objeto (como código Python)
Recomendado para debugging y logging
"Persona('Ana', 30)"
"""

class carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __repr__(self): #Esta mas orientada al programador
        return f"{self.__class__.__name__}(marca='{self.marca}', modelo='{self.modelo}')" #Se recomienda q el retorno sea mas pareciod a cuando esta en codigo siendo un formato algo asi objeto(atributo=valor,....)
    
    #Se puede obtener el nmbre declase usando obj.__clas__.__name__ o con type(obj).__name__

    def __str__(self): #Esta mas orientada al usuario
        return f"Carro: {self.marca} {self.modelo}"
    #Si no esta definido el metodo __str__, se usara __repr__ por defecto

    
carro1= carro("xd", "xd2")
print(carro1)
print(repr(carro1)) #Se puede llamar asi
print(f'{carro1!r}') # O usando !r para que se mande a llamar el metodo repr

#ATRIBUTOS EN PYTHON
#PUBLICOS, PRIVADOS Y PROTEGIDOS
class MiClase:
    def __init__(self):
        self.atributo_publico = "Soy un atributo público" # Atributo público, accesible desde fuera de la clase se escribe con un solo guion bajo
        self._atributo_protegido = "Soy un atributo protegido" # Atributo protegido, accesible desde la clase y subclases, se escribe con un guion bajo
        self.__atributo_privado = "Soy un atributo privado" # Atributo privado, solo accesible desde la clase, se escribe con dos guiones bajos

        #Para acceder y modificar a los atributos publicos se puede hacer como objeto.atributo_publico. Aunque nos deje tambien los protegidos, los privados ya mandan un error.
        #Para acceder y modificar un atributo privado y modificarlo existe la opcion de objeto._MiClase__atributo_privado

        #Sin embargo, para acceder a los atributos protegidos y privados, se recomienda hacerlo haciendo uso de métodos getter y setter. Usando decoradores @property y @atributo.setter

    def mostrar_atributos(self):
        print(self.atributo_publico)
        print(self._atributo_protegido)
        print(self.__atributo_privado)

objeto = MiClase()
objeto.mostrar_atributos()


#ORDEN DE INCIALIZACION DE OBJETOS
class padre:
    def __init__(self):
        print("iniciando padre")

    def metodo(self):
        print("metodo de padre")

class hijo(padre):
    def __init__(self):
        print("iniciando hijo")  
        super().__init__()        #De manera opcional se puede mandar a llamar al metodo __init__ de la clase padre haciendo uso de la palabra clave super() y posteriormente el metodo que en este caso es el init
    
    def metodo(self): #Al sobreescribir un metodo de la clase padre, ya no se llama este al menos que se use el metodo super, si no exisitiera el meodo se llama al de la clasepadre
        print("metodo de hijo")
        super().metodo()

padre1 = padre()
padre1.metodo()

hijo1 = hijo() # Al crear un objeto de la clase hijo, si no hay metodo init, se llama al de la clase padre.
hijo1.metodo()

# Ejemplos herencia simple
class listaSimple:
    def __init__(self, elementos: list):
        self.elementos = list(elementos)

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def mostrar(self):
        for elemento in self.elementos:
            print(elemento)

    def __getitem__(self, index: int): #El metodo Este método permite acceder a elementos del objeto usando la sintaxis de corchetes (obj[key]), como si fuera una lista o diccionario.
        return self.elementos[index]

    def __len__(self): #Este método permite usar la función len(objeto) sobre tu clase personalizada, como si fuera una lista.
        return len(self.elementos)

    def ordenar(self):
        self.elementos.sort()

lista = listaSimple([3, 1, 4, 2])
print(lista.mostrar())  # Muestra los elementos
lista.agregar(5)  # Agrega un elemento
print(lista.mostrar())  # Muestra los elementos nuevamente
print(lista.ordenar())

# Ejemplo de herencia simple
class ListaSimple:
    def __init__(self, elementos):
        self._elementos = list(elementos)

    def agregar(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self, indice):
        return self._elementos[indice]

    def ordenar(self):
        self._elementos.sort()

    def __len__(self):
        return len(self._elementos)

    def __repr__(self):
        return f'{self.__class__.__name__}({self._elementos!r})'
class ListaOrdenada(ListaSimple):
    def __init__(self, elementos=[]):
        super().__init__(elementos)
        # Ordenamos siempre los elementos una vez inicializados
        self.ordenar() #Se hereda el  metodo de la clase padrepor tanto se puede usar

    def agregar(self, elemento):
        super().agregar(elemento)
        # Ordenamos el nuevo elemento
        self.ordenar()

# Lista sólo acepta números
class ListaEnteros(ListaSimple):
    def __init__(self, elementos=[]):
        for elemento in elementos:
            self._validar(elemento)
        # Una vez validados los elementos, los agregamos
        super().__init__(elementos)

    def _validar(self, elemento):
        # Validamos si el elemento es de tipo entero
        if not isinstance(elemento, int):
            raise ValueError(f'No es un valor entero: {elemento}')

    # Sobreescribimos el método agregar de la clase padre
    def agregar(self, elemento):
        self._validar(elemento)
        # Una vez validado lo agregamos a la lista
        super().agregar(elemento)

# Lista simple
lista_simple = ListaSimple([5, 3, 6, 8])
print(lista_simple)
# Lista ordenada
lista_ordenada = ListaOrdenada([4,3,6,9,10,-1])
print(lista_ordenada)
lista_ordenada.agregar(-14)
print(lista_ordenada)
print(len(lista_ordenada))
#Lista enteros
lista_enteros = ListaEnteros([1, 3, 4, -15])
print(lista_enteros)

# Herencia multiple 
class ListaEnterosOrdenada(ListaEnteros, ListaOrdenada):
    pass

listaIntOrdenada = ListaEnterosOrdenada([4, 3, 6, 9, 10, -1])
print(listaIntOrdenada) #Como no tiene metodo init, se llama a los de las clases padre
listaIntOrdenada.agregar(-14) # Manda a lalamar al metodo agregar de ListaEnteros, sin embargo como esta tiene super, ahora se manda a llamar al siguiente clase padre q es listaOrdenada y finalmente como este tiene superahora va mandar al de listasimple
print(listaIntOrdenada)
try:
    listaIntOrdenada = ListaEnterosOrdenada([4, 3, 6, 9, 10, -1])
except ValueError as e:
    print(e) #Manda a llamar al metodo _validar primero al metodo agregar de listaEnteros y posterirmente de listaOrdenada

#Saber clases padre y su orden
print(ListaEnterosOrdenada.__mro__) #MRO es el método de resolución de orden, donde nos dice como va el orden
#El MRO es la lista de clases que Python revisa, en orden, para encontrar un método o atributo cuando lo llamas sobre un objeto.


#Nota: super() en las clases llama al siguiente método en el orden de resolución de métodos (MRO) después de la clase actual, no necesariamente al padre directo.

"""
Reglas clave:
Funciona según el MRO (ClaseActual.__mro__).
No se limita al padre inmediato.
En herencia múltiple permite que todas las clases participen.
Evita escribir el nombre explícito de la clase padre.
Cuándo usarlo:
En métodos sobreescritos para añadir y no reemplazar completamente la lógica del padre.
En constructores (__init__) para inicializar todas las clases base.
En herencia múltiple para no romper la cadena de llamadas.


| Característica  | Herencia simple                              | Herencia múltiple                                                 |
| --------------- | -------------------------------------------- | ----------------------------------------------------------------- |
| **Definición**  | Una clase hereda de **una sola** clase base. | Una clase hereda de **dos o más** clases base.                    |
| **Sintaxis**    | `class Hija(Padre): ...`                     | `class Hija(Padre1, Padre2, ...): ...`                            |
| **MRO**         | Lineal y predecible.                         | Usa algoritmo **C3 Linearization** para definir orden.            |
| **`super()`**   | Salta al padre único.                        | Salta al siguiente en el **MRO** (no siempre el padre “directo”). |
| **Ventajas**    | Simplicidad, fácil de leer y mantener.       | Permite combinar comportamientos de varias clases.                |
| **Desventajas** | Menos flexibilidad.                          | Más compleja, riesgo de ambigüedad si no se entiende el MRO.      |
| **Ejemplo**     | `class Perro(Animal)`                        | `class PerroRobot(Perro, Robot)`                                  |
"""

class clasea:
    def __init__(self):
        print("iniciando clase A")

class claseb(clasea):
    def __init__(self):
        print("iniciando clase B")
        super().__init__()

class clasec(clasea):
    def __init__(self):
        print("iniciando clase C")
        super().__init__()

class clased(claseb, clasec): #El orden de las clases padre afecta al orden de inicializacion
    def __init__(self):
        print("iniciando clase D")
        super().__init__()
        clasec.__init__(self)  #Para mandar a llamar metodos init de clases propias se hace lo siguiente clasec.__init__(self)
        #Si queremos usar metodos de clases padres usamos la sintaxis clasePadre.metodo(argumentos)

print(clased.__mro__) #MRO, el cual es D, B, C, A
print(clased())
#Generalmente se recomienda usar super() para llamar a los métodos de las clases padre en lugar de hacerlo directamente pues se cumple con lo que es herencia multiple

#Nota recordar que siempre se heredan los metodos, por lo tanto tambien su orden de invocacion sigue a MRO
#En resumen cuando usamos super en herencia multiple, lo que pasa es que se sigue el orden MRO, el orden en que se acomodan las clases en la jerarquia de herencia siendo que aunque una clase padre sea hija de una, si hay otro padre, se lalamara al metodo de dicha clase si es que existe

#Metodo isinstance, verifica si un objeto es instancia de una clase o de una subclase, su sintaxis es isinstance(objeto, clase),siendo True si es instancia y False si no lo es, si fuera una instancia de una clase padre, se consideraría también como instancia de la clase base
print(isinstance(clased(), object)) #True, devuelve porque objeect es una clase padre de todas las clases
#Tambien se puede usar para verificar si la instancia es de un tipo de dato
print(isinstance(5, int)) #True
print(isinstance("hola", str)) #True
print(isinstance(5.0, float)) #True
print(isinstance(clased(), clased)) #True
#Se puede pasar una tupla de clases para saber si un objeto es instancia de alguna de ellas
print(isinstance(clased(), (clased, str, int))) #True

#Decoradores de clase
#Permiten transformar de manera sencilla y elegante el comportamiento de las clases, es similar a los decoradores de funciones. Los decoradores de clase en Python son funciones que reciben una clase como argumento y devuelven una nueva clase (o la misma, posiblemente modificada). Se usan para modificar o extender el comportamiento de una clase sin cambiar su código fuente directamente.

def decoradorREPR(cls):
    print("Ejecutando decorador")
    print(f"Clase original: {cls.__name__}")
    
    # Revisamos los atributos de la clase con el método vars
    atributos = vars(cls)
    print(f'Atributos de la clase {cls.__name__}: {atributos}')
    # Iteramos cada atributo
    # for nombre, atributo in atributos.items():
    #     print(nombre, atributo)

    # Revisamos si se ha sobreescrito el método __init__
    if '__init__' not in atributos:
        raise TypeError(f'{cls.__name__} no ha sobreescrito el método __init__')

    firma_init = inspect.signature(cls.__init__) #Devuelve la firma del metodo q se pase, la sintaxis es inspect.signature(metodo) y su retorno devuelve un diccionario con los parametros
    print(f'Firma método __init__: {firma_init}')
    # Recuperamos los parámetros, excepto el primero que es self
    parametros_init = list(firma_init.parameters)[1:]
    print(f'Parámetros init: {parametros_init}')

    # Revisamos si cada parámetro tiene un método property asociado
    for parametro in parametros_init:
        # property es un valor de tipo built-in para preguntar si
        # se está utilizando el decorador property, el metdo get es como atributos[parametro] pero para evitar eerror
        es_metodo_property = isinstance(atributos.get(parametro), property) #el get devuelve el valor asociado a la key

    # Crear el método repr dinámicamente
    def metodo_repr(self):
        # Obtenemos el nombre de la clase dinámicamente
        nombre_clase = self.__class__.__name__
        print(f'Nombre clase: {nombre_clase}')

        # Obtenemos los nombres de las propiedades y sus valores dinámicamente
        # Expresion Generadora, crear nombre_atr=valor_atr
        generador_arg = (f'{nombre}={getattr(self, nombre)}' for nombre in parametros_init) 
        #La sintaxis del metodo getattr es getattr(objeto, "atributo") que devuelve el valor del atributo
        # Lista del generador
        lista_arg = list(generador_arg)
        #Cadena de la lista
        argumentos = ', '.join(lista_arg)
        print(f'Argumentos del método repr: {argumentos}')
        # Creamos la forma del método __repr__, sin su nombre, solo el resultado 
        resultado_metodo_repr = f'{nombre_clase}({argumentos})'
        print(f'Resultado método repr: {resultado_metodo_repr}')
        return resultado_metodo_repr

    setattr(cls, "__repr__", metodo_repr) # Agrega el método __repr__ a la clase, la función setattr tiene la siguiente sintaxis setattr(clase, "atributo", valor)

    return cls #Siempre debe de existir el return cls pues este regresa 


"""La función vars() en Python se usa para obtener el diccionario de atributos de un objeto, es decir, un mapeo de los nombres de atributos a sus valores actuales.

Qué hace vars():
Si le pasas un objeto, devuelve su atributo __dict__ (los atributos del objeto en forma de diccionario). Devuelve el diccionario __dict__ del objeto: los atributos que ese objeto tiene asignados directamente (nombre → valor).
Si no recibe argumento, devuelve el diccionario local actual (igual que locals()).
Si se pasa una clase, devuelve el diccionario __dict__ de la clase: los atributos y métodos definidos en la clase (no los de cada instancia).Los property en Python son descriptores definidos en la clase, normalmente con el decorador @property.Estos property son objetos que viven en el diccionario de la clase bajo el nombre del atributo (la propiedad).
"""


@decoradorREPR #Cuando añadimos un decorador, lo primero que se crea al crear un objeto es el metodo decorador
class Persona: 
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self._nombre} {self._apellido} y tengo {self.edad} años.")

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido
    
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @apellido.setter
    def apellido(self, valor):
        self._apellido = valor

persona = Persona("Juan", "Perez",5)


# -----------------------------
# Apunte: Decoradores de clase en Python
# -----------------------------
# Cosas que puedes hacer con un decorador de clase:
# 1. Agregar métodos o atributos a la clase (y mantenerlos si ya existen)
# 2. Registrar clases automáticamente
# 3. Modificar comportamiento o metadatos
# 4. Aplicar patrones como Singleton o añadir validaciones
# 5. Decorar todas las instancias (interceptar creación, etc.)

registro_clases = []

def decorador_completo(cls):
    # 1. Agregar métodos o atributos (si no existen)
    if not hasattr(cls, "nuevo_metodo"): # El metodo hasattr verifica si el atributo existe
        def nuevo_metodo(self):
            print("Método agregado por decorador")
        cls.nuevo_metodo = nuevo_metodo # Agrega el nuevo método a la clase
    if not hasattr(cls, "nuevo_atributo"):
        cls.nuevo_atributo = "Valor agregado" # Agrega el nuevo atributo a la clase

    # 2. Registrar la clase automáticamente
    registro_clases.append(cls) 

    # 3. Modificar comportamiento o metadatos
    cls.es_decorada = True

    # 4. Aplicar patrón Singleton (opcional)
    # Descomenta para activar Singleton
    # instancia = None
    # def __new__(cls_, *args, **kwargs):
    #     nonlocal instancia
    #     if instancia is None:
    #         instancia = super(cls_, cls_).__new__(cls_, *args, **kwargs)
    #     return instancia
    # cls.__new__ = staticmethod(__new__)

    # 5. Decorar instancias: interceptar creación
    original_init = cls.__init__
    def nuevo_init(self, *args, **kwargs):
        print(f"Creando instancia de {cls.__name__}")
        original_init(self, *args, **kwargs)
    cls.__init__ = nuevo_init

    return cls

@decorador_completo
class PersonaDecorada:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self):
        print(f"Hola, soy {self.nombre}")

# Pruebas
p = PersonaDecorada("Ana")
p.saludar()              # Hola, soy Ana
p.nuevo_metodo()         # Método agregado por decorador
print(p.nuevo_atributo)  # Valor agregado
print(PersonaDecorada.es_decorada) # True
print(registro_clases)   # [<class '__main__.PersonaDecorada'>]