# ===========================================
# POOL DE CONEXIONES EN PYTHON (psycopg2)
# ===========================================

# Importamos el módulo de conexión pool desde psycopg2
from psycopg2 import pool

# ===========================================
# ¿Qué es un pool de conexiones?
# -------------------------------------------
# Es una técnica para reutilizar conexiones a la base de datos
# sin tener que abrir y cerrar una nueva cada vez.
# Ahorra recursos, mejora rendimiento y permite manejar muchas
# solicitudes concurrentes sin saturar la base de datos.
# ===========================================

# -------------------------------------------
# 1. SimpleConnectionPool
# -------------------------------------------
# ❗ No es thread-safe → NO usar en programas con múltiples hilos.
# ✅ Útil en scripts simples, CLI o entornos de ejecución secuencial.
# Mantiene un conjunto de conexiones activas reutilizables.

simple_pool = pool.SimpleConnectionPool(
    minconn=1,               # Número mínimo de conexiones que se mantienen abiertas
    maxconn=5,               # Número máximo de conexiones simultáneas permitidas
    user="postgres",         # Usuario de la base de datos
    password="1234",         # Contraseña
    host="localhost",        # Dirección del servidor
    port="5432",             # Puerto (por defecto para PostgreSQL)
    database="test_db"       # Nombre de la base de datos
)

# -------------------------------------------
# 2. ThreadedConnectionPool
# -------------------------------------------
# ✅ Diseñado para aplicaciones multihilo (thread-safe)
# Ideal para servidores web (Flask, Django, FastAPI) que
# manejan múltiples solicitudes concurrentes.

threaded_pool = pool.ThreadedConnectionPool(
    minconn=2,
    maxconn=10,
    user="postgres",
    password="1234",
    host="localhost",
    port="5432",
    database="test_db"
)

# -------------------------------------------
# 3. PersistentConnectionPool
# -------------------------------------------
# ✅ Mantiene conexiones "persistentes"
# 🔁 Si una conexión falla, la reemplaza automáticamente.
# Útil cuando trabajas con conexiones que pueden caerse (red inestable)
# o quieres mantener conexiones activas sin cerrarlas nunca.

persistent_pool = pool.PersistentConnectionPool(
    minconn=1,
    maxconn=3,
    user="postgres",
    password="1234",
    host="localhost",
    port="5432",
    database="test_db"
)

# -------------------------------------------
# USO DE UN POOL DE CONEXIONES
# -------------------------------------------

# Usamos el simple_pool para demostrar el flujo básico

# 1. Obtener una conexión del pool
conn = simple_pool.getconn()  # El pool "presta" una conexión

try:
    # 2. Usar la conexión para ejecutar una consulta
    cursor = conn.cursor()
    cursor.execute("SELECT version();")  # Ejemplo: obtener versión de PostgreSQL
    resultado = cursor.fetchone()
    print("Versión de PostgreSQL:", resultado)

    # Siempre cerrar el cursor manualmente (buena práctica)
    cursor.close()

finally:
    # 3. Devolver la conexión al pool para que otro la use
    simple_pool.putconn(conn)

# -------------------------------------------
# CERRAR TODAS LAS CONEXIONES DEL POOL
# -------------------------------------------
# Esto se hace generalmente al finalizar la aplicación
simple_pool.closeall()

# -------------------------------------------
# MÉTODOS DISPONIBLES (resumen)
# -------------------------------------------

# getconn()           → Obtiene una conexión del pool (prestar)
# putconn(conn)       → Devuelve una conexión al pool (devolver)
# closeall()          → Cierra todas las conexiones (se debe usar al final)
# minconn / maxconn   → Valores definidos al crear el pool (cantidad de conexiones)
# status              → En algunos pools, permite ver estado actual
# used / idle         → En PersistentConnectionPool: conexiones usadas / libres

# ===========================================
# RESUMEN: ¿CUÁL USAR?
# ===========================================
# 🧱 SimpleConnectionPool:
#    - Scripts, automatizaciones, tareas sin concurrencia.
#    - Más rápido de implementar en pruebas pequeñas.

# 🧵 ThreadedConnectionPool:
#    - Aplicaciones multihilo: servidores web, APIs, workers paralelos.
#    - Recomendado en producción con tráfico concurrente.

# 🔁 PersistentConnectionPool:
#    - Aplicaciones que necesitan mantener sesiones abiertas siempre.
#    - Ambientes inestables o con reconexiones frecuentes.

# ===========================================
# BUENAS PRÁCTICAS
# ===========================================
# ✔️ Siempre usar `putconn()` al finalizar.
# ✔️ Cerrar cursores cuando ya no se usen.
# ✔️ Cerrar el pool con `closeall()` al terminar el programa.
# ✔️ No compartir una conexión entre hilos (usa pool.threaded si necesitas concurrencia).


# Ventajas del uso de pools:
# - Reutilización de conexiones: evita el overhead de abrir y cerrar conexiones repetidamente.
# - Mejora el rendimiento: reduce la latencia en aplicaciones con alta concurrencia.
# - Manejo eficiente de recursos: limita el número de conexiones activas, evitando saturación del servidor.
# - Facilita la escalabilidad: permite manejar más solicitudes sin necesidad de aumentar el número de
# - Crear una conexión a la base de datos es costoso (en tiempo y recursos).
# - Un pool mantiene conexiones abiertas y listas, lo que reduce el tiempo de respuesta.
# - Ideal para aplicaciones con muchas peticiones (como APIs, sitios web, etc.).