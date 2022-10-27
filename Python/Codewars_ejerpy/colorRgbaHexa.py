hexa = {
    "10":"A",
    "11":"B",
    "12":"C",
    "13":"D",
    "14":"E",
    "15":"F"
}


nInicial = 7000
l1 =[str(nInicial % 16)]
while nInicial > 16:
    nInicial //= 16
    resto = nInicial % 16
    l1.insert(0,str(resto))
l2 = []
#for rhexa in l1:
#    if rhexa in hexa:
#        l2.append(hexa[rhexa])
#        continue
#    l2.append(rhexa)


print( "".join(l2))

