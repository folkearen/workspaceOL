
#Convertidor millas a kilometros
kilometros = 12.25
millas = 7.38

millas_a_kilometros = millas * 1.60
kilometros_a_millas = kilometros / 1.60

print(millas, " millas son ", round(millas_a_kilometros,1), " kilómetros ")
print(kilometros, " kilómetros son ", round(kilometros_a_millas,1), " millas ")
#Round() se le entrega como parámetro el número de decimales
#a los que se desea redondear, si se pone cero redondea a 0 (por ende entero connotado como flotante)
#Convertidor de celcius a farenheit

celcius = 1
farenheit = 1

celcius_a_farenheit = (celcius*9/5) + 32
farenheit_a_celcius = (farenheit - 32) * 5/9

print("1 grado C es igual ", round(celcius_a_farenheit, 3), "grados Farenheit")
print("1 grado F es igual", round(farenheit_a_celcius, 3), "grados celcius")

#Conversor horas a segundos
#este programa calcula los segundos en cierto número de horas determinadas 
# este programa fue escrito hace dos días

horas = 1
segundos = 3600 # número de segundos en una hora

print("Horas: ", horas) 
print("Segundos en", horas, "horas: ", horas * segundos)

#caclcular hipotenusa
cateto_a = float(input("Inserta la longitud del primer cateto: "))
cateto_b = float(input("Inserta la longitud del segundo cateto "))
hipo = (cateto_a**2 + cateto_b**2) ** .5
print("La longitud de la hipotenusa es: ", hipo)
#o tambien 
cateto_a = float(input("Inserta la longitud del primer cateto: "))
cateto_b = float(input("Inserta la longitud del segundo cateto "))
print((cateto_a**2 + cateto_b**2) ** .5) #print acepta como argumento operaciones numericas,
#permitiendo obviar una variable de almacenamiento para la operación
#esto implica que el resultado no se podra ocupar para otras operaciones.

cateto_a = float(input("Ingresa la longitud del primer cateto: "))
cateto_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es: " + str((cateto_a**2 + cateto_b**2) ** .5))
#Tansforma el resultado numeral en una cadea
#Lo importante es buscar el factor de conversión

var = 1
print(var)
var = var + 1
print(var)
var += 1 #metodo abreviado, simplifica el tener que escribir nuevamente el nombre de la variable a la derecha
print(var)

#Calcular la hora de termino segun hora de entrada y duración(horas/minutos)
hora = int(input("Hora de inicio (horas): "))
minu = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
minu = minu + dura # encuentra el total de minutos
hora = hora + min // 60 # encuentra el número de horas ocultos en los minutos y actualiza las horas
minu = minu % 60 # corrige los minutos para que estén en un rango de (0..59)
hora = hora % 24 # corrige las horas para que estén en un rango de (0..23)
print(hora, ":", minu, sep='')

#mi versión
hora = int(input("Hora de inicio (horas): "))
minu = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

