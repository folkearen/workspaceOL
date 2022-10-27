def run():
    
    lista_enemigos = ['LUKE SKYWALKER', ]
    

    while True:
        
        opcion = input("""
        Bienvenidos al sistema de busqueda de enemigos del Imperio Galactico.
        Ingrese la opcion segun su interes:
        1 - Si desea ingresar el nombre de un enemigo del imperio.
        2 - Si desea buscar un enemigo del imperio.
        3 - Si desea visualizar toda la lista de enemigos.
        Presione cualquier otra tecla para salir del sistema
        ------------------------------------------------------------
        Ingrese opcion: """)

        if opcion == '1':
            otro_nombre = 'SI'
            while otro_nombre == 'SI':
                nn = input('Ingrese el nombre del enemigo a reportar: ')
                lista_enemigos.append(nn.upper())
                print("""Enemigo agregado a los registros del Imperio Galactico.
                Agradecemos su cooperacion, puede retirar sus Creditos Imperiales
                """)
                otro_nombre = input('Desea agragar otro nombre? indique SI/NO: ')
                otro_nombre = otro_nombre.upper()
      
        elif opcion == '2':
             nn = input('Ingrese nombre a buscar: ')
             nn = nn.upper()
             for nombre in lista_enemigos:
                if nombre != nn:
                    continue
                print(nombre, 'es un enemigo del imperio')

        elif opcion == '3':
            print(lista_enemigos)
          
        else:
            break
                   

if __name__ == '__main__':
    run()