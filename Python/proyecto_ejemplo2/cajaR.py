calcular = ""
terminar = "@"
productos = []
precios_un = []
precios = []
cantidades = []


def lector_producto_precio():
    print('                                           ')
    print('                Bienvenidos                ')
    print('                                           ')
    while True:
        producto = input("Ingrese producto: ")
        producto = producto.upper()
        productos.append(producto)

        cantidad = int(input("Ingrese cantidad de productos "))
        cantidades.append(cantidad)
        
        precio = int(input("Ingrese precio del producto: "))
        precios_un.append(precio)
        precio = precio * cantidad
        precios.append(precio)

        calcular = input("Presiona enter para agregar otro producto, sino presiosna T: ")
        calcular = calcular.upper()

        if calcular == "T":
            break


def total_sin_iva():
    return sum(precios)


def total_con_iva(sin_iva):
    return sin_iva*1.19


def calcular_iva(tsi, tci):
    return tci - tsi


def generar_boleta():
    print('                                           ')
    print("-----------------Boleta----------------")
    print('                                           ')
    for i,a,c,j in zip(productos, precios_un, cantidades, precios):
        print(i,"UN",a,"X", c, "$",j)

    print('                                           ')
    print("Total de su compra $",(total_sin_iva()), "pesos")
    print('                                           ')
    print("IVA $", round((calcular_iva(total_sin_iva(), total_con_iva(total_sin_iva())))), "pesos")
    print('                                           ')
    print("Total a pagar $", round(total_con_iva(total_sin_iva())), "pesos") 


def procesar_pago(total_a_pagar):
    print('                                           ')
    while True:
        pago = int(input('Ingrese el pago del del cliente $: '))
        if pago >= total_a_pagar :
            vuelto = pago - total_a_pagar
            print('                                           ')
            print('El vuelto es de $',round(vuelto), ' pesos')
            print('                                           ')
            terminar = input("Presiona cualquier tecla para terminar la venta: ")
            print('                                           ')

            if terminar == "":
                break

        elif pago < total_a_pagar and pago > 0 :
            print('                                           ')
            print('Ingrese la cantidad suficiente para completar el pago o ingrece 0 para anular la compra')
            print('                                           ')

        else:
            print('                                           ')
            break


def run():
    while True:
        lector_producto_precio()
        generar_boleta()
        procesar_pago(total_con_iva(total_sin_iva()))

if __name__ == "__main__":
    run()




