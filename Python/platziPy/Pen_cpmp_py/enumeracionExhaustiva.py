"""Tambien llamada adivana y verifica
De los primeros algoritmos que debes tratar


Enumera todas las posibilidades, es mas ineficiente pero no importa con la rapidez
de las computadoras actuales
"""

objetivo = int(input("Escoje un entero: "))
respuesta = 0

while respuesta**2 < objetivo:
    respuesta += 1

if respuesta**2 == objetivo:
    print(f"La raiz cuadrada de {objetivo} es {respuesta}")
else:
    print(f"{objetivo} no tiene raiz cuadrada  exacta")