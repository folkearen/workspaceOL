#if 5 > 3:
   #print('5 es mayor a 3')

x = 5
y = 'Chanchito feliz' 
#print(x,y)

email = 'alan.b@ceinted.com'
#print(email)

_32 = "loreto"
#print (_32)

a,b,c = "alan", 22, 'Casa'
#print (c)
#print (a)
#print (b)
Valor1=valor2=valor3='sol'
#print (Valor1)
#print(valor2,valor3)

Nombre = 'Alan '
Apellido = 'Munoz'

#print(Nombre +  Apellido)

palabra = 'Hola mundo' #String pueden ir con comillas simeples o dobles

entero = 20 #número entero o también llamado integer

conDecimales = 65.324 #llamados float o flotante

Complejos = 4j # al numero le sigue una letra j por convención 

#print(palabra,entero,conDecimales,Complejos)

lista = [1,2,3,3,3]
lista2 = lista.copy() #copia el elemento indicado previo al .copy
lista.append("A") #Agrega elementos al elemento previo al .append
#lista.clear()
lista3 = lista.copy() 
#print(lista)
#print(lista2)
#print(lista3) 

print (lista3.count(2)) #Cuenta cuantos elementos de valor indicado se encuentran dentro del elemento previo al .count
print (len(lista),len(lista2)) #len cuenta cuantos elementos hay dentro de una elemnto.

lista4 = ['a','b','c']
lista4.append('d')
#print(lista4)

#print(lista4[2]) #para accede un elemento indicando un indice desde cero en adelante

lista4.pop() #elimna el último lemento deuna lista

#print(lista4)
lista4.remove('b') #elimina el elemnto indicado de la lista
#print(lista4)

conteo = [0,1,2,3]
#rint(conteo)

conteo.reverse() #invierte el orden de los elementos de la lista
#print(conteo)

conteo.sort() #ordena de menor a mayor los elementos, siempre y cuando seán el mismo tipo de elemento
#print(conteo)

decimal = [2.3, 6.5, 9.8]
#print(decimal)
decimal.reverse()
#print(decimal)
decimal.sort()
#print(decimal)!!


tupla = ('Hola', 'mundo', 'feliz', 'hola', 'FELIZ')
#print(tupla)
print(tupla.count('Hola'), tupla.count('feliz')) #cuenta cuantos elementos hay de un elemento especifico en la tupla definida antes de .count

print(tupla.index('hola')) #.index arroja el indice en que se encuentra elelemento indicado

print(tupla[1])#puedo indicar el numero de índice y saber que elemento contine dentro de la tupla dicho índice

listaDeTupla = list(tupla) #list trasforma una tupla a lista
listaDeTupla.append('Casa')

#print(listaDeTupla)

rango = range(6) #indica que nuestro rango irá de 0 a 6 importante para las interaciones
#print(rango)

Diccionario = {
   "nombre" : "Ashoka", #recordar coma para separar varios elementos
   "raza" : "Esfinge",
   "Edad" : 2
} #van enetre llaves

#print(Diccionario)
#print(Diccionario["nombre"]) #puedo ocupar los corchtes para indicar la información que requiero
#print(Diccionario.get("raza")) #puedo usar el método get para hacer más explicto el llamada a la infromación solicitda entre 
Diccionario["nombre"] = "Ashoka2" #Para modificar el un elemento determinado dentro del diccionario
#print (Diccionario)
#print(len(Diccionario))
Diccionario["raza"] = "egypt"
#print (Diccionario)

Diccionario["Color"] = 'blanco' #Agrega elementos al diccionarios al final de este solo indicando el nuevo elemento en corchetes y = valor que tendrá de este
#print (Diccionario)
diccio2 = Diccionario.copy()
Diccionario.pop('Color') #Elimina un elemento del diccionario pero a diferencia d elas listas hay que indicar el elemnto a borar
#print(Diccionario)
Diccionario.popitem()# Elimina el último elemento del diccionario
#print(Diccionario)
del Diccionario["raza"] #Con la palabra reservada del se elimina el elemento del diccionario que se indica enre los corchetes
#print(Diccionario)
#print(diccio2)
Diccionario.clear() #Elimina todos los datos de un diccionario
#print(Diccionario)
Diccionario3 = dict(diccio2) #Sirve para copiar un diccionario
#print(Diccionario3)

animales = { #Este es un diccionario anidado, dicionarios dentro de un diccionario
   "Gatos": {
      "Nombre": "Gatiño",
      "edad": 4
   },
   "Perros": {
      "Nombre": "Poleth",
      "edad":4
   }
}
#print(animales)
#Otra forma de anidar diccionario entrega como valor de un elemnto del deiciconario otro diccionario
Gatos = {
      "Nombre": "Gatiño",
      "edad": 4
      }

Perros= {
      "Nombre": "Poleth",
      "edad":4
   }

animales = {
   "Gatos": Gatos,
   "Perros": Perros
   }
#print(animales)

#Diicionario con contructor dict, ejecutado como función que se le entrgan parámetros

cursosCantidadAlumnos = dict(cuarto = 21 , tercero = 35, segundo = 12, primero = 25 )
#print(cursosCantidadAlumnos)

#Prueba con diccionarios
listaPrimero = ['Sara','Pedro','Jose']
listaSegundo = ['Antonia', 'Raul', 'vivi']
Profesores = {
   "Lenguaje" : 'Sara', 
   "Matematica" : 'Verónica'
   } 
Estudiantes = {
   "1ro" : listaPrimero,
   "2do" : listaSegundo, 
} 
Asistentes = {
      "Inspectores" : 'Rolando',
      "Aseo" : 'Jasmin' 
   }

Colegio = dict(Personal = Profesores, Personal2 = Estudiantes, Personal3 = Asistentes)

print(Colegio)

#Experimento con lsitas
alumnos1A = ["Juan", "Maria", "Antonia"]
#print(alumnos1A)
#alumnos1A.append("Alejandro")
#print(alumnos1A)
#alumnos1A.reverse()
#print(alumnos1A)
#alumnos1A.sort()
#print(alumnos1A)
#alumnos1A.pop()
#print(alumnos1A)
#print(alumnos1A[0])
#print(alumnos1A.index("Alejandro"))
#alumnos1A.remove("Alejandro")
#print(alumnos1A.index("Antonia"))
#print(alumnos1A[0])
#print(alumnos1A)
#print(alumnos1A.count("Juan"))


