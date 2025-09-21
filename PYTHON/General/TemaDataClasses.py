#DataClasses, es un modulo de python qur provee decoradores y funciones para facilitar la creación de clases que se utilizan principalmente para almacenar datos. Su objetivo principal es simplificar la creación de clases que son esencialmente "contenedores de datos", eliminando la necesidad de escribir métodos especiales como __init__, __repr__ y __eq__ manualmente.

from dataclasses import dataclass, ClassVar

@dataclass(eq=False, frozen=True)
class Persona:
    nombre: str #Se indican los atributos de la clase especificando su tipo de dato
    edad: int = 0 #De manera opcional se puede asignar un valor por defecto
    direccion: str
    contador_Persona : ClassVar[int] = 0 # Para asignar atributos de clase se usa la sintaxis de ClassVar[tipoDato]= valorDefault

    #Metodo post_init, se utiliza para realizar inicializaciones o validaciones adicionales al metodo init
    def __post_init__(self):
        if self.edad < 0:
            raise ValueError("La edad no puede ser negativa")
        Persona.contador_Persona += 1

    #Si queremos ir haciendo una modificacion de un atributo de la clase
persona1= Persona("Juan", 30, "Calle Falsa 123") #Se crea una instancia de la clase Persona
print(persona1)  # Imprime: Persona(nombre='Juan', edad=30, direccion='Calle Falsa 123')

#Revisar igualdar entre objetos, aqui se implementa el metodo eq
persona2= Persona("Juan", 30, "Calle Falsa 123")
print(persona1 == persona2)  # Imprime: True

#Agregar clase a una coleccion
coleccion= [persona1, persona2] #En natural un objeto debe ser inmutable sin embargo si queremos que esto no pase se agrega el decorador frozen como true a dataclass


"""

Qué puedes hacer con dataclasses:
- Definir clases simples para almacenar datos sin escribir mucho código.
- Generar automáticamente métodos como __init__, __repr__, __eq__, __lt__, etc.
- Establecer valores por defecto para atributos.
- Crear clases inmutables con frozen=True.
- Definir campos que no se inicializan en el constructor.
- Usar campos con valores mutables seguros con default_factory.
- Personalizar la representación con repr=False.
- Excluir campos de comparación y hashing.
- Usar InitVar para recibir argumentos temporales en __init__.
- Crear jerarquías (herencia) con dataclasses.
- Validar o modificar datos tras la creación con __post_init__.
- Convertir objetos a diccionario o tupla con asdict() y astuple().
- Definir opciones para comparación, orden, hashing y más.

---

Cómo usar dataclasses:
- Importar el decorador y funciones desde dataclasses.
- Declarar clases con @dataclass.
- Definir atributos con anotaciones de tipo (opcional pero recomendado).
- Opcionalmente usar field() para personalizar atributos.
- Definir __post_init__ para inicialización/validación extra.
- Pasar argumentos opcionales al decorador para controlar comportamiento.

---

Argumentos que acepta @dataclass:

- init: bool (default True)  
  Genera o no el método __init__.

- repr: bool (default True)  
  Genera o no el método __repr__.

- eq: bool (default True)  
  Genera o no el método __eq__.

- order: bool (default False)  
  Genera métodos de comparación (<, <=, >, >=).

- unsafe_hash: bool (default False)  
  Genera método __hash__ aunque la clase no sea inmutable.

- frozen: bool (default False)  
  Hace la instancia inmutable (los atributos no se pueden modificar).
---
"""

from dataclasses import dataclass, field, InitVar, asdict, astuple

# ---------------------------------------------
# 1. Declaración básica de una dataclass
# ---------------------------------------------
@dataclass
class Persona:
    """
    Clase básica con dataclass.
    Define atributos con anotaciones de tipo.
    Python genera automáticamente:
      - __init__: constructor
      - __repr__: representación en string
      - __eq__: comparación de igualdad
    """
    nombre: str           # atributo obligatorio sin valor por defecto
    edad: int = 30        # atributo con valor por defecto


# ---------------------------------------------
# 2. Campos que no se incluyen en __init__
# ---------------------------------------------
@dataclass
class PersonaConID:
    """
    Usamos field(init=False) para no incluir 'id' en el constructor.
    Se inicializa en __post_init__ después de __init__.
    """
    nombre: str
    edad: int
    id: int = field(init=False)

    def __post_init__(self):
        # Inicializamos id basado en nombre
        self.id = hash(self.nombre)


# ---------------------------------------------
# 3. Campos con valores mutables usando default_factory
# ---------------------------------------------
@dataclass
class Grupo:
    """
    Para evitar que todas las instancias compartan la misma lista,
    usamos default_factory para crear una lista nueva por instancia.
    """
    miembros: list = field(default_factory=list)


