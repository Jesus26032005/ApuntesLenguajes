/// Declaracion de variables
 
//Forma vieja var
var nombre = "Juan";
var edad = 30;

//Forma nueva (Recomendable)
let nombreNuevo = "Juan";
let edadNueva = 30;

console.log(nombreNuevo);
console.log(edadNueva);

/*
Ámbito (scope):

var tiene ámbito de función, es decir, su alcance es toda la función donde se declara.
let tiene ámbito de bloque, solo existe dentro del bloque {} donde se declara (por ejemplo, dentro de un if, for, etc.).
Hoisting:
Las variables declaradas con var se "elevan" al inicio de la función, pero su valor es undefined hasta que se asigna. Es decir que incluso se pueden utilizar antes de su declaración pero su valor sera undefined.
Las variables con let también se elevan, pero no pueden usarse antes de su declaración (causan error). Por lo que es recomendable para tener un codigo mas ordenado

Re-declaración:
var permite declarar la misma variable varias veces en el mismo ámbito.
let no permite re-declarar la misma variable en el mismo bloque.
Uso recomendado:

Se recomienda usar let (o const) en vez de var para evitar errores y tener un código más predecible.
*/

// Tipos de datos
//Number
let numero= 50;
let numeroDecimal= 50.5;
console.log(numero);
console.log(numeroDecimal);
//String
let texto = "hola mundo";
let textoComillaSimple = 'hola mundo';
console.log(texto);
console.log(textoComillaSimple);
//Boolean
let verdadero = true;
let falso = false;
console.log(verdadero);
console.log(falso);
//Null
let nulo = null;
console.log(nulo); 
// Undefined
let indefinido;
console.log(indefinido);

/// Funcion typeof: Regresa el tipo de dato de la variable
console.log(typeof texto);
console.log(typeof numero);
console.log(typeof verdadero);
console.log(typeof nulo);
console.log(typeof indefinido);

/// Constantes, para declarar una constante se utiliza la palabra reservada const y palabras clave en mayúsculas, una vez declarada no se puede cambiar su valor, ademas de q si tiene mas de dos palabras se recomienda usar guion bajo
const PI = 3.1416;
console.log(PI);