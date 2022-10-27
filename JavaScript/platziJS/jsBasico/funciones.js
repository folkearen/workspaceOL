//Funciones Declarativas, se declara la varibale directamente

function miFuncion() {
    return 3;
}

function miFuncionParam(a,b) {
    return a * b
}

//Expresion, se crea una variable cuyo valor es una funcion
//Se conocen como variables anonimas ya que el nombre lo
//lleva la variab;e y no la funcion.
//Como toda funcion puede tener o no parametros
//Scope gobla; estan fuera de las funciones y puedo tener acceso
//a esas variables en todo el scope global y dentro de las funciones

var miFuncionEX = function() {
    return 5;
}

var miFuncionExParam = function(a,b) {
    return a + b;
}

//Para llamar una funcion declarativa o de expresion
// debo ocupar la nomenclatura nombreFuncion() o nombreVariable()

//El scope local, son las variables dentro de una funcion
// solo esta disponible dentro de la funcion en la que fue declarado

//Hoisting es cuando se hace un llamado a una variabnle 
//ha sido declarada pero no inicializada, e incluso el navegador
//la inicializa cuando la llamaa, al no estar inicializada
//se inicia la variable como undefine

//Por buenas paracticas las funciones se declaran al inicio del codigo

//Coersion  js es debilmente tipado, por ende, puede meaclar tipo de valores
//Coersion implicita, el lenguaje cambia de un tipo de valor a otro
//para encontrar consistencia y arrojar un resultado.
//Coersion explicita, nosotros obligamos a un valor a cambiar de tipo
var a = 4 + '7'; //El resultado sera '47' porque al tener un signo + 
//de concatenacion el lenguaje asume que el 4 debio ser una cadena
//entonces devuelve la cade '47'

var b = 4 * '7'; //En este caso la respuesta es 28, al ser un signo
//de multiplicacion, el lenguaje asume que deseamos hacer una 
//operacion matematica y convierte el '7' que es string en numero
//dando como resultado el entero 28

//Coersion explicita
var a = 20
var b = String(a)//Convierte el valor de a a un string
//en este caso de 20 a '20'.
c = Number(b)//Covertipos el valor de b en un numero
//'20' pasa a 20