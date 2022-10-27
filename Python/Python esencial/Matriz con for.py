from random import *


#Matriz con random y simplificada
matriz = [[randint(1,10)for i in range(3)] for j in range(3)]
for i in matriz:
    print(i, '\n')

#Obtener una columna de una matriz

c = int(input('Digite columna a obtener: '))
b = []
print(len(matriz))

for i in range(len(matriz)):
    b.append(matriz[i][c])
print(b)

# print('Creando un matriz 5x5 con un total de 25 números')

for filas in range(3):
     for columnas in range(3):
         matriz[filas][columnas] = int(input('ingrese un número entero '))

# print('\n'+'Generando su matriz'+'\n')

# for i in matriz:
#     print(i,'\n')




#Matrices son conjuntos de elementos horizontales o verticales, de una, dos y tres dimenciones.
#Matriz = Array o Arreglo

#Matriz unidimencional de 6x6 vertical

# for i in  range (1,7):
#     print(i)
#     print("")

# #Matriz unidimencional de 6x6 horizontal
# for i in  range (1,7):
#     print(i, end = " ")

# print("\n")
# print("\n")
# print("\n")
#Matriz bidimencional de 6x6

# 



# for i in range (1,7):
#     for j in range (1,7):
#         print(f"({i},{j})", end = " ")
#     print("\n")

#matriz ejercicio colocar un 1 en diagonal
# for i in range (1,7):
#     for j in range (1,7):
#         if (i == j):
#             print(1, end = "  ")
#         else:
#             print(0, end = "  ")
#     print(" ")


    

# matriz = []
# contador = 0
# for i in range(5):
#     matriz.append([0]*5)
# print(matriz)

# for filas in range(5):
#     for columnas in range(5):
#         contador += 1
#         matriz[filas][columnas] = int(input('ingreso de numeros, %d de 25 : ' %(contador)))

# for i in matriz:
#     print(i,'\n')