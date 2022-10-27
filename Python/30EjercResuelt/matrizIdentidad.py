matriz = []
matriz = [[[None]for i in range(5)] for j in range(5)]

for filas in range(5):
    for columnas in range(5):
        if filas == columnas:
            matriz[filas][columnas] = 1
        else:
            matriz[filas][columnas] = 0

print('\n'+'Generando su matriz'+'\n')
for i in matriz:
        print(i,'\n')