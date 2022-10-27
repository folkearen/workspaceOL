numero = [1,2,3,4,5,6,7,8,9,10]

seleccionar = lambda x: True if x % 2 == 0 else False 
#Funcion labda con if para seleccionar los numero pares de una lista
#si la condicion es true los considerara.

"""Filter solo aplica a aquellos elemntos dentro del iterable que cumple la condicion"""
filtrado = filter(seleccionar, numero)
#designo la funcion filter a una variable, le entrgo como parametros una funcion, puede ser
#normal o lambda, luego el parametro que servira como argumento para la funcion 
#en este caso la lista numero.
filtrado2 = filter(lambda x: x %2 !=0, numero )
#De igual manera puedo escribir la funcion lambda directamente en el filter, idicandole
#Que considere como retorno solo los numeros impares

filtrado3 = list(filter(lambda x: x % 3 == 0, numero))
#Puedo asignar inmediatamente la conversiona lista del filter una variable determinada

print(list(filtrado))
print(list(filtrado2))
#Se debe convertir el resultado de los filter en listas para ser legibles, sino indicara
#un espacio de memoria

print(filtrado3)
#Al ya estar convertida en lista el contenido de la variable filtrado3,
#  puedo imprimir directamente

#otro eejemplo filter

comienzaJ = list(filter(lambda x: x.lower().startswith("j"), ["casa", "Julio", "jirafa"]))
print(comienzaJ)

"""Lo anterior en su version larga"""

def miSeleccion(lista):
    pares = []
    impares = []
    for i in lista:
        if i% 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares,impares

numero2 = [11,12,13,14,15,16,17,18,19,20]
a, b = miSeleccion(numero2)
print(a)
print(b)

#Lo de la funcion es una boludez, ya que sin ella se ahorra el desempaquetado de tupla XD