#EVALUACIONES
# a == b para condicionar si una variable es igual a otra
# a < b si una variable es menor que otra
# a > b Si una variable es mayor que otra 
# a != b Si una variable no es igual a otra
# a <= b Si es menor o igual a otra
# a >= b Si es meyor o igual a otra

#if 4 == 5 :
    #print("seis es mayor que cinco")
#elif 4 == 5 :  # Segunda instrucción que se ejecuta solo si la primera arroja falso, independiente que  ambas sea verdadera
    #print("4 es menor que 5") 
#elif 2 == 1 : #Puedo integrar cuentas evaluaciones elif desee
    #print("Datos correctos")
#else: #Se ejecuta si todo lo anterior es falso
    #print("los datos esablecidos no son correctos") 
usuario = "islerkain"
contraseña = "Astrid54"

#if contraseña == "Astrid21" :
    #print("Acceso autorizado")
#else:#Puedo utilizar else sin necesidad de elif
    #print("Acceso denegado")

#if  2 > 1: print("Dado pal éxito") #if de una linea para evaluaicones cortas
#print("Holi") if 5 > 2 else print("Chau") #if de una línea que evalua true y false tambien llamado operador ternario

#cerrar = "boton entrar"
#print("USted ha salido, hasta pronto" )if cerrar == "boton exit" else print("Error, vuelva a precionar el boton")

#if 2 < 5 and 3 < 1: #para evaluar dos condiciones, si amabs se cumplen (son true) se ejecuta lo indicado}
 #   print("ambas devuelven true")

#elif 2 < 0 or 1 > 0: #Para evaluar true en una de las dos condiciones y ejecutar el script, si ambas son false no se  ejecuta
   # print("Hay un true en este script")
#elif 5 == 5 and "perro" != "perro":
 #   print("SSS")
#else: #Tambien se pueden agregar elif y else
 #   print("Los parametros son false")

if usuario == "islerkain" and contraseña == "Astrid54": print("Acceso permitido")