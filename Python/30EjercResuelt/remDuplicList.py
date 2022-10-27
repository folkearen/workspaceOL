"""Eliminar todos los duplicados de la lista."""

lista = [1,2,3,3, "Alan", "Pascal", "Alan", False, True]

print(set(lista))

#Otra forma
resultado = []
for data in lista:
    if data not in resultado:
        resultado.append(data)
        
print(resultado)