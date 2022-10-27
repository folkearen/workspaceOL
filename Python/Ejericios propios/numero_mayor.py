import random 

lis = []
for i in range(10):
    i = random.randint(1,100)
    lis.append(i)
print(lis)    

mayor = 0
for i in lis:
    if i > mayor:
        mayor = i
    else:
        continue

print(mayor)
print(max(lis))

numero1 = int(input("Ingrese un n1úmero: "))
numero2 = int(input("Ingrese un número: "))
numero3 = int(input("Ingrese un número: "))
elmayor = max(numero1, numero2, numero3)
print(elmayor)