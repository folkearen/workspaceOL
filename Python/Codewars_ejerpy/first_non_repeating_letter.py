"""Escriba una función llamada first_non_repeating_letterque tome una entrada de cadena y devuelva el primer carácter que no se repite en ninguna parte de la cadena.

Por ejemplo, si se le da la entrada 'stress', la función debe devolver 't', ya que la letra t solo aparece una vez en la cadena y aparece primero en la cadena.

Como desafío adicional, las letras mayúsculas y minúsculas se consideran el mismo carácter , pero la función debe devolver el caso correcto para la letra inicial. 
Por ejemplo, la entrada 'sTreSS'debería devolver 'T'.

Si una cadena contiene todos los caracteres repetidos , debería devolver una cadena vacía ( "") o None-- ver ejemplos de pruebas."""

def first_non_repeating_letter(string):
    repetitions = [ string.count(h) for h in string]
    if 1 not in repetitions:
        return ""
    amount = string.lower()
    for i in amount:
        if amount.count(i) == 1:
            noRepeat = i
            break
    for j in string:
        if j == noRepeat or j == noRepeat.upper():
            return j

def first_non_repeating_letter(string):
    for x in string:
        if string.lower().count(x.lower()) == 1:
            return x
    return ''

def first_non_repeating_letter(string):
    singles = [i for i in string if string.lower().count(i.lower()) == 1]
    return singles[0] if singles else ''