# Requests es una biblioteca de Python que permite enviar solicitudes HTTP de manera sencilla. Incluye varias funciones para realizar solicitudes GET, POST, PUT, DELETE, entre otras. Es ampliamente utilizada para interactuar con APIs y obtener datos de la web. Con Requests, puedes enviar datos en el cuerpo de la solicitud, manejar cookies, establecer encabezados personalizados y mucho más. Es una herramienta esencial para cualquier desarrollador que trabaje con APIs o necesite realizar solicitudes HTTP en sus proyectos.
# Existen otras como httplib, urllib, etc. pero Requests es más fácil de usar y tiene una sintaxis más clara. Además, maneja automáticamente las conexiones persistentes, lo que mejora el rendimiento al realizar múltiples solicitudes al mismo servidor. En resumen, Requests es una biblioteca poderosa y fácil de usar para trabajar con HTTP en Python.
import requests

# Metodo get: se utiliza para solicitar datos de un recurso específico. Por ejemplo, si quieres obtener información de un usuario en una API, puedes usar el método GET para enviar una solicitud a la URL correspondiente y recibir los datos del usuario en respuesta.
response = requests.get('https://api.example.com/users/1')
# Tenemos los atributos:
# status_code: el código de estado HTTP de la respuesta (por ejemplo, 200 para éxito, 404 para no encontrado).
# headers: los encabezados de la respuesta, que pueden incluir información sobre el tipo de contenido, la longitud del contenido, etc. Devolverá un diccionario con los encabezados de la respuesta.
# content: el contenido de la respuesta en formato bruto (bytes).
# text: el contenido de la respuesta como una cadena de texto (útil para respuestas en formato JSON o HTML).
# json(): un método que intenta analizar el contenido de la respuesta como JSON y devuelve un diccionario de Python.
print(response.status_code)  # Imprime el código de estado HTTP
print(response.headers)      # Imprime los encabezados de la respuesta
print(response.text)         # Imprime el contenido de la respuesta como texto
print(response.json())       # Imprime el contenido de la respuesta como un diccionario de Python
print(response.url)          # Imprime la URL de la solicitud realizada

# Atributo header:
#date: la fecha y hora en que se generó la respuesta.
#content-type: el tipo de contenido de la respuesta (por ejemplo, application/json para respuestas en formato JSON).
#content-length: la longitud del contenido de la respuesta en bytes.


# Enviar parametros en una solicitud GET:
# Puedes enviar parámetros en una solicitud GET utilizando el argumento params de la función requests.get(). Esto te permite incluir datos adicionales en la URL de la solicitud. Por ejemplo, si quieres buscar usuarios por nombre, puedes enviar un parámetro de búsqueda de la siguiente manera:
params = {'name': 'John'}
response = requests.get('https://api.example.com/users', params=params)
# Podemos enviar mas de un parametro:
params = {'name': 'John', 'age': 30}
response = requests.get('https://api.example.com/users', params=params)


# Se pueden formatear los valores devueltos
# Si la respuesta es un JSON, puedes formatearla.
response.json()  # Devuelve un diccionario de Python con los datos del JSON


# SENTENCIA POST
# El método POST se utiliza para enviar datos a un servidor para crear o actualizar un recurso. Por ejemplo, si quieres crear un nuevo usuario en una API, puedes usar el método POST para enviar los datos del usuario en el cuerpo de la solicitud.

# Existen varios argumentos donde podemos enviar los datos, como data, json, files, etc. El argumento data se utiliza para enviar datos en formato de formulario (application/x-www-form-urlencoded), mientras que el argumento json se utiliza para enviar datos en formato JSON (application/json). Por ejemplo, si quieres crear un nuevo usuario con un nombre y una edad, puedes usar el método POST de la siguiente manera:

data = {'name': 'John', 'age': 30}
response = requests.post('https://api.example.com/users', json=data, data=data)