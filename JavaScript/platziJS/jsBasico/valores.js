// null o undefine so valores vacios, en js true o false
// comienzan con minuscula a diferencia de python que empeiza con mayuscula
//Array entre corchetes, parecido a las listas de py
//Objeto entre llaves, parecido a los diccionarios de py
//typeof = type de paython
//Se pueden de clarar e inicializar variables por se parado, a diferencia de python


//variables
var nombre = "Alan";

//declarar
var edad;

//inicializar
edad = 30; 




//Array declaro e inicializo
var elementos = ["computadora", 'Celular'];

//Objeto declarado e inicializado
var persona = {
    nombre: 'Diego',
    edad: 30 
}


//Array

var frutas = ['Manzanas', 'Platanos', 'Cerezas', "Fresas"]

console.log(frutas.length); //para saber la cantidad de elemntos dentro del array
console.log(frutas[0]); //Acceso via index

frutas.push('Uvas');//Agrega un elemnto al final del array
frutas.pop(); //Elimina el ultimo elemnto del array
frutas.unshift('Duraznos')//Agrega un elemnto al inicio del array, idex 0
frutas.shift()//Elimina el primer elemnto del array

frutas.idexof(fresas)//Devuelve el index del elemnto indicado
