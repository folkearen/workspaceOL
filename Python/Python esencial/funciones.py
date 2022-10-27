
def nombre_completo(nombre, apellido, inverso=False):
    if inverso: #inverso=True
        return f'{apellido}{nombre}'
    else:
        return f'{nombre}{apellido}'


# print(nombre_completo('Alan', ' Munoz' ))#inverso queda por defecto
# print(nombre_completo(' Alan', 'Munoz', inverso=True ))
# print(nombre_completo(apellido=' Munoz', nombre='Alan'))


def suma(*args): #Trabajar con multiples parametros, los convierte a tupla, args es un convencion, puedo usar otra palabra, 
    #solo el asterisco es obligatorio
    resultado = 0
    for i in args:
        resultado += i
    print(resultado)
    
suma(1,2,3,4,5)

def resta(a=1,b=1,c=1):#puedo predefinir uno o todos los parametros, 
    #lo importante es que los parametros definidos deben ir despues de los definidos
    resultado = a-b-c
    print(resultado)

resta()
resta(5)
resta(5,2)
resta(5,2,4)


def inventarioCoches(**kwargs):#toma los parametros predefinidos y lo convierte a diccionarios
    print(kwargs)

inventarioCoches(tipo="coche",color="rojo" ) 


#Multiples return, retona una tupla con los multiples resultados
def operaciones(a,b):
    return a + b, a - b, a * b, a / b 

resultados = operaciones(5,2)

print(resultados)

#Funcion lambda es una funcion anonima aosciada a una variable

anonima= lambda: print("hola")
anonima()
#Lambda con parametros
lamParametros = lambda nombre, nombre2: print("hola",nombre, "adios",nombre2)
lamParametros("alan", "alan")

#Lambda con retorno, no requiere la palabra reservada return

sumatoria = lambda x: x+x #<==== lo que retorna

print(sumatoria(2))
