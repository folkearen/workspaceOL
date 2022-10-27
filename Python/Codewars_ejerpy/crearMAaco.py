"""
************************
*  Create a frame!      *
*           __     __   *
*          /  \~~~/  \  *
*    ,----(     ..    ) *
*   /      \__     __/  *
*  /|         (\  |(    *
* ^  \  /___\  /\ |     *
*    |__|   |__|-..     *
*************************
Dada una matriz de cadenas y un carácter que se usará como borde, genere el marco con el contenido dentro.

Notas:

Mantenga siempre un espacio entre la cadena de entrada y los bordes izquierdo y derecho.
La cadena más grande dentro de la matriz siempre debe caber en el marco.
La matriz de entrada nunca está vacía.
Ejemplo
frame(['Create', 'a', 'frame'], '+')

Producción:

++++++++++
+ Create +
+ a      +
+ frame  +
++++++++++
""" 

def frame(text, char):
    a = [len(i) for i in text] #Se paro las longitudes de las plabras para sacar la mas larga y generar margenes superior e inferior
    c = ''#Inicio la variable
    for i in text:
        c += f"{char} {i}{' '*(max(a)-len(i))} {char}\n" #recorro la lista generando un texto con el caracter mas un espcio mas la plabra mas espacios distantes al margen derecho, margen derecho y salto de linea
    return f'{char * (max(a) + 4)}\n{c}{char * (max(a) + 4)}' #retorna magen superior, palabras con margen izquierdo, espacio m espacio y margen derecho


print(frame(["alan", 'Munoz', 'Badillo'], "+"))




    