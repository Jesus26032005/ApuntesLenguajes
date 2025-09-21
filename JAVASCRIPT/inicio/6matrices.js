// ==================================================
// APUNTE DETALLADO DE MATRICES EN JAVASCRIPT
// ==================================================

// Una "matriz" en JavaScript NO es un tipo especial de dato
// sino un **array de arrays**, lo que permite representar datos en 2D o más dimensiones.
// Ejemplo: tabla, tablero, grilla, etc.

// ----------------------------------
// DECLARACIÓN DE MATRICES
// ----------------------------------

// 1. Matriz 2x3 (2 filas, 3 columnas)
let matriz = [
    [1, 2, 3],   // Fila 0
    [4, 5, 6]    // Fila 1
];

// 2. Matriz vacía con asignación posterior
let matrizVacia = [];
matrizVacia[0] = [10, 20, 30];
matrizVacia[1] = [40, 50, 60];

// 3. Matriz 3D (array de arrays de arrays)
let matriz3D = [
    [
        [1, 2], 
        [3, 4]
    ],
    [
        [5, 6], 
        [7, 8]
    ]
];

// ----------------------------------
// ACCESO A ELEMENTOS
// ----------------------------------
// Sintaxis general: matriz[fila][columna]
console.log(matriz[0][0]); // 1 (fila 0, col 0)
console.log(matriz[1][2]); // 6 (fila 1, col 2)

// También podemos modificar por medio del indice:
matriz[0][1] = 99; // cambia el valor 2 → 99
console.log(matriz[0]); // [1, 99, 3]

// ----------------------------------
// RECORRIDO DE MATRICES
// ----------------------------------

// 1. Bucle for anidado
for (let i = 0; i < matriz.length; i++) {            // recorre filas
    for (let j = 0; j < matriz[i].length; j++) {     // recorre columnas
        console.log(`Fila ${i}, Col ${j} → ${matriz[i][j]}`);
    }
}

// 2. for...of anidado
for (let fila of matriz) {
    for (let valor of fila) {
        console.log(valor);
    }
}

// 3. forEach anidado
matriz.forEach((fila, i) => {
    fila.forEach((valor, j) => {
        console.log(`Posición [${i}][${j}] = ${valor}`);
    });
});

// ----------------------------------
// CREACIÓN DINÁMICA DE MATRICES
// ----------------------------------

// Crear matriz de 3x4 rellena de ceros
let filas = 3, columnas = 4;
let matrizCeros = Array.from({ length: filas }, () => Array(columnas).fill(0));
console.log(matrizCeros);

// Crear matriz con valores calculados (ej: producto i*j)
let matrizProducto = Array.from({ length: filas }, (_, i) =>
    Array.from({ length: columnas }, (_, j) => i * j)
);
console.log(matrizProducto);

// ----------------------------------
// OPERACIONES COMUNES
// ----------------------------------

// 1. Sumar todos los elementos
let suma = 0;
for (let fila of matriz) {
    for (let valor of fila) {
        suma += valor;
    }
}
console.log("Suma:", suma);

// 2. Buscar un valor
let valorBuscado = 99;
let encontrado = false;
for (let i = 0; i < matriz.length; i++) {
    for (let j = 0; j < matriz[i].length; j++) {
        if (matriz[i][j] === valorBuscado) {
            console.log(`Encontrado en [${i}][${j}]`);
            encontrado = true;
            break;
        }
    }
    if (encontrado) break;
}

// ----------------------------------
// MATRICES IRREGULARES (JAGGED ARRAYS)
// ----------------------------------
// No todas las filas tienen que tener la misma longitud
let matrizIrregular = [
    [1, 2, 3],
    [4, 5],
    [6]
];
console.log(matrizIrregular);
