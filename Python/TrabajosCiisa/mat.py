matriz = []
lis = []

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
            lis.append(i)
    


def suma_total(fuente):
    sum_total =sum(fuente)
    print('La suma total de los números de la matriz es: ', sum_total)
    return sum_total


def sum_pares(fuente):
    sum_par = 0
    for i in fuente:
        if i % 2 == 0:
            sum_par += i
        else:
            continue

    print('La suma total de todos los números pares de la matriz es: ',sum_par)


def sum_impares(fuente):
    sum_impar = 0
    for i in fuente:
        if i % 2 == 1:
            sum_impar += i
        else:
            continue

    print('La suma total de todos los números impares de la matriz es: ',sum_impar)


def media_aritmetica(fuente):
    suma=sum(fuente)
    media = suma/25

    print ('La media artimética de la matriz es: ', media)


crear_matriz()
suma_total(lis)
sum_pares(lis)
sum_impares(lis)
media_aritmetica(lis)





