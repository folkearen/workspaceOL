import sys 
sys.path.append("/Users/alanm/Desktop/imprimeHolaMundo.py")
#Importo el modulo sys,el path es una lista de direcciones donde python busca los modulos integrados,
#y es una lista de python, por tanto puedo agregar la ruta de un modulo que este en una carpeta diferente al del main.
#en este caso la ruta a la carpeta ejemplo2 y el modulo imprimeHolaMundo.



import ejemSumaMod #En la misma carpeta creo un modulo de Pyhton (archivo.py)
#luego lo importo, import seguido del nombre del modulo

import ejemSaludoModu as sal
#Puedo imprtar un modulo y media "as" asignarle un alias, 
# así se acortan el nommbre de modulos muy largos y aw ocupan normalmente





opereracion = ejemSumaMod.operaciones(2,2) 
#Para ocupar las funciones debo poener el nombre del módulo.funcion()

print(opereracion)
print(ejemSumaMod.pan) 
#Puuedo ocupar sus variables, en% este caso la var pan = "batido"

ejemSumaMod.pan = "Coliza" 
#Incluao puwso modificarla dentro de otro módulo, no fecta la var en modulo
# original. 

print(ejemSumaMod.pan) 

luzCocina = ejemSumaMod.Lampara()
#Puedo instancias objetos de clases que pertenecen a otros módulos
print(dir(luzCocina))


saludar = sal.saludar("Alan")
#EStoy ocupando la función saludar del modulo ejemSaludoModu, mediante al abreviatura "sal"
#UtilIzando la misma sintaxis de modulo.funcion()
print(saludar)

print(sal.como_me_llamo())
 #devuelve en nombre del modulo "ejemSaludoModu". 
 #Si esta función fuera porpia de este modulo y la ejecutara desde este mismo, devolveria
 # __main__ y no "importModulo", si creara la función aquí e importara este módulo a otro,
 #y ejecutra la función, si apareceria con el nombre desigando, basicamente main es 
 #asiganado como nombre al modulo que se esta ejecutando.


