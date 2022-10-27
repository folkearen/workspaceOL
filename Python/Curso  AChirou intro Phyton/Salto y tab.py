#Si coloco \n se produce un salto de línea
print("Insertaré un salto de línea aquí \nesto estará en la línea de abajo")
#Si coloco \t incerta una tabulación
print("\tInsetaré una tabulación aquí \tdebería haber una espacio ampli antes")
#Si debo escribir \n o \t y no deseo realizar la acción debo por r antes de la cadena
print(r"no se realizara la acción C:\nombres\trabajo")
#Tabién puedo usar triple comilla para ahorra el \n pero no funciona para \t
print("""Debe imprimir los saltos
sin mayor problema
las líneas que desee""")

#print("casa" , "Perro" , "Auto")
print("Mi", "nombre", "es", "Python.", sep="//**") #argumento de palabra clave sep separa los argumentos con la cadena que se le indique
print("Monthy Python", end= "    *    ") #En reemplaza el salto de línea de la ejecución de print por una cadena que se le indique
print("Prueba")

print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
print("print")

print("Fundamentos","Programación","en", sep="***", end="...")
print("Python")

print("Casa" *3)#Puedo multiplicar las veces que se imprime el mismo estring la veces deseadas

#Recordar \ se denomina scape y excente de la regla de sintaxis en las cadenas.
print("Me llaman \"super Alan\" ") #En este ejemplo puedo usar comillas
#dentro de un cadena si que esta se rompa tambien puedo intercalar entre comillas simples y dobles
print('Me llaman "super Alan" ')

print(2**3)#potencias