"""Un radar común de detección de velocidad de la policía de caminos emite un rayo de microondas a una frecuencia f0. El rayo es reflejado por un automóvil que se aproxima y el rayo reflejado es captado y analizado por la unidad de radar. La frecuencia del rayo reflejado es cambiada ligeramente de f0 a f1 debido al movimiento del automóvil.

La relación entre la velocidad del automóvil, v, en millas por hora, y las dos frecuencias de microondas es:

Donde las ondas emitidas tienen una frecuencia de:

f0 = 2 x10^10 sec ^–1

Usando la fórmula dada, escriba un programa para calcular y desplegar la velocidad correspondiente a una frecuencia recibida de 2.0000004 x 10^10 sec–1.

Ahora aplicamos el procedimiento de desarrollo de software a este problema."""


frecuencia0 = 2e-10 
frecuencia1 = 2.0000004e-10 
velocidad=6.685e8*(frecuencia1-frecuencia0)/(frecuencia1+frecuencia0)
print(f'{velocidad :.2f} ')
   