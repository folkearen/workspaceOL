"""Probablemente conozcas el sistema de "me gusta" de Facebook y otras páginas. Las personas pueden dar "me gusta" a las publicaciones de blog, imágenes u otros elementos. Queremos crear el texto que debe mostrarse junto a dicho elemento.

Implemente la función que toma una matriz que contiene los nombres de las personas a las que les gusta un elemento. Debe devolver el texto de visualización como se muestra en los ejemplos:
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Nota: Para 4 o más nombres, el número en simplemente aumenta."and 2 others"
"""
def likes(names):
    if len(names) == 0 :
        return ("no one likes this")
    elif len(names) == 1:
        return (f"{names[0]} like this" )
    elif len(names) == 2:
        return (f"{names[0]} and {names[1]} like this" )
    elif len(names) == 3:
        return (f"{names[0]}, {names[1]} and {names[2]} like this" )
    else:
        return (f"{names[0]}, {names[1]} and {len(names) - 2} others like this")

print(likes(["Alan", "Pascal", "Maria", "Julio", "Tamara"]))

#Otra forma
def likes(names):
    output = {
        0 : "no one likes this",
        1 : "{} likes this",
        2 : "{} and {} like this",
        3 : "{}, {} and {} like this",
        4 : "{}, {} and {others} others like this",
    }
    
    count = len(names)
    
    return output[min(4,count)].format(*names[:3], others=count-2)

#Otra froma
def likes(names):
    match names:
        case []: return 'no one likes this'
        case [a]: return f'{a} likes this'
        case [a, b]: return f'{a} and {b} like this'
        case [a, b, c]: return f'{a}, {b} and {c} like this'
        case [a, b, *rest]: return f'{a}, {b} and {len(rest)} others like this'


 
