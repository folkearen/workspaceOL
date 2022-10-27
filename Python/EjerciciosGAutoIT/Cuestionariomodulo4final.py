'''
Pregunta 1
La función format_address separa partes de la cadena de dirección en nuevas cadenas: house_number y street_name, y devuelve: 
"house number X on street named Y". El formato de la cadena de entrada es: número de casa numérico, seguido del nombre de la
 calle que puede contener números, pero nunca solos, y puede tener varias palabras. Por ejemplo, "123 Main Street", "1001 1st Ave" o "55 North Center Drive". 
 Rellena los huecos para completar esta función. '''

def format_address(addres_string):
    house_number = "" #Inicia las variable
    street_name = "" #Inicia las variable
    addres_string = addres_string.split() #Corata el string en diversos string mediante los espacios creando una lista con ellos.
    for i in addres_string: #Recorro la lista
        if i.isnumeric(): #verifico si el string de la lista iterado esta compuiesto solo de numeros.
            house_number += i #si es asi lo sumo al string house_numer
        else:
            street_name += i + " " #Sino corresponde el nombre de calle y los sumo a street_name, mas un espacio para separar la palbras.
    
    return "house numer {} on street named {}".format(house_number, street_name) #retorna los datos en una cadena fomateada

"""Pregunta 2
La función Highlight_word cambia la palabra dada en una oración a su versión en mayúsculas. Por ejemplo, resaltar_palabra("Que tengas un buen día", "bueno")
devuelve "Que tengas un BUEN día". ¿Puedes escribir esta función en una sola línea?"""

def highlight_word(sentence, word):
	return sentence.replace(word,word.upper()) #Uso el metodo replace, utilizando como parametros la palabra que debe ser convertida en mayuscula dentro de la sentencia.
    
print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

"""Pregunta 3
Un profesor con dos asistentes, Jamie y Drew, quiere una lista de asistencia de los estudiantes, en el orden en que llegaron al salón de clases. 
Drew fue el primero en notar qué estudiantes llegaban y luego Jamie se hizo cargo. Después de la clase, cada uno ingresó sus listas en la computadora y 
las envió por correo electrónico al profesor, quien debe combinarlas en una sola, en el orden de llegada de cada estudiante. Jamie envió un correo electrónico de seguimiento, 
diciendo que su lista está en orden inverso. Complete los pasos para combinarlos en una lista de la siguiente manera: el contenido de la lista de Drew, seguido de la lista de 
Jamie en orden inverso, para obtener una lista precisa de los estudiantes cuando llegaron.
"""
#Lista2 Drew fueron los primeros
#Lista1 Jamie sigue a los de Drew pero la anoto al reves
def combine_lists(list1,list2):
    list = list2 #Creo una nueva lista con los miebros de la lista 2 segun re1urimeinto, podria omitirse este paso y trabajar directamente con la lista 2
    list1.reverse()#invierto la lista 1 con el metodo reverse
    list.extend(list1)#extiendo lista que ya tiene los elemento de lista dos, con los elemntos de lista yuno invertidos
    return list #Retorno la lista


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

"""Ejercicio 4
Usa una lista de comprensión para crear una lista de números cuadrados (n*n). La función recibe las variables inicio y fin, 
y devuelve una lista de cuadrados de números consecutivos entre inicio y fin inclusive.
Por ejemplo, cuadrados (2, 3) debería devolver [4, 9].
"""
def squares(star,end):
    return [n*n for n in range(star, end + 1)]#Tambien n**2

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

"""Ejericio 5
Complete el código para iterar a través de las claves y valores del diccionario car_prices, 
mprimiendo información sobre cada uno.
"""
def car_listing(car_price):
    result = "" #Inicia la variable, cadena vacia
    for car, price in car_price.items(): #Itera el los items (claves y valores) de4l diccionario y los almacena en las variables car y price respectivavemente
        result += "{} costs {} dollars".format(car, price) + "\n" #suma la cadenas formateados con el modelo del carro y precio, y los ordena mediante un salto de linea.
    return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

"""Ejercicio 6
Taylor y Rory organizan una fiesta. Enviaron invitaciones y cada uno recopiló respuestas en diccionarios, con los nombres de sus amigos
y cuántos invitados traería cada amigo. Cada diccionario es una lista parcial, pero la lista de Rory tiene información más actualizada 
sobre el número de invitados. Complete los espacios en blanco para combinar ambos diccionarios en uno, con cada amigo enumerado solo una vez,
 y el número de invitados del diccionario de Rory tiene prioridad, si se incluye un nombre en ambos diccionarios. Luego imprima el diccionario resultante.
"""
# Combine ambos diccionarios en uno, con cada clave en la lista
# solo una vez, y el valor de guest1 tiene prioridad

def combine_guests(guests1, guests2):#Parametros que ser[an diccionarios.]
    guests2.update(guests1) #Actualiso el diccionario 2 con el diccionario 1, mezclandolos, considerando que el argumento de update reemplazara por sus valores si existe claves en comun con el diccionario a actualizar
    return guests2 #Retorna el segundo diccionario actualizado.


Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))


"""Ejercicio 7
Use un diccionario para contar la frecuencia de las letras en la cadena de entrada. Solo se deben contar las letras,
no los espacios en blanco, los números ni la puntuación. Las mayúsculas deben considerarse lo mismo que las minúsculas. 
Por ejemplo, count_letters("This is a sentence") debería devolver {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.
"""
# Ir a través de cada letra en el texto
# Verifique si la letra debe contarse o no
# Agrega o incrementa el valor en el diccionario

def count_letters(text):
    text = text.lower() #transfoma el contenido de text a minuscula para evitar disciminar entre mayuscula y minuscula
    result = {} #Inicia el diccionario 

    for letter in text: #Recorrre el el texto(string), letra a letra, mediante la variable letter
        if letter.isalpha(): #Si letter es una letra (de lo contrario descarta implicitamente)
            if letter not in result: #Si letter no se encuentra en el diccionario resultado, agrega la letra del texto(almacenada en letter) como clave con valor cero
                result[letter] = 0
            result[letter] += 1 #Luego le agrega el valor de 1 a la clave letter, y seguira sumando 1 al valor cada vez que se repita la letra en el texto
    return result #Devuelve el diccionario

print(count_letters("AaBbCc"))
print(count_letters("Math is fun! 2+2=4"))
print(count_letters("This is a sentence."))

