print("Ingrese un nuevo usuario y contraseña solo de nuemros y de cuatro digitos: ")

nuevoUsuario = input("Ingrese usuario: ")
nuevaContraseña = " "

while nuevaContraseña != int:
    nuevaContraseña = input ('Ingrese contraseña de solo numero: ')
    try: 
        nuevaContraseña = int(nuevaContraseña)
    except: 
        nuevaContraseña = " " 
    
    if nuevaContraseña != " " : break


print(nuevaContraseña)

inte = 3
contraseña = int(input("Ingrese contraseña: "))

while contraseña != 3125 :
    
    print("Contraseña incorrecta, intente nuevamente")
    for op in range(2):
        print("Le quedan", inte - 1)
        contraseña = int(input("Ingrese contraseña: "))
        if op == 1:
            print("contraseña invalidad, ha sido expulsado del sistema"), exit()

print ("Contraseña correcta")

