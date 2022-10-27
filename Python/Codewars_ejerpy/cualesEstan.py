"""
Dadas dos matrices de cadenas y devuelve una matriz ordenada en orden lexicográfico de las cadenas de 
las cuales son subcadenas de cadenas de .a1 a2 r a1 a2
ejemplo:
a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

Devuelve ["arp", "live", "strong"]
"""

def in_array(array1, array2):
    
    resultado = []
    for i in array1:
        for j in array2:
            if i in j:
                if i in resultado:
                    continue
                resultado.append(i.lower())
    return sorted(resultado)

               
   
in_array(["arp", "live", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"])
    
    
    #return []