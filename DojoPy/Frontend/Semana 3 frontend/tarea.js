//PEDIR AL USUARIO UN AÑO DE INICIO Y UN AÑO FINAL 
//ej(1490 y 1990) mostrar en la consola qué años entre 
//ese rango son bisiestos.



// let inicio = +prompt("Ingrese el año de inicio: ")

// let termino= +prompt("Ingrese el año de termino: ")

// let bisiesto = []

// for(i=inicio; i<=termino; i++){
//     if(i % 4 === 0 && i % 100 != 0 || i % 400 === 0){
//         bisiesto.push(i)
//     }
//  }
// console.log(bisiesto)

function calcularBisiesto(inicio, termino){
    let bisiesto = []
    for(i=inicio; i<=termino; i++){
        if(i % 4 === 0 && i % 100 != 0 || i % 400 === 0){
            bisiesto.push(i)
        }
     }
     return bisiesto
}

console.log(calcularBisiesto(+prompt("Ingrese el año de inicio: "),
+prompt("Ingrese el año de termino: ")))

