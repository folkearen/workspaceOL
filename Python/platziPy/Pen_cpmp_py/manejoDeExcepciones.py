"""Las execpciones se manejan con try, except, finally
no se deben manejar de manera silecniosa
para crear exepciones propias, utilizar raise
"""
def divide_elementos_de_lista(lista, divisor):
    #Si ponemos la exepcion dentro de la funcion, estamos asegurandonos
    #Ante un error,programacion defensiva
    try:
        return [i / divisor for i in lista] #Inteta resolver lafuncion
    except ZeroDivisionError as e:
        return f"{lista} No se puede dividir por cero" #de no poder devolvera la lista, y no se truncara el programa


lista = list(range(10))
divisor = 0

print(divide_elementos_de_lista(lista, divisor))