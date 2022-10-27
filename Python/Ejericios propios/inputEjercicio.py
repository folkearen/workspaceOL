def repeite_nombre(name,number):
#Cramos una función que exiga los parametros de name y numero
    return f"{name}\n" * number
#y que retorna una cadena de texto del nombre, entregado como argumente más adelante, y con el caracter salto de línea.
#Luego, multipiicamos la cadena por el numero definido cuando entregemos los argumentos.
#Es buena practica no imprimir en patalla directamente en la función, sino retornar el resultado e imprimir en el entorno global del progama

def multi_name(name):
#Creamos la función que pida como argumento el nombre
    return f"{name.lower()}\n{name.upper()}\n{name.title()}"
#Retornamos una cadena de texto que incluye saltos de líneas.
#Usamos el parametro name, acompañadod e la funciones para cadena de texto, lower() convierte a mminpuscula una String
#upper() convierte la cadena de texto a mayúscula y tittle() va colocando mayúscula a la primera letra de cada palabra luego de un espacio.


nombre = input("Ingrese nombre: ") 
#Solicita al ususario el ingreso por teclado del nombre.
numero = int(input("Ingrese número: ")) 
#Solicita un numero, como los ingresos por telcado son cadenas de texto, lo convertimos en un entero añadiendo int().

print(repeite_nombre(nombre,numero))
#Imprimimosel retorno de nuestra función, dando como argumentos las viariables nombre y numero.

print(multi_name(nombre))
#Imprimimos el retorno de nuestra función, entregando como argumento la varble nombre antes definida e iniciada.
"""
Ojo puedes separa los programas een modulos.py diferentes, lo tendrías que repetir el input del nombre en el entorno global de cada script
También, lee este código e inteta entender como funciona, luego escribelo por tu cuenta sin mirar la imagen, comprueba y ve corrigiendo,
si bien podriamos sentirnos tentados a copiar, el hacerlo nos impide aprender y avanzar, éxito y saludos.
"""