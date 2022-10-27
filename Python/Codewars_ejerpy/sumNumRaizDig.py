"""
DESCRIPCIÓN:
La raíz digital es la suma recursiva de todos los dígitos de un número.

Dado , tome la suma de los dígitos de . Si ese valor tiene más de un dígito, continúe reduciendo de esta manera hasta que se produzca un número de un solo dígito. La entrada será un entero no negativo.nn

Ejemplo
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""
def digital_root(n):
    n = str(n)
    while len(n) > 1:
        suma = [int(i) for i in n]
        n = str(sum(suma))
    return(int(n))

#Otra forma
def digital_root(n):
    return 1 + ((int(n) - 1) % 9) if n>0 else 0

#Otra forma
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

# Otra forma
def digital_root(n):
    root = 0
    for d in str(n):
        root += int(d)
    if len(str(root)) > 1:
        root = digital_root(root)
    return root


print(digital_root(132189))