# ---------------------------------------------
# 4. Opciones avanzadas en @dataclass
# ---------------------------------------------
@dataclass(order=True, frozen=True, unsafe_hash=True)
class Producto:
    """
    order=True genera métodos de comparación (<, >, etc.) basados en el orden
    de los campos declarados.

    frozen=True hace la instancia inmutable (atributos no se pueden cambiar).

    unsafe_hash=True fuerza la generación de __hash__ aun cuando frozen=False.
    """
    nombre: str
    precio: float
    codigo: str = field(compare=False)  # campo excluido de comparación


# ---------------------------------------------
# 5. Ocultar campos en __repr__
# ---------------------------------------------
@dataclass
class Usuario:
    """
    repr=False en el field hace que el campo no aparezca en la representación.
    Útil para ocultar datos sensibles como contraseñas.
    """
    nombre: str
    password: str = field(repr=False)


# ---------------------------------------------
# 6. Herencia con dataclasses
# ---------------------------------------------
@dataclass
class Empleado(Persona):
    """
    Se heredan atributos y métodos de Persona.

    El constructor generado incluye los campos de ambas clases.
    """
    salario: float


# ---------------------------------------------
# 7. Método __post_init__ para validaciones o inicialización extra
# ---------------------------------------------
@dataclass
class PersonaConValidacion:
    nombre: str
    edad: int

    def __post_init__(self):
        # Validamos que la edad sea válida
        if self.edad < 0:
            raise ValueError("Edad no puede ser negativa")


# ---------------------------------------------
# 8. Campos excluidos de comparación o hashing
# ---------------------------------------------
@dataclass(eq=True, frozen=True)
class PersonaSinEdadEnEq:
    """
    El campo edad no se incluye en comparación ni hashing
    (por ejemplo, para ignorar campos que no afectan identidad).
    """
    nombre: str
    edad: int = field(compare=False)


# ---------------------------------------------
# 9. Uso de InitVar para argumentos solo del constructor
# ---------------------------------------------
@dataclass
class PersonaConInitVar:
    nombre: str
    edad: int
    edad_legal: InitVar[int]  # parámetro solo en __init__, no se guarda como atributo

    def __post_init__(self, edad_legal):
        # Creamos atributo derivado basado en InitVar
        self.mayor_de_edad = self.edad >= edad_legal


# ---------------------------------------------
# 10. Convertir a diccionario y a tupla
# ---------------------------------------------
def ejemplos_asdict_astuple():
    p = Persona("Ana", 25)
    print("Como diccionario:", asdict(p))  # {'nombre': 'Ana', 'edad': 25}
    print("Como tupla:", astuple(p))        # ('Ana', 25)

#Nota tambien se puede Puedes tener campos que son otras dataclasses, lo que permite estructuras complejas anidadas fácilmente:
@dataclass
class Direccion:
    calle: str
    ciudad: str

@dataclass
class Persona:
    nombre: str
    direccion: Direccion

# ---------------------------------------------
# Programa principal para probar ejemplos
# ---------------------------------------------
if __name__ == "__main__":
    # 1. Dataclass básica
    persona = Persona("Luis")
    print(persona)  # Persona(nombre='Luis', edad=30)

    # 2. Campo init=False con post_init
    persona_id = PersonaConID("Ana", 28)
    print(persona_id)  # PersonaConID(nombre='Ana', edad=28, id=...hash...)

    # 3. Campo mutable con default_factory
    grupo = Grupo()
    grupo.miembros.append(persona)
    print(grupo)  # Grupo(miembros=[Persona(nombre='Luis', edad=30)])

    # 4. Opciones avanzadas
    producto = Producto("Camiseta", 19.99, "A001")
    print(producto)
    # producto.precio = 25.0  # Error: frozen=True, instancia inmutable

    # 5. Ocultar campo en __repr__
    usuario = Usuario("admin", "123456")
    print(usuario)  # Usuario(nombre='admin')

    # 6. Herencia
    empleado = Empleado("Marta", 40, 50000)
    print(empleado)

    # 7. Validación en __post_init__
    try:
        p_inv = PersonaConValidacion("Carlos", -5)
    except ValueError as e:
        print(f"Error: {e}")

    # 8. Campo excluido de comparación
    p1 = PersonaSinEdadEnEq("Juan", 25)
    p2 = PersonaSinEdadEnEq("Juan", 30)
    print(p1 == p2)  # True, porque edad se ignora en comparación

    # 9. InitVar y atributo derivado
    p3 = PersonaConInitVar("Laura", 20, edad_legal=18)
    print(p3.mayor_de_edad)  # True

    # 10. asdict y astuple
    ejemplos_asdict_astuple()
