import random

def run():
    valor_pan_completoxgramo = 1.5 #pesos por gramo
    peso_en_gramos = random.randint(700, 1500 )#simulación de una pesa que va desde los 700 a 1500 gramos

    print('Bienvenido a la panaderia de la senora sofia')

    seleccion = input('Que desea llevar? ')

    if seleccion == "pan de completo" :
        cantidad = int(input('Indique cuantos '))
        peso_pan_completo = peso_en_gramos
        print('Su pan pesa ', peso_pan_completo,' gramos')
        coste = peso_pan_completo * valor_pan_completoxgramo
        print('El precio a pagar es ', coste, "pesos")

        acepta_pago = input('Acepta el pago, indique Si o No ' )
        acepta_pago =  acepta_pago.lower()
# 
        if acepta_pago == 'si':
            print('Gracias por su compra')
            print('Se han regalado 10 panes extras')
            pan_envalado = cantidad + 10
            print('Se han envalados ', pan_envalado, ' panes, puede retirar su compra')
            print('Hasta luego vuelva pronto')
        else:
            print('''Lo lamentamos, de igual forma somos los mas economicos del barrio.
             hasta luego, vuelva pronto''')
    else:
        print('No tenemos lo que necesita, vuelva pronto')

   
if __name__ == '__main__':
    run()