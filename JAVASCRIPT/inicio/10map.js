/*
Un Map es una colección que nos permite almacenar pares de clave-valor, introducida en el estándar ECMAScript 6.

A diferencia de los objetos (Object) (que también almacenan pares clave-valor) los Map ofrecen varias ventajas en términos de rendimiento y funcionalidad. Estas son.

Claves de cualquier tipo, las claves pueden ser de cualquier tipo (no solo strings o símbolos)
Orden, mantienen el orden de inserción.
Propiedad size, que indica cuántos pares clave-valor contiene.
Fácilmente iterable, podemos recorrer sus elementos fácilmente.
Mejor rendimiento, para operaciones de inserción y eliminación.
*/

//Para crear un Map, simplemente utilizamos el constructor de la clase:
const mapa = new Map();
//Aquí hemos creado un Map vacío, listo para almacenar pares clave-valor.
//También podemos inicializar un Map con una colección iterable de pares clave-valor:
const mapa2 = new Map([
  ['clave1', 'valor1'],
  ['clave2', 'valor2'],
  [3, 'valor3']
]);

// Añadir elementos al Map, Para añadir elementos a un Map, utilizamos el método .set(), la sintaxis es mapa.set(clave, valor)
mapa.set('clave3', 'valor3');
mapa.set(4, 'valor4');

// Acceder a elementos del Map, Para acceder a un elemento de un Map, utilizamos el método .get(), la sintaxis es mapa.get(clave)
console.log(mapa.get('clave3')); // 'valor3'
console.log(mapa.get(4)); // 'valor4'

// Verificar si un elemento existe en el Map, Para verificar si un elemento existe en un Map, utilizamos el método .has(), la sintaxis es mapa.has(clave)
console.log(mapa.has('clave3')); // true
console.log(mapa.has(5)); // false

// Para eliminar un elemento de un Map, utilizamos el método .delete(), la sintaxis es mapa.delete(clave)
mapa.delete('clave3');
console.log(mapa.has('clave3')); // false

//Si se desea eliminar todos los elementos de un Map, podemos utilizar el método .clear()
mapa.clear();
console.log(mapa.size); // 0

// Recorrer un Map, Para recorrer un Map, podemos utilizar el método .forEach(), la sintaxis es mapa.forEach((valor, clave) => { ... });
mapa2.forEach((valor, clave) => {
  console.log(`Clave: ${clave}, Valor: ${valor}`);
});

// También podemos utilizar un bucle for...of para recorrer un Map
for (const [clave, valor] of mapa2) {
  console.log(`Clave: ${clave}, Valor: ${valor}`);
}