// TAREA 
//  UNA SASTRERÍA TIENE UNA PROMOCIÓN, A TODOS LOS TRAJES QUE 
// CUESTEN MÁS DE QUE 800$ SE APLICARÁ UN DESCUENTO DE 15, 
// EN CASO DE SER MENOR QUE 800$ , SOLAMENTE TENDRÁ UN DESCUENTO DEL 8%.
// CREE EL CÓDIGO NECESARIO PARA PREGUNTAR AL CLIENTE CUÁNTO 
// ES EL PRECIO ORIGINAL DEL TRAJE QUE QUIEREN, SEGÚN ESO CALCULAR 
// EL PRECIO FINAL

let precioProducto = +prompt("Ingrese el precio del traje elegido $");
if(precioProducto > 800){
    let valorDescuento = precioProducto * 0.15;
    let precioFinal = precioProducto - valorDescuento;
    console.log(`    ------Boleta-------

    El precio del producto es $${precioProducto}.

    Tiene un descuento del 15% equivalente a $${valorDescuento}.

    El precio final es $${precioFinal}.

    ----------Gracias por su compra--------`)
}else if(precioProducto <= 800 && precioProducto > 0){
    let valorDescuento = precioProducto * 0.08;
    let precioFinal = precioProducto - valorDescuento;
    console.log(`    ------Boleta-------

    El precio del producto es $${precioProducto}.

    Tiene un descuento del 8% equivalente a $${valorDescuento}.

    El precio final es $${precioFinal}.

    ----------Gracias por su compra--------`)
}
else {
    console.log("Ingrese un precio valido")
}