//Qué es el BOM en JavaScript
//El BOM (Browser Object Model) es un conjunto de interfaces y objetos en JavaScript que permiten interactuar con el navegador y su entorno (como la ventana, la pantalla, la URL y el historial). A diferencia del Document Object Model (DOM), que manipula el contenido de la página web, el BOM está orientado a interactuar con el navegador y sus características.

/*
Los principales elementos que conforman el Browser Object Model (BOM) son:

Elemento del BOM	Descripción
window	Representa la ventana del navegador
navigator	Proporciona información sobre el navegador
screen	Representa la pantalla del usuario
location	Contiene información sobre la URL actual (permite cambiarla)
document	Representa el contenido de la página web
history	Permite manipular el historial de navegación del navegador,
console	Proporciona métodos para la depuración
performance	Proporciona acceso a la información de rendimiento de la página web
applicationCache	Permite acceder a la caché de la aplicación (en desuso)
*/


/* WINDOW
El objeto global window representa la ventana del navegador y es la raíz del BOM. A través de window se pueden acceder a muchas de las propiedades y métodos del BOM.

Comando	Descripción
window.innerHeight	Obtiene la altura de la ventana del navegador.
window.innerWidth	Obtiene el ancho de la ventana del navegador.
window.resizeTo(500, 500)	Cambia el tamaño de la ventana a 500x500 píxeles.
window.status = "Cargando..."	Modifica el texto de la barra de estado.
window.setDefaultStatus("Listo")	Establece el texto predeterminado de la barra de estado.
*/

console.log(window.innerHeight); // Altura de la ventana
console.log(window.innerWidth); // Ancho de la ventana

/* NAVIGATOR
El objeto navigator proporciona información sobre el navegador que está siendo utilizado. Entre otras cosas, se puede utilizar para detectar el nombre y la versión del navegador, así como la plataforma en la que se está ejecutando.
Comando	Descripción
navigator.userAgent	Devuelve el agente de usuario (user agent) del navegador. info del navegador
navigator.appVersion	Devuelve la versión del navegador.
navigator.platform	Devuelve el sistema operativo en el que se está ejecutando el navegador. la plataforma en que se ejecuta
navigator.language	Devuelve el idioma preferido del usuario.
navigator.geolocation	Proporciona acceso a la ubicación geográfica del usuario.
*/
console.log(navigator.userAgent); // Información sobre el navegador
console.log(navigator.platform); // Plataforma en la que se está ejecutando
console.log(navigator.language); // Idioma preferido del usuario
console.log(navigator.geolocation); // Información de geolocalización   

/* SCREEN
El objeto screen proporciona información sobre la pantalla del usuario, como su tamaño y resolución.
Comando	Descripción
screen.width	Devuelve el ancho de la pantalla en píxeles.
screen.height	Devuelve la altura de la pantalla en píxeles.
screen.availWidth	Devuelve el ancho disponible de la pantalla en píxeles (sin incluir la barra de tareas).
screen.availHeight	Devuelve la altura disponible de la pantalla en píxeles (sin incluir la barra de tareas).
screen.colorDepth	Devuelve la profundidad de color de la pantalla en bits.
screen.pixelDepth	Devuelve la profundidad de píxel de la pantalla en bits.
*/
console.log(screen.width); // Ancho de la pantalla
console.log(screen.height); // Altura de la pantalla
console.log(screen.availWidth); // Ancho disponible de la pantalla
console.log(screen.availHeight); // Altura disponible de la pantalla
console.log(screen.colorDepth); // Profundidad de color de la pantalla
console.log(screen.pixelDepth); // Profundidad de píxel de la pantalla

/* LOCATION
El objeto location contiene información sobre la URL actual y permite cambiarla para navegar a otras páginas.
Comando	Descripción
location.href	Devuelve la URL completa de la página actual. Sirve también para redirigir a otra URL.
location.protocol	Devuelve el protocolo de la URL (http:, https:, etc.).
location.host	Devuelve el host de la URL (incluye el puerto si está presente).
location.pathname	Devuelve la ruta de la URL.
location.search	Devuelve la cadena de consulta de la URL.
location.hash	Devuelve el fragmento de la URL (parte después del #).
*/

