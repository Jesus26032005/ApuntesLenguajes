// Los templates strings (o plantillas de cadena) en TypeScript son una forma conveniente de crear cadenas 
// de texto que pueden incluir expresiones embebidas.
const primerNombre: string = "Juan";
const apellido: string = "Pérez";

// COMO REALIZARLO
// Para crear una cadena utilizando template strings, se utilizan las comillas invertidas (` `) en lugar de las comillas
// simples (' ') o dobles (" ").
const nombreCompleto: string = `${primerNombre} ${apellido}`;
console.log(nombreCompleto);


// VENTAJAS 
// CARACTERES ESPECIALES
// Lo que evita esto es usar lo que son los caracteres de escape para ciertos caracteres especiales, 
// como las comillas simples o dobles.
const mensajeConCaracteresEspeciales: string = `Él dijo: "Hola, ¿cómo estás?" y luego agregó: '¡Bienvenido!'`;
console.log(mensajeConCaracteresEspeciales);

// REALIZAR MAS FACIL LA LECTURA DE CADENAS MULTILÍNEA
const mensajeMultilinea: string = `Este es un mensaje
que abarca varias líneas
y es más fácil de leer.`;
console.log(mensajeMultilinea);

// INSERTAR VARIABLES MAS FACILMENTE
const formaAntigua = "Hola, " + primerNombre + " " + apellido + "!";
const formaNueva = `Hola, ${primerNombre} ${apellido}!`;
console.log(formaAntigua);
console.log(formaNueva);

// EXPRESIONES EMBEBIDAS O FUNCIONES
const a: number = 5;
const b: number = 10;
console.log(`La suma de ${a} y ${b} es ${a + b}`); // Salida: La suma de 5 y 10 es 15