def conversor(tipo_pesos, valor_dolar):
    pesos = float(input("Ingrese pesos " + tipo_pesos + " a convertir:  "))
    dolares_disponibles = pesos / valor_dolar
    dolares_disponibles = round(dolares_disponibles, 2)
    dolares_disponibles = str(dolares_disponibles)
    print( 'Usted dispone de $' + dolares_disponibles + ' Dolares' )

menu =  """  
Bienvenido al conversor de monedas
1 - Pesos chilenos
2 - Pesos mexicanos
3 - Pesos argentinos

Elige un opción:  """ 

opcion = int(input(menu))

if opcion == 1:
    conversor("chilenos", 805.40)
elif opcion == 2:
    conversor("mexicanos", 20.37)
elif opcion == 3:
     conversor("argentinos", 99.63)
else:
    print("Ingresa una opción correcta") 