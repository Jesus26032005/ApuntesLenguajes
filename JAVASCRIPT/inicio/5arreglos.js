// Arreglos
// Estructura de datos que permite almacenar una coleccion de elementos en una sola variable en lugar de declarar variables individuales para cada elemento

// Declaracion de un arreglo let arreglo[]
let arreglo = [];
// Declaracion de un arreglo con elementos
let numeros = [1, 2, 3, 4, 5];

// Inicializacion de arreglo vacio
arreglo = [1, 2, 3, 4];

// Acceso a elementos del arreglo, se empieza desde el indice 0
console.log(arreglo[0]); // 1
console.log(arreglo[1]); // 2

// ==================================================
// APUNTE DETALLADO DE ARREGLOS EN JAVASCRIPT
// ==================================================

// Un array es un objeto especial para almacenar múltiples valores indexados.
// Los índices comienzan desde 0 y pueden ser enteros no negativos.
// Puede almacenar cualquier tipo de dato: números, strings, objetos, funciones, arrays, etc.

// -------------------------
// DECLARACIÓN DE ARREGLOS
// -------------------------

// Array vacío
let arrVacio = [];

// Array con valores iniciales
let arrNums = [1, 2, 3, 4];

// Constructor Array (menos común, puede tener comportamientos raros)
let arrContructor = new Array(5); // Crea array con 5 espacios vacíos (length=5)

// ----------------------------------
// MÉTODOS DE MODIFICACIÓN (MUTAN)
// ----------------------------------

// 1. push()
// Agrega uno o más elementos al final del array
// Sintaxis: array.push(elemento1, elemento2, ...)
// Parámetros:
//  - elementoN (Any): valores a agregar (pueden ser de cualquier tipo)
// Retorno: (Number) nueva longitud del array
// Modifica el array original: Sí
let arr = [1, 2];
arr.push(3);          // -> arr = [1, 2, 3]
arr.push(4, 5);       // -> arr = [1, 2, 3, 4, 5]

// 2. pop()
// Elimina y retorna el último elemento
// Sintaxis: array.pop()
// Parámetros: ninguno
// Retorno: (Any) elemento eliminado o undefined si está vacío
// Modifica el array original: Sí
arr.pop();            // -> elimina 5, arr = [1, 2, 3, 4]

// 3. unshift()
// Agrega uno o más elementos al inicio
// Sintaxis: array.unshift(elemento1, elemento2, ...)
// Retorno: (Number) nueva longitud
// Modifica el array original: Sí
arr.unshift(0);       // -> arr = [0, 1, 2, 3, 4]

// 4. shift()
// Elimina y retorna el primer elemento
// Sintaxis: array.shift()
// Retorno: (Any) elemento eliminado o undefined si está vacío
// Modifica el array original: Sí
arr.shift();          // -> elimina 0, arr = [1, 2, 3, 4]

// 5. splice()
// Inserta, elimina o reemplaza elementos en cualquier posición
// Sintaxis: array.splice(inicio, cantidadEliminar, item1, item2, ...)
// Parámetros:
//   - inicio (Number): índice desde donde se aplicará
//   - cantidadEliminar (Number): cuántos eliminar desde 'inicio'
//   - itemN (Any): elementos a insertar (opcional)
// Retorno: (Array) con los elementos eliminados
// Modifica el array original: Sí
arr.splice(1, 2, 99, 100); // desde índice 1, elimina 2 → arr = [1, 99, 100, 4]

// ------------------------------
// MÉTODOS QUE NO MUTAN (COPIAS)
// ------------------------------

// 6. concat()
// Une arrays y/o valores en uno nuevo
// Sintaxis: array.concat(valor1, valor2, ...)
// Retorno: (Array) nuevo array combinado
// Modifica el array original: No
let arr2 = [5, 6];
let arrConcat = arr.concat(arr2, 7, [8, 9]); // [1, 99, 100, 4, 5, 6, 7, 8, 9]

// 7. slice()
// Crea una copia de una sección del array
// Sintaxis: array.slice(inicio, fin)
// Parámetros:
//   - inicio (Number): índice de inicio (incluido), si es negativo cuenta desde el final
//   - fin (Number): índice de fin (excluido), si es negativo cuenta desde el final
// Retorno: (Array) nuevo array con los elementos extraídos
// Modifica el array original: No
let arrSlice = arrConcat.slice(1, 4); // [99, 100, 4]

