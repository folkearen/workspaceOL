"""
Un pangrama es una oración que contiene cada letra del alfabeto al menos una vez. Por ejemplo, la frase "El zorro marrón rápido salta sobre el perro perezoso" es un pangrama, porque usa las letras A-Z al menos una vez (el caso es irrelevante).

Dada una cadena, detecte si es o no un pangrama. Devuelve True si lo es, False si no. Ignora los números y la puntuación.
"""

def is_pangram(s):
    a = s.lower()
    comparador = "abcdefghijklmnopqrstuvwxyz"
    noRepetidas = []
    repetidas = []
    for letra in a:
        if letra not in noRepetidas and letra.isalpha():
            repetidas.append(letra) 
        noRepetidas.append(letra)
   
    return comparador == "".join(sorted(repetidas))
    
#Otra forma
def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True

#Otra forma
import string
def is_pangram(s):
    return set(string.ascii_lowercase).issubset(s.lower())

#Otra forma 
import string

def is_pangram(s):
    s = s.lower()
    for token in string.ascii_lowercase:
        if token not in s:
            return False
    return True

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))