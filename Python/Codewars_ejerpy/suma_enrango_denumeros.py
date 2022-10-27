"""Nota, los rangos range() no pueden ir de menor a mayor, 
siempre de menor a mayor, incluso con 0 o negativos

al menos que se use reversed(range())
"""
#Usando comprhension
def get_sum(a,b):
    suma = [i for i in range(min(a, b), max(a,b)+1)]        
    return sum(suma)

    #Otra forma
    suma = 0
    for i in range(min(a,b), max(a,b) +1):
        suma += i
    return(suma)



def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))

print(get_sum(1,5))