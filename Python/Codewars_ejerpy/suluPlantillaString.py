"""
¡Oh, no! Timmy no siguió las instrucciones con mucho cuidado y olvidó cómo usar la nueva función Plantilla de cadena. 
¡Ayuda a Timmy con su plantilla de cadena para que funcione como él espera!
"""

def pasatiempos(*pas): #Puedo colocar el signo multiplicador para ingresar n argumentos
    return "Mis pasatiempos son {}".format(", ".join(pas)) #Tambien me permite considerar multiples argumentos, en funciones que solo reciben uno.

print(pasatiempos("Escribir", "Leer"))