horas_a_minutos = hora*60
minutosTotales = (((horas_a_minutos + minu + dura)//60)%24)
fraccionMinutos =((horas_a_minutos + minu + dura)%60)

print(minutosTotales, ":", fraccionMinutos)

#Busqueda de un número mayor con función max()
# lee tres números
numero1 = int(input("Ingresa el primer número:"))
numero2 = int(input("Ingresa el segundo número:"))
numero3 = int(input("Ingresa el tercer número:"))

# verifica cuál de los números es el mayor
# y pásalo a la variable de mayor número

numeroMayor = max(numero1,numero2,numero3)#se entregan como parametros los argumentos del input
numeroMenor = min(numero1,numero2,numero3)#Calcula el número menor
# imprimir el resultado
print("El número más grande es:", numeroMayor, " y el más pequeño es:", numeroMenor) 
#NOTA: al variable no almacena todos los numeros ingresados
#solo va almacenando el que ocupa e lugar de menor y mayor antes
#del nuevo ingreso de argumentos. 

# Almacenamiento de numero mayor con while
numeroMayor = -999999999

# Ingresa el primer valor
numero = int(input ("Introduzca un número o escriba -1 para detener:"))

# Si el número no es igual a -1, continuaremos

while numero != -1:
    # ¿Es el número más grande que el número más grande?
    if numero > numeroMayor:
        # Sí si, actualiza el mayor númeroNúmero
        numeroMayor = numero
    # Ingresa el siguiente número
    numero = int (input("Introduce un número o escribe -1 para detener:"))
print("El número más grande es:", numeroMayor)
#Almacenamiento de numero mayor con while más brack 
numeroMayor = -99999999
contador = 0

while True:
    numero = int (input ("Ingresa un número o escribe -1 para finalizar el programa:"))
    if numero == -1:
        break
    contador += 1
    if numero > numeroMayor:
        numeroMayor = numero
        print("Hay", contador, "número almacenados")

if contador != 0:
    print("El número más grande es", numeroMayor)
else: print("No ha ingresado ningún número")
# Imprimir el número más grande
print("El número más grande es:", numeroMayor)

#Calculadora de impuestos
ingreso=float(input("Ingrese el ingreso anual:"))


if ingreso <= 85528 :
    impuesto = ((ingreso/100*18)-556.2)
    if impuesto <= 0: impuesto = 0.0
elif ingreso > 85528 :
    excedente = ingreso - 85528
    impuesto = ((excedente/100*32) + 14839.2)
    if impuesto <= 0: impuesto = 0.0

impuesto=round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")

#Calculadora de año bisiesto 
#Mi versión 
año = int(input("Introduzca un año:"))


if año <= 1582 : print("El año ingresado no pertenece al calendario gregoriano")

if año >= 1582 :
    if (año % 4 == 0) :
        print("Año bisiesto")
    elif (año % 100 == 0) :
        print("Año común")
    elif (año % 400 == 0) :
        print("Año bisiesto")
    else :
        print("Año común")
        

#Con las condiciones invertidas, se puede ocupar el else con 
#bloques condicionales anidados
año = int(input("Introduzca un año:"))

if año < 1582:
	print("No dentro del período del calendario gregoriano")
else:
     if año % 4 != 0:
          print("Año común")
     elif año % 100 != 0:
          print("Año bisiesto")
     elif año % 400 != 0:
          print("Año común")
     else:
          print("Año bisiesto")

#contador de número pares e impares 
numerosImpares = 0
numerosPares = 0

numero = int(input("Introduzca unn numero o escriba 0 para terminar: "))

while numero != 0 :
    if numero % 2 == 1 :
        numerosImpares += 1
    else:
        numerosPares += 1
        
    numero = int(input("Introduzca unn numero o escriba 0 para terminar: "))

print("Total de números imapares ingresados: ", numerosImpares)
print("Total de números impares ingresados: ", numerosPares)

#Implementaciónd e un contador
contador = 5
while contador != 0:
    print("Dentro del ciclo: ", contador)
    contador -= 1
print("Fuera del ciclo", contador)


#Adivina el número secreto
numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
numero = int(input("Indica el número : "))

while numero != numeroSecreto:
    print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
    numero = int(input("Indica el número : "))
print("¡Bien hecho, muggle! Eres libre ahora")

#Palabra clave while +  break 
while True :
    palabras =input("Introduzca la plabara secreta: ")
    if palabras == "chupacabras":
        print("¡Has dejado el ciclo con éxito!")
        break

#Cálculo de potencias con cilco for
pow = 1
for exp in range(16):
    print ("2 a la potencia de", exp, "es", pow)
    pow *= 2 


#Contador de segundos en mississippi
import time

    # Escribe un ciclo for que cuente hasta cinco.
    # Cuerpo del ciclo: imprime el número de iteración del ciclo y la palabra "Mississippi".
    # Cuerpo del ciclo - uso: time.sleep (1)

# Escribe una función de impresión con el mensaje final.
for s in range(1,6):
    print(s, "Mississippi")
    time.sleep(1)

#Comedor de vocales
userWord = input("Ingrese una palabra: ")
userWord = userWord.upper()

for letter in userWord:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else : print(letter)



#construcción de piramide con bloques sumando uno por cada piso que es la altura

bloques = int (input("Ingrese el número de bloques:"))

altura = 0
encapa = 1 # numero de bloques por capa empieza en 1
while encapa <= bloques:
	altura += 1
    
	bloques -= encapa
  
	encapa += 1
    
print("La altura de la pirámide:", altura)

#En 1937, un matemático alemán llamado Lothar Collatz formuló una hipótesis intrigante (aún no se ha comprobado) que se puede describir de la siguiente manera:
#Toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0.
#Si es par, evalúa un nuevo c0 como c0 ÷ 2.
#De lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1.
#Si c0 ≠ 1, salta al punto 2.
#El número siempre tiende a 1

#Mi versión
c0 = int(input("Ingrese número entero que no se negativo ni cero: "))
paso = 0
while c0 != 1 :
	if c0 % 2 == 0 :
		c0 //= 2
		paso += 1
		print(c0)
	elif c0 % 2 == 1 :
		c0 = 3 * c0 + 1
		paso += 1
		print(c0)
else: print("Número incorrecto")

print("Pasos", + paso)

#versiónSolución 
c0 = int (input("Ingrese c0:"))

if c0 > 1:
    pasos = 0
    while c0 != 1:
        if c0 %2 != 0:
            cnew = 3 * c0 + 1
        else:
            cnew = c0 // 2
        print(c0)
        c0 = cnew
        pasos += 1
        print("pasos =", pasos)
else:
        print("Valor de c0 incorrecto")

#Cambiar un elemnto de string por "X"
for digit in "0165031806510" :
	if digit == "0":
		print("x", end="")
		continue

	print(digit, end="")