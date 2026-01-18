from fastapi import FastAPI

app = FastAPI()

# App es la instancia de la aplicacion , y get es el metodo que se encarga de manejar las peticiones GET
# get es el metodo que se encarga de manejar las peticiones GET
# Siempre que se llama a un servidor la funcion tiene que ser async
# Esto se debe a que el servidor tiene que esperar a que la funcion termine de ejecutarse
@app.get("/")
def read_root():
    return "Hola mundo"

# Diferencia entre usar async y no usar async:
#
# 1. async def:
#    - Se usa cuando la función realiza operaciones que pueden ser "esperadas" (awaitable), 
#      como leer de una base de datos asíncrona, hacer peticiones a otras APIs, etc.
#    - FastAPI ejecuta estas funciones directamente en el bucle de eventos (event loop).
#    - Si ejecutas una operación bloqueante (como time.sleep(10)) dentro de un async def, 
#      bloquearás todo el servidor.
#
# 2. def (sin async):
#    - Se usa para funciones síncronas estándar.
#    - FastAPI ejecuta estas funciones en un "thread pool" separado para no bloquear el 
#      bucle de eventos principal.
#    - Es seguro usar operaciones bloqueantes aquí, ya que corren en hilos separados.
#
# Regla general: Si tu función usa 'await', definela con 'async def'. Si no, usa 'def'.

# DOCUMENTACION
# Existen dos formas una proporcionada por swagger y otra proporcionada por redoc
# Sus links correspindientes son:
# Swagger: http://127.0.0.1:8000/docs, para desactivarla se debe quitar colocar como parametro docs_url=None
# Redoc: http://127.0.0.1:8000/redoc, para desactivarla se debe quitar colocar como parametro redoc_url=None


## REALIZAR TESTEO
# Se puede usar postmant
# Es una herramienta que permite realizar peticiones a un servidor en este caso nos permitira probar nuestra api
# En otro caso usando vs code se puede usar la extension "Thunder Client" o "REST Client"

