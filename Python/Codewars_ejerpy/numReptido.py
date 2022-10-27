"""
Complete la función para encontrar el conteo del elemento más frecuente de una matriz. Puede suponer que la entrada es una matriz de enteros. Para un retorno de matriz vacío0

Ejemplo
input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
ouptut: 5 
El número más frecuente en la matriz es -1y ocurre 5veces.
"""



def most_frequent_item_count(collection):
    a = [collection.count(i) for i in collection]
    return max(a) if len(collection) > 0 else 0

print(most_frequent_item_count([]))

#Otras formas
def most_frequent_item_count(collection):
    if collection:
        return max([collection.count(item) for item in collection])
    return 0

def most_frequent_item_count(collection):
    return max([collection.count(i) for i in collection]+[0])