numero = [1,2,3,4,5,6,7,8,9,10]
"""La funcion map, aplica a cada elemento del iterable"""
filtrado1 = list(map(lambda x: x % 3 == 0, numero))
#En este caso al haber una condicion la aplica a cada elemnto de la lista, 
# y devulve True si la cumple y false si no. No esta hecha para esto
print(filtrado1)

filtrado2 = list(map(lambda x: x**2, numero))
#Buen uso aplica la funcion lambda a toda la lista nuemro
print(filtrado2)
#Como ya esta convertida en lista aplico directamente
