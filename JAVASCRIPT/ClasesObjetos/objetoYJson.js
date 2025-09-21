/*
JSON es un formato de intercambio de datos ligero, fácil de leer para seres humanos, y fácil de parsear y generar para máquinas.
La relación entre JSON y los objetos JavaScript es muy estrecha. De hecho, JSON significa JavaScript Object Notation
Trabajar con JSON con JavaScript es una tarea común, ya que JSON es un formato de ampliamente utilizado en aplicaciones web y APIs para el intercambio de datos.

En JavaScript, JSON se representa como una cadena de texto que sigue una estructura similar a la de un objeto o array JavaScript, pero en formato de texto plano.
JSON utiliza una sintaxis similar a los objetos de JavaScript, pero hay algunas diferencias clave:
Las claves deben estar entre comillas dobles.
Las propiedades no pueden ser funciones, Symbols, o valores undefined.

JSON:
{
    "nombre": "Luis",
    "edad": 30,
    "habilidades": ["JavaScript", "Python", "Java"]
}

JS: const persona = {
    nombre: "Luis",
    edad: 30,
    habilidades: ["JavaScript", "Python", "Java"],
    saludar: function() { //... }
};

Los valores de las propiedades pueden ser cadenas, números, arrays, objetos, true, false o null,
*/


// CONVERSION ENTRE OBJETOS Y JSON: JavaScript proporciona métodos integrados para convertir objetos a JSON y viceversa: JSON.stringify() y JSON.parse().

//Objeto a JSON: Para convertir un objeto de JavaScript a una cadena JSON, se utiliza JSON.stringify(). Este método toma un objeto como argumento y devuelve su representación en formato JSON.
const persona = {
    nombre: "Luis",
    edad: 30,
    ciudad: "Madrid"
}

const personaJSON = JSON.stringify(persona);
console.log(personaJSON); //JSON.stringify() no puede manejar propiedades que sean funciones, undefined o símbolos. Si el objeto tiene estas propiedades se omitirán en la cadena JSON resultante.

//JSON a un Objeto: Para convertir una cadena JSON a un objeto JavaScript, utilizamos el método JSON.parse().
const personaObj = JSON.parse(personaJSON);
console.log(personaObj);

//Al convertir JSON a objetos JSON.parse(), pueden ocurrir errores si intentamos parsear un JSON no válido. por lo tanto es recomendable usar un bloque try-catch

