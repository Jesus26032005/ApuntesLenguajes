// ACCEDER Y MODIFICAR PROPIEDADES DEL DOM
// =======================================================
// Este apunte explica cómo acceder y modificar propiedades de elementos HTML usando JavaScript y el DOM.
// Igual que en accederDoom.js, se detallan los métodos y propiedades más comunes, con ejemplos y comentarios detallados.

/*
Cuando trabajamos con el DOM, además de seleccionar elementos, es fundamental saber cómo acceder y modificar sus propiedades, atributos, clases, estilos y valores.

JavaScript ofrece muchas propiedades y métodos para interactuar con los elementos seleccionados.
*/

// Supongamos que tenemos este HTML:
// <div id="miDiv" class="caja destacado">Hola <span>mundo</span></div>
// <input type="text" id="miInput" value="Texto">
// <input type="checkbox" id="miCheck" checked>

/*
1️⃣ CONTENIDO DEL ELEMENTO
-------------------------------------------------------
- innerHTML: Devuelve o modifica el HTML interno del elemento (incluye etiquetas).
- outerHTML: Devuelve el HTML completo del elemento, incluyendo la propia etiqueta.
- textContent: Devuelve solo el texto dentro del elemento, sin etiquetas.
- innerText: Devuelve el texto visible, respetando saltos de línea y estilos CSS.
*/
const div = document.getElementById("miDiv"); // Selecciona el div por su id
console.log(div.innerHTML);   // "Hola <span>mundo</span>"
console.log(div.outerHTML);   // "<div id=...>Hola <span>mundo</span></div>"
console.log(div.textContent); // "Hola mundo"
console.log(div.innerText);   // "Hola mundo"

/*
2️⃣ ATRIBUTOS
-------------------------------------------------------
- id, className: Acceso directo a atributos comunes.
- getAttribute(), setAttribute(), removeAttribute(): Métodos para leer, modificar y eliminar atributos personalizados o estándar.
*/
console.log(div.id);                // "miDiv"
console.log(div.className);         // "caja destacado"
console.log(div.id) //Acceso directo al atributo, tambien se puede modificarasi
console.log(div.getAttribute("id")); // "miDiv"
div.setAttribute("data-info", "123"); // Agrega atributo personalizado
div.removeAttribute("data-info");     // Elimina atributo personalizado

/*
3️⃣ CLASES CSS
-------------------------------------------------------
- classList: Permite manipular las clases CSS del elemento.
  Métodos: add(), remove(), toggle(), contains()
*/
console.log(div.classList);       // DOMTokenList ["caja", "destacado"]
div.classList.add("nuevo");       // Agrega clase
div.classList.remove("caja");     // Quita clase
div.classList.toggle("activo");   // Agrega o quita clase según exista
div.classList.contains("destacado"); // Verifica si tiene la clase

/*
4️⃣ ESTILOS CSS
-------------------------------------------------------
- style: Permite modificar estilos en línea del elemento.
- offsetWidth, offsetHeight: Tamaño visible incluyendo bordes.
- clientWidth, clientHeight: Tamaño del contenido sin bordes.
*/
div.style.color = "red";          // Cambia color del texto
div.style.backgroundColor = "yellow"; // Cambia fondo
div.style.border = "1px solid black"; // Ejemplo de agregar borde
console.log(div.offsetWidth);     // Ancho visible incluyendo borde
console.log(div.offsetHeight);    // Alto visible incluyendo borde
console.log(div.clientWidth);     // Ancho del contenido sin borde
console.log(div.clientHeight);    // Alto del contenido sin borde

/*
5️⃣ INPUTS Y FORMULARIOS
-------------------------------------------------------
- value: Valor de un input, textarea o select.
- checked, disabled: Estado de inputs tipo checkbox/radio.
*/
const input = document.getElementById("miInput"); // Selecciona el input por id
console.log(input.value);         // "Texto"
input.value = "Nuevo texto";      // Cambia el valor del input

const check = document.getElementById("miCheck"); // Selecciona el checkbox por id
console.log(check.checked);       // true (si está marcado)
check.checked = false;            // Desmarca el checkbox
console.log(check.disabled);      // false (si está habilitado)
check.disabled = true;            // Deshabilita el input

/*
6️⃣ RELACIONES Y POSICIÓN EN EL DOM
-------------------------------------------------------
- parentNode: Nodo padre del elemento.
- children: Colección de hijos (HTMLCollection).
- firstChild, lastChild: Primer y último hijo (puede ser texto o elemento).
- nextSibling, previousSibling: Hermanos adyacentes en el DOM.
*/
console.log(div.parentNode);      // Nodo padre
console.log(div.children);        // Hijos (HTMLCollection)
console.log(div.firstChild);      // Primer hijo
console.log(div.lastChild);       // Último hijo
console.log(div.nextSibling);     // Hermano siguiente
console.log(div.previousSibling); // Hermano anterior

/*
7️⃣ BÚSQUEDAS DENTRO DE UN ELEMENTO
-------------------------------------------------------
- querySelector(): Selecciona el primer elemento que coincide dentro del elemento.
- querySelectorAll(): Selecciona todos los elementos que coinciden dentro del elemento (NodeList).
*/
const span = div.querySelector("span");   // Primer <span> dentro del div
const todosSpans = div.querySelectorAll("span"); // Todos los <span> dentro del div
