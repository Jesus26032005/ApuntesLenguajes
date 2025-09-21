// Funciones incorporadas

// Obtener largo cadena
let cadena = "hola mundo"
console.log(cadena.length);

// No se puede modificar una cadena en JavaScript, una cadena es inmutable
cadena[0] = "H";
console.log(cadena); //No cambia el indice

// Si se puede asignar una nueva cadena
cadena = "Hola mundo";
console.log(cadena); //Si cambia porq se crea una nueva cadena

// Recorrer una cadena
for (let i = 0; i < cadena.length; i++) {
    console.log(cadena[i]);
}

for (let letra of cadena) {
    console.log(letra);
}

// SUBCADENAS, son un conjunto de caracteres que se extraen de una cadena existente
let subcadena = cadena.substring(0, 4); // Extrae desde el índice 0 hasta el 4 (sin incluirlo) , se usa el metodo substring() de sintaxis cadena.substring(inicio, fin), el fin no se cuenta
console.log(subcadena); // "Hola"

// También se puede usar slice() que es más versátil
let subcadena2 = cadena.slice(0, 4);
console.log(subcadena2); // "Hola"

// CONCATENACION CADENAS
let cadena2 = " Adios";
let cadena3 = cadena + cadena2; // Se puede usar el operador + para concatenar cadenas
console.log(cadena3); // "Hola mundo Adios"

let cadena4 = cadena.concat(cadena2, " ", cadena3); // También se puede usar el método concat()
console.log(cadena4); // "Hola mundo Adios Hola mundo Adios"

// CONCATENACION CON TEMPLATE LITERALS
let cadena5 = `Saludos: ${cadena3}`;
console.log(cadena5); // "Saludos: Hola mundo Adios Hola mundo Adios"

// Convertir cadena a mayúsculas
console.log(cadena.toUpperCase()); // "HOLA MUNDO"

// Convertir cadena a minúsculas
console.log(cadena.toLowerCase()); // "hola mundo"

// Convertir cadena a numero, se puede usar parseFloat() o parseInt()
let numero = parseFloat(cadena); //Si es una cadena no numerica devuelve NaN
console.log(numero); // NaN

let numero2 = parseFloat("123.45");
console.log(numero2); // 123.45

let numero3 = parseInt("123");
console.log(numero3); // 123

// Convertir número a cadena, se usa toString()
let cadena6 = numero3.toString();
console.log(cadena6); // "123"

// Valor absoluto de un numero
let numeroabsoluto = Math.abs(-10); // Devuelve el valor absoluto de un número
console.log(numeroabsoluto); // 10

// Redondeo y truncado
let numeroRedondeo = Math.round(4.5); // Redondea al entero más cercano apartir de .5
console.log(numeroRedondeo); // 5

let numeroRedondeo1 = Math.floor(4.9); // Trunca hacia abajo independientemente de .9
console.log(numeroRedondeo1); // 4

let numeroRedondeo2 = Math.ceil(4.1); // Trunca hacia arriba independientemente de .1
console.log(numeroRedondeo2); // 5

let numeroTruncado = Math.trunc(4.9); // Trunca el decimal
console.log(numeroTruncado); // 4