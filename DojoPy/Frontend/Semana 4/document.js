//dcocument es un objeto que me permite modificar el DOM
//El DOM es una serie de nodos (objetos) creados
//al momento de interpretar un html, cada nodo seria una etiqueta html
//getElementById sirve para traer el id del html a js

let titulo =document.getElementById('titulo')

//innertHTML, es una propiedad, contiene el htmal de un elemto
//Permite incertar codigo html o modificarlo

titulo.innerHTML = "<i> Nuevo titulo de mi app<i>"
titulo.style.color ="red"
titulo.style.backgroundColor = "cyan"
titulo.style.padding = "10px"


//.querySelectorAll para llamar al html por clases hacia mi js

let cajitas = document.querySelectorAll(".cajita")

cajitas.forEach((caja) => {
    caja.innerHTML = "Contenido cajitas"
    caja.style.width = "200px"
    caja.style.height = "200px"
    caja.style.backgroundColor = "red"
})