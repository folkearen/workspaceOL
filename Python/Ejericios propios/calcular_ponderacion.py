def calcular_ponderacion(notas):
    promedio = 0
    x = 0
    for i in notas:
        x = (i * 70) / 100
        print ("{:>8} - {}".format(i, x))
        promedio += x
    promedio = promedio // len(notas)
    print("El promedio es: ",promedio)
    return promedio

calcular_ponderacion([98, 84, 97, 79, 99, 92, 84, 95, 92, 85])