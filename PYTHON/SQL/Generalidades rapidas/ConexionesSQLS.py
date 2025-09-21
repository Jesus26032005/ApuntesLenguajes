import psycopg2

with psycopg2.connect(
        dbname="test_db",         # nombre de la base de datos
        user="postgres",        # nombre de usuario de PostgreSQL
        password="ezio1969+", # contraseña del usuario
        host="localhost",         # dirección del servidor (localhost si es local)
        port="5432" 
) as conn:
    with conn.cursor() as cursor:
        cursor.execute("insert into persona (nombre,apellido, email) values ('ezio', 'auditore', 'ezio.auditore@assassins.com');")

import mysql.connector

with mysql.connector.connect(    
    host="localhost",
    user="root",
    password="ezio1969+",
    database="proyectocurso",
    port="3308"
) as conn:
    with conn.cursor() as cursor:
        cursor.execute("insert into persona (nombre,apellido, membresia) values ('ezio', 'auditore', 'ezio.auditore@assassins.com');")

import pyodbc
conn_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=prueba_db;"
    "UID=sa;"
    "PWD=ezio1969+;"
    "TrustServerCertificate=yes;"
    "Trusted_Connection=no;"             # Usa autenticación SQL Server
    "ConnectionPooling=Yes;"            # Pool automático activado
    "PORT=1433;"
    "TIMEOUT=30;"
    "ENCRYPTION=no;"
    "CHARSET=UTF-8;"
    "ApplicationIntent=ReadWrite;"
    "Ansi_Nulls=ON;"
    "Ansi_Padding=ON;"
    "Command_Timeout=30;"
)
with pyodbc.connect(conn_str) as conn:
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO persona (nombre, apellido, correo) VALUES ('ezio', 'auditore', 'ezio.auditore@assassins.com')")