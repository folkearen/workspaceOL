
#Definición de una función
def mifuncion():
    print("mi primera funcion")

#Llamado de la función
#mifuncion()


def imprimeDato(argumrntoUno): #Un argumento es una varieble que a funcion pedira para realizar su operacion
    print("Mi argumento es ", argumrntoUno)

#imprimeDato(input()) #Cuando la funcion es invocada se le llama parametro a la variable de argumento

#Si a la función se le asignana dos argumentos, se le debe entregar dos parametros
def identificacion(nombre, apellido):
    print("Su nombre es: ", nombre, apellido)

#identificacion(input("Nombre: "), input("Apellido: "))

#Funcion con catidaad de argumentos variables...usa *
def compraSupermercado(*productos):
    print("La lista de supermercado es: ", productos)

#compraSupermercado(input("Ingrese productos: "))

#Puedo indicar nomeclaruta indice para que lo impirma el dato deseado
def estudiantes1ro(*nombres):
    print(nombres[0])

#estudiantes1ro(input(), input(), input())

#Cuando al llamar ala funcion no me acuerdo del orden de los argumentos para ingresar la info cocrrercta en los parametros
def nombreCompleto(apellido, nombre):
    print(nombre,apellido)

#nombreCompleto(nombre = 'alan', apellido = 'Muñoz')

#kewars o argumento de llave, la función lleva por argumento un diccionario, y los parametros deben ser difinidos si o si nombrandolso = valor a agregar
def nombreEdad(**kwargs) :
    print(kwargs["nombre"], kwargs["edad"])

#nombreEdad(nombre = "Alan", edad= 32)

