// Ciclos
// Los ciclos permiten ejecutar un bloque de codigo varias veces mientras se cumpla una condicion

// Ciclo while, se ejecuta el bloque de codigo mientras la condicion sea verdadera, su sintaxis es while (condicion) { bloque }, aqui se evalua la condicion antes de ejecutar el bloque
let i = 0;
while (i < 5) {
    console.log(i);
    i++;
}

// Ciclo do-while, se ejecuta el bloque de codigo al menos una vez y luego se evalua la condicion, su sintaxis es do { bloque } while (condicion);
let j = 0;
do {
    console.log(j);
    j++;
} while (j < 5);

// Ciclo for, se utiliza para iterar sobre una secuencia (como un array) o un rango de numeros, su sintaxis es for (inicializacion; condicion; actualizacion) { bloque }
for (let k = 0; k < 5; k++) { // Sobre rango de numeros
    console.log(k);
}
// Ciclo for each: El bucle forEach es una estructura de control en JavaScript que facilita iterar sobre elementos de una colección o secuencia de datos (como arrays, o conjuntos). En JavaScript este bucle se realiza a través del método forEach(), que está disponible en las colecciones (en realidad, en los elementos iterables). El bucle forEach ofrece varias ventajas sobre otros bucles tradicionales. La sintaxis del bucle forEach es más clara y sencilla. Al no depender de índices, reduce la posibilidad de cometer errores al acceder a elementos de la colección. La sintaxis básica de un bucle forEach en JavaScript es la siguiente:

let coleccion = [1, 2, 3, 4, 5];

coleccion.forEach(function(elemento) {
    // Código a ejecutar para cada elemento de la colección
    //Colección: Es la colección de la que se van a iterar los elementos.
    //Elemento: Es el nombre de la variable que representa cada elemento en la iteración.
    //Instrucciones a ejecutar: Aquí se especifican las instrucciones que se ejecutan en cada iteración.
});

//otra forma de escribirlo es usando arrow functions
coleccion.forEach((elemento) => {
    //Una de las limitaciones del bucle forEach es que no permite modificar la colección que se está iterando directamente.
});

//Ciclo for in: El bucle for...in es utilizado para iterar sobre las propiedades enumerables de un objeto. La sintaxis es la siguiente
for (const key in object) {
    // Bloque de código
    //Donde key es el nombre de la propiedad actual en la iteración.
    //Y object[key] es el valor de esa propiedad.
    //for...in itera sobre las propiedades enumerables del objeto (incluyendo las propiedades heredadas de la cadena de prototipos).
    //Orden de iteración: El orden en que se iteran las propiedades no está garantizado.
}

// Ciclo for of: El bucle for...of es utilizado para iterar sobre los valores de objetos iterables (como arrays, strings, maps), sets y otros tipos de colecciones. La sintaxis es la siguiente
let iterable = [1, 2, 3, 4, 5];

for (const valor of iterable) {
    // Bloque de código
    //value: Una variable que representa el valor de cada elemento en el objeto iterable en cada iteración.
    //iterable: El objeto iterable cuyos valores serán iterados.
    //Iteración sobre valores: Itera sobre los valores de un objeto iterable
    //Orden de iteración: Itera en el orden natural de los elementos en el iterable.
    //No itinerable: no puede ser usado directamente con objetos que no son iterables, (como objetos literales normales)
}


//Usa for...in con objetos: Para objetos literales y cuando necesites iterar sobre las claves y sus valores. Usa for...of con arrays y otros iterables: Preferido para iterar sobre arrays, strings y otros objetos iterables