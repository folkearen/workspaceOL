def anioBisiesto(anio):
    if (anio % 4 == 0 and anio % 100 !=0) or anio % 400 == 0:
        return f"El año {anio} es bisiesto."
    else:
        return f"El año {anio} no es bisiesto."
     
print(anioBisiesto(int(input("Ingrese un año para saber si es bisiesto: "))))