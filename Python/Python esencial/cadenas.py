
"""Separa los argumentos de un print con un elemtno determinado"""

print("Mi", "nombre", "es", "Monty", "Python.", sep= "-")




""" reemplza el salto de linea al final de la invocación por otro caracter """
print("Mi nombre es ", end= "")
print("Monty Python.")

"""Si deseo solo imprimira una digonnal debo colocar doble \\ ya qyeb una sola \ es el símbolo de escape"""

print("\\")


"""Se peuden emzclar ambas palabras claves"""
print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")


a = "caSa"

a.lower() #Convierte a minuscula
a.upper() #Conviernte a mayuscula
a.capitalize() #Coloca la primera letra de la cadena em mayuscula
a.title() #Coloca la primera letra de cada plabra de la cadena en mayuscula.

color = "amarillo"
tamano = "enorme"
temperatura = 1000
print(f"el sol es {color}, su tamano es {tamano} y su temperatura {temperatura}")

#los fstring funcionan ejecutando codigo python dentro de las llaves por tanto, puedo usar metodos
#funciones, realizar operaciones

def elevar(a,b):
    return a**b

print(f" 1 + 2 = {1+2} el resultado es {'tres'.upper()} y puedo portenciar por si mismo {elevar(3,3)}")

a = "a3_"

print(a.isnumeric())
print(a.isdecimal())
print(a.isdigit())
print(a.isidentifier())





































