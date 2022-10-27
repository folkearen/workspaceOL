def hgrb(r, g, b):
    hexa = {
    "10":"A",
    "11":"B",
    "12":"C",
    "13":"D",
    "14":"E",
    "15":"F"}
    l2 = []
    l1 = []
    rgbT = (r,g,b)
    
    for nInicial in rgbT:
        if nInicial > 255:
            nInicial = 255
        elif nInicial < 0:
            nInicial = 0
        l1 =[str(nInicial % 16)]
        while nInicial > 16:
            nInicial //= 16
            resto = nInicial % 16

            l1.insert(0,str(resto))

        for rhexa in l1:
#            if len(rhexa) == 1:
#               rhexa = "0" + rhexa
            if rhexa in hexa:
                l2.append(hexa[rhexa])
                continue 
            l2.append(rhexa)
        print(l2)
  #Agrupar en una variable el ciclo, y luego agregar dicha variable a la lista 
    # return "".join(l2)
    

print(hgrb(1, 424,17))