// =======================================================
//      APUNTE DE MANEJO DE ELEMENTOS Y FORMULARIOS JS
// =======================================================

// -------------------------------------------------------
// 1️⃣ Seleccionar elementos del DOM
// -------------------------------------------------------

// Por ID (único)
const div = document.getElementById("miDiv");

// Por clase → devuelve HTMLCollection
const parrafos = document.getElementsByClassName("parrafo");

// Por etiqueta → devuelve HTMLCollection
const items = document.getElementsByTagName("li");

// Con selectores CSS
const primeraCaja = document.querySelector(".caja"); // 1ro que coincide
const todasCajas = document.querySelectorAll(".caja"); // NodeList de todos


// -------------------------------------------------------
// 2️⃣ Propiedades comunes de los elementos
// -------------------------------------------------------

// Contenido
console.log(div.innerHTML);    // HTML interno
console.log(div.outerHTML);    // HTML completo (incluye etiqueta)
console.log(div.textContent);  // Solo texto
console.log(div.innerText);    // Texto visible (respeta estilo)

// Atributos
console.log(div.id);           // "miDiv"
console.log(div.className);    // "caja destacado"
div.setAttribute("title", "info extra");
console.log(div.getAttribute("title")); // "info extra"

// Clases CSS
div.classList.add("nuevo");    // agrega clase
div.classList.remove("caja");  // quita clase
div.classList.toggle("activo");// alterna clase
console.log(div.classList.contains("destacado")); // true/false

// Estilos
div.style.color = "red";
div.style.backgroundColor = "yellow";
console.log(div.offsetWidth, div.offsetHeight);   // tamaño con borde
console.log(div.clientWidth, div.clientHeight);   // tamaño contenido

// Relaciones en el DOM
console.log(div.parentNode);       // padre
console.log(div.children);         // hijos
console.log(div.firstChild);       // primer hijo (puede ser texto)
console.log(div.nextSibling);      // siguiente nodo


// -------------------------------------------------------
// 3️⃣ Inputs básicos (text, password, number, etc.)
// -------------------------------------------------------
const input = document.getElementById("miInput");

// 🔹 Propiedades más comunes de inputs
console.log(input.value);      // valor actual del campo
input.value = "Nuevo valor";   // modificar valor
console.log(input.type);       // tipo de input (text, number, password…)
console.log(input.name);       // nombre del input
console.log(input.placeholder);// placeholder (texto de ayuda)
console.log(input.required);   // si es obligatorio
input.required = true;         // hacerlo obligatorio
console.log(input.disabled);   // true/false → deshabilitado
input.disabled = false;        // habilitar
console.log(input.readOnly);   // true/false → solo lectura
input.readOnly = true;         // volverlo de solo lectura
console.log(input.maxLength);  // máximo de caracteres permitidos
input.maxLength = 20;          // cambiar longitud máxima


// -------------------------------------------------------
// 4️⃣ Checkbox y Radio
// -------------------------------------------------------
const check = document.getElementById("miCheck");
console.log(check.checked);    // true/false → marcado?
check.checked = false;         // desmarcar
check.disabled = true;         // deshabilitar
console.log(check.name);       // nombre del campo
console.log(check.value);      // valor que enviará si está marcado

// Radio buttons → mismo "name" agrupa opciones
// form.genero.value devuelve la seleccionada


// -------------------------------------------------------
// 5️⃣ Select (listas desplegables)
// -------------------------------------------------------
// <select name="pais">
//   <option value="mx">México</option>
//   <option value="es">España</option>
// </select>
const select = document.forms["registro"].pais;

console.log(select.value);            // valor de la opción seleccionada
select.value = "es";                  // seleccionar por valor
console.log(select.selectedIndex);    // índice seleccionado
console.log(select.options.length);   // número de opciones
console.log(select.options[0].text);  // texto visible de la 1ª opción


// -------------------------------------------------------
// 6️⃣ Textarea
// -------------------------------------------------------
// <textarea name="comentarios" rows="4" cols="40"></textarea>
const textarea = document.forms["registro"].comentarios;

console.log(textarea.value);       // texto dentro
textarea.value = "Nuevo texto";    // cambiar texto
console.log(textarea.rows);        // número de filas visibles
console.log(textarea.cols);        // número de columnas visibles
console.log(textarea.maxLength);   // máximo de caracteres (si está definido)


// -------------------------------------------------------
// 7️⃣ Formularios con document.forms, devuelve un html collection
// -------------------------------------------------------

// Acceso a formularios
const form1 = document.forms[0];              // por índice
const formRegistro = document.forms["registro"]; // por name

// Acceso a campos
console.log(formRegistro.usuario.value);    // acceso directo
console.log(formRegistro.elements[1].name); // "correo"
console.log(formRegistro["usuario"]) 
// Evento submit con validación
formRegistro.addEventListener("submit", function(e) {
  e.preventDefault(); // evita recarga

  const usuario = formRegistro.usuario.value;
  const correo = formRegistro.correo.value;
  const edad = formRegistro.edad.value;

  console.log("Usuario:", usuario);
  console.log("Correo:", correo);
  console.log("Edad:", edad);

  // Validación rápida
  if (usuario.trim() === "") {
    alert("El usuario es obligatorio");
    return;
  }
  if (edad < 18) {
    alert("Debes ser mayor de edad");
    return;
  }
  if (!correo.includes("@")) {
    alert("Correo inválido");
    return;
  }

  alert("Formulario válido ✅");
});


// -------------------------------------------------------
// 8️⃣ Usando FormData (leer todo automáticamente) //Objeto que sirve para recoger y manipular los datos de un formulario de html
// -------------------------------------------------------
formRegistro.addEventListener("submit", function(e) {
  e.preventDefault();

  const datos = new FormData(formRegistro);

  // Recorrer todos los campos con sus valores
  for (let [campo, valor] of datos.entries()) {
    console.log(campo + ":", valor);
  }

  // Métodos útiles de FormData
  console.log(datos.has("usuario"));   // true/false → si existe
  datos.append("extra", "123");        // agregar un valor
  datos.delete("extra");               // eliminar un campo
});
