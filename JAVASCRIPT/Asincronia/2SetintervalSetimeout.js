/* SET INTERVAL Y SET TIMEOUT
En JavaScript setInterval y setTimeout son una de las formas más sencillas para gestionar la temporización de tareas.
Estos dos métodos frecuentemente usados, y son una forma fácil de aproximarse a la programación asíncrona.
setTimeout se usa para retrasar la ejecución de una función una sola vez.
setInterval se utiliza para ejecutar código repetidamente a intervalos regulares
FUNCIONAMIENTO DE AMBOS
Tanto setTimeout como setInterval dependen del event loop de JavaScript, un mecanismo que permite manejar tareas asíncronas. Cuando usas una de estas funciones:
1.La tarea programada se registra en la cola de tareas.
2.Una vez transcurrido el tiempo especificado, el event loop coloca la función en la pila de ejecución.
3.La función se ejecuta cuando la pila de ejecución esté vacía.*/

/* SET TIMEOUT
setTimeout es una función que ejecuta una función o un bloque de código después de un tiempo específico. La sintaxis básica de setTimeout es:
let timeoutId = setTimeout(función, tiempo, [argumentos...]);
    función: La función que se ejecutará después de que transcurra el tiempo.
    tiempo: El tiempo en milisegundos antes de ejecutar la función.
    [argumentos…]: Opcionalmente, argumentos que se pasarán a la función.

setTimeout() no devuelve el resultado de tu callback, sino un ID numérico (o un objeto, según el entorno) que identifica ese temporizador.
Ese ID sirve para cancelar el temporizador usando clearTimeout().*/

//EJEMPLO BASICO
function saludar() {
  console.log('Hola, mundo');
}
setTimeout(saludar,2000) // Se ejecuta la funcion saludar después de 2 segundos

function suma(a,b) {
  console.log(a + b);
}

setTimeout(suma, 3000, 5, 10); // Ejecuta suma(5, 10) después de 3 segundos


// FUNCIONES ARROW, puede recibir funciones arrow siendo de la siguiente forma
setTimeout(() => { console.log('Hola, mundo con arrow function'); }, 2000);



//CANCELACION DE TIMEOUT
//Para cancelar una acción programada por setTimeout, utiliza clearTimeout, pasando el identificador devuelto por setTimeout.
function mostrarNotificacion() {
  console.log('¡Notificación importante!');
}
let timeoutId = setTimeout(mostrarNotificacion, 3000);
clearTimeout(timeoutId); // Cancela la notificación antes de que se muestre
//En este caso, la llamada a clearTimeout evita que mostrarNotificacion se ejecute después de 3 segundos.








/* SET INTERVAL
setInterval es una función que permite ejecutar una función o un bloque de código de manera repetitiva en intervalos regulares de tiempo. La sintaxis básica de setInterval es:
let intervaloId = setInterval(función, intervalo, [argumentos...]);
    función: La función que se ejecutará repetidamente.
    intervalo: El tiempo en milisegundos entre cada ejecución de la función.
    [argumentos…]: Opcionalmente, argumentos que se pasarán a la función.
setInterval() no devuelve el resultado de tu callback, sino un ID numérico (o un objeto, según el entorno) que identifica ese temporizador.
Ese ID sirve para cancelar el temporizador usando clearInterval().
*/
// EJEMPLO BASICO
function saludar() {
  console.log('Hola, mundo');
}
let intervaloId = setInterval(saludar, 1000); // Ejecuta `saludar` cada segundo

// CANCELACION DE SETINTERVAL
// Para detener la ejecución repetitiva iniciada por setInterval, utiliza clearInterval, pasando el identificador devuelto por setInterval.

function saludar() {
  console.log('Hola, mundo');
}
let intervaloIdXD = setInterval(saludar, 1000);
setTimeout(() => {
  clearInterval(intervaloIdXD); // Detiene la ejecución de `saludar` después de 5 segundos
}, 5000);


// COMO OBTENER EL RETORNO SI USO FUNCIONES CON RETORNO? Usar un callback
function pruebaConCallback(callback) {
  setTimeout(() => {
    callback("Hola");
  }, 1000);
}

pruebaConCallback((valor) => {
  console.log("Valor recibido:", valor); // ✅ "Hola"
});

//Usar async/await o promesas