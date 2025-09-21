# Apunte completo: Procesamiento de JSON en Python

import json
from typing import Any, Dict, List

# 1. ¿Qué es JSON?
# JSON (JavaScript Object Notation) es un formato ligero de intercambio de datos, fácil de leer y escribir para humanos y máquinas.

# 2. Sintaxis básica de JSON
# - Objetos: { "clave": valor, ... }
# - Listas: [ valor1, valor2, ... ]
# - Valores: string, number, true, false, null

# 3. Módulo json de Python
# Permite convertir entre objetos Python y cadenas/archivos JSON.

# 4. Funciones principales del módulo json:
#   json.load(file)      -> Lee JSON desde un archivo y lo convierte a objeto Python
#   json.loads(str)      -> Lee JSON desde un string y lo convierte a objeto Python
#   json.dump(obj, file) -> Convierte objeto Python a JSON y lo escribe en un archivo
#   json.dumps(obj)      -> Convierte objeto Python a JSON en un string

# ¿Qué devuelven las funciones principales del módulo json?
# - json.load(fp): Devuelve un objeto Python (dict, list, etc.) leído desde un archivo JSON. Si el JSON es un objeto (es decir, está entre {}), json.load() devuelve un diccionario (dict) de Python. Si el JSON es un array (es decir, está entre []), devuelve una lista (list) de Python.
# - json.loads(s): Devuelve un objeto Python (dict, list, etc.) leído desde un string JSON.
# - json.dump(obj, fp): Escribe el objeto Python como JSON en un archivo. Devuelve None.
# - json.dumps(obj): Devuelve un string JSON representando el objeto Python.

# Argumentos opcionales de las funciones del módulo json:
# json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
#   - cls: clase personalizada para el decodificador
#   - object_hook: función para transformar dicts en objetos personalizados
#   - parse_float, parse_int, parse_constant: funciones para convertir números y constantes
#   - object_pairs_hook: función para transformar pares clave-valor
#
# json.loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
#   - Igual que json.load pero para strings
#
# json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
#   - skipkeys: ignora claves no string
#   - ensure_ascii: True para escapar caracteres no ASCII
#   - check_circular: detecta referencias circulares
#   - allow_nan: permite NaN, Infinity, -Infinity
#   - cls: clase personalizada para el codificador
#   - indent: número de espacios para indentar
#   - separators: tupla para separar elementos (por defecto (', ', ': '))
#   - default: función para serializar tipos no soportados
#   - sort_keys: ordena las claves alfabéticamente
#
# json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
#   - Igual que json.dump pero para strings
#

# 5. Ejemplo: Leer JSON desde archivo
with open('personas.json', 'r', encoding='utf-8') as f:
    personas: List[Dict[str, Any]] = json.load(f)
print("Personas desde archivo:", personas)

# 6. Ejemplo: Leer JSON desde string
json_str = '[{"nombre": "Ana", "edad": 25}]'
personas2 = json.loads(json_str)
print("Personas desde string:", personas2)

# 7. Ejemplo: Escribir JSON a archivo
nueva_persona = {"nombre": "Luis", "edad": 28, "email": "luis@email.com"}
personas.append(nueva_persona)
with open('personas_mod.json', 'w', encoding='utf-8') as f:
    json.dump(personas, f, indent=2, ensure_ascii=False)

# 8. Ejemplo: Convertir objeto Python a string JSON
json_nuevo = json.dumps(nueva_persona, indent=2, ensure_ascii=False)
print("JSON como string:\n", json_nuevo)

# 9. Opciones útiles de json.dump/json.dumps:
#   indent: número de espacios para indentar (mejor legibilidad)
#   ensure_ascii: False para permitir caracteres especiales (ñ, á, etc.)
#   sort_keys: True para ordenar las claves alfabéticamente

# 10. Convertir JSON a objetos personalizados (dataclass)
from dataclasses import dataclass
@dataclass
class Persona:
    nombre: str
    edad: int
    email: str = ""

# Convertir lista de dicts a lista de objetos Persona
def dicts_a_personas(lista_dicts: List[Dict[str, Any]]) -> List[Persona]:
    return [Persona(**d) for d in lista_dicts]

personas_obj = dicts_a_personas(personas)
print("Lista de objetos Persona:", personas_obj)

# 11. Convertir objetos a JSON (serialización)
def persona_a_dict(persona: Persona) -> Dict[str, Any]:
    return persona.__dict__

json_personas = json.dumps([persona_a_dict(p) for p in personas_obj], indent=2, ensure_ascii=False)
print("Personas serializadas a JSON:\n", json_personas)

# 12. Manejo de errores
try:
    json.loads('{nombre: Ana, edad: 25}')  # Error: claves sin comillas
except json.JSONDecodeError as e:
    print("Error de decodificación:", e)

# 13. Leer solo parte del archivo (streaming, archivos grandes)
#   Usar json.load() lee todo el archivo en memoria. Para archivos muy grandes, usar librerías como ijson.

# 14. Otras utilidades
#   - json.JSONEncoder y json.JSONDecoder para personalizar la serialización/deserialización
#   - Soporte para tipos personalizados (ver documentación oficial)

# Resumen:
# - json.load()/loads() -> JSON a Python
# - json.dump()/dumps() -> Python a JSON
# - Manejo de archivos, strings, errores y objetos personalizados
# - Opciones para formato, codificación y orden de claves
