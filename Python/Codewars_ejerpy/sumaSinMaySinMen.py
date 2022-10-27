"""Tarea
Suma todos los números de una matriz dada (cq. list), excepto el elemento más alto y el más bajo (¡por valor, no por índice!).

El elemento más alto o más bajo, respectivamente, es un solo elemento en cada borde, incluso si hay más de uno con el mismo valor.

Cuidado con la validación de entrada."""

def sum_array(arr):
    if len(arr) > 1:
        arr.remove(max(arr))
        arr.remove(min(arr))
        arr = sum(arr)
        return arr
    else:
        return 0


lis= [4,3,1,5,2]
lis.sort()
lis = sum(lis[1:-1])

print(lis)
#Otra forma
def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0