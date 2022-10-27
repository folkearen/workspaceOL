def convertir_cetigrado_kelvin():
    grad_cen = float(input(""" Usted ha escogido convertir de grados Centígrado a Kelvin.
    Ingrese la cantidad de grados Centigrados: 
    """))
    conversion = grad_cen + 273.15
    print(str(grad_cen) + " grados Centígrados equivalen a " + str(conversion), " grados Kelvin")

def convertir_kelvin_centígrados():
    grad_kel = float(input(""" Usted ha escogido convertir de grados Kelvin a Centígrados.
    Ingrese la cantidad de grados Kelvin: 
    """))
    conversion = grad_kel - 273.15
    print(str(grad_kel) + " grados Kelvin equivalen a " + str(conversion) + " grados Centígrados")

def run():
    respuesta = ""
    while respuesta != "NO":
        opcion = input("""
        Bienvenido al conversor de Temperatura °C|°K
        Si desea convertir de grados Centígrados a Kelvin presione 1
        Si desa convertir de grados Kelvin a Centígrados presione 2

        Escoja opción: 
        """)
        if opcion == "1": 
            convertir_cetigrado_kelvin()
            respuesta = input("¿Desea realizar otra consulta? si/no: ")
            respuesta = respuesta.upper()

        elif opcion == "2": 
            convertir_kelvin_centígrados()
            respuesta = input("¿Desea realizar otra consulta? si/no: ")
            respuesta = respuesta.upper()
        
        else:
            print("Ingrese una opociópn valida")

if  __name__ == "__main__":
    run()

        