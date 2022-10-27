"""Zip toma elemntos de iterables diferentes y los empareja segun indice"""

nombre = ["alan", "Pascal","Tamara","sol"]
edad = [34, 10, 32, 55, 66]
#empareja los elemntos en una tupla, si sobra alguno no lo considera
for i, j in zip(nombre, edad):
    print(i,j)


print(list(zip(nombre, edad)))
#Genera una lista de tupla

a, b , c, d = zip(nombre,edad)

#al ser tuplas los puedo desempaquetar

print(type(a))

a = "casa"
b = "asac"

print(list(zip(a,b)))
#otro ejemplo, las cadenas son iterables, por tanto tambien se puede usar con, 
# la funcion zip