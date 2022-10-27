var edad = 18;

if (edad === 18) {
    console.log('Puede votar, tu primera votacion');
} else if (edad > 18) {
    console.log("Puedes votar de nuevo");
} else  {
    console.log("No puedes votar");
}


//operador de condicion ternario

//condicion ? true:false

var numero = 1

var resultado = numero === 1 ? "Si soy un uno" : "No soy un 1"

//switch

var num = 1

switch (num) {
    case 1:
        console.log("Soy un 1");
        break;
    case 2:
        console.log("Soy un 10");
        break;
    case 3:
        console.log("Soy un 10");
        break;
    default:
        console.log ("Lo siento, no soy lo que buscas");
}