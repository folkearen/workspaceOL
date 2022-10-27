matriz = [[[None]for i in range(5)] for j in range(5)]
print('Creando un matriz 5x5 con un total de 25 números... \n')

def crear_matriz():

    for filas in range(5):
        for columnas in range(5):
            matriz[filas][columnas] = int(input('ingrese un número entero '))

    print('\n'+'Generando su matriz'+'\n')

    for i in matriz:
        print(i,'\n')
    
    
def matriz_operacional():
    matriz_operacional = matriz[0] + matriz[1] + matriz[2] +  matriz[3] +  matriz[4]
    return matriz_operacional


def suma_total(fuente):
    sum_total =sum(fuente)
    print('La suma total de los números de la matriz es: ', sum_total)


def suma_pares(fuente):
    suma_par_total = 0
    for i in fuente:
        if i % 2 == 0:
            suma_par_total += i
        else:
            continue

    print('La suma total de todos los números pares de la matriz es: ',suma_par_total)


def suma_impares(fuente):
    suma_impar_total = 0
    for i in fuente:
        if i % 2 == 1:
            suma_impar_total += i
        else:
            continue

    print('La suma total de todos los números impares de la matriz es: ',suma_impar_total)


def media_aritmetica(fuente):
    suma=sum(fuente)
    media_aritmetica_t = suma/5

    print ('La media artimética de la matriz es: ', media_aritmetica_t)


def run():
    crear_matriz()
    matriz_operacional()
    suma_total(matriz_operacional())
    suma_pares(matriz_operacional())
    suma_impares(matriz_operacional())
    media_aritmetica(matriz_operacional())


if __name__ == '__main__':
    run()