// ----------------------------------
// MÉTODOS DE ITERACIÓN / TRANSFORMACIÓN
// ----------------------------------

// 8. map()
// Aplica una función a cada elemento y retorna nuevo array con resultados
// Sintaxis: array.map(callback(elemento, indice, array), thisArg)
// Parámetros:
//   - callback: función a ejecutar
//   - thisArg: valor para 'this' en callback (opcional)
// Retorno: (Array) nuevo con resultados
// Modifica el array original: No
let arrMap = arrConcat.map(x => x * 2); // cada elemento *2

// 9. filter()
// Filtra elementos que cumplan condición
// Sintaxis: array.filter(callback, thisArg)
// Retorno: (Array) nuevo con los elementos que pasen el filtro
let arrFilter = arrConcat.filter(x => x > 5);

// ----------------------------------
// MÉTODOS DE BÚSQUEDA
// ----------------------------------

// 10. includes()
// Verifica si un valor existe
// Sintaxis: array.includes(valor, desdeIndice)
// Retorno: (Boolean)
arrConcat.includes(5); // true

// 11. indexOf()
// Retorna el índice de la primera coincidencia o -1 si no existe
// Sintaxis: array.indexOf(valor, desdeIndice)
// Retorno: (Number)
arrConcat.indexOf(100); // 2

// 12. lastIndexOf()
// Igual que indexOf pero desde el final hacia atrás
arrConcat.lastIndexOf(5); // índice de la última vez que aparece

// 13. find()
// Retorna el primer elemento que cumpla condición o undefined
// Sintaxis: array.find(callback, thisArg)
let encontrado = arrConcat.find(x => x > 6); // 7

// ----------------------------------
// ORDEN Y REORGANIZACIÓN
// ----------------------------------

// 14. sort()
// Ordena los elementos (mutando el array)
// Sintaxis: array.sort(funcionComparacion)
// Sin comparación: ordena como strings (peligroso en números)
arrConcat.sort((a, b) => a - b); // orden numérico ascendente

// 15. reverse()
// Invierte el orden de los elementos
// Modifica el array original: Sí
arrConcat.reverse();

// ----------------------------------
// CONVERSIÓN A CADENA
// ----------------------------------

// 16. join()
// Une todos los elementos en un string
// Sintaxis: array.join(separador)
// Retorno: (String)
arrConcat.join(", "); // "10, 9, 8, ..."

// 17. toString()
// Convierte array a string separado por comas
arrConcat.toString(); // igual que join() sin separador

// ----------------------------------
// FORMAS DE ITERAR
// ----------------------------------

// 18. for clásico
for (let i = 0; i < arrConcat.length; i++) {
    console.log(arrConcat[i]);
}

// 19. for...of → valores
for (let valor of arrConcat) {
    console.log(valor);
}

// 20. forEach()
// Ejecuta callback por cada elemento
// Sintaxis: array.forEach(callback(elemento, indice, array), thisArg)
// Retorno: undefined
// Modifica array original: No (a menos que modifiques manualmente sus elementos)
arrConcat.forEach((valor, i) => {
    console.log(`Índice ${i} → ${valor}`);
});

// DESTRUCTURACION DE ARRAY
// La desestructuración de arrays es una forma de desempaquetar valores de arrays y asignarlos a variables de manera directa. Por ejemplo, en lugar de extraer valores de un array usando índices, podemos hacerlo de forma directa con la desestructuraciónS. 
// La desestructuración de arrays utiliza corchetes ([]) para asignar valores a variables individuales. El orden de las variables coincide con el orden de los valores en el array. La sintaxis seria
let arregloxd = [1 , 2 ,3]
let [a, b, c] = arregloxd;
console.log(a, b, c);

//Puedes ignorar ciertos valores utilizando comas.
const numerosxd = [10, 20, 30];
const [, segundo] = numerosxd; // Ignora el primer valor

console.log(segundo); // 20

//Valores por defecto: Si el array no tiene suficientes valores, puedes asignar valores predeterminados.
const numerosxdd = [10];
const [d, e = 20] = numerosxdd;

console.log(d); // 10
console.log(e); // 20

// Uso con rest parameter
// Puedes capturar el resto de los valores en un array utilizando ...rest. Recuerda que el operador ... debe ir al final para capturar el resto de los valores.
const numerosxddd = [1, 2, 3, 4, 5];
const [f, g, ...rest] = numerosxddd;

console.log(f); // 1
console.log(g); // 2
console.log(rest); // [3, 4, 5] 