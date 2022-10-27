tabla = int(input("Ingrese ek numero que desea conocer su tabla de multiplicar"))

for i in range(1,11):
    operacion = tabla * i
    print(f'{tabla} X {i} = {operacion}')