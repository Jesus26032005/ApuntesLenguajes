
import pandas as pd
archivo_csv = 'ruta/al/archivo.csv'
df = pd.read_csv(archivo_csv)


# Localizar valores unicos en un DataFrame
# Para localizar valores únicos en un DataFrame, puedes utilizar el método unique() de Pandass 
# Supongamos que tienes un DataFrame llamado df y quieres localizar los valores únicos en una columna específica llamada 'columna1'. Puedes hacer lo siguiente:

valores_unicos = df['columna1'].unique()
print(valores_unicos)

# Si quisieramos ver una condicion especifica, por ejemplo, localizar los valores únicos en la columna 'columna1' que sean mayores a 10, podríamos hacer lo siguiente:
valores_unicos_mayores_a_10 = df['columna1']>10
print(valores_unicos_mayores_a_10)
# Esto devolverá un array de valores únicos en la columna 'columna1' que son mayores a 10. Puedes ajustar la condición según tus necesidades para localizar los valores únicos que deseas.


# pero si lo que quisieramos es devolver un DataFrame con los valores en la columna 'columna1' que sean mayores a 10, podríamos hacer lo siguiente:
df_valores_unicos_mayores_a_10 = df[df['columna1']>10]
print(df_valores_unicos_mayores_a_10)

# Para guardar un DataFrame en un archivo CSV, puedes utilizar el método to_csv() de Pandas. Aquí tienes un ejemplo de cómo hacerlo:
df.to_csv('ruta/al/nuevo_archivo.csv', index=False)
# El argumento index=False se utiliza para evitar que se guarde el índice del DataFrame en el archivo CSV. Si deseas incluir el índice, puedes omitir este argumento o establecerlo en True.
# También puedes especificar otras opciones al guardar el DataFrame, como el separador de campos (delimiter) o el formato de fecha (date_format). Por ejemplo:
df.to_csv('ruta/al/nuevo_archivo.csv', index=False, sep=';', date_format='%Y-%m-%d')
# Esto guardará el DataFrame en un archivo CSV con un separador de campos ';' y formateará las fechas en el formato 'YYYY-MM-DD'. Puedes ajustar estas opciones según tus necesidades al guardar el DataFrame en un archivo CSV.

# Para guardar un DataFrame en un archivo Excel, puedes utilizar el método to_excel() de Pandas. Aquí tienes un ejemplo de cómo hacerlo:
df.to_excel('ruta/al/nuevo_archivo.xlsx', index=False)
# El argumento index=False se utiliza para evitar que se guarde el índice del DataFrame en el archivo Excel. Si deseas incluir el índice, puedes omitir este argumento o establecerlo en True



# Existen varias formas de guardar un DataFrame en un archivo, dependiendo del formato que desees utilizar. Aquí te presento algunas opciones comunes:
# Guardar en formato CSV
df.to_csv('ruta/al/nuevo_archivo.csv', index=False)
# Guardar en formato Excel
df.to_excel('ruta/al/nuevo_archivo.xlsx', index=False)
# Guardar en formato JSON
df.to_json('ruta/al/nuevo_archivo.json', orient='records', lines=True)
# Guardar en formato Parquet
df.to_parquet('ruta/al/nuevo_archivo.parquet', index=False)
# Guardar en formato HDF5
df.to_hdf('ruta/al/nuevo_archivo.h5', key='df', mode='w')
# Guardar en formato SQL (requiere una conexión a una base de datos)
from sqlalchemy import create_engine
engine = create_engine('sqlite:///ruta/al/nueva_base_de_datos.db')
df.to_sql('nombre_tabla', con=engine, index=False, if_exists='replace')