"""
► Enunciado:

Escribir un programa que solicite al usuario 3 números, compararlos y decir cual es mayor.
"""


lis = []
posicion = ['primer', 'segundo', 'tercer']
for i in range(3):
    numero = int(input(f"Ingrese el {posicion[i]} numero "))
    lis.append(numero)

print(f'El numero mayor entre los tres es {max(lis)}')


#Otra forma
primerNumero = int(input("Ingrese el primer numero "))
segundoNumero = int(input("Ingrese el segundo numero "))
tercerNumero = int(input("Ingrese el tercer numero "))

posibleMayor = primerNumero

if segundoNumero > posibleMayor:
    posibleMayor = segundoNumero
elif tercerNumero > posibleMayor:
    posibleMayor = tercerNumero

print(f"El numero mayor es {posibleMayor}")