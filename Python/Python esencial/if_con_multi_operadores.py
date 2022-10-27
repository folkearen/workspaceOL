salario_presidente = int(input('ingrese salario del presidente: '))
print('Salario del presidente es ' + str(salario_presidente))

salario_director = int(input('ingrese salario del director: '))
print('Salario del director es ' + str(salario_director))

salario_supervisor = int(input('ingrese salario del supervisor: '))
print('Salario del supervisor es ' + str(salario_supervisor))

salario_administrativo = int(input('ingrese salario del administrativo: '))
print('Salario del administrativo es ' + str(salario_administrativo))

if salario_administrativo<salario_supervisor<salario_director<salario_presidente:
    print('Todo esta correcto')
else:
    print("Hay una falla en la empresa")


edad = int(input('Ingrese edad: '))

if 17<edad<100:
    print('Puede entrar')
else:
    print('No puede entrar')