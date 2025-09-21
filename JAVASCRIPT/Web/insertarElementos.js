//Insertar y eliminar elementos en el DOM 
//Uno de los tarase que realizaremos con mayor frecuencia al manipular el DOM es insertar o eliminar nodos.

// CREAR E INSERTAR ELEMENTOS
/* createElement()
Para insertar nuevos elementos en el DOM, primero debes crear los nodos que deseas añadir. Esto se realiza utilizando el método document.createElement() sin añadirlo al DOM inmediatamente. 
*/
const nuevoElemento = document.createElement('div');
nuevoElemento.textContent = 'Este es un nuevo div';


// Para añadir los elementos se requiere un elemento HTMLElement que es creado por createElement().
/* appendChild()
Una vez creado el nuevo elemento, puedes insertarlo en el DOM usando el método appendChild(), que añade el elemento al final de la lista de hijos del nodo padre.
*/
const contenedor = document.getElementById('contenedor');
contenedor.appendChild(nuevoElemento);

/* insertBefore()
Si deseas insertar un nuevo nodo antes de un nodo existente en el DOM, puedes usar el método insertBefore(). Este método requiere dos parámetros: el nuevo nodo a insertar y el nodo de referencia antes del cual se insertará el nuevo nodo.
*/
const nuevoElemento = document.createElement('div');
nuevoElemento.textContent = 'Elemento insertado';
const contenedor2 = document.getElementById('contenedor2');
const referencia = document.getElementById('referencia');
contenedor2.insertBefore(nuevoElemento, referencia);

// REEMPLAZAR ELEMENTOS: También podemos reemplazar un nodo existente del DOM por otro, con el metodo replaceChild().
/* replaceChild()
La función replaceChild() permite reemplazar un elemento existente en el DOM con otro elemento creado con createElement().
Esta función toma dos argumentos: el elemento que se va a agregar y el elemento que se va a reemplazar.
*/

const oldElement = document.getElementById('old');
parentElement.replaceChild(newElement, oldElement);

// ELIMINAR ELEMENTOS
/* removeChild()
Para eliminar un nodo hijo, primero debes seleccionar el nodo a eliminar y su nodo padre. Luego, utiliza el método removeChild() del nodo padre.
*/
const contenedor3 = document.getElementById('contenedor3');
const hijo = document.getElementById('hijo');
contenedor3.removeChild(hijo);

// remove():Si solo necesitas eliminar el propio elemento sin necesidad de referenciar su padre, puedes usar el método remove() directamente en el nodo.
const elemento = document.getElementById('mi-elemento');
elemento.remove();

// Eliminar todo: Si necesitas eliminar todos los hijos de un nodo, puedes utilizar innerHTML para establecer el contenido del nodo a una cadena vacía.
const contenedor4 = document.getElementById('contenedor4');
contenedor4.innerHTML = '';

// Usar framgmentos de codigo: Cuando necesites añadir múltiples elementos al DOM, es más eficiente utilizar un DocumentFragment. Esto evita múltiples render y mejora el rendimiento.
const fragmento = document.createDocumentFragment();
for (let i = 0; i < 3; i++) {
    const nuevoElemento = document.createElement('div');
    nuevoElemento.textContent = `Elemento ${i + 1}`;
    fragmento.appendChild(nuevoElemento);
}
const contenedor5 = document.getElementById('contenedor5');
contenedor5.appendChild(fragmento);