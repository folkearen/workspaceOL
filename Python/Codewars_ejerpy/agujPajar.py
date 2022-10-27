"""
¿Puedes encontrar la aguja en el pajar?

Escriba una función findNeedle()que tome un arraymontón de basura pero que contenga uno"needle"

Después de que su función encuentre la aguja, debería devolver un mensaje (como una cadena) que dice:

"found the needle at position "además indexencontró la aguja, así que:

find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
debe volver "found the needle at position 5"(en COBOL "found the needle at position 6")
"""

def find_needle(haystack):
    return f"found the needle at position {haystack.index('needle')}"

print(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))

# otra forma
def find_needle(haystack):
    for i, x in enumerate(haystack):
        if x == 'needle': 
            return 'found the needle at position %d' % i