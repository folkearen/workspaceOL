menu =  """  
Bienvenido al conversor de monedas
1 - Pesos chilenos
2 - Pesos mexicanos
3 - Pesos argentinos

Elige un opción:  """ 

opcion = int(input(menu))

if opcion == 1:
    CLP = float(input('Ingrese CLP a convertir:  '))
    valor_dolar = 805.40
    dolares_disponibles = CLP / valor_dolar
    dolares_disponibles = round(dolares_disponibles, 2)
    dolares_disponibles = str(dolares_disponibles)
    print( 'Usted dispone de $' + dolares_disponibles + ' Dolares' )
elif opcion == 2:
    MEX = float(input('Ingrese MEX a convertir:  '))
    valor_dolar = 24
    dolares_disponibles = MEX / valor_dolar
    dolares_disponibles = round(dolares_disponibles, 2)
    dolares_disponibles = str(dolares_disponibles)
    print( 'Usted dispone de $' + dolares_disponibles + ' Dolares' )
elif opcion == 3:
    ARG = float(input('Ingrese ARG a convertir:  '))
    valor_dolar = 99.63
    dolares_disponibles = ARG / valor_dolar
    dolares_disponibles = round(dolares_disponibles, 2)
    dolares_disponibles = str(dolares_disponibles)
    print( 'Usted dispone de $' + dolares_disponibles + ' Dolares' )
else:
    print("Ingresa una opción correcta")