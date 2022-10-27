class Electro:
    nombre = ""
    encendido = False
    def __init__(self, nombre):
        self.nombre = nombre
        print(nombre)
    def encender(self):
        encendido = True
        print("Ha encendido", self.nombre)
    def apagar(self):
        encendido = False
        print("Ha apagdo",self.nombre)

#elec1 = Electro("Electro 1")
#print(elec1.encendido)
#elec1.encender()
#elec1.apagar()

class Lampara(Electro):
    tipoDeLuz = ""
    def __init__(self, nombre, potencia):
        super().__init__(nombre)
        self.potencia = potencia
        print(potencia)
luzCocina = Lampara("Luz cocina", 60)


