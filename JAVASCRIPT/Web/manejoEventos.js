/* EVENTOS
En JavaScript un evento es simplemente un indicador de que algo ha ocurrido. Esto permite que nuestro código responda dinámicamente a diversas situaciones. Por ejemplo:
    Un usuario presiona una tecla.
    Un temporizador termina.
    Se recibe una señal desde una API.
Los eventos son un mecanismo sencillo para la programación asíncrona, ya que nos permite gestionar tareas de forma no bloqueante.

COMO FUNCIONAN
Al empezar con los eventos, una de las cosas que cuestan es entender los conceptos y términos (sin mezclarlos).
El evento en JavaScript es un suceso que ocurre en el navegador. Por ejemplo, puede estar causado por el usuario o por el sistema.
Para responder al evento, tenemos que asociar una función manejadores de eventos (event handlers), que se ejecutara cuando ocurra el evento.
Finalmente, el evento también incluye un objeto, que contiene información sobre el evento.
    En resumen:
    Evento: Un suceso que ocurre
    Manejador de eventos: Una función que se ejecuta cuando ocurre el evento
    Objeto de evento: Un objeto que contiene información sobre el evento
*/

/* FUNCIONES MANEJADORAS DE EVENTOS
La función manejadora de eventos (event handler) es simplemente una función que definimos que se ejecutará cuando ocurra el evento.
Para ello, antes tenemos que asociar una función con un emisor de eventos.
Para asociar la función al evento usamos los métodos siguientes:
    En el navegador addEventListener
    En Node.js on
La funcion addEventListener recibe 3 argumentos, el tipo de evento, la función manejadora y un objeto de opciones.
    */
// Vincular un manejador con `addEventListener`
miEmisor.addEventListener("miEvento", (evento) => {
  console.log("Manejando el evento:", evento);
});

/* LANZAR EVENTOS
Lanzar un evento, también conocido como emitir un evento, implica crear una instancia del evento y desencadenarlo en un objeto específico.
JavaScript proporciona varias formas de hacerlo. El método más común para lanzar eventos en JavaScript es
    En el navegador, dispatchEvent.
    En Node.js, emit.
*/
// Crear un evento estándar
let evento = new Event("miEvento");
// Disparar el evento
document.dispatchEvent(evento);
//Creamos un evento llamado miEvento.
//Utilizamos dispatchEvent para lanzarlo, activando así el manejador asociado.

/* CREAR EVENTOS PERSONALIZADOS
Los eventos personalizados son eventos que definimos nosotros mismos. Esto es útil cuando queremos transmitir información específica sobre una acción que ha ocurrido en nuestra aplicación. Además de manejar eventos predefinidos, podemos crear eventos personalizados. Esto es útil en proyectos complejos, porque podemos dar más información que con eventos genéricos.
Para crear un evento personalizado, utilizamos las clases Event y CustomEvent.
*/

/* EVENT
La clase Event se utiliza para crear eventos estándar en JavaScript. Estos eventos son simples y no llevan información adicional. Event es una clase muy sencilla, que nos deja añadir un mensaje (opcional) para identificar el evento. Su sintaxis sería new Event("nombreDelEvento").
*/

// 1. Crear el evento
let evento3 = new Event("miEventoPersonalizado", {
  bubbles: true,      // El evento burbujará en el DOM: Que un evento "burbujea" significa que, cuando ocurre en un elemento, el evento se propaga desde ese elemento hacia arriba por la jerarquía del DOM, pasando por sus padres y ancestros. Por ejemplo, si haces clic en un botón dentro de un div, el evento "click" primero se dispara en el botón, luego en el div que lo contiene, luego en el body, y así sucesivamente hasta el documento.
  cancelable: true    // El evento se puede cancelar con preventDefault()
});

// 2. Seleccionar el elemento donde se lanzará el evento
let elemento = document.getElementById("miDiv");

