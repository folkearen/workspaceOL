"""
DESCRIPCIÓN:
Escriba una función, , que toma un parámetro positivo y devuelve su persistencia multiplicativa, que es el número de veces que debe multiplicar los dígitos hasta alcanzar un solo dígito.persistencenumnum

Por ejemplo (Entrada --> Salida):

39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)
"""
   #Comprobar si el len de la variable es 1, para retornar cero, asignar el valor de
   #la variable a otra para poder seguir trabajando con la misma en caso contrario.

def persistence(n):
    r = n
    if r < 9:
        return 0
    while len(str(n)) > 1:
        resultado = 1
        for digito in str(n):
            resultado *= int(digito)
            n = resultado
            persistencia =+ 1
    return persistencia


print(persistence(999))
 