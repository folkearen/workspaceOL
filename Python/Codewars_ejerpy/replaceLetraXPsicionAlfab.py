"""
Reemplazar con la posición del alfabeto
Bienvenido.

En este kata se requiere que, dada una cadena, reemplace cada letra con su posición en el alfabeto.

Si algo en el texto no es una carta, ignóralo y no lo devuelvas.

"a" = 1 "b" = 2

Ejemplo
alphabet_position("The sunset sets at twelve o' clock.")
Debe devolver ( como una cadena )"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

"""
def alphabet_position(text):
    text = text.lower()
    alphabet = "-abcdefghijklmnopqrstuvwxyz"
    position = ""
    for char in text:
        if char in alphabet:
            position += str(alphabet.index(char)) + " "

    return position.strip()

print(alphabet_position("The sunset sets at twelve o' clock."))

#Otra forma
def alphabet_position(s):
  return " ".join(str(ord(c)-ord("a")+1) for c in s.lower() if c.isalpha())

#Otra forma
from string import ascii_lowercase


def alphabet_position(text):
    return ' '.join(str(ascii_lowercase.index(n.lower()) + 1) for n in text if n.isalpha())