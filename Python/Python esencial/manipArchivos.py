#Permisos
#"r" = lectura
#"a" = append, agrego informacion al final
#"w" = escritura
#"x" = crate

#"t" = texot
#"b" = binario

f = open("C:/Users/alanm/Desktop/a.txt", 'r') #abre el fichero
f2 = open("C:/Users/alanm/Desktop/a.txt", 'r') 
f3 =open("C:/Users/alanm/Desktop/a.txt", 'r') 
f4 =open("C:/Users/alanm/Desktop/a.txt", 'r') 
datos = f.read()
#realizo la lectura del texto gurdado en la variable f, y lo guardo en la variable datos
algunosDatos = f2.read(15)
#Puedo indicar que lea un determinado numero de caracteres el salto de linea tambien es un
# caracter a considerar \n
listaDatos= f3.readlines()
#Coloca cada linea de texto como un elemento dentro de una lista
lineaAlinea = f4.readline()
#Lee una linea del documento, lee la primera y se situa en la siguiente, si vuelvo a invocar
#el metodo leera la segunda y asi sucesivamente,

f.close()
f2.close()
f3.close()
f4.close()
#Cierro el fichero f por buena practica.
print(datos)
print(algunosDatos)
print(listaDatos)
print(lineaAlinea)
#Puedo trabajar con el texto guardado.

txtw = open("miFichero1.txt", "w")
#Creo un archivo en la ruta deseada, en este caso la carpeta donde estoy.
#El permiso w sobre escribe el archvivo
txtw.write("""
El caso es que
podemos escribir
aqui
1234354
""")
txtw.write("""
he sobre escrito
""")
#Podemos escribir lo que deseemos.
txtw.close()

txta = open("miFichero2.txt", "a")
#Creo mi archivo, con permiso a de agregar
txta.write("casa\n")
#escribe el texto designado al final, sin importar si ya existe, lo repite
txta.close()


creaTexto = open("miFichero3.txt", "w")
palabras = ["La ", "casa ", "es ", "hermosa\n", "y ", "es ", "mia."]
#Creo una lista con palabras

creaTexto.writelines(palabras)
#Es cribe un texto con las plabras dadas en la lista, 
# respeta espacios y salto de linea
creaTexto.close()
