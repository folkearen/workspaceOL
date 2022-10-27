"""Encuentra el número duplicado en la lista de enteros."""

lista = [ 3, 4, 5, 2, 111, 5, 3, 111]
repetidos = []
for i in lista:
    if lista.count(i) > 1 and i not in repetidos:
        repetidos.append(i)

print(repetidos)        


#Otra forma
sinRepetir = []
repetidos2 = []
for i in lista:
    if i in sinRepetir:
        repetidos2.append(i)
    sinRepetir.append(i)

print(repetidos2)


#Otra forma con set
duplicates, seen = set(), set()
for element in lista:
    if element in seen:
        duplicates.add(element)
    seen.add(element)

print(list(duplicates))
