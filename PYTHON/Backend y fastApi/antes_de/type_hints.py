# Los type hints son una forma de indicar el tipo de dato que se espera que reciba una funcion o variable

# Sintaxis
# def nombre_funcion(parametro: tipo_dato) -> tipo_dato:
#     codigo

# Ejemplo
# def suma(a: int, b: int) -> int:
#     return a + b

# Tambien se puede usar para variables, donde la sintaxis es la siguiente: nombre_variable: tipo_dato = valor
# a: int = 1

def suma(a: int, b: int) -> int:
    return a + b
print(suma(1, 2))
# Usar type hints no afecta el funcionamiento del codigo, solo es una forma de indicar el tipo de dato que se 
# espera que reciba una funcion o variable esto ayuda a los desarrolladores a entender mejor el codigo y a  
# prevenir errores 
