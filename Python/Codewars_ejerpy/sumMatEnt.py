"""
Escribe una función que tome una matriz de números y devuelva la suma de los números. Los números pueden ser negativos o no enteros. Si la matriz no contiene ningún número, debe devolver 0.

Ejemplos
Entrada: [1, 5.2, 4, 0, -1]
Salida:9.2

Entrada: []
Salida:0

Entrada: [-2.398]
Salida:-2.398

suposiciones
Puedes asumir que solo te dan números.
No puede asumir el tamaño de la matriz.
Puede suponer que obtiene una matriz y, si la matriz está vacía, devuelve 0.
"""

def sum_array(a):
    return sum(a) 
print(sum_array([]))