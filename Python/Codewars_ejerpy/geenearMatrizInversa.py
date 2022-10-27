"""
Dado un número aleatorio no negativo, debe devolver los dígitos de este número dentro de una matriz en orden inverso.
ejemplo:
348597 => [7,9,5,8,4,3]
0 => [0]
""" 

def digitize(n):
    return [int(i) for i in reversed(str(n))]


# Otra forma
# def digitize(n):
    # return map(int, str(n)[::-1])


print(digitize(348597))

