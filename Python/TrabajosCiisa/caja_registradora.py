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


def procesar_pago():
    print('                                           ')
    print("-----------------Boleta----------------")
    print('                                           ')
    for i,a,c,j in zip(productos, precios_un, cantidades, precios):
        print(i,"UN",a,"X", c, "$",j)

    print('                                           ')
    precio_total = sum(precios)
    print("Total de su compra $", precio_total, "pesos")
    total_iva = precio_total * 1.19

    iva = total_iva - precio_total
    print('                                           ')
    print("IVA $", round(iva), "pesos")
    print('                                           ')
    print("Total a pagar $", round(total_iva), "pesos") 

    print('                                           ')
    while True:
        pago = int(input('Ingrese el pago del del cliente $: '))
        if pago >= total_iva :
            vuelto = pago - total_iva
            print('                                           ')
            print('El vuelto es de $', vuelto, ' pesos')
            print('                                           ')
            terminar = input("Presiona cualquier tecla para terminar la venta: ")
            print('                                           ')

            if terminar == "":
                break

        elif pago < total_iva and pago > 0 :
            print('                                           ')
            print('Ingrese la cantidad suficiente para completar el pago o ingrece 0 para anular la compra')
            print('                                           ')

        else:
            print('                                           ')
            break
   

def run ():
    while True:
        lector_producto_precio()
        procesar_pago()
    


if __name__ == "__main__":
    run()
