# Pandas es una biblioteca de Python que se utiliza para la manipulación y análisis de datos. Proporciona estructuras de datos y funciones para trabajar con datos tabulares, como DataFrames y Series. A continuación, se muestra cómo cargar datos en un DataFrame utilizando Pandas:
import pandas as pd

# Pandas nos permite leer datos desde diferentes fuentes, como archivos CSV, Excel, SQL, entre otros. Aquí hay algunos ejemplos de cómo cargar datos en un DataFrame:
# Cargar datos desde un archivo CSV
df_csv = pd.read_csv('ruta/al/archivo.csv')

# Al leer los datos este archivo CSV nos los devolvera en un DataFrame, que es una estructura de datos tabular con filas y columnas. Puedes acceder a los datos utilizando las funciones y métodos de Pandas para realizar análisis, manipulación y visualización de los datos.

# Para acceder a las primeras filas del DataFrame, puedes usar el método head():
print(df_csv.head())
# Para acceder a las columnas del DataFrame, puedes usar el nombre de la columna entre corchetes:
print(df_csv['nombre_columna'])

# Un dataframe es una estructura de datos bidimensional que puede contener diferentes tipos de datos (como números, cadenas, etc.) y tiene etiquetas para las filas y columnas. Es una de las estructuras de datos más utilizadas en Pandas para trabajar con datos tabulares. Se podria entender como un diccionario de listas, donde cada clave del diccionario es el nombre de una columna y el valor asociado es una lista de los datos correspondientes a esa columna.

# Para crear un DataFrame a partir del ya abierto archivo CSV, puedes usar el siguiente código:
x = df_csv[['columna1', 'columna2']]

# Esto seleccionará las columnas 'columna1' y 'columna2' del DataFrame df_csv y las almacenará en un nuevo DataFrame llamado x. Puedes reemplazar 'columna1' y 'columna2' con los nombres reales de las columnas que deseas seleccionar.

# Otra forma de crear un DataFrame a partir de un archivo CSV es utilizando el método read_csv directamente para cargar solo las columnas que necesitas:
x = pd.read_csv('ruta/al/archivo.csv', usecols=['columna1', 'columna2'])

# Otra forma es con el objeto DataFrame constructor, que te permite crear un DataFrame a partir de un diccionario de listas:
data = {
    'columna1': [1, 2, 3],
    'columna2': ['A', 'B', 'C']
}
df = pd.DataFrame(data)
# Si fuera con el archivo serias
df_nuevo = pd.DataFrame(df_csv, columns=['columna1', 'columna2'])
# o 
df_nuevo = pd.DataFrame(df_csv[['columna1', 'columna2']])

# Se puede acceder a cada elementos del DataFrame utilizando el nombre de la columna y el índice de la fila mediante el método .loc. Por ejemplo, para acceder al elemento en la primera fila y la columna 'columna1', puedes usar:
elemento = df_csv.loc[0, 'columna1']
elemento = df_csv.iloc[0, 0]  # Usando índices numéricos con iloc

# Se puede reasignar el indice de un dataframe con una lista de valores utilizando el métodoo index. Por ejemplo, si tienes un DataFrame llamado df y quieres reasignar el índice con una lista de valores llamada nueva_lista, puedes hacer lo siguiente:
nueva_lista = ['A', 'B', 'C']  # Asegúrate de que la longitud de la lista coincida con el número de filas del DataFrame
df.index = nueva_lista
# Otra forma de reasignar el índice es utilizando el método set_index, que te permite establecer una columna específica como el nuevo índice del DataFrame. Por ejemplo, si quieres establecer la columna 'columna1' como el nuevo índice, puedes hacer lo siguiente:
df.set_index('columna1', inplace=True)
# Podemos igual con una lista de valores, pero con el método set_index:
nueva_lista = ['A', 'B', 'C']  # Asegúrate de que la longitud de la lista coincida con el número de filas del DataFrame
df['nuevo_indice'] = nueva_lista
df.set_index('nuevo_indice', inplace=True, drop=True) # El argumento de drop=True eliminará la columna 'nuevo_indice' después de establecerla como índice y inplace = True hará que el cambio se realice en el DataFrame original sin necesidad de asignarlo a una nueva variable.

# SLICING 
# El slicing en Pandas se refiere a la selección de un subconjunto de filas o columnas de un DataFrame. Puedes usar el operador de slicing (:) para seleccionar un rango de filas o columnas. Aquí hay algunos ejemplos:
# Seleccionar un rango de filas
subset_filas = df_csv[10:20]  # Selecciona las filas desde la 10 hasta la 19 (el índice final no se incluye)
# Seleccionar un rango de columnas
subset_columnas = df_csv.loc[:, 'columna1':'columna3']  # Selecciona las columnas desde 'columna1' hasta 'columna3' (incluyendo ambas)
# Seleccionar filas y columnas específicas
subset_filas_columnas = df_csv.loc[10:20, 'columna1':'columna3']  # Selecciona las filas desde la 10 hasta la 19 y las columnas desde 'columna1' hasta 'columna3'
# También puedes usar el método iloc para seleccionar filas y columnas por índice numérico:
subset_filas_columnas = df_csv.iloc[10:20, 0:3]  # Selecciona las filas desde la 10 hasta la 19 y las columnas desde el índice 0 hasta el índice 2 (el índice final no se incluye)


