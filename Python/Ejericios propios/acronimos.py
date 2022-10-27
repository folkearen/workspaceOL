def initials(phrase):
    print(phrase)
    words = phrase.split()
    print(words)
    result = ""
    for word in words:
        result += word[0]
    return result.upper()

print(initials("Diseno Universal de Aprendizaje"))