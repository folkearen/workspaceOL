"""
escríbeme una función stringyque tome a sizey devuelva a stringde alternando '1s'y '0s'.

la cadena debe comenzar con un 1.

una cadena con size 6 debería devolver: '101010'.

con size4 debe devolver : '1010'.

con size12 debe devolver : '101010101010'.

El tamaño siempre será positivo y solo usará números enteros.
"""

def stringy(size):
    return "".join(["1" if i % 2 != 0 else "0" for i in range(1, size +1)])


print(stringy(42))