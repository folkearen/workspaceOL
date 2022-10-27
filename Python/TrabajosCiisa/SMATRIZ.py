# sumaimpares=0
# sumapar=0
# pares=0
# bb=0
# prom =0

def examen():
    matriz=[]
    lista=[]
    filas = int(input("cantidad de fila: "))
    columnas = int(input("cantiadad de columnas:"))

    for i in range(filas):
        matriz.append([0] * columnas)

    for f in range(filas):
        for c in range(columnas):
            matriz [f][c] = int(input("elemento %d, %d : " % (f, c)))

    print(matriz)

    return lista


def sumares(lista):
    for num in lista:
        print(num)


def sumatotal(lista):
    acum = 0
    for num in lista:
        acum += num
    print("la suma total es: ",acum)
    prom = acum / 25
    print("el promedio es",prom)

def impares(lista):
    sumaimpares= 0
    sumapar= 0
    for num in lista:
        if num %2==0:
            sumapar += num
            
        else:
            sumaimpares+=num
           
    print("los pares son:", sumapar)
    print("los impares son:", sumaimpares)

        
lis = examen()
sumatotal(lis)
impares(lis)