// 3. Escuchar el evento
elemento.addEventListener("miEventoPersonalizado", function(e) {
  console.log("Tipo:", e.type);      // "miEventoPersonalizado"
  console.log("Target:", e.target);  // El elemento donde se lanzó el evento (elemento)
  console.log("Bubbles:", e.bubbles); // true
  console.log("Cancelable:", e.cancelable); // true
});

// 4. Lanzar el evento
elemento.dispatchEvent(evento3);

// CUSTOM EVENT: CustomEvent extiende las capacidades del evento estándar, permitiendo pasar datos adicionales en el momento de emitir el evento.
// 1. Crear el evento personalizado con datos extra y opciones
let evento4 = new CustomEvent("miEventoPersonalizado", {
  detail: { //En CustomEvent, solo puedes enviar datos extra usando la propiedad detail, que puede contener cualquier tipo de dato (objeto, número, string, array, etc.).
    usuario: "Ana",
    edad: 25,
    activo: true,
    lista: [1, 2, 3],
    objeto: { clave: "valor" }
  },
  bubbles: true,      // El evento burbujará en el DOM
  cancelable: true    // El evento se puede cancelar con preventDefault()
  //Todos los datos extra van dentro de detail (puede ser cualquier estructura de datos). Las demás opciones (bubbles, cancelable, etc.) controlan el comportamiento del evento, no son datos personalizados.

});

// 2. Seleccionar el elemento donde se lanzará el evento
let elemento2 = document.getElementById("miDiv");

// 3. Escuchar el evento y acceder a los datos extra
elemento.addEventListener("miEventoPersonalizado", function(e) {
  console.log("Tipo:", e.type);         // "miEventoPersonalizado"
  console.log("Target:", e.target);     // El elemento donde se lanzó el evento
  console.log("Detail:", e.detail);     // Todos los datos extra enviados
  console.log("Bubbles:", e.bubbles);   // true
  console.log("Cancelable:", e.cancelable); // true
});

// 4. Lanzar el evento
elemento.dispatchEvent(evento4);


// INTEGRANDO CON PROMESAS: En ocasiones, puedes querer integrar el manejo de eventos con Promesas. Esto es útil para sincronizar tareas asíncronas.

function esperarEvento(evento) {
  // Devuelve una promesa que se resolverá cuando ocurra el evento
  return new Promise((resolve) => {
    // Registramos un listener para el evento
    // { once: true } significa que se ejecutará solo una vez
    // resolve es la función que resolverá la promesa
    document.addEventListener(evento, resolve, { once: true });
  });
}

async function main() {
  console.log("Esperando evento...");

  // Aquí main se pausa hasta que la promesa devuelta por esperarEvento se resuelva
  // Mientras tanto, el listener agregado en esperarEvento sigue activo, esperando el evento
  await esperarEvento("miEvento");

  // Cuando se dispara el evento, el listener llama a resolve(),
  // la promesa se resuelve, y main continúa su ejecución aquí
  console.log("Evento recibido.");
}

// Ejecutar la función principal
main();

// Simulamos el evento
// Esto dispara todos los listeners registrados para "miEvento",
// incluyendo el listener creado dentro de esperarEvento
document.dispatchEvent(new Event("miEvento"));


/*
Cómo funciona realmente:

Cuando llamas a:
await esperarEvento("miEvento")
esperarEvento se ejecuta completamente de inmediato.
Lo que hace es registrar un listener dentro de document.addEventListener.
Después de registrar el listener, esperarEvento devuelve una promesa pendiente.
La función esperarEvento NO se “pausa”; lo que se pausa es main() en el await.

main() se pausa en el await hasta que la promesa se resuelva. pues se queda pendiente.
En este momento, el “canal principal” de JavaScript no está bloqueado.
Otras cosas pueden seguir ejecutándose (por ejemplo, document.dispatchEvent(...)).

Cuando haces:
document.dispatchEvent(new Event("miEvento"));
El listener registrado detecta el evento.
Llama a resolve(), resolviendo la promesa.
Esto hace que await termine y main() continúe desde donde se pausó.
*/