#ejemplos
file_counts = {"jpg":10, "txt":14, "csv":2, "py":23 }
print(file_counts)

print(file_counts['txt'])
print("jpg" in file_counts)
print("html" in file_counts)

#Agregaremos nuevos elementos al diccionario
file_counts["cfg"]= 8
print(file_counts)

#Reemplazar los valores asociados a una palabra clave
#CSV antes era 2 ahora es 17
file_counts["csv"] = 17

print(file_counts)

#Para eliminar un elemnto del diccionario
del file_counts['cfg']

print(file_counts)

#Iterar un diccionario. devuelve las claves

for extension in file_counts:
    print(extension)

 #Para recorrer las claves y valores al mismo tiempo

for ext, amount in file_counts.items():
    print("There are {} file with the .{} extension".format(amount,ext))
#Imprimir claves y valores por separado
print(file_counts.keys())
print(file_counts.values())

#Otra forma de solo iterar las llaves
for i in file_counts.keys():
    print(i)
#Forma de solo iterar valores
for i in file_counts.values():
    print(i)

#Ejercicio de contar letras de un texto y crear un diccionario
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for clothes, colors in wardrobe.items(): #Recorre la clave y su valor(que es una lista)
    #separandas en dos variables clothes y color
	for color in colors: #Solo recorro la lista que es el valoor de la clave. 
        #Almacenada en la variable colors
		print("{} {}".format(color, clothes))

#Numeros de elementos en un diccionario

print(len(wardrobe)) #muestra la cantidad de elemntos en el diccionario, Los elementos son las claves
print(wardrobe.get("shirt")) #muestra los valores aosciados  a determinada clave

wardrobe.update(file_counts) #Actualiza un diccionario anadiendole otro diccionario existente
#Si un elemnto (clave) esta en ambos diccionarios los valores del primero se reemplazan'
#por los valores del segundo
print(wardrobe)

wardrobe.clear()#Vacia un diccionario
print(wardrobe)

