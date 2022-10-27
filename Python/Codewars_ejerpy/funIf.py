"""
Cree una función llamada _ifque tome 3 argumentos: un valor booleano booly 2 funciones
 (que no toman ningún parámetro): func1 y func2

Cuando bool es veraz, func1debe llamarse; den​​lo contrario, llame al func2.
"""
def truthy(): 
  print("True")
  
def falsey(): 
  print("False")

def _if(bool, func1, func2):
    return func1() if bool == True else func2()

_if(True,truthy,falsey)
_if(False,truthy,falsey)
