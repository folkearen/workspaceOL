"""
Para manejar defensivamente posibles errores
assert <expresion booleana>, <mensaje de error>
"""
def primera_letra(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:

        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra)>0 , f'No se admiten str vacios'
        assert palabra != " ", f'No se admiten espacios en blanco' 

        primeras_letras.append(palabra[0])
    
    
    
    return "".join(primeras_letras)


print(primera_letra(['amor','lago', 'amanecer','n']))
