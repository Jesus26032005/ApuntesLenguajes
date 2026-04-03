import pandas as pd
import numpy as np

# =================================================================
# 1. PANDAS SERIES (Unidimensional)
# =================================================================
# Una Serie es un arreglo unidimensional etiquetado (como una columna).
data_list = [10, 20, 30, 40, 50]
s = pd.Series(data_list)

# --- Acceso a Elementos ---
# Por etiqueta (label) o posición entera
print(s[2])          # Valor 30 (etiqueta 2)
print(s.iloc[3])     # Valor 40 (posición 3)
print(s[1:4])        # Rango de elementos

# --- Atributos y Métodos de Series ---
# s.values           -> Datos como NumPy array
# s.index            -> Etiquetas del índice
# s.shape            -> Dimensiones (ej. (5,))
# s.size             -> Número de elementos
# s.mean(), s.sum()  -> Estadísticas
# s.unique()         -> Valores únicos
# s.sort_values()    -> Ordenar datos
# s.isnull()         -> Detectar nulos
# s.apply(func)      -> Aplicar función a cada elemento

# =================================================================
# 2. PANDAS DATAFRAMES (Bidimensional)
# =================================================================
# Estructura de tabla (filas y columnas).

# --- Creación desde un Diccionario ---
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data_dict)


# --- Selección y Acceso ---
# Columnas
print(df['Name'])             # Seleccionar una columna (se vuelve Serie)
print(df[['Name', 'Age']])    # Seleccionar múltiples columnas (DataFrame)

# Filas
print(df.iloc[2])             # Tercera fila por posición (Charlie)
print(df.loc[1])              # Segunda fila por etiqueta de índice

# Slicing (Rebanado)
print(df[1:3])                # Filas de la 1 a la 2 (excluye la 3)

# --- Filtrado Condicional ---
# Ejemplo: Personas mayores de 25 años
mayores_25 = df[df['Age'] > 25]

# --- Valores Únicos ---
edades_unicas = df['Age'].unique() # Retorna un array de edades únicas
print(edades_unicas)

# --- Atributos y Métodos de DataFrames ---
# df.shape           -> (filas, columnas)
# df.info()          -> Resumen de tipos de datos y nulos
# df.describe()      -> Estadísticas descriptivas de columnas numéricas
# df.head(n)         -> Primeras n filas
# df.sort_values('Age')-> Ordenar por columna específica
# df.groupby('City') -> Agrupar para agregaciones
# df.fillna(0)       -> Llenar valores nulos
# df.drop('Age', axis=1) -> Eliminar columna

# =================================================================
# 3. EXPORTACIÓN DE DATOS
# =================================================================
# Guardar sin el índice numecio