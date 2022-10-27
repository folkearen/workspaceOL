palabras = ["casa", "sol", "perro"]

for i in palabras:
    if i == 'sol':
        print("Encontrada")
        break
else:
    print("No encontrasa")

"""Puedo usa un else junto a un for para dar un respuesta, el else se ejecutara siempre
salvo que el bucle se rompa por eso el break"""

for i in range(100,0,-1):
    print(i)

for i in reversed(range(1,101)):
    print(i)