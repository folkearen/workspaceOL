lista = [3, 4]
#  Lista como una pila:
# El ultimo que entra es el primero que sale.
lista.append(10) # lista = [3, 4, 5, 6, 10]
print(">>> Pila Antes    : " + str(lista))
lista.pop() # lista = [3, 4, 5, 6]
print(">>> Pila Despues  : " + str(lista))
 
# Lista como una cola.
# El ultimo que entra es el ultimo que sale
lista.insert(0, 5) # lista = [5, 3, 4, 5, 6]
print(">>> Cola Antes    : " + str(lista))
lista.pop() # lista = [5, 3, 4, 5]
print(">>> Cola Despues  : " + str(lista))