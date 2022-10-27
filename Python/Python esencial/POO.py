from abc import ABC, abstractmethod #Para poder crear una clase

class Electro:#Nombre de clases comienzan con mayúscula
    _encendido = False #cuando comienza la propiedad con un _, quiere decir que no debe ser modificada directamente
    #desde sus instancia, sino que utilizar los metodos de la clase para hacer las modificaciones correspondientes.

    def __init__(self, name): #Este es el metodo constructo, sirve para exiguir cirtas porpiedades a las instancias de clase, en este caso el parametro name, para indicar que equipo es.
        categoria = "Electro" #También puedo predterminar propiedades con su valores.
        print("Este equipo es:",name)
        print(categoria)

    def encender(self):
        self._encendido = True
    
    def apagar(self):
        self._encendido = False
    
    def isEncendido(self):
        return self._encendido

class Lampara(Electro): #Clase lampara hereda de electro, se usa parentesis 
    #y el nombre de la clase padre al declarar la clase, puedo heredar de mas clase seoarandolas con coma ,
    # sería herencia multiple, pero es buena practica evitarla.
    tipoDeApolleta = ""


luzSala = Lampara("Luz de la Sala") #Creo el objeto luzSala que es Instancia de la clase lampara y posee sus propiedades y metodos, además exige parametros para cumpkir con el constrcutor, estos van entre parentisis, sin constructor o cosntructor vacío, solo debo colocar los parentesis.

#luzSala._encendido = True, se puede asignar valor a las propiedades de un obejto pero es mala practica,
#sobre todo si lleva un _ al inicio que enfatiza el no modificar directamente

print(luzSala._encendido) #Imprimo el estado de encendido del objeto luzSala, arroja False
luzSala.encender() #enciendo la luz de la sala mediante el metodo encender
print(luzSala._encendido)#Arroja True


luzCocina = Lampara("Luz de la Cocina") #exige parametros para cumpkir con el constrcutor, estos van entre parentisis, sin constructor o cosntructor vacío, solo debo colocar los parentesis.

luzCocina.encender() #enciende luzcocina
print(luzCocina.isEncendido()) #imprime si esta encendida o no, en este caos el True por que la encendi
luzCocina.apagar()#Apago luzcocina
print(luzCocina.isEncendido())#Imprime false porque la acabo de apagar


print(dir(luzCocina))#Sirve para ver las porpiedades y métodos disponibles para una clases, ya sean propios o heredados

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass
        
class Perro(Animal):
    def sonido(self):
        print("Guau")

maltes = Perro()

maltes.sonido()
