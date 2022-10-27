class animal:
    clasificacion = ""
    es_domestico = False

    def __init__(self, clasificacion, domestico):
        self.clasificacion = clasificacion
        self.es_domestico = domestico

class automovil:
    patente = ""
    marca = ""

    def __init__(self, patente, marca):
        self.patente = patente
        self.marca = marca

    def __str__(self):
        return f"La marca es {self.marca} y su placa es {self.patente}"
        #Sobre cargo el metodo string para poder imprimir un representacion legible,
        #del objeto para el usuario, y ya no arroja un direccion de memoria
        

perro = animal("mamifero", True)

print(type(perro))
print(perro) #arroja el tipo de objeto y su direccion en memoria

camioneta = automovil("12.ad", "Mazda")
print(type(camioneta))
print(camioneta) #Arrroja un cadena entendible ya que he sobrecargado el emtodo __str__


