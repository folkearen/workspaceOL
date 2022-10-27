matriz = []
lista1 = [] 
filas = 5
columnas =5


for i in range(filas):
    matriz.append([0]*columnas)


for f in range(filas):
    for c in range(columnas):
        matriz[f][c] = int(input("Elemento %d, %d : " % (f,c)))
        

for i in matriz:
    print(i, '\n')

#ista1 = matriz[f][c]
print(lista1)


for j in range(len(matriz)):
    contador = j
    for i in matriz[contador]:
        lista1.append(i)

print(lista1)

# numeropar = 0
# numeroimpar= 0
# c =0
# suma_total = 0




