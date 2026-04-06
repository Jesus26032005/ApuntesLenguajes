import requests
from bs4 import BeautifulSoup
import pandas as pd

# ==========================================
# 1. TRABAJANDO CON APIs (Librería Requests)
# ==========================================

url_api = "https://jsonplaceholder.typicode.com/posts"

# --- GET: Recuperar datos ---
params = {"userId": 1} # Parámetros de consulta (?userId=1)
headers = {"Authorization": "Bearer TOKEN_AQUÍ"} # Encabezados (auth, tipo de contenido)

response = requests.get(url_api, params=params, headers=headers)

if response.status_code == 200:
    data = response.json() # Parsear el JSON a un diccionario/lista de Python
    print(f"Éxito: {data[0]['title']}")
else:
    print(f"Error {response.status_code}")

# --- POST, PUT, DELETE: Modificar datos ---
nuevo_post = {"title": "Mi Post", "body": "Contenido", "userId": 1}

# POST: Crear (usamos json= para enviar el header application/json automáticamente)
requests.post(url_api, json=nuevo_post)

# PUT: Actualizar recurso existente
requests.put(f"{url_api}/1", json=nuevo_post)

# DELETE: Borrar recurso
requests.delete(f"{url_api}/1")


# ==========================================
# 2. WEB SCRAPING (BeautifulSoup)
# ==========================================

html_dummy = """
<html>
    <body>
        <div id="main-content">
            <h1 class="titulo">Lista de Jugadores</h1>
            <ul class="jugadores">
                <li><a href="/p1" class="link">Messi</a></li>
                <li><a href="/p2" class="link">Ronaldo</a></li>
            </ul>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_dummy, 'html.parser')

# --- Búsquedas básicas ---
# find(): Devuelve el primero que coincida
titulo = soup.find('h1', class_='titulo')
print(titulo.text) # "Lista de Jugadores"

# find_all(): Devuelve una lista de todos los que coincidan
links = soup.find_all('a', class_='link')

# --- Acceso a Atributos y Navegación ---
for link in links:
    texto = link.text           # El nombre (ej. "Messi")
    url_relativa = link['href'] # Atributo (ej. "/p1")
    padre = link.parent         # Sube al <li>
    hermano = link.find_next_sibling() # Busca el siguiente elemento al mismo nivel

# --- Selectores CSS (select) ---
# Muy útil para rutas complejas como "div > ul > li a"
enlaces_css = soup.select("ul.jugadores li a")


# ==========================================
# 3. PANDAS + SCRAPING (Integración)
# ==========================================

# Convertir la lista de links a un DataFrame
df = pd.DataFrame([{"nombre": l.text, "url": l['href']} for l in links])

# Guardar resultados
# df.to_csv("datos_web.csv", index=False)
print(df)