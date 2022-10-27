"""Crea una función que responda a la pregunta "¿Estás tocando el banjo?".
Si tu nombre comienza con la letra "R" o "r" minúscula, ¡estás tocando el banjo!

La función toma un nombre como único argumento y devuelve una de las siguientes cadenas:

name + " plays banjo" 
name + " does not play banjo"

Nota: habia olvidador poner los parentesis al metodo lower(), y sobraba un espacio al final de la cadena del else.


"""

def are_you_playing_banjo(name):
    return name + " plays banjo" if name[0].lower() == 'r' else name + " does not play banjo"

print(are_you_playing_banjo("Rikke"))

#otra forma
    # if name.startswith('R') or name.startswith('r'):
    #     return name + ' plays banjo'
    # else:
    #     return name + ' does not play banjo'