'''
Cotandor de caracteres, palabras o frases en un texto
'''
def concatenarCaracteres():
    entrada_usuario = input("Ingrese una palabra o frase ").casefold().split() #Ojo a esta forma
    caracter_a_contar =input("Que caracter desea contar?\n").casefold()
    palabra_final = "".join(entrada_usuario)
    cuenta_caracter = palabra_final.count(caracter_a_contar)
    
    return f'Su palabra o frase inngresada es: {palabra_final}\nEl caracter "{caracter_a_contar}"aparece {cuenta_caracter} veces.'

print(concatenarCaracteres())