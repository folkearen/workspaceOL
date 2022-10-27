"Comprueba elementos de la lista"

listaA = [1 == 1, 2 == 2, 2 == 4]
listaB = [1 == 1, 2 == 2, 3 == 3]

print(any(listaA)) #Devuelve True si al menos uno de los elemntos es verdadero

print(all(listaA)) #Devuelve True si todos los elemntos son verdaderos

print(all(listaB))