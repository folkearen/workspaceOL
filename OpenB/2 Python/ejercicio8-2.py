"""
En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis 
una clase Vehículo, haréis un objeto de ella,
lo guardaréis en un archivo y luego lo cargamos.
"""
import pickle

class Vehiculo:
    marca = ""
    placa = ""

    def __init__(self, marca, placa) -> None:
        self.marca = marca
        self.placa = placa

v1 = Vehiculo("Toyota", "12ABCD")
print(v1.marca, v1.placa)

f = open("vehiculo.bin", "wb")
pickle.dump(v1, f)
f.close()

r = open("vehiculo.bin", "rb")
v2 = pickle.load(r)
r.close()

print(v2.marca, v2.placa)


