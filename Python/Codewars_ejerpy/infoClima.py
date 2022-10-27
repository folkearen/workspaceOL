"""
Convertidor de depuración de celsius
Tu amigo está viajando a los Estados Unidos, por lo que escribió un programa para convertir Fahrenheit a Celsius. Desafortunadamente, su código tiene algunos errores.

Encuentre los errores en el código para que el convertidor Celsius funcione correctamente.

Para convertir Fahrenheit a Celsius:

celsius = (fahrenheit - 32) * (5/9)

Recuerde que, por lo general, las temperaturas en las condiciones climáticas actuales se dan en números enteros. 
Es posible que los sensores de temperatura informen las temperaturas con una mayor precisión, como la décima más cercana. 
Sin embargo, el error del instrumento hace que este tipo de precisión no sea confiable para muchos tipos de sensores de medición de temperatura.
"""

def weather_info (temp):
    c = convert_to_celsius(temp)
    if (c < 0):
        return f"{c} is freezing temperature"
    else:
        return f"{c} is above freezing temperature"
    
def convert_to_celsius (temperature):
  celsius = (temperature - 32) * (5/9)
  return celsius

print(weather_info(50))