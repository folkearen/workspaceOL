miTupla = ("lala", 1, 1.6, True) #Las tuplas son inmutables
 #No se pueden agregar, quitar o cambiar elementos.

print(miTupla) #Puedo imprimir Tuplas6
print(miTupla[2])#Puedoo consultar un indice específico de la tupla
print(miTupla.index("lala"))#Consultar qué elemento se ecuentra en% determinado índice
print("lala" in miTupla)#Consultar la existencia de un elemento dentro de una tupla

miLista = list(miTupla)

lista = ["juan", 2, False, 45.34]
listas = tuple(lista) #C333363onvierte una lista en tupla


print(listas.count(2)) #Indica la cantidad de veces que ese elemnto esta en la tupla
print(len(listas)) #Indica el número de elementos contenidos en la tupla

tupla2 = "alan", 20, 4, 1988 #Las tuplas se pueden escribir sin parentecis
#a esto se le llama empaquetado de tupla.
 
 #Puedo asignar cada elemento de la tupla a diferentes variable
 #  #Esto se llama desempaquetado de Tupla

nombre, dia, mes, año = tupla2
print(tupla2)
print(nombre)
print(dia)
print(mes)
print(año)
