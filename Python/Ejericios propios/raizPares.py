lis = [1,2,4,5,6,7,8,9,10]

def raicesPares(lista):
    return [n**0.5 for n in lista if n%2 == 0]


print(raicesPares(lis))




def raicesPares2(lista):
    raicesPares = []
    for n in lista:
        if n % 2 == 0:
            raicesPares.append(n**0.5)
    return raicesPares

print(raicesPares2(lis))