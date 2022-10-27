cubos = {}

# for i in range(1,101):
#     cubos[i] = i**3
cubos = {i:i**3 if i % 3 !=0 else "A" for i in range(1,101) }
print(cubos)

raices = {i:i**0.5 for i in range(1,1001)}
print(raices)