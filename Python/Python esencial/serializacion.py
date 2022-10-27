import pickle
class Juguete:
    nombre = ""
    precio = 0.0

    def __init__(self,nombre,precio) -> None:
        self.nombre = nombre
        self.precio = precio

    def getNombre(self):
        return self.nombre

    def getPrecio(self):
        return self.precio

j1 = Juguete("Max Steel",32.000)

f = open("classJuguete.bin", "wb")
#Creo un fichero con extension binaria, con los permisos escribir binario wb
pickle.dump(j1, f) 
#con el modulo piclle serializo la instancia j1 dentro del fichero.
f.close()

r = open("classJuguete.bin", "rb")
#Leo el archivo bin y lo guardo eb la variable r
juguete1 = pickle.load(r)
#cargo los datos vinarios con pickle en la variable juguete1, como j era
#instancia de juguete, juguete1 tambien lo sera
print(juguete1.getNombre())
#Compruebo al utilizar un metodo de la clase juguete en jueguete 1