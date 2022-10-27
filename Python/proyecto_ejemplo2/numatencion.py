def run():
    print(""" Bienvenido a la configuracion de la maquina de atencion
    _________________________________________________________________""")

    seleccion_operativa = int(input("""
    Si desea configurar el sistema de atencion presione 1
    Si desea inciar el sistema de atencion presione 2
    """))

    if seleccion_operativa == 1:
        pass
    elif seleccion_operativa == 2:
        eleccion_atencion = int(input('''
        Bienvenidos a La Ferreteria
        Si usted necesita comprar presione 1.
        Si usted necesita consultar y solucionar dudas presione 2.
        Ingrese su opcion:
        '''))
        asignar_numvent = 0
        asignar_numcon = 0
        while True:
            if eleccion_atencion == 1:
                asignar_numvent += 1 
                print(asignar_numvent)
                eleccion_atencion = int(input('''
                Bienvenidos a La Ferreteria
                Si usted necesita comprar presione 1.
                Si usted necesita consultar y solucionar dudas presione 2.
                Ingrese su opcion:
                '''))
                
            elif eleccion_atencion == 2:
                asignar_numcon += 1 
                print(asignar_numcon)
                eleccion_atencion = int(input('''
                Bienvenidos a La Ferreteria
                Si usted necesita comprar presione 1.
                Si usted necesita consultar y solucionar dudas presione 2.
                Ingrese su opcion:
                '''))
                
            else:
                eleccion_atencion = int(input('''
                Elija una opcion correcta.
                Si usted necesita comprar presione 1.
                Si usted necesita consultar y solucionar dudas presione 2.
                Ingrese su opcion:
                '''))


