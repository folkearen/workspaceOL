#Creación de usuario automática con el nombre completo

nombre = input("Ingrese su primer nombre: ")
apellido = input("Ingrese su primer apellido: ")
fechaNac = " "

while fechaNac == " ":
    fechaNac = input("Ingrese año de nacimiento en números: ")
    try: 
        fechaNac = int(fechaNac)
    except: 
        fechaNac = " " 
    
    if fechaNac == int: break 
    

fechaNac = str(fechaNac)

userName = nombre[0:2] + apellido[0:2]  + fechaNac[0] + fechaNac[3]

print("Sun nombre completo es: " , nombre , " " , apellido)
print("Su nombre de ususario es: " , userName)
