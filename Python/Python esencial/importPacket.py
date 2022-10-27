from operacionesPacket import suma 
#Forma 1 de importar paquetes.
import operacionesPacket.resta
#Forma 2 de imporatar paquetes.

from importPacket import potencia, dividir
from operacionesPacket import multiplicacion as mul 
#puedo crear un acortador para llamar al modulo

print(suma.suma(2,2))
#Imprimo el retorno de la función suma del paquete operacionesPacket
#Que fue llamado de la foma uno, solo utilizo el nombredelmodulo.funcion
print(operacionesPacket.resta.resta(4,2))
#Imprimo el retorno de la funcion resta del paquete operacionesPacket
#Que fue llamado de la forma dos, se utiliza nombrepaquete.nombremodulo.nombrefuncion

print(mul.multiplicacion(3,3))
#Llamo al paquete, sus modulos y funciones mediante acortador.



"""Puedo importar subpaquetes, creado sub carpetas y llamandolas jerarquicamente
paquete.subpaque.modulo.funcion()
"""