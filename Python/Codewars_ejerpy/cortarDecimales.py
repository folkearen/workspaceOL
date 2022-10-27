"""
Cada número de punto flotante debe formatearse para que solo se devuelvan los dos primeros lugares decimales. 
No necesita verificar si la entrada es un número válido porque solo se usan números válidos en las pruebas.

¡No redondees los números! ¡Solo córtalos después de dos decimales!

Right examples:  
32.8493 is 32.84  
14.3286 is 14.32

Incorrect examples (e.g. if you round the numbers):  
32.8493 is 32.85  
14.3286 is 14.33
"""

# Este pense yo y no funcionaba en todos los casos
#El problema radicaba en la cantidad de elemntos antes del punto decimal
# def two_decimal_places(number):
#     n = str(number)
#     return float(n[:5]) 

def two_decimal_places(number):
    number = str(number)
    return float(number[:number.index('.') + 3])

print(two_decimal_places(32.8493))
