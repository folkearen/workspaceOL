"""
Contar el número de duplicados
Escriba una función que devuelva el recuento de caracteres alfabéticos distintos que no
 distinguen entre mayúsculas y minúsculas y dígitos numéricos que se producen más de una 
 vez en la cadena de entrada. Se puede suponer que la cadena de entrada contiene solo 
 alfabetos (tanto en mayúsculas como en minúsculas) y dígitos numéricos.


Ejemplo
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
"""

def duplicate_count(text):
    return len([i for i in 'abcdefghijklmnopqrstuvwxyz1234567890' if text.lower().count(i) > 1 ])
    #Directamente en el return solo se genera la lista y no colocarle una viariable para ella

print(duplicate_count("aabccdd"))