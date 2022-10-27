def parImpar(numeros):
    par = [ i for i in numeros if i % 2 == 0]
    impar = [i for i in numeros if i % 2 != 0]
   
    for i, j in zip(par, impar):
        print(i,j)
    return par, impar

a = parImpar([1, 2, 3, 4, 5, 6])

par, impar = a
print(par)
print(impar)