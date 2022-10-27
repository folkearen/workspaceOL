def count_letter(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letter("Tres tristes tigres trigaban trigo en un trigal"))


#Mas complejo, evita la descriminacion entre mayuscula y minuscula, ademas considera solo las letras, ni espacios, signos ni nuemros.
def count_letters(text):
    text = text.lower()
    print(text)
    result = {}

    for letter in text:
        if letter.isalpha():
            if letter not in result:
                result[letter] = 0
            result[letter] += 1
    return result

print(count_letters("AaBbCc"))
print(count_letters("Math is fun! 2+2=4"))
