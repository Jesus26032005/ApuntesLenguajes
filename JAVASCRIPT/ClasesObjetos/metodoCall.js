// ---------------------------
// MÉTODO CALL EN JAVASCRIPT
// ---------------------------

// 1️⃣ Qué es:
// `call` permite invocar una función especificando el valor de `this`
// y pasar argumentos de forma individual.

// Sintaxis:
// funcion.call(thisArg, arg1, arg2, ...)

// --------------------------------------------------
// 2️⃣ Ejemplo básico de uso
const persona1 = {
    nombre: "Ana",
    saludar: function(saludo) {
        console.log(`${saludo}, soy ${this.nombre}`);
    }
};

const persona2 = { nombre: "Juan" };

// Usamos call para que el método "saludar" use persona2 como "this"
persona1.saludar.call(persona2, "Hola"); // "Hola, soy Juan"

// --------------------------------------------------
// 3️⃣ Comparación con apply
// call → argumentos individuales
// apply → argumentos en un array
persona1.saludar.apply(persona2, ["Hola"]); // "Hola, soy Juan"

// --------------------------------------------------
// 4️⃣ Herencia de constructores usando call
function Persona(nombre) {
    this.nombre = nombre;
}

function Estudiante(nombre, curso) {
    // Llamamos al constructor Persona y asignamos this del Estudiante
    Persona.call(this, nombre);
    this.curso = curso;
}

const estudiante1 = new Estudiante("Ana", "Matemáticas");
console.log(estudiante1.nombre); // "Ana"
console.log(estudiante1.curso);  // "Matemáticas"

// --------------------------------------------------
// 5️⃣ Reutilizar funciones genéricas
function mostrarNombre() {
    console.log(this.nombre);
}

const obj1 = { nombre: "Ana" };
const obj2 = { nombre: "Juan" };

mostrarNombre.call(obj1); // "Ana"
mostrarNombre.call(obj2); // "Juan"

// --------------------------------------------------
// ✅ Resumen:
// - call: invoca una función con un "this" específico
// - Los argumentos se pasan uno por uno
// - Muy útil para:
//   1) Herencia de constructores
//   2) Reutilizar métodos en diferentes objetos
//   3) Controlar "this" en funciones independientes
