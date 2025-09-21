# ===============================
# APUNTE COMPLETO: USAR SQL SERVER 2022 CON PYTHON
# ===============================

# Este apunte explica cómo conectar Python con SQL Server 2022,
# cómo usar el manejo automático de conexiones (pooling)
# y cómo trabajar con contextos 'with' para asegurar cierre correcto de recursos.

# -------------------------------
# 1. INSTALACIÓN REQUERIDA
# -------------------------------
# pip install pyodbc
# Además, instalar el "ODBC Driver 18 for SQL Server" oficial desde:
# https://learn.microsoft.com/sql/connect/odbc/download-odbc-driver-for-sql-server

# -------------------------------
# 2. CADENA DE CONEXIÓN
# -------------------------------
# Parámetros importantes:
# - DRIVER: Controlador ODBC instalado (ejemplo: ODBC Driver 18 for SQL Server)
# - SERVER: Nombre o IP del servidor SQL Server (localhost o remoto)
# - DATABASE: Nombre de la base de datos a usar
# - UID: Usuario de SQL Server (si usas autenticación SQL)
# - PWD: Contraseña del usuario
# - TrustServerCertificate: 'yes' para evitar errores de certificado TLS en conexiones locales
# - ConnectionPooling: 'Yes' para activar pool de conexiones (por defecto está activado)

# Ejemplo de cadena de conexión:

connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=prueba_db;"
    "UID=sa;"
    "PWD=ezio1969+;"
    "TrustServerCertificate=yes;"
    "Trusted_Connection=no;"  # Usar autenticación de Windows si es necesario
    "ConnectionPooling=Yes;"  # Activar pool de conexiones automático
    "port=1433;"  # Puerto por defecto de SQL Server
    "timeout=30;"  # Tiempo de espera para conexión en segundos
    "encryption=no;"  # Desactivar cifrado si no es necesario
    #"ApplicationName=;"  # Nombre de la aplicación que se conecta
    #"autocommit=True;"  # Activar autocommit si es necesario
    "charset=UTF-8;"  # Codificación de caracteres a usar
    "ApplicationIntent=ReadWrite;"  # Indica que la aplicación realizará escrituras
    "ansi_nulls=on;"  # Manejo de NULLs ANSI
    "ansi_padding=on;"  # Manejo de espacios en blanco ANSI
    "command_timeout=30;"  # Tiempo de espera para comandos en segundos qye una consulta se ejecute
)

# -------------------------------
# 3. CONEXIÓN BÁSICA CON PYODBC
# -------------------------------

import pyodbc

try:
    # Crear conexión
    conexion = pyodbc.connect(connection_string)
    cursor = conexion.cursor()

    # Ejecutar consulta
    cursor.execute("SELECT * FROM empleados")

    # Leer resultados
    for fila in cursor.fetchall():
        print(fila)

    # Cerrar cursor y conexión
    cursor.close()
    conexion.close()

except pyodbc.Error as e:
    print("Error en conexión o consulta:", e)

# -------------------------------
# 4. USAR CONTEXTO WITH (Gestión automática)
# -------------------------------
# La forma recomendada para evitar olvidos de cierre de conexión o cursor es usar "with"
# Esto garantiza que se cierre automáticamente aunque haya error.

def obtener_empleados():
    with pyodbc.connect(connection_string) as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT nombre, edad FROM empleados")
            for fila in cursor.fetchall():
                print(f"Nombre: {fila.nombre}, Edad: {fila.edad}")

# Llamar función
obtener_empleados()

# -------------------------------
# 5. INSERCIÓN DE DATOS CON PARÁMETROS Y COMMIT
# -------------------------------

def insertar_empleado(nombre, edad):
    with pyodbc.connect(connection_string) as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                "INSERT INTO empleados (nombre, edad) VALUES (?, ?)",
                (nombre, edad)
            )

insertar_empleado("Jesus", 28)

# -------------------------------
# 6. POOL DE CONEXIONES EN PYODBC
# -------------------------------
# El pool de conexiones está activado por defecto si usas un driver ODBC moderno.
# No necesitas código adicional para manejarlo.
# El pool permite reutilizar conexiones y mejora el rendimiento.

# Sólo asegúrate que en la cadena de conexión esté:
# "ConnectionPooling=Yes;"  (por defecto suele estar así)

# Cada vez que haces pyodbc.connect(), el driver reutiliza conexiones si es posible.

# -------------------------------
# 7. RECOMENDACIONES FINALES
# -------------------------------
# - Usa siempre parámetros (?) para evitar inyección SQL.
# - Usa bloques with para manejo automático de recursos.
# - Maneja excepciones para capturar errores.
# - Verifica tener instalado el driver ODBC adecuado.
# - En producción, considera usar librerías como SQLAlchemy para manejo avanzado.

# ===============================
# Fin del apunte
# ===============================
