"""
► Teoría:

En la práctica, existe un código estándar, el código ASCII (código estándar amer icano para intercambio de información), que relaciona cada letra, número o símbolo con una cifra del 0 al 255 (con una secuencia de 8 bits):

La "a" es el número 97
La "b" es el número 98
La "A" es el número 65,
La "B" es el número  67.
El  "0" es el número 48
El  "1" es el número 49, etc.

Así se tiene una forma muy cómoda de almacenar la información en ordenadores, ya que cada letra ocupará exactamente un byte (8 bits: 8 posiciones elementales de memoria).

► Enunciado:
Escribir un programa que solicite al usuario una letra y diga si esta es MAYÚSCULA o minúscula.
"""
letra = input("Ingrese una letra: ")
if letra == letra.upper():
    print("La letra es mayuscula")
else:
    print("La letra es minuscula")

#Otra solucion\
letra = input("Ingrese una letra: ")
if letra <= 'z'  and letra >= 'a':  # a-z (97-122)
    print('La letra es minuscula.')
 
elif letra <= 'Z' and letra >= 'A':  # A-Z (65-90)
    print('La letra es Mayuscula.')
else:
    print('El valor introducido no es una letra.')