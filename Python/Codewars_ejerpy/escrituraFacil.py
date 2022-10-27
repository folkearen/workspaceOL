"""
Una palabra cómoda es una palabra que puede escribir siempre alternando la mano con la que escribe (suponiendo que escriba con un teclado QWERTY 
y use los dedos como se muestra en la imagen a continuación).

Dicho esto, completa la función que recibe una palabra y devuelve truesi es una palabra cómoda y en falsecaso contrario.

La palabra siempre será una cadena que constará únicamente de letras ascii desde ahasta z.

Para evitar problemas con la disponibilidad de imágenes, aquí está la lista de letras para cada mano:

Izquierda:q, w, e, r, t, a, s, d, f, g, z, x, c, v, b
Correcto:y, u, i, o, p, h, j, k, l, n, m
Ejemplos
"yams"  -->  true
"test"  -->  false
"""
from optparse import Values


def comfortable_word(word):
    izquierda = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']
    c = ""
    for i in word:
        if i in izquierda:
            c += "1"
        else:
            c += "0"
    return "00" not in c and "11" not in c
print(comfortable_word('alan')) 


# word = 'test'
# izquierda = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']
# derecha = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm'] 
# c = len(word)
# for i in word:
#     if i in izquierda:
#         c -= 1

# if c != len(word) and c > 0:
#     print(True)
# else:
#     print(False)
