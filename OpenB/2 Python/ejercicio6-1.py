class Vehiculo:
    color = "por defecto"
    ruedas = 0
    puertas = 0

class Coche(Vehiculo):
    velocidad = 0
    ciilindrada = 0

automovil = Coche()
print(f"""
Color del automovil: {automovil.color} 
Número de ruedas: {automovil.ruedas} 
Número de puertas: {automovil.puertas}
Velocidad: {automovil.velocidad}
Cilindrada: {automovil.ciilindrada}
""")