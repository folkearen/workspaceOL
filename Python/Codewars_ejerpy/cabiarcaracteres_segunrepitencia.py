"""Se presento un problema con los signos ( ) presentes en la cena
a analizar, ya que al ir cambiando las letras a ( ) detecta siempre 
mas ( ) de los que deberia

Solucion, crear una lista con la cantidad de veces presente por cada
caracter un int, luego convertir ese int en ( o ) agregando a nueva 
variable creando una nueva cadena
"""

def duplicate_encode(word):
    word = word.lower()
    count = [word.count(i) for i in word]
    newword=""
    
    for i in count:
        if i == 1:
            newword += "("
        else:
            newword += ")"
            
    return newword
       
#Otraforma
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

print(duplicate_encode("JHA ntfCTULhThgfD("))