console.log(location.href); // URL actual
console.log(location.host); // Host de la URL actual
console.log(location.pathname); // Ruta de la URL actual
location.href = "https://www.ejemplo.com"; // Redireccionar a otra página

/* DOCUMENT
El objeto document representa el contenido de la página web y proporciona métodos y propiedades para manipularlo.El objeto document representa la página web cargada en la ventana del navegador y es la raíz del DOM.
Comando	Descripción
document.getElementById("miElemento")	Devuelve el elemento con el ID especificado.
document.getElementsByClassName("miClase")	Devuelve una colección de elementos con la clase especificada.
document.getElementsByTagName("miEtiqueta")	Devuelve una colección de elementos con la etiqueta especificada.
document.querySelector("miSelector")	Devuelve el primer elemento que coincide con el selector CSS especificado.
document.querySelectorAll("miSelector")	Devuelve una colección de elementos que coinciden con el selector CSS especificado.
document.createElement("miEtiqueta")	Crea un nuevo elemento con la etiqueta especificada.
document.body	Representa el elemento <body> de la página.
document.head	Representa el elemento <head> de la página.
document.title	Devuelve o establece el título de la página.
document.URL	Devuelve la URL de la página actual.
*/
 // Título de la página
console.log(document.title);

// Cuerpo de la página
console.log(document.body); 

// Elemento con el ID "miElemento"
console.log(document.getElementById("miElemento")); 


/* HISTORY
El objeto history permite acceder al historial de navegación del navegador.JavaScript permite modificar el historial del navegador utilizando el objeto history. Por ejemplo, podemos agregar una nueva entrada en el historial del navegador utilizando el método pushState().

Comando	Descripción 
history.back()	Navega a la página anterior en el historial.
history.forward()	Navega a la página siguiente en el historial.
history.go(n)	Navega a la página en la posición n del historial.
history.length	Devuelve el número de entradas en el historial.
history.pushState(...)	Agrega una nueva entrada al historial con una URL modificada.
history.replaceState(...)	Reemplaza la entrada actual del historial con una nueva URL.
*/

// agrega una nueva entrada en el historial del navegador 
// con una URL que contiene el parámetro `page` con el valor `1`.
history.pushState({page: 1}, "Title", "?page=1"); //Lo más común es usar URLs relativas para mantener compatibilidad con entornos locales y producción.

// reemplaza la entrada actual en el historial con una nueva entrada 
// con una URL que contiene el parámetro `page` con el valor `2`.
history.replaceState({page: 2}, "Title", "?page=2");

/* PERFORMANCE
El objeto performance proporciona métodos y propiedades para medir el rendimiento de la aplicación web. Como tiempos de carga y ejecución de scripts.
Comando	Descripción
performance.now()	Devuelve el tiempo actual en milisegundos con precisión de submilisegundos.
performance.mark("miMarca")	Establece una marca de tiempo en el rendimiento.
performance.measure("miMedida", "miMarca")	Establece una medida de rendimiento entre dos marcas.
performance.getEntries()	Devuelve una lista de todas las entradas de rendimiento.
performance.clearMarks()	Elimina todas las marcas de rendimiento.
performance.clearMeasures()	Elimina todas las medidas de rendimiento.
performance.timing	Proporciona un objeto con detalles sobre los tiempos de navegación y carga de la página.
performance.getEntries()	Devuelve todas las entradas de rendimiento disponibles.
*/
// Tiempo en milisegundos desde el inicio de la carga
console.log(performance.now()); 

/* APPLICATION CACHE
El objeto applicationCache proporciona métodos y propiedades para gestionar la caché de la aplicación web. lo que facilita el almacenamiento de recursos (como archivos CSS, imágenes y JavaScript) para su uso offline.
Comando	Descripción
applicationCache.addEventListener("updateready", ...)	Escucha el evento cuando hay una nueva versión de la caché disponible.
applicationCache.update()	Actualiza la caché de la aplicación.
applicationCache.swapCache()	Intercambia la caché activa con la nueva caché.
applicationCache.status	Devuelve el estado actual de la caché de la aplicación.
applicationCache.status	Devuelve el estado actual del caché de la aplicación.
*/