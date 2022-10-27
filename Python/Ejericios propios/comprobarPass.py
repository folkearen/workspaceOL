password = " "
pswd = ""
while password != pswd: 
    password = input("Ingrese una contrasena nueva: ")
    intento = 1
    
    pswd = input("Escriba la contrasena para logearse: ")
    
    if pswd == password:
        print("Login correcto")
        break 
    else:
        print(f'Login fallido. Intento {intento}')
        while intento < 5:
            intento += 1
            pswd = input("Escriba la contrasena para logearse: ")
            if password == pswd:
                print("Login correcto")
                break
            print(f'Login fallido. Intento {intento}')
    