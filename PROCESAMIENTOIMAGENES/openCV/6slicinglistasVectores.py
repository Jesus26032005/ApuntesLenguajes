# El slicing en Python es una forma de extraer subconjuntos de datos de una secuencia (listas, cadenas, tuplas, etc.) usando la sintaxis:
# secuencia[inicio:fin:paso]
# Parámetros:
# inicio → índice desde donde empieza (incluido).
# fin → índice hasta donde termina (excluido).
# paso → salto entre elementos (por defecto es 1).
# Ejemplos con listas:
lista = [0, 1, 2, 3, 4, 5, 6]

print(lista[1:5])      # [1, 2, 3, 4] → desde índice 1 hasta 4
print(lista[:4])       # [0, 1, 2, 3] → desde el inicio hasta el índice 3
print(lista[3:])       # [3, 4, 5, 6] → desde índice 3 hasta el final
print(lista[::2])      # [0, 2, 4, 6] → de 2 en 2
print(lista[::-1])     # [6, 5, 4, 3, 2, 1, 0] → lista invertida