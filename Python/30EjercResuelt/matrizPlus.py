

def crear_matriz():
    matriz = [[[None]for i in range(3)] for j in range(3)]
    print('Creando un matriz 5x5 con un total de 25 números... \n')
    for filas in range(3):
        for columnas in range(3):
            matriz[filas][columnas] = int(input('ingrese un número entero '))
    
    print('\n'+'Generando su matriz'+'\n')

    for i in matriz:
        print(i,'\n')
    return(matriz)

def contarDatosMatriz(matriz):
    cantidadDatosMatriz = 0
    for i in matriz:
        cantidadDatosMatriz += len(i)
    print(cantidadDatosMatriz)


contarDatosMatriz(crear_matriz())