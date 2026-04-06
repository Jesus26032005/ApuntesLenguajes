# El web scraping consist en extraer información de sitios web. Es una técnica utilizada para recopilar datos de páginas web de manera automatizada. En Python, existen varias bibliotecas que facilitan el proceso de web scraping, como BeautifulSoup, Scrapy y Selenium.

# BeautifulSoup es una biblioteca de Python que permite analizar y extraer información de documentos HTML y XML. Es fácil de usar y proporciona una forma sencilla de navegar por la estructura del documento para encontrar los datos que necesitas. Puedes usar BeautifulSoup para buscar elementos específicos, como etiquetas, clases o atributos, y extraer su contenido.

# Para realizar web scraping con BeautifulSoup, primero debes enviar una solicitud HTTP a la página web que deseas analizar utilizando la biblioteca Requests. Luego, puedes pasar el contenido de la respuesta a BeautifulSoup para analizarlo y extraer la información que necesitas.
from bs4 import BeautifulSoup
import requests

# Ejemplo de web scraping con BeautifulSoup
url = 'https://www.example.com'
response = requests.get(url)
# EN este caso response.text contiene el contenido HTML de la página web, que luego se pasa a BeautifulSoup para su análisis. El segundo argumento 'html.parser' indica que se utilizará el analizador HTML incorporado de Python para procesar el contenido.
soup = BeautifulSoup(response.text, 'html.parser')
# AUnque html.parse es el analizador incorporado de Python, también puedes usar otros analizadores como lxml o html5lib, que pueden ofrecer un rendimiento mejorado o una mayor compatibilidad con ciertos tipos de documentos HTML. Para usar lxml, por ejemplo, simplemente cambia 'html.parser' por 'lxml' al crear el objeto BeautifulSoup.

print(soup) # Imprime el contenido HTML de la página web


# Puedes usar BeautifulSoup para buscar elementos específicos en el documento HTML. Existen varias funciones para buscar elementos, como find(), find_all(), select(), etc. Lo que devuelven son objetos de BeautifulSoup que representan los elementos encontrados, y puedes acceder a sus atributos y contenido utilizando métodos y propiedades de estos objetos. Por ejemplo, si quieres encontrar todos los enlaces en una página web, puedes usar la función find_all() para buscar todas las etiquetas <a> (que representan los enlaces) y luego acceder a sus atributos href para obtener las URL de los enlaces.

#METODOS
# Find: devuelve el primer elemento que coincide con los criterios de búsqueda especificados.
# Find_all: devuelve una lista de todos los elementos que coinciden con los criterios de búsqueda especificados.
# Select: permite buscar elementos utilizando selectores CSS, lo que proporciona una forma más flexible de encontrar elementos en el documento HTML.
links = soup.find_all('a')  # Encuentra todos los elementos <a> (enlaces) en la página web
for link in links:
    print(link.get('href'))  # Imprime el valor del atributo href de cada enlace encontrado
    print(link["href"])  # Otra forma de acceder al atributo href de cada enlace encontrado
    print(link.attrs) # Imprime un diccionario con todos los atributos de cada enlace encontrado

seleccionado = soup.select('div.content')  # Selecciona todos los elementos <div> con la clase "content"
for elemento in seleccionado:
    print(elemento.text)  # Imprime el texto contenido en cada elemento seleccionado

# Atributos de los elementos encontrados:
# text: devuelve el texto contenido dentro del elemento HTML.
# get('atributo'): devuelve el valor de un atributo específico del elemento HTML. Por ejemplo, get('href') devuelve el valor del atributo href de un enlace.


# Podemos navegar por la estructura del documento HTML utilizando métodos como parent, children, next_sibling, previous_sibling, etc. Estos métodos permiten acceder a los elementos relacionados en el árbol de la página web. Por ejemplo, si quieres acceder al elemento padre de un enlace específico, puedes usar el método parent para obtener el elemento que lo contiene.
enlace = soup.find('a')  # Encuentra el primer elemento <a> (enlace) en la página web
padre = enlace.parent  # Obtiene el elemento padre del enlace
print(padre)  # Imprime el elemento padre del enlace

# Se puede usar la navegacion por atriutos donde podemos buscar un elemento 
elemento = soup.div.a.text # Accede al texto del primer elemento <a> dentro de un elemento <div>

# NAVIGABLE STRING
# Es un tipo de objeto en BeautifulSoup que representa el texto contenido dentro de un elemento HTML. Es una cadena de texto que se encuentra entre las etiquetas de un elemento HTML. Por ejemplo, si tienes un elemento <p> con el texto "Hola, mundo!", el texto "Hola, mundo!" sería un NavigableString. Puedes acceder a este texto utilizando la propiedad .string de un elemento HTML. Por ejemplo:
parrafo = soup.find('p')  # Encuentra el primer elemento <p> en la página web
texto = parrafo.string  # Obtiene el texto contenido dentro del elemento <p>
print(texto)  # Imprime el texto contenido en el elemento <p>