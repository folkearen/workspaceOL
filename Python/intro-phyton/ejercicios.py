#dato = input("Ingrese dato: ")

#lista = ('Hola', 'Hello', 'Paka', 'Salut')

#if lista.count(dato):
    #print('Ha dicho hola en algun idioma', dato)
#else:
    #print('Palabra desconocida :(', dato)



listaNegra = ["Juan", "Maria", "Pedro"]

Juan = {
    "Nombre Completo" : "Juan Vasquez",
    "Edad": 40,
    "Motivo": "Bajo rendimiento"
}

Maria = {
    "Nombre Completo" : "Maria Perez",
    "Edad" : 18,
    "Motivo" : "Faltas injustificadas"
}

Pedro = {
    "Nombre Completo" : "Pedro Gonzalez",
    "Edad" : 25,
    "Motivos" : "Problemas legales"
}

#listadeInfo = [Juan, Maria, Pedro ]
#print (listadeInfo)

##################################################


print("Ingrese un nuevo usuario y contraseña")

nuevoUsuario = input("Ingrese usuario: ")
nuevaContraseña = input('Ingrese contraseña: ')

print ("Datos alacenados correctamente ;)")

print ("____________________________________________")

print ("Ingrese su usuario y contraseña registrados")
usuario = input("Ingrese su usuario: ")
contraseña = input("Ingrese su contraseña: " )

print ("____________________________________________")


if usuario == nuevoUsuario and contraseña == nuevaContraseña :
    print ("Acceso correcto")

elif usuario != nuevoUsuario and contraseña != nuevaContraseña :
    print ("Acceso denegado, intentelo nuevamente")
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if usuario == nuevoUsuario and contraseña == nuevaContraseña :
        print ("Acceso correcto")
    elif usuario != nuevoUsuario and contraseña != nuevaContraseña :
        print ("Acceso denegado, será expulsado")
        exit()
     
print("______________________________________________")

print(" Precione 1 si desea consultar nuestra lista negra \n Presione 2 si desea agregar un nombre a la lista \n Presione 3 si desea borrar un nombre e infromación de la lista y conocer su infromación \n Presione 4 si desea buscar un nombre en la lista \n presione cualquier otra tecla para salir")



opcion = input("Ingrese opción: ")

if opcion == "1" :
    print(listaNegra)

elif opcion == "2" :
    print(listaNegra)
    nn = input("Ingrece nombre: ")
    listaNegra.append(nn)
    print ("Nombre agregado")
    print (listaNegra)

elif opcion == "3" :
    print(listaNegra)
    nn = input ("Ingrese nombrea borrar: ")
    listaNegra.remove(nn)
    #listadeInfo.remove(nn)
    print("Nombre Borrado")
    print(listaNegra)

elif opcion == "4" :
    nn = input("Ingrese nombre a buscar: ")
    if listaNegra.count(nn) :
        print("El nombre se encuentra en la lista negra")
        if nn == "Juan" :
            print(Juan)
        elif nn == "Maria" :
            print(Maria)
        elif nn == "Pedro" :
            print(Pedro)
    else:
        print("Nombre no está en la lista negra")

else:
    print("Saliendo del sitema de lista negra \n ::::::::::::::::::::::::::::::" )
    exit()



    