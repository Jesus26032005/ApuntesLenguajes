// VARIABLES
// Para declarar una variable en TypeScript, usamos las palabras reservadas "let", seguido del tipo de dato y el 
// valor asignado.
let nombre: string = "Zaddkiel"
let edad: number = 20

// CONSTANTES
// Podemos declarar constantes usando la palabra reservada "const". Las constantes no pueden cambiar su valor y deben
// ser inicializadas al momento de su declaración, ademas de estar con mayusculas por convención.
const NUMERO = 10
// Cuando no especificamos el tipo de dato, TypeScript pone el tipo de dato como el valor asignado, facilita almacenqmiento, 
// sin embargo, es recomendable especificarlo para mayor claridad y evitar errores.

// Imprimimos en consola las variables y la constante
console.log("Mi nombre es " + nombre + " y tengo " + edad + " años.")
console.log("El valor de la constante NUMERO es: " + NUMERO)


// USO DE VAR
// También podemos usar "var" para declarar variables, pero su uso no es recomendado debido a su alcance global y
// posibles problemas de hoisting.
var ciudad: string = "Ciudad de México"
console.log("Vivo en " + ciudad)

// Tipos de datos
// En typescript existen los siguientes tipos de datos primitivos:
// string: para cadenas de texto
// number: para números (enteros y decimales)
// boolean: para valores verdaderos o falsos
// any: para cualquier tipo de dato (no recomendado su uso frecuente)
// void: para funciones que no retornan ningún valor
// null y undefined: para valores nulos o indefinidos
// unknown: para valores desconocidos (más seguro que any)
let valorNulo : null = null
console.log("El valor nulo es: " + valorNulo)

// Tipos de datos personalizados : Definidos por el usuario para satisfacer necesidades específicas.
// Literales: Permiten definir un conjunto específico de valores que una variable puede tomar, su sintaxis es <tipo_literal1> | <tipo_literal2> | ... ;
let estado: "activo" | "inactivo" | "pendiente";
estado = "activo"; // Correcto
// tuplas : Permiten definir un array con un número fijo de elementos y tipos específicos para cada posición, su sintaxis es let <nombre_variable>: [<tipo1>, <tipo2>, ...] = [<valor1>, <valor2>, ...];
let coordenadas: [number, number] = [10, 20];
console.log("Coordenadas: " + coordenadas[0] + ", " + coordenadas[1]);
// arrays: Permiten definir una colección de elementos del mismo tipo, su sintaxis es let <nombre_variable>: <tipo>[] = [<valor1>, <valor2>, ...];
let numeros: number[] = [1, 2, 3, 4, 5];
let nombres: string[] = ["Juan", "María", "Pedro"];
let generico: Array<any> = [1, "dos", true]; // Array de cualquier tipo
console.log("Números: " + numeros);
console.log("Nombres: " + nombres);
console.log("Generico: " + generico);

// Tipos compuestos
// Tipó unión: Permiten definir una variable que puede contener valores de diferentes tipos, su sintaxis es <tipo1> | <tipo2> | ... ;
let valor: string | number;
valor = "Hola";
// Tipo intersección: Permiten combinar múltiples tipos en uno solo, su sintaxis es <tipo1> & <tipo2> & ... ;
type A = { nombre: string };
type B = { edad: number };
type C = A & B;
let persona: C = { nombre: "Ana", edad: 30 };
console.log("Nombre: " + persona.nombre + ", Edad: " + persona.edad);
// Uso de alias: Un Alias de tipo en TypeScript nos permite crear un nombre alternativo para un tipo específico (ya sea estándard, o definido por nosotros). Los alias son una gran ayuda para mejorar la legibilidad del código. Son especialmente útiles cuando trabajamos con tipos complejos (como uniones, intersecciones y tipos personalizados). La sintaxis para definir un alias de tipo es: type <nombre_alias> = <tipo>;
type Punto = { x: number; y: number };
let origen: Punto = { x: 0, y: 0 };
console.log("Origen: (" + origen.x + ", " + origen.y + ")");
type resultado = "éxito" | "error" | "pendiente";
let estadoResultado: resultado = "éxito";
console.log("Estado del resultado: " + estadoResultado);