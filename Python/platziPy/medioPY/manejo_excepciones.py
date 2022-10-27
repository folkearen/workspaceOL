"""
rice (eleva, levanta)
try(probar)
except(exeptoque, hago lo siguiente)
finally (rara de ver, siver para cerrar archivos, accesos a BBDD, liberar
recurso externos.Va depues de un bloque try o try exept)
"""
# Ejemplo
palabra = ' '
def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("No se puede ingresar una cadena vacia")
        return print(string == string[::-1])
    except ValueError as ve: #Se le pone un nombre al error as ve, ve abreviatura ValueError
        print(ve) #Imprime el mensaje de error del raise
        return False

try: #prueba ejecutar la funcion 
    palindrome(palabra)
except TypeError: #si sucede un TypeError haz lo siguiente
    print("Solo puede ingresar strings") 
#Llamamos a la funcion con un numero y no un string. aroja error

"""
Ejemplo finally

f = oprn("archivo.txt")
 se trabaja con el archivo, bla bla ,bla

finally:
    f.close()

"""

def divisors(num):
    divisor = []
    for i in range (1,num + 1):
        if num % i == 0:
            divisor.append(i)
    return divisor

def run():
    numero = int(input("Ingresa un numero "))
    try:
        if numero < 0:
            raise ValueError ("Debes ingresar numeros positivos")
        print(divisors(numero))
    except ValueError as ve:
        print(ve)
        return False



if __name__ == '__main__':
    run()
