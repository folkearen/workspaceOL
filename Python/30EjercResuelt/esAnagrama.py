def isAnagrama(palabra1, palabra2):
    if len(palabra1) == len(palabra2):
        megaPalabra = palabra1.lower() + palabra2.lower()
        conteoLetras = [megaPalabra.count(i) for i in megaPalabra]
       
        if 1 in conteoLetras:
            print("No es un Anagrama")
        else:
            print("Es Anagrama")

    else:
        print("No es un Anagrama")

#otra forma
def esAnagrama(palabra1, palabra2):
    if len(palabra1) == len(palabra2):
        palabra1 = palabra1.lower()
        palabra2 = palabra2.lower()
        if sorted(palabra1) == sorted(palabra2):
            print("Es anagrama")
        else:
            print("No es un Anagrama")   
        
    else:
         print("No es un Anagrama")   

#Otra forma
def is_anagram(s1, s2):
    return set(s1) == set(s2) 
print(is_anagram("ballena", "llenaba"))

isAnagrama("perro", "Dinosaurio")
isAnagrama("Casa", "Caso")
isAnagrama("bellena", "Llenaba")
isAnagrama( 'Enrique', 'quieren')

esAnagrama("perro", "Dinosaurio")
esAnagrama("Casa", "Caso")
esAnagrama("ballena", "Llenaba")
esAnagrama( 'Enrique', 'quieren')
