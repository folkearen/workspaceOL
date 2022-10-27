
matriz = [[[None]for i in range(3)] for j in range(3)]
print('Creando un matriz 5x5 con un total de 25 números... \n')
lista = []

def crear_matriz():

    for filas in range(3):
        for columnas in range(3):
            matriz[filas][columnas] = int(input('ingrese un número entero '))

    print('\n'+'Generando su matriz'+'\n')

    for i in matriz:
        print(i,'\n')
    

def crear_lista():
    for j in range(len(matriz)):
        contador = j
        for i in matriz[contador]:
            lista.append(i)


def suma_total():
    suma = 0
    for j in range(len(matriz)):
        contador = j
        for i in matriz[contador]:
            suma  += i
    print("La suma de todos los números ingresados en la matriz es: ",suma)
    print('La media aritmetica es: ', suma/5)
    return suma




        
def media_aritmética(fuente):
    media = fuente/5
    print("La meida aritmpetica de la matriz es: ", media)
    

crear_matriz()
#crear_lista()
suma_total()
# media_aritmética(sume)

# def suma_pares(fuente):
#     suma_par_total = 0
#     for i in fuente:
#         if i % 2 == 0:
#             suma_par_total += i
#         else:
#             continue

#     print('La suma total de todos los números pares de la matriz es: ',suma_par_total)


# def suma_impares(fuente):
#     suma_impar_total = 0
#     for i in fuente:
#         if i % 2 == 1:
#             suma_impar_total += i
#         else:
#             continue

#     print('La suma total de todos los números impares de la matriz es: ',suma_impar_total)


# def media_aritmetica(fuente):
#     suma=sum(fuente)
#     media_aritmetica_t = suma/5

#     print ('La media artimética de la matriz es: ', media_aritmetica_t)


# def run():
#     crear_matriz()
#     matriz_operacional()
#     suma_total(matriz_operacional())
#     suma_pares(matriz_operacional())
#     suma_impares(matriz_operacional())
#     media_aritmetica(matriz_operacional())


# if __name__ == '__main__':
#     run()





