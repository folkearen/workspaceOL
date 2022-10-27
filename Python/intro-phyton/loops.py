#i = 0

#while i <= 5: #while = mientras
 #   print(i)
  #  i += 1 # versión corta de i=i+1


#print("_________________")

#a = 2
#while a <= 100 :
    #print (a)
   # if a == 32: 
  #      break #rompe el ciclo en esa condicion sin volver a evaluar.
 #   a *= 2

#print ("_______________")

#b = 10
#while b <= 100 :
#    b += 10
#    if b == 80:
#        continue
#    print (b)


caso1= "Alan Muñoz"

#for letra in caso1 :
    #print(letra)

listaNegra = ["Juan", "Maria", "Pedro"]

for negros in listaNegra:
    print(negros)

print("::::::::::::::::::::::::::::::::::")

listaNegra = ["Juan", "Maria", "Pedro"]

for negros in listaNegra:
    print(negros)
    if negros == "Maria": 
        break
   

print("::::::::::::::::::::::::::::::::::")

listaNegra = ["Juan", "Maria", "Pedro"]

for negros in listaNegra:
    if negros == "Maria": continue
    print(negros)

for lsitaNegra in range(5) :
    print(listaNegra)
else: 
    print("Hemos terminado")


edades = [25, 52, 40]

for negros in listaNegra:
    for edad in edades:
        print(listaNegra, edades)
    