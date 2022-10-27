from functools import reduce


numero = [2,3,4,5,6,7,8,9,10]

"""Reduce requiere siempre dos elementos, dentro de la funcion y reducir"""
reduccion = reduce(lambda x, y:  x + y, numero)
#En este caso reduce resive como funcion lambda dos elemntos que se deben sumar, 
# entonces toma de numero los primeros dos lementos y los sumas, ese resultado
#pasa a ser elemento 1 y toma como elemento dos el siguiente de la lista, 
# en este caso el tercer elemnto de la lista, y asi sucesivamente.
print(reduccion)

palabras = ["casa", "sol", "perro", "gato"]
reduccion2 = reduce(lambda x, y: x + y, palabras)

print(reduccion2)


def potenciador(x, y):
    print(f"valor x {x}, valor y {y}")
    return x + y
#Podemos ver el proceso recursivo de reduce
reduccion3 = reduce(potenciador, numero)
print(reduccion3)
