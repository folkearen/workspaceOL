var articulos = [
    {nombre: "Bicicleta", costo: 3000},
    {nombre: "Televisor", costo: 2500},
    {nombre: "Libro", costo: 320},
    {nombre: "Celular", costo: 10000},
    {nombre: "Laptop", costo: 20000},
    {nombre: "Teclado", costo: 500}, 
    {nombre: "Audifonos", costo: 1500},   
]

//Recorridos de array

//filter
var articulosFiltrados = articulos.filter(function(){
    return articulos.costo <= 500
});

//map
var nombreArticulos = articulos.map(function(articulo) {
    return articulo.nombre
});

//fine, si esta genera un nuevo array sino no devuelve nada
//buscar objeto dentro del array
var encuentraArticulo = articulos.find(function(articulo){
    return articulo.nombre === "Laptop"
});

//forEach, no genera nuevo array se llama directamente con el array
//existente

articulos.forEach(function(articulo) {
    console.log(articulo.nombre);
});

//Some, genera nuevo array , solo devuelve true o false si la condicion se cumple o no
//en este caso si hay productos con coste menor a 700
var articulosBaratos = articulos.some(function(articulo){
    return articulo.costo <= 700;
});
