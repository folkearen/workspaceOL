
"""Separa los argumentos de un print con un elemtno determinado"""

print("Mi", "nombre", "es", "Monty", "Python.", sep= "-")




""" reemplza el salto de linea al final de la invocación por otro caracter """
print("Mi nombre es ", end= "")
print("Monty Python.")

"""Si deseo solo imprimira una digonnal debo colocar doble \\ ya qyeb una sola \ es el símbolo de escape"""

print("\\")


"""Se peuden emzclar ambas palabras claves"""
print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")




mi_lista = ['Juan','Maria', 'Pedro'] #Entre corchetes
print(mi_lista)
print(mi_lista[:3]) #imprime del indice cero al 2, el ultimo digito se excluye

mi_lista.append('Susi') #Agrega el nuevo objeto de la lista al final de esta
mi_lista.insert(1, 'Lola')#Se debe indicar el indice en el cual deseamos insetar el nuevo objeto, y luego definir el objeto/
print(mi_lista)

mi_lista.extend(['Sandra', 'Ramiro', 'Ana']) #Anade varios elemnto, practicamente concatena otra lista.
print(mi_lista)

print(mi_lista.index('Sandra')) #Indica el indice en el que se encuentra determinado elemento
#Si hay elementos reptidos devuelve el indice del primer elemnto.

print('Ramiro' in mi_lista) #Devuelve True o False comprubea si el elemnto esta en la lista.
print('Sol' in mi_lista)

mi_lista.remove("Ana")#Borra un elemnto determinado de la lista, indicandolo.
mi_lista.pop()#Elinmina el [ultimo elemnto agregado a lista

print(mi_lista)
print(len(mi_lista))#Len idica la cantidad de elemntos actuales en la lista

print(mi_lista.count("Susi")) #Indica la cantidad de veces que ese elemnto esta en la lista


mi_lista2 = ['Jose', 'Rosa'] * 5 #multiplica, repite, los elemntos de la lista determinadas veces

lista3 = mi_lista + mi_lista2 # Cocatena los elemntos de una lista

print(lista3)

#Para evitar errores al generar listas con otras listas
#Se prefiere la clonacion

a = [1,2,3]
b = list(a)
c = a[::] #Notacion de slice, de cero:al final:de uno en uno

prueba = ["Alan", 20, 4, 1990]
print(prueba)

#Se puede desempaquetar listas
nombre, dia, mes, año = prueba
print(nombre)
print(dia)
print(mes)
print(año)


"""LLenar lista de forma simplificada, con determinado numero de elementos"""

lis = []
while True:
    lis.append(input('Ingrese letras').upper())
    if len(lis) == 10:
        break
print(lis)

#Eliminar espacios al rededor de la cadena.
palabra = " abaco "
print(palabra)
print(palabra.strip())
print(palabra.lstrip()) #elimina los espacios a la izquierda 
print(palabra.rstrip())#Elimina los espacios a la derecha

#Cuantas veces aparece un sub cadena en una cadena
frase = 'tres tristes tigres trigaban trigo en un trigal'
print(frase.count("t"))
# endswitch verifica si la cadena termina en determinada subcadena
print(frase.endswith('casa'))
print(frase.endswith('gal'))


#Comprueba si la cadena esta compuesta solo de numeros
c1 = 'casa'
c2 = '1234'
print(c1.isnumeric())
print(c2.isnumeric())
#Si esta copuesta de numeros puedo transformarla en entero
int(c2)
print(c2)
print(c1.isalpha)#Este metodo comprueba si solo hay letras en una cadena

#Metodo join (union), sirve para unir cadenas de una lista con difertes caractes 
# incluyendo espacios
p1 = ['La', 'cada', 'esta', 'limpia']
print(' '.join(p1))

#Separaciones sons sep
print("El", "perro" "salta", "alto", "cuando", "come", sep = "   _____  ")

#Cotar cadena con split
f1= "La nave a alunizado"
print(f1.split()) #Corta entre los espacios en blanco
f1= """La nave a alunizado, exitosamente
en cinco horas
Tres minutos"""
print(f1.split('\n')) #Corta e al detectar salto de linea
f1= "La nave a alunizado, exitosamente"
print(f1.split(',')) #Cortar al encontrar una com , 

