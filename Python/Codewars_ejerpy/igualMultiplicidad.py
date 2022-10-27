"""
Dadas dos matrices y escribe una función (o) que comprueba si las dos matrices tienen los "mismos" elementos, con las mismas multiplicidades (la multiplicidad de un miembro es el número de veces que aparece). "Igual" significa, aquí, que los elementos en son los elementos en cuadrado, independientemente del orden.abcomp(a, b)compSame(a, b)ba

Ejemplos
Matrices válidas
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) devuelve verdadero porque en 121 es el cuadrado de 11, 14641 es el cuadrado de 121, 20736 el cuadrado de 144, 361 el cuadrado de 19, 25921 el cuadrado de 161, y así sucesivamente. Se hace obvio si escribimos los elementos de 's en términos de cuadrados:bb

a = [121, 144, 19, 161, 19, 144, 19, 11] 
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
Matrices no válidas
Si, por ejemplo, cambiamos el primer número a otra cosa, ya no está devolviendo true:comp

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a,b) devuelve false porque en 132 no es el cuadrado de ningún número de .ba

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
comp(a,b) devuelve false porque en 36100 no es el cuadrado de ningún número de .ba
"""


def comp(array1, array2):
    if array1 == None or array2 == None :
        return False
    elif type(array1) is not list or type(array2) is not list:
        return False
    elif len(array1) == 0 or len(array2) == 0:
        return False
    elif len(array2) == 1:
        array2.append(array2[0])
    cuadrados = [i**2 for i in array1]
    return sorted(array2) in sorted(cuadrados)
#Otra forma
def comp(a, b):
    try:
        return sorted(i*i for i in a) == sorted(b)
    except:
        return False

print(comp([2,2],[4]))