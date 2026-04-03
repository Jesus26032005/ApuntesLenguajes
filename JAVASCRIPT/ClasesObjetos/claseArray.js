/************************************************************
 📚 APUNTE COMPLETO: Clase Array en JavaScript
************************************************************/

/*
  ▌1. INTRODUCCIÓN
  -----------------
  La clase `Array` es un objeto global usado para crear listas ordenadas de elementos.
  Un array puede contener cualquier tipo de dato: números, cadenas, booleanos,
  objetos, funciones, otros arrays (matrices) e incluso valores mixtos.
*/

/*
  ▌2. CREACIÓN DE ARRAYS
  ----------------------
*/

// Forma literal (recomendada)
let frutas = ["manzana", "pera", "uva"];

// Con el constructor (NO recomendado si se pasa un solo número)
let numeros = new Array(1, 2, 3); // [1, 2, 3]
let vacios = new Array(3); // [ <3 elementos vacíos> ]

// Desde otros iterables o array-like
let desdeCadena = Array.from("Hola"); // ['H','o','l','a']
let desdeSet = Array.from(new Set([1, 2, 3])); // [1,2,3]

/*
  ▌3. PROPIEDADES IMPORTANTES
  ----------------------------
*/
let ejemplo = [10, 20, 30];
console.log(ejemplo.length); // 3 (cantidad de elementos)
ejemplo.length = 5; // Añade espacios vacíos
console.log(ejemplo); // [10,20,30, <2 vacíos>]

/*
  ▌4. MÉTODOS ESTÁTICOS DE ARRAY
  ------------------------------
*/
Array.isArray([1,2,3]); // true
Array.of(1,2,3);        // [1,2,3]
Array.from("abc");      // ['a','b','c']

/*
  ▌5. MÉTODOS DE INSTANCIA (POR CATEGORÍA)
  ----------------------------------------
*/

/* A) Añadir / Eliminar elementos */
let arr = [1, 2, 3];
arr.push(4);         // Añade al final -> [1,2,3,4]
arr.pop();           // Elimina último -> [1,2,3]
arr.unshift(0);      // Añade al inicio -> [0,1,2,3]
arr.shift();         // Elimina primero -> [1,2,3]
arr.splice(1, 1);    // Desde índice 1, eliminar 1 elemento -> [1,3]
arr.splice(1, 0, 2); // Insertar en índice 1 -> [1,2,3]
arr.fill(0);         // Rellena todo con 0 -> [0,0,0]

/* B) Buscar elementos */
let nums = [10, 20, 30, 20];
nums.indexOf(20);        // 1 (primera coincidencia)
nums.lastIndexOf(20);    // 3 (última coincidencia)
nums.includes(30);       // true
nums.find(x => x > 15);  // 20 (primer valor > 15)
nums.findIndex(x => x > 15); // 1

/* C) Recorrer */
let frutas2 = ["manzana", "pera", "uva"];
frutas2.forEach((fruta, i) => console.log(i, fruta)); // Recorre sin devolver
for (let valor of frutas2) console.log(valor); // Itera valores

/* D) Transformar / Filtrar */
let dobles = [1,2,3].map(x => x * 2);     // [2,4,6]
let pares = [1,2,3,4].filter(x => x % 2 === 0); // [2,4]
let suma = [1,2,3].reduce((acc, val) => acc + val, 0); // 6
let sumaDerecha = [1,2,3].reduceRight((a,v) => a+v, 0); // 6

/* E) Ordenar y manipular */
let desorden = [3, 1, 4];
desorden.sort();          // [1,3,4] (ordena como string)
desorden.sort((a,b) => a-b); // [1,3,4] (numérico ascendente)
desorden.reverse();       // Invierte el orden

/* F) Combinar y cortar */
let a = [1,2];
let b = [3,4];
let combinado = a.concat(b); // [1,2,3,4]
let copia = combinado.slice(1,3); // [2,3] (sin modificar original)

/* G) Conversión a string */
let palabras = ["Hola", "Mundo"];
palabras.join(" "); // "Hola Mundo"
palabras.toString(); // "Hola,Mundo"

/* H) Vaciar array */
let temp = [1,2,3];
temp.length = 0; // []

/*
  ▌8. CONSIDERACIONES IMPORTANTES
  --------------------------------
  - Los arrays en JS son dinámicos: crecen y se reducen automáticamente.
  - Los índices son siempre numéricos y comienzan en 0.
  - Se pueden dejar "huecos" (elementos vacíos), pero suele ser mala práctica.
  - `.sort()` ordena como texto por defecto, para números se debe pasar una función de comparación.
  - Métodos mutables (modifican el array original): push, pop, shift, unshift, splice, reverse, sort, fill.
  - Métodos inmutables (devuelven nuevo array): map, filter, slice, concat, flat, flatMap.
*/
