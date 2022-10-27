"""
¿ Conoces los números de Fibonacci ?

Son una secuencia de números enteros construida usando una regla muy simple:

el primer elemento de la secuencia es igual a uno ( Fib 1 = 1 )
el segundo también es igual a uno ( Fib 2 = 1 )
cada número subsiguiente es la suma de los dos números anteriores:( Fib i = Fib i-1 + Fib i-2 )
Estos son algunos de los primeros números de Fibonacci:

fib_1 = 1 fib_2 = 1 fib_3 = 1 + 1 = 2 fib_4 = 1 + 2 = 3 fib_5 = 2 + 3 = 5 fib_6 = 3 + 5 = 8 fib_7 = 5 + 8 = 13
"""

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
 
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum
 
 
for n in range(1, 10): # testing
    print(n, "->", fib(n))

#Forma mas simple
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)