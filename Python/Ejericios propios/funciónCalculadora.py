def calculadora():
    print ("Calculadora báisca")

    primerDigito = input("Ingrese digito : ")

    try: 
        primerDigito = int(primerDigito)
    except:
        primerDigito = " "

    if primerDigito == " " : print("No ha ingresado un número"), exit()


    operador = input('Ingrese operación "+" "-" "*" "/" : ' ) 


    segundoDigito = input("Ingrese digito : ")

    try: 
        segundoDigito = int(segundoDigito)
    except:
        segundoDigito = " "

    if segundoDigito == " " : print("No ha ingresado un número"), exit()


    if operador == "+": resultado = primerDigito + segundoDigito
    elif operador == "-": resultado = primerDigito - segundoDigito
    elif operador == "*": resultado = primerDigito * segundoDigito
    elif operador == "/": resultado = primerDigito / segundoDigito
    elif operador == "=": print(resultado)
    else:
        print("El operador no es valido"), exit()

    while operador != "=" :
        operador = input('Ingrese operación "+" "-" "*" "/" o "=": ' )

        if operador != "=" :
            Digito = input("Ingrese primer digito : ")

            try: 
                Digito = int(Digito)
            except:
                Digito = " "

            if Digito == " " : print("No ha ingresado un número"), exit()

        if operador == "+": resultado = resultado + Digito
        elif operador == "-": resultado = resultado - Digito
        elif operador == "*": resultado = resultado * Digito
        elif operador == "/": resultado = resultado / Digito
        elif operador == "=": print(resultado)
        else:
            print("El operador no es valido"), exit()

calculadora()