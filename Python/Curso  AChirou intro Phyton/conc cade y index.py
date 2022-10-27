variable1 = "Día"
variable2 = " Nublado"
diaPerfecto = variable1 + variable2
#print(diaPerfecto)


variable3 = "Alan Muñoz"
print(variable3[0])#muestra el dato presente en es indice partiendo de 0
print(variable3[1:7]) #muestra una grupo de caracter entre los indices 
#indicados, el primero inclusive pero el último lo omite
print(variable3[-10])#muestra el caracter a la inversa contando desde el
#ultimo como -1
print(variable3[0:]) #Podemos indicar solo el indice de inicio y leera todo el resto del indice
print(variable3[3:])
print(variable3[:7])#Podenos indicar solo el indice final que deseemos y leeara todos los indices hasta el indicado

#Se puede jugar un poco
print(variable3[2:] + variable3[:2]) #Concatena los trosos de cadena segun el indice
print(variable3[5:7] + variable3[1:3]) #Da mula XD
print(variable3[-9:3])
print(variable3[:])# imprime la palabra completa pero para eso solo imprimo la variable


#Función len sirve para contar la cantidad de elementos dentro de una variable.. cuantos índices hay
print(len(variable3)) #Tambien cuenta el espacio como un indice 
