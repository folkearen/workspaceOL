var estudiantes = ['Maria', 'Sergio', 'Rosa', 'Daniel'];

function saludarEstudaintes(estudiante) {
    console.log(`Hola, ${estudiante}`);
}

//Ciclo for
//Se declara i con valor 0 y luego se le da una condicion de terminio, luego
//se aumenta su valor en 1, el valor que adquierta i sera el index para el arreglo
//dentro de la funcion 
for(var i = 0; i < estudiantes.length; i++){
    saludarEstudaintes(estudiantes[i]);
}

//Ciclo for of
//La variable reccore el arreglo y va asuemidno su contenid, como en PY
//podri ser var i sin problema
for(var estudiante of estudiantes){
    saludarEstudaintes(estudiante);
}

//Ciclo while
//la condicion es que la longitud de estudiantes sea mayor a cero.
//genero una variable que asumo el valor de arrglo.shift() o sea el valor
//del primer elemnto del arreglo, al ser metodo shift lo elimanra del asrreglo
//por tanto su longitud se disminuye en un elemnto, el ciclos e repite hasta
//haber eliminado todos los elemntos de la lista y su longitud sea cero

while(estudiantes.length > 0 ) {
    var estudiante = estudiantes.shift();
    saludarEstudaintes(estudiante)

}

//El primer tipo de for me ahorra condidionales

let menu = ["Completo", "Hamburgueza","Churrasco", "Papas fritas" ]

let eleccion = +prompt (`Indique la opcion deseada: 
                        0. Completo
                        1.Hamburgueza
                        2. Churrasco
                        3. Papas fritas`)

for(let i=0; i< createImageBitmap.length; i++){
    if(eleccion === i){
        console.log(`Usted a elegido ${carta[i]}`);
        break}
}// Se ahorra un if por cada opcion.
                        