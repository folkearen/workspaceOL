# paso 1
beatles = []
print("Paso 1:", beatles)

# paso 2
beatles.append("Jhon Lenon")
beatles.append("Paul McCartney")
beatles.append("George Harrinson")
print("Paso 2:", beatles)

# paso 3
for i in range(1):
    beatles.append(input("Agregue al miembro Stu Sutcliffe : "))
    beatles.append(input("Agregue al miembro Pete Best: "))
print("Paso 3:", beatles)

# etapa 4
del beatles[3]
del beatles[3]
print("Paso 4:", beatles)

# paso 5
beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fab", len(beatles))
