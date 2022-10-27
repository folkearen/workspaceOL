//Objeto en JS -- POO -- sintaxis diccionario PY
// objeto = {}; sintaxis

var miAuto = {
    marca: 'toyota',
    modelo: 'Corola',
    annio: 2020,
    detalleDelAuto: function() {
        console.log(`Auto ${this.modelo} ${this.annio}`)
    }
}; 

//Se llamar con el nombre de la variable / mi Auto
//Para llamar a los valores / miAuto.marca la variable mas la llave

//Los valores dentro del objeto se llaman propiedades
//Una propiedad puede ser una funcion y esa funcion puede interactuar con las
//otras propiedades del mismo objeto.

//Una propiedad con una funcion como valor se llama "metodo"
//Para llamar al metodo dentro del objeto    miAuto.detalleDelAuto()
//this. hace referencia al objeto padre a la cual pertenece this == miAuto
//es la forma de acceder a los objetos, en este contexto a su propio objeto.


//Funcion constructura, plantilla de un  objeto --POO

function auto(marca, modelo, annio) {
    this.marca = marca;
    this.modelo = modelo;
    this.annio = annio;
}
//Obejto nuevo
var autoNuevo = new auto('Tesla', 'Model 3', 2020);
var autoNuevo2 = new auto('Toyota', 'Yaris', 2018);
var autoNuevo3 = new auto('Chevrolette', 'Cavallier', 1998)
console.log(autoNuevo)
console.log(autoNuevo2)
console.log(autoNuevo3)