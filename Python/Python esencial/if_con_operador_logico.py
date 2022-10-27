print('''
Para obtener la beca debe cumplir con todos los siguientes requisitos
1. Vivir a mas de 30 km de la univesidad.
2. Tener mas de un hermano
3. el ingreso famiiar no debe sobrepasar los 1000

*Si sufre alguna discapacidad, la beca se otorga sin necesidad de requisitos
 ''')

distancia = int(input('Ingrese km de distancias a los que se encuetra su casa de la universidad: '))
hermanos = int(input('Ingrese el numero de hermnaos: '))
ingreso = int(input('Indique su ingreso familiar: '))
discapacidad = int(input('Si tiene una discapacidad marque 1 sino marque 0: '))
print('\n')
print(distancia, 'km de distancia')
print('Tiene ', hermanos, ' hermanos')
print('El ingreso es ', ingreso)
print('\n')

#Uso and y or
if distancia > 30  and hermanos> 1 and ingreso < 1000 or discapacidad == 1:
    print('Baeca aprobada')
else:
    print('No cumple los requisitos')


#uSO DE in
print('Escrituras electivas 2021')
print('DEbe elegir una de las sigientes asignaturas: "Fisica", "Quimica", "Biologia" ')

asignaturas = input('Escriba las asignaturas elegidas: ')
asignaturas = asignaturas.lower()

if asignaturas in ("fisica", "quimica", "biologia"):
    
    print('Las asignaturas ', asignaturas, ' han sido inscritas correctamente.')

else:
    print('La asignatura escogida no esta contemplada')