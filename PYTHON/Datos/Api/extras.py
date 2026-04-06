#Pandas: Permite manipular y analizar datos de manera eficiente. Proporciona estructuras de datos como DataFrame y Series, que facilitan la manipulación de datos tabulares y la realización de operaciones como filtrado, agrupamiento y agregación. Principalmente se usa parara archivos CSV, Excel.

import pandas as pd
file = pd.read_csv('datos.csv')

# Si el csv no tiene encabezados podemos usar .columns para asignar nombres a las columnas
file.columns = ['columna1', 'columna2', 'columna3']


# JSON: Es un formato de datos ligero y fácil de leer que se utiliza comúnmente para intercambiar datos entre aplicaciones web. En Python, puedes usar la biblioteca json para trabajar con datos JSON. Puedes convertir un diccionario de Python a una cadena JSON utilizando json.dumps(), y puedes convertir una cadena JSON a un diccionario de Python utilizando json.loads(). Además, puedes leer y escribir archivos JSON utilizando json.load() y json.dump(), respectivamente.
import json
# Convertir un diccionario de Python a una cadena JSON
data = {'name': 'John', 'age': 30, 'city': 'New York'}
json_string = json.dumps(data)
print(json_string)  # Imprime la cadena JSON

# leer unn archivo JSON y convertirlo a un diccionario de Python
with open('data.json', 'r') as file:
    data = json.load(file)
print(data)  # Imprime el diccionario de Python con los datos del JSON

# Para leer xml podemos usar la biblioteca xml.etree.ElementTree, que proporciona funciones para analizar y manipular documentos XML. Puedes usar ElementTree.parse() para leer un archivo XML y obtener un objeto ElementTree, y luego puedes usar métodos como find(), findall() y iter() para navegar por la estructura del documento XML y extraer los datos que necesitas.
import xml.etree.ElementTree as ET
# Leer un archivo XML y obtener el elemento raíz
tree = ET.parse('data.xml')
root = tree.getroot()
# buscar un elemento específico en el XML
element = root.find('elemento')

# Bucle for : Podemos usar el bucle for para iterar sobre los nodos del XML y extraer los datos que necesitamos. Por ejemplo, si queremos imprimir el texto de todos los elementos <item> en un archivo XML, podemos usar el siguiente código:
for item in root.findall('item'):
    print(item.text)  # Imprime el texto contenido en cada elemento <item>