"""
Algoritmo importante
Similar a enumeracion exhaustiva pero no necesita un respuesta exacta.
Podemos aproximar soluciones con un margen de rror que llmaremos epsilon (diferencia entre 
la solucion y lo cerca que estamos de ella)

Preicion vs rapidez
"""
objetivo = int(input("Escoje un entero: "))
epsilon = 0.0001 #Que tan cerca queremos estar de nuestro obajetivo
paso = epsilon**2 #Que tanto nos vamos acercando a la respuesta con cada iteracion
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and  respuesta <= objetivo: #Abs numero absoluto
    respuesta += paso

if abs(respuesta**2 - objetivo) >+ epsilon:
    print(f"No se encontro la raiz cuadrada del {objetivo}")

else:
    print(f"La raiz cuadra de {objetivo} es {respuesta}")


