/************************************************************
 📚 APUNTE DETALLADO: Set en JavaScript
************************************************************/

/*
  ▌1. DEFINICIÓN
  ----------------
  Un Set es una colección de **valores únicos**, es decir,
  no permite duplicados.  
  Es **iterable**, no tiene índices como los arrays, y
  conserva el **orden de inserción** de los elementos.
*/

/*
  ▌2. CREACIÓN DE SETS
  ---------------------
*/

// Crear un Set vacío
let numeros = new Set();

// Crear un Set con valores iniciales
let letras = new Set(["a", "b", "c", "a"]);
console.log(letras); // Set { 'a', 'b', 'c' }

// A partir de array
let array = [1, 2, 2, 3];
let setDesdeArray = new Set(array);
console.log(setDesdeArray); // Set {1,2,3}

/*
  ▌3. MÉTODOS PRINCIPALES
  -----------------------
*/

// add(valor) → Agrega un elemento al Set
numeros.add(1);
numeros.add(2).add(3); // encadenable
console.log(numeros); // Set {1,2,3}

// delete(valor) → Elimina un elemento y retorna true si existía
numeros.delete(2); 
console.log(numeros); // Set {1,3}

// has(valor) → Devuelve true si el valor existe
console.log(numeros.has(1)); // true
console.log(numeros.has(2)); // false

// clear() → Elimina todos los elementos
numeros.clear();
console.log(numeros); // Set {}

// size → Propiedad que devuelve la cantidad de elementos
let colores = new Set(["rojo","verde","azul"]);
console.log(colores.size); // 3

/*
  ▌4. RECORRIDO DE SETS
  ----------------------
*/

// 1. for...of
for (let color of colores) {
    console.log(color);
}

// 2. forEach
colores.forEach((valor, valor2, set) => {
    console.log(valor); // el segundo parámetro también es el valor
});

// 3. Convertir a array y recorrer
let arrColores = Array.from(colores);
arrColores.forEach(c => console.log(c));

/*
  ▌5. OPERACIONES ÚTILES CON SET
  --------------------------------
*/

// Unión de sets
let setA = new Set([1,2,3]);
let setB = new Set([3,4,5]);
let union = new Set([...setA, ...setB]); // {1,2,3,4,5}

// Intersección
let interseccion = new Set([...setA].filter(x => setB.has(x))); // {3}

// Diferencia
let diferencia = new Set([...setA].filter(x => !setB.has(x))); // {1,2}

/*
  ▌6. CONSIDERACIONES IMPORTANTES
  --------------------------------
  - Los valores de Set son **únicos** (no hay duplicados).
  - No tiene índices, no se puede acceder como array (numerando posiciones).
  - Es iterable: podemos usar for...of, forEach o spread operator.
  - Los objetos se comparan por **referencia**, no por contenido:
    let a = {}; let b = {};
    new Set([a,b,a]); // { {}, {} } → a y b son distintos objetos
  - Ideal para: eliminar duplicados, operaciones de conjunto, búsqueda rápida.
*/
