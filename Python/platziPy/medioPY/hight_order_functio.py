"""
Hight order funcions, funciones de orden superior

funciones que reciben como parametro otra funcion
"""

from functools import reduce

def saludo(func):
    func()

def hola():
    print("Hola!!!")

def adios():
    print("Adios!!!")

saludo(hola)
saludo(adios)

"""----------------------------------------------------"""
my_list =[1,2,3,4,5,6,7,8,9,10]

odd = list(filter(lambda x: x % 2 != 0, my_list))
print(odd)

"""_____________________________________________________"""
my_list =[1,2,3,4,5,6,7,8,9,10]

squares = list(map(lambda x: x**2 , my_list))
print(squares)

"""*******************************************************"""
# sumlis = [1,2,3,4,5]
# allsum = 0
# for i in sumlis:
#     allsum += i
# print(allsum)
"""Debo importar reduce"""
sumlis = [1,2,3,4,5]

allsum = reduce(lambda a, b : a + b, sumlis)
print(allsum) 

"""En la primera interacion los parametros a y b seran el primer 
y segundo elemento de la lista, en la seguninteracion, el producto
de los primeros dos elemntos de la lista pasan a ser el parametro a
y el b el tercer elemento de la lista, y ese producto pasa a ser parametro a
y b el siguiente elemnto de la lista, sucesibamente"""
 