"""
Relaciones isA = herencia (Clase Perro es de Clase Animal)
Relaciones hasA = Composición (Clase a contiene b, clase a se compopne de b,c,d etc)
Ejemplo de composición
"""
class Ruedas:
    cantidad = 4
    
    def cambiarCantidad(self, cantidad):
        self.cantidad = cantidad

class Ventanas: 
    cantidad = 6
    def cambiarCantidad(self, cantidad):
        self.cantidad = cantidad

class Motor:
    tipoMotor ="Diesel"

class Carroceria:
    numeroVentanas = Ventanas()
    numeroRuedas = Ruedas()

class Coche:
    motor = Motor()
    carroceria = Carroceria()

lada = Coche()

print(lada.carroceria.numeroRuedas.cantidad)
#Instancio unobjeto coche y puedo acceder a las clases que los componen
#en este caso a la propiedad carroceria de la clase Coche, que es un objeto de la clase carroceria
#puedo ingresara a la propiedad numero de ruedas, que instancia de la clase Ruedas, de la Clase Carroceria,
#Al poder ingresar a la clase Ruedas mediantes su instancia, accedo a la porpiedad cantidad, que es porpiedad de la clase Rueda.

print(lada.carroceria.numeroVentanas.cantidad) #El mismo proceso

lada.carroceria.numeroVentanas.cambiarCantidad(3) #Puedo acceder tambien a los metodos de las clases
lada.carroceria.numeroRuedas.cambiarCantidad(3)

print(lada.carroceria.numeroRuedas.cantidad) #Despues de ejecturar los metodos han cambiado las cantidades
print(lada.carroceria.numeroVentanas.cantidad)