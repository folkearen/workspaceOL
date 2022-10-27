"""
Su objetivo en este kata es implementar una función de diferencia, que resta una lista de otra y devuelve el resultado.‎

Debe eliminar todos los valores de la lista, que están presentes en la lista manteniendo su orden.‎ab

array_diff([1,2],[1]) == [2]

Si un valor está presente en , todas sus apariciones deben eliminarse del otro:‎b

array_diff([1,2,2,2,3],[2]) == [1,3]
"""
def array_diff(a, b):
    for i in a:
        for j in b:
            if j in a:
                a.remove(j)
    return(a)
print(array_diff([1,2,2,2,3],[1,2,3]))

#Otra forma
# def array_diff(a, b):
#     return [x for x in a if x not in b]