#Formatos de cadenas
s1 = 'Sol'
s2 = 9876272
print("Mi nombre es {}, y mi numero de telefono es {}".format(s1, s2))
#Las llaves marcaran donde colocar las variables indicadas en el 
# orden dentro de .format, de esta manera no devemos transfeomr 
# los enteros con int() cada vez que se necesite. se hace autom[articamente.
s1 = 'Sol'
s2 = 9876272
print("Mi nombre es {nombre}, y mi numero de telefono es {numero}".format(nombre = s1, numero = s2))
#Se pueden asignar variaboles a las llaves y luego asignarles la
#informacion en el .format. para ordenarlos segun necesidades.

#Podemos manipular los decimales en el formato
precio = 100.15
pre_iva = precio * 1.9
print(precio, pre_iva)
print("El precio es {:.0f}. mas iva es {:.2f}".format(precio, pre_iva))
#reducir cantidad de decimales e incluso redondea
#{:.0f} esto se llama expresion de formato
#Si los marcadores de posición incluyen dos puntos, lo que viene 
# después de los dos puntos es una expresión de formato.
#  Consulte a continuación la referencia de la expresión.
#

def to_celcius(x):
    return (x - 32)*5/9

for x in range (0, 101, 10):
    print("{:>3} F \ {:>6.2f} C".format(x, to_celcius(x)))

#Aqui la expresion de formato {:>3} alinea el cantidad de espacios al magen


#Otra manera de ordenar las variables en los fomatos.
#Esta vez usando numeros desde 0.

# "{0} {1}".format(first, second)

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)

"""Outputs:
apple carrot banana
"""

#Este metodo reemplaza una cadena o parte de ella por una nueva a lo alrgo de la misma
h1= "Laberinto infinito"

print(h1)

print(h1.replace("i", "1")) #Aqui reemplaza todas las i por 1

#Otra forma de dar formwto a cadenas

nombre = 'alan'
edad = 33
animo = 'enojado'

print(f'Hola {nombre} sabemos que  tus {edad} anos estas {animo}')

#Funcion enumerar
winners = ["Alan", "Maria", "Pascal"]
for index, person in enumerate(winners):
    print("{} - {}". format(index + 1, person))

#Compresion de una lista, para lista basadas en iteraciones, secuencias o rangos
multiples = []
for x in range(1,11):
    multiples.append(x*7)

multiples = [x*7 for x in range(1,11)] #Forma comprimida

#Otro ejempplo con comprension de lista con condicional
z = [x for x in range(101) if x % 3 == 0]

#Ordenar listas, tambien sirven letras, signos, mezclas
l=[5,3,2,4,1]
print(l)
l.sort()
print(l)
print(sorted(l))

def pasatiempos(*pas): #Puedo colocar el signo multiplicador para ingresar n argumentos
    return "Mis pasatiempos son {}".format(", ".join(pas)) #Tambien me permite considerar multiples argumentos, en funciones que solo reciben uno.

print(pasatiempos("Escribir", "Leer"))


#Ordenamiento de lista
lista_4 = [5,2,7,8,1,4]
lista_4.sort() #Ordena la lista sobreescribiendola
print(lista_4)

lista_5 = ["Maria", "Pascal", "Julio", "Tamara", "Alan"]
print(sorted(lista_5)) #Ordena la lista pero crea una diferente
print(lista_5) #La lista original queda tal cual fue creada

print(sorted(lista_5, key=len)) #Se le puede agregar un criterio de ordenacion, en este caso la longitud de los elemntos en la lista.



#cREAR RELLENOS center, centra la cadena y anade
#X cantidad de caracter a ambos lados del centro
ANCHO = 13
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""

print(CADENA_VACIA.center(ANCHO,RELLENO1))

print(ord("a")) #funcion ord devuelve el numero correspondiente a la letra en unicode
print(chr(97)) #Devuelve la letra asociada a ese numero en unicode


#Invertir listas y cadenas
word = 'castor'
new_word =""
c = []
r =[]
for i in word:
    c.insert(0,i)
    r.append(i)
    new_word = i + new_word
     
print(new_word)    
print(c)
print(r)


lista = [1,4,5,2,3]

listaordenada = sorted(lista)
listaInvertida =sorted(lista, reverse=True)
print(listaordenada) 
print(listaInvertida) 

a = "casa"
print("".join(reversed(a)))