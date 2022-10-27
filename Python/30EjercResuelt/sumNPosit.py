numeroLimite = int(input("Ingresa un numero: "))
resultado = 0

for i in range(0, numeroLimite + 1):
    resultado += i

print(resultado) 

sumador = 0
resultado2 = 0
vueltas = 0
while sumador < numeroLimite:
    vueltas += 1
    sumador += 1
    resultado2 += sumador
    print(f"vuelta numero {vueltas} sumador es {sumador} -  resultado es {resultado2}")

#Formula dada 

suma =  numeroLimite * (numeroLimite + 1) / 2
print(suma)