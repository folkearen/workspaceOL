import random
import os
"""
Reglas incorporar comprehension
Manejo de errores
Manejo de archivos
Investigar funcion enumerate
metodo get de diccionario
la sentencia os.sistem("clear") para limpiar la pantalla

Mejoras anadir sistema de puntos, dibujar un ahorcado con sistema ASCII
mejorar interfaz
"""
def read_data(ruta):
    with open(ruta, "r", encoding="utf8") as f:
        words = []
        for word in f:
            words.append(word.strip().upper()) #strip quita lo que esta alrrededor, en este caso el salto de linea
                        #word.replace("\n", '') a canio de strip.
        return words

def run():
    data = read_data("medioPY/data.txt") #Ejecuto la funcion que extrae las palabras del la BB.DD, y elamaceno su tertorno en la variable DATA
    chosen_word = random.choice(data) #Escojer una palabra al azar de data
    chosen_word_list = [letter for letter in chosen_word ]#Crea una lista con cada una d elas letras de la palabra al azar
    chosen_word_list_underscores = ["_"] * len(chosen_word_list)#Crea una lista compuesta de guinoes bajos igual al numero de letras de la palabra escogida
    letter_index_dict = {} #DEclara un diccionario para los indices de las letras
    for idx, letter in enumerate(chosen_word): #enumerate enumera desde el cero los contenidos que se asignen, al recorrer la lista vamos almacenado cada numero y cada letra en las variables correspondientes
        if not letter_index_dict.get(letter):#Si la letra de la plabra no existe como clave en el diccionario
            letter_index_dict[letter] = [] #agraga esa clave con varlor vacio como lista ( entre conchetes, para luego usarlos como iindices)
        letter_index_dict[letter].append(idx)#Luego a esa clave que la letra de la palabra ya existente, le asigna valor numerico idx
    
    while True:
        os.system("clear")#Comando limpia la termina
        print("¡Adivina la palabra!")
        for element in chosen_word_list_underscores:#Recorreo la lista de guines
            print(element + " ", end="")#Imprime guinos con un espacio entre ellos, y da termino con un string
        print("\n")#imprime salto de linea
        
        letter = input("Ingrese una leta: ").strip().upper()
        assert letter.isalpha(), "Solo puedes inrgresa letras"

        if letter in chosen_word_list: #busca la letra en la lista de letras de la plabra escogida
            for idx in letter_index_dict[letter]: #Recorer con idx el diccionario
                chosen_word_list_underscores[idx] = letter
        
        if "_" not in chosen_word_list_underscores: #Si no quedan guiones bajos
            os.system("clear")
            print("¡Ganaste! La palabra era ", chosen_word )
            break #Sale del ciclo



    
    
    
    



if __name__ == '__main__':
    run()