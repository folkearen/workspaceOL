lista = [1 , "alan", 2.3, 5, "root"]

#Mostrar un elemento de la lista mediante su índice
print(lista[1])
print (lista[-1])
print(lista[1] + " " + lista[-1])

#Concatenar listas
primera = [1,2,3,4]
segunda = [5,6,7,8]

print(primera + segunda)

print(primera + [11,12,13,14])

#Sustituir un elemento determinado de la lista meidante búsqueda ´por indice
sustituir = [1, 2, 3, "error", 5]
print(sustituir)
sustituir[3] = 4
print(sustituir)
#Agregar elementos a la lista, se agrega al finañ
sustituir.append(6)
print(sustituir)
#Puedo agregar resultados de operaciones como elementos de lista
sustituir.append(50+50)
print(sustituir)
sustituir.append("alan" + " muñoz")
print(sustituir)

#modificar elementos en un rango de indices
sustituir[:2] = ["a", "b"] #recordar que el rango final no se ve afectado
print(sustituir)

#Anidar listas
primero = [1, 2, 3]
segundo = [4, 5, 6]
tercero = [7, 8, 9]
todas = [primero,segundo,tercero]
print(todas)

#Arrojar elemento por indice de lista y de elemnto de esa lista
print(todas[1][2])  #arroja la lista lojada en el indice 1 y el elemnto alojado en el indice 2 de la lista alojada en 1

#copiar un valor de una lista en otro índice de la misma
cop = [1,2,"Casa",3]
print(cop)
cop[0]=cop[2]
print(cop)

#Insertar elementos a la lista

pruList = [1,2,3,4,5]
pruList.append(6) #agrega un número al final de la lista
print(len(pruList))
print(pruList[2])
print(pruList)


pruList.insert(2,0)#Agrega un elemento en el índice que le hemso ídicado, los indices y elementos se desplazan a la derecha para dar lugar.
print(len(pruList))
print(pruList[2])
print(pruList)

#Agregar elemntos a una lista vacia automaticamente con fot
miLista = [] # creando una lista vacía


for i in range (5):
    miLista.append (i + 1)#Va agregando los nu,eros al final de la lista por ende en orden

print(miLista)


miLista = [] # creando una lista vacía

for i in range(5):
    miLista.insert(0, i + 1)#Va agregando los elemntos en el indice 0 por ende va desplazando el anyerior hascia la izquierda provcando un orden inverso

print(miLista)