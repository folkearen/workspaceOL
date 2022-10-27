matriz = []
lista = []

for i in range(5):
     matriz.append([0]*5)


print('Creando un matriz 5x5 con un total de 25 números... \n')

def crear_matriz():

    for filas in range(5):
        for columnas in range(5):
            matriz[filas][columnas] = int(input('ingrese un número entero '))

    print('\n'+'Generando su matriz'+'\n')

    for i in matriz:
        print(i,'\n')
    
    for j in range(len(matriz)):
        contador = j
        for i in matriz[contador]:
            lista.append(i)
    print(lista)

crear_matriz()