def factoriales(n):
    """
    Calcula el factorial de n
    n int > 0
    returns n!

    """
    print(n)
    if n == 1:
        return 1
    return n * factoriales(n-1)


n = int(input("Escribe un numero: "))

print(factoriales(n))

print(id(n))