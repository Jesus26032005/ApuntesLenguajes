// ACCEDER AL DOM
//Para acceder al DOM (Document Object Model) de HTML en JavaScript, usas objetos y métodos que te da el navegador a través del objeto global document.

/*
Cuando trabajamos con el DOM, lo que queremos es poder modificar los elementos del documento (su contenido, añadirlos, eliminarlos).

Por tanto, lo primero que tenemos que hacer es aprender a seleccionar los elementos que queremos.

JavaScript ofrece varios métodos para seleccionar elementos en el DOM. Estos métodos se pueden clasificar en dos categorías principales:
    Métodos basados en identificadores, clases y etiquetas
    Métodos basados en selectores CSS.
*/

/*  RESULTADOS DE SELECCION
Los métodos de selección van a devolverte un resultado, con la selección (obvio). En función del método que uses, el resultado puede ser,

Tipo	Selecciona	Cantidad devuelta	Estático o no
HTMLElement	Elemento	1️⃣ (o null)	(no aplica): Es un único nodo, por ejemplo, un solo <div>.
HTMLCollection	Elemento	♾️ (mismo tipo)	Dinámico: Es devuelto por métodos como getElementsByTagName() y getElementsByClassName(). Es dinámico, lo que significa que si agregas o eliminas elementos en el DOM, el HTMLCollection reflejará esos cambios automáticamente.
NodeList	Nodo	♾️ (pueden ser distintos tipos)	Estático: Puede ser devuelto por varios métodos, como querySelectorAll(). Es estático, lo que significa que no se actualiza si el DOM cambia después de la selección.
*/

/* METODOS BASADOS EN IDENTIFICADORES, CLASES Y ETIQUETAS
Estos métodos son los primeros que existieron. Nos permiten seleccionar un único elemento o un conjunto de elementos basados en sus identificadores, clases o etiquetas elementos.
    - getElementById(id): Selecciona un único elemento por su ID.
    - getElementsByClassName(clase): Selecciona todos los elementos que tienen la clase especificada.
    - getElementsByTagName(etiqueta): Selecciona todos los elementos con la etiqueta especificada.
*/

// METODO getElementById: El método getElementById() se utiliza para seleccionar un único elemento basado en su atributo id. Dado que id debe ser único dentro de un documento HTML, este método siempre devolverá un único elemento. Devuelve un elemento HTMLELEMENT permitiendo su manipulación, si no se encuentra ninguno, devuelve null.

let elemento = document.getElementById("titulo");
console.log(elemento)

// METODO getElementsByClassName: El método getElementsByClassName() se utiliza para seleccionar todos los elementos que tienen la clase especificada. Este método devuelve un HTMLCollection, que es una colección dinámica de elementos. La coleccion esta hecha de HTMLElements. Para iterar sobre la colección, puedes usar un bucle for.
let elementos = document.getElementsByClassName("parrafo");
console.log(elementos)

// METODO getElementsByTagName: El método getElementsByTagName() se utiliza para seleccionar todos los elementos con la etiqueta especificada. Este método también devuelve un HTMLCollection. Igual que getElementsByClassName() devuelve una lista de HTMLElements. Para iterar sobre la coleccion se puede usar un bucle for
let etiquetasP = document.getElementsByTagName("p");
console.log(etiquetasP)

/* METODOS BASADOS EN SELECTORES CSS
Los métodos basados en selectores CSS son más nuevos (se añadieron con HTML5). Ofrecen una forma más flexible de seleccionar elementos, ya que permiten usar uso de la enorme variedad de selectores disponibles.
    - querySelector(selector): Selecciona el primer elemento que coincide con el selector CSS especificado.
    - querySelectorAll(selector): Selecciona todos los elementos que coinciden con el selector CSS especificado y devuelve un NodeList.
*/

// METODO querySelector:El método querySelector() devuelve el primer elemento que coincide con el selector CSS especificado. Este método es útil cuando se necesita seleccionar un único elemento que coincide con un selector. Devuelve un único elemento o null si no se encuentra ninguno.
let elementoEstilo = document.querySelector("#titulo");
console.log(elementoEstilo);
// METODO querySelectorAll: El método querySelectorAll() devuelve una NodeList de todos los elementos que coinciden con el selector CSS. A diferencia de querySelector(), este método devuelve todos los elementos que coinciden, no solo el primero.
let elementosEstilo = document.querySelectorAll(".parrafo");
console.log(elementosEstilo);

