// let gradosCelcius = +prompt("Ingrese grados celcius: ");
// let gradosFarenheit = (gradosCelcius * 9/5) + 32;
// console.log(gradosFarenheit)

// // O directamente imprimir la formula
// let gradosCelcius = +prompt("Ingrese grados celcius: ");
// console.log((gradosCelcius * 9/5) + 32);

console.log("Bienvenidos al conversor de Temperatura  °C - °F");
option = prompt("Precione 1 si desea convertir de celcius a Farenheit o 2 para convertir de Farenheit a Celcius");

if(option == "1"){
    let gradosCelcius = +prompt("Ingrese grados celcius: ");
    console.log(`${gradosCelcius} grados Celcius son ${(gradosCelcius * 9/5) + 32} Grados Farenheit`);
}else if(option == "2"){
    let gradosFarenheit = +prompt("Ingrese grados Farenheit: ");
    console.log(`${gradosFarenheit}  grados Farenheit son ${(gradosFarenheit - 32) * 5/9} Grados Celcius`);
}else{
    console.log("Ingrese una opcion correcta");
}