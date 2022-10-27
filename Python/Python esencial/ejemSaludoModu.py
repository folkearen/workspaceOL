def saludar(name):
    return f"Hola estimado {name}, que tenga buen día"

def como_me_llamo():
    return __name__ #devuelve en nombre del modulo "ejemSaludoModu", si ha sido importado
    #y se ejecuta desde otro módulo, si se ejecuta del mismo modulo devolvera __main__

print(como_me_llamo())



"""
print("hola) si se escribe codigo en el ámbito global, o sea fuera de funciones y clases
este se ejecutara si o si desde el modulo al que hemos importado, ejemplo, si importara este modulo
a otro, el print se ejecutaria en ese otro modulo, por eso se debe tener cuidado.

 """ 