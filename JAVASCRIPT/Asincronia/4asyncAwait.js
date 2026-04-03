// ASYNC Y AWAIT
/*En JavaScript, async y await son una sintaxis para escribir código asíncrono que es más sencillo más fácil de leer y mantener que las alternativas anteriores (como los callbacks y las promesas)
Introducido en ECMAScript 2017, async/await nos permite escribir código secuencialmente, en lugar de anidar callbacks o encadenar promesas.
Internamente, async/await se basa en promesas. De hecho then/catch y async/await son funcionalmente equivalentes.
Pero async/await proporciona una sintaxis más cómoda de usar, que anidar promesas (es syntacic sugar para simplificarnos la vida).
Otra ventaja de async/await es que maneja los errores de manera forma más sencilla. Con async/await, puede usar la estructura try/catch (que es más familiar y fácil de entender para los desarrolladores).*/

/*SINTAXYS DE ASYNC/AWAIT
La sintaxis async/await se basa en dos palabras clave,
    async se coloca antes de la función para indicar que contiene código asincrónico.
    await se coloca antes de cualquier operación que devuelva una promesa para indicar que el código debe esperar a que se resuelva la promesa antes de continuar.

*/

/* ASYNC 
La palabra clave async se usa para declarar una función asincrónica. Una función marcada con async siempre devuelve una promesa.
    Si la función retorna un valor, la promesa se resuelve con ese valor.
    Si la función lanza una excepción, la promesa se rechaza con esa excepción.
la Sintaxis es 
async function nombreFuncion() {
    // código asincrónico
    return valor; // valor si es resolve
}
ASYNC Devuelve una promesa que se resuelve con el valor retornado por la función o en caso de error se rechaza con el error lanzado por la función
Una función async no está obligada a devolver algo explícitamente. Si no devuelves nada, la función igualmente retorna una promesa que se resuelve con undefined.

*/

async function miFuncion() { return 'Hola, mundo' }
miFuncion().then(console.log); // 'Hola, mundo'

async function suma(a, b) {return a + b;} //Facilita el pasar argumentos
suma(5, 10).then(resultado => { console.log(resultado); }); // 15

/* AWAIT
La palabra clave await se utiliza dentro de una función async para esperar la resolución de una promesa.
await pausa la ejecución de la función async hasta que la promesa se resuelve o se rechaza.
la sintaxis es 

async function nombreFuncion() {
    const resultado = await promesa; // Espera a que la promesa se resuelva y devuelva el resultado
    return resultado;
}
await solo se puede usar dentro de funciones declaradas con async*/

async function miFuncion2() {
  let valor = await Promise.resolve('Hola, mundo');
  console.log(valor); // 'Hola, mundo'
}

miFuncion2();

/*Esto sería equivalente a un código, sin usar async y await
function obtenerDatos() {
  // Llamar a la función que devuelve una promesa
  FuncionQueDevuelvePromesa()
    .then((respuesta) => {
      // Manejar la respuesta cuando la promesa se resuelve
      console.log(respuesta);
    })
    .catch((error) => {
      // Manejar errores si la promesa se rechaza
      console.error(error);
    });
}
*/

/* ENTRE TRY CATCH ASYNC Y AWAIT Q PASA?
funcionalmente son equivalentes: ambas manejan promesas), sino en cómo se escriben y leen.

1️⃣ Con .then() / .catch()
promesaPersonalizada(5)
  .then(resultado => {
    console.log("Éxito:", resultado);
  })
  .catch(error => {
    console.error("Error:", error);
  });


Se basa en encadenamiento de callbacks.
Cada .then() recibe el valor resuelto de la promesa anterior.
.catch() captura errores de toda la cadena.
Problema: si tienes muchas promesas encadenadas, puede volverse difícil de leer (“callback hell moderno”).

2️⃣ Con async / await
async function ejecutar() {
  try {
    const resultado = await promesaPersonalizada(5);
    console.log("Éxito:", resultado);
  } catch (error) {
    console.error("Error:", error);
  }
}

ejecutar();


Se ve como código secuencial, aunque sigue siendo asíncrono.
await “pausa” la ejecución de la función hasta que la promesa se resuelva.
try...catch captura errores igual que en código síncrono.

🔑 Resumen rápido
Aspecto	.then() / .catch()	async / await
Legibilidad	Encadenado, puede complicarse	Secuencial, más claro
Manejo de errores	.catch()	try...catch
Necesita función	No	Sí, await solo funciona dentro de async
Funcionalidad	Esperar/promesa → obtener valor	Esperar/promesa → obtener valor
*/

/* NOTA EXTRA: async tambien nos permite “crear” promesas de forma más directa usando return y throw.
No necesitamos new Promise(...) salvo que queramos control total del flujo asíncrono (por ejemplo, con setTimeout o llamadas externas).
Es por eso que decimos que async hace que la promesa sea menos controlada manualmente, pero más fácil de escribir y leer.
Sin embargo si no se coloca return devuelve undefined en .resolve y si se pasa un error esto lo guarda en un objeto de tipo "error".
*/

