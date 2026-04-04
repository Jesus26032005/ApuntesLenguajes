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


#NOTA ADICIONAL PODEMOS CREAR UN DF CON UN DICCIONARIO DE LISTAS, DONDE CADA CLAVE DEL DICCIONARIO ES EL NOMBRE DE UNA COLUMNA Y EL VALOR ASOCIADO ES UNA LISTA DE LOS DATOS CORRESPONDIENTES A ESA COLUMNA. POR EJEMPLO:
data = {
    'columna1': [1, 2, 3],
    'columna2': ['A', 'B', 'C']
}
df = pd.DataFrame(data)

# Metodo describe 
# El método describe() en Pandas se utiliza para generar estadísticas descriptivas de un DataFrame. Proporciona un resumen estadístico de las columnas numéricas del DataFrame, incluyendo medidas como la media, la desviación estándar, el valor mínimo, el percentil 25, el percentil 50 (mediana), el percentil 75 y el valor máximo. Aquí hay un ejemplo de cómo usar el método describe():
# Supongamos que tenemos un DataFrame llamado df con algunas columnas numéricas:
data = {
    'columna1': [1, 2, 3, 4, 5],
    'columna2': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)
# Ahora, podemos usar el método describe() para obtener un resumen estadístico de las columnas numéricas:
resumen_estadistico = df.describe()
print(resumen_estadistico)


# Metodo drop
# El método drop() en Pandas se utiliza para eliminar filas o columnas de un DataFrame. Puedes especificar las filas o columnas que deseas eliminar utilizando sus etiquetas o índices. Aquí hay algunos ejemplos de cómo usar el método drop():
# Supongamos que tenemos un DataFrame llamado df con algunas filas y columnas:
data = {
    'columna1': [1, 2, 3, 4, 5],
    'columna2': [10, 20, 30, 40, 50],
    'columna3': ['A', 'B', 'C', 'D', 'E']
}
df = pd.DataFrame(data)
# Para eliminar una columna específica, puedes usar el siguiente código:
df_sin_columna2 = df.drop('columna2', axis=1)
print(df_sin_columna2)
# Para eliminar una fila específica, puedes usar el siguiente código:
df_sin_fila2 = df.drop(1, axis=0)  # Elimina la fila con índice 1 (la segunda fila)
print(df_sin_fila2)
# También puedes eliminar varias filas o columnas a la vez pasando una lista de etiquetas o índices:
df_sin_columna2_y_columna3 = df.drop(['columna2', 'columna3'], axis=1)
print(df_sin_columna2_y_columna3)
df_sin_fila2_y_fila4 = df.drop([1, 3], axis=0)  # Elimina las filas con índices 1 y 3 (la segunda y cuarta fila)
print(df_sin_fila2_y_fila4)

# metodo dropna
# El método dropna() en Pandas se utiliza para eliminar filas o columnas que contienen valores faltantes (NaN) de un DataFrame. Puedes especificar si deseas eliminar filas o columnas utilizando el parámetro axis. Aquí hay algunos ejemplos de cómo usar el método dropna():
# Supongamos que tenemos un DataFrame llamado df con algunos valores faltantes:
data = {
    'columna1': [1, 2, None, 4, 5],
    'columna2': [10, None, 30, 40, 50],
    'columna3': ['A', 'B', 'C', None, 'E']
}
df = pd.DataFrame(data)
# Para eliminar filas que contienen valores faltantes, puedes usar el siguiente código:
df_sin_filas_con_na = df.dropna(axis=0)
print(df_sin_filas_con_na)
# Para eliminar columnas que contienen valores faltantes, puedes usar el siguiente código:
df_sin_columnas_con_na = df.dropna(axis=1)
print(df_sin_columnas_con_na)


# FUncion duplicated
# El método duplicated() en Pandas se utiliza para identificar filas duplicadas en un DataFrame. Devuelve una serie booleana que indica si cada fila es un duplicado de una fila anterior. Aquí hay un ejemplo de cómo usar el método duplicated():
# Supongamos que tenemos un DataFrame llamado df con algunas filas duplicadas:
data = {
    'columna1': [1, 2, 3, 2, 4],
    'columna2': ['A', 'B', 'C', 'B', 'D']
}
df = pd.DataFrame(data)
# Para identificar filas duplicadas, puedes usar el siguiente código:
duplicados = df.duplicated()
print(duplicados)

# Metodo groupby
# El método groupby() en Pandas se utiliza para agrupar datos en un DataFrame según una o más columnas y luego aplicar funciones de agregación a cada grupo. Esto es útil para resumir y analizar datos agrupados. Aquí hay un ejemplo de cómo usar el método groupby():        
# Supongamos que tenemos un DataFrame llamado df con datos de ventas por categoría:
import pandas as pd
data = {
    'categoria': ['A', 'B', 'A', 'B', 'A'],
    'ventas': [100, 200, 150, 250, 300]
}
df = pd.DataFrame(data)
# Para agrupar los datos por la columna 'categoria' y calcular la suma de las ventas para cada categoría, puedes usar el siguiente código:
ventas_por_categoria = df.groupby('categoria')['ventas'].sum()
print(ventas_por_categoria)

# Metodo merge 
# El método merge() en Pandas se utiliza para combinar dos DataFrames en función de una o más columnas clave. Es similar a la operación de JOIN en SQL. Aquí hay un ejemplo de cómo usar el método merge():
# Supongamos que tenemos dos DataFrames, df1 y df2, con una columna común llamada 'id':
data1 = {
    'id': [1, 2, 3],
    'nombre': ['Alice', 'Bob', 'Charlie']
}
data2 = {
    'id': [2, 3, 4],
    'edad': [25, 30, 35]
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
# Para combinar los DataFrames df1 y df2 en función de la columna 'id', puedes usar el siguiente código:
df_combinado = pd.merge(df1, df2, on='id', how='inner')  # Puedes cambiar 'inner' por 'left', 'right' o 'outer' según el tipo de combinación que desees
print(df_combinado)