"""En Python las funciones lambda. funciones anonimas o funciones 
si nombre, son funciones sin identificador

Su estructura 

lambda argumentos : expresion

en PY se escribe en una sola linea de codigo, pero todos los
argumentos que necesitemos.

se expresa con un identificador, que es una variable que contiene
un objeto de tipo funcion que retorna toda la expresion, y se 
llama con el noombre de la variable
No es necesario el return
"""
palindrome = lambda string :  string == string [::-1]

print(palindrome('ana'))
print(palindrome('kayak'))
print(palindrome('castor'))
