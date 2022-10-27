print ('Bienvenido al conversor de monedas US$/CLP')
print('----------------------------------------------')
valor_dolar = 805.40
moneda_convertir = input('Seleccione la moneda a convertir, presione 1 si es CLP o 2 si es US$ ' )
if moneda_convertir == '1' :
    CLP = int(input('Ingrese CLP a convertir:  '))
    dolares_disponibles = CLP / valor_dolar
    dolares_disponibles = round(dolares_disponibles, 2)
    dolares_disponibles = str(dolares_disponibles)
    print( 'Usted dispone de ' + dolares_disponibles + ' Dolares' )

elif  moneda_convertir == '2':
    US = int(input('Ingrese US$ a convertir:  '))
    pesoschilenos_disponibles = US * valor_dolar
    pesoschilenos_disponibles = round(pesoschilenos_disponibles, 2)
    pesoschilenos_disponibles = str(pesoschilenos_disponibles)
    print('Usted dispone de ' + pesoschilenos_disponibles + ' Pesos chilenos')
else:
    print('A ingresado una opcion invalida')

# def suma(a, b):
#     resultado = a + b 
#     return resultado

# resultado = suma(2, 2)

# nueva_suma = resultado + 1

# print(nueva_suma)
