print("Bienvenidos a sumar, ingresa dos número y obtendras la suma de estos")

#primero = input("Ingrese primer número: ")
#segundo = input("Ingrese segundo número: ")

#primerNumero = int(primero)
#segundoNumero = int(segundo)

#print(primerNumero + segundoNumero)

primerDato = input("Ingrese dato: ")

try: # "intenta" ejecturar la lógica indicada
    uno = int(primerDato)
except: # "si no puede has algo" ejecutar la lógica la convierte en un dato indicadp
    uno = " "
#Validación inmediata
if uno == " ": print("dato incorreceto"), exit()

segundoDato = input("Ingrese dato: ")

try:
    dos = int(segundoDato)
except: 
    dos = " "
#Valudación inmediata
if dos == " ": print("dato incorreceto"), exit()

print(uno + dos)

#Validación al final
#if uno == " " or dos == " ":
    #print("Ingresaste mal los datos intenta solo con númro")
#else:
   # print(uno + dos)