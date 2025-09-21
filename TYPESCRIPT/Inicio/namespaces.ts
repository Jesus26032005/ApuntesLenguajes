// Los Namespaces (espacios de nombres) son una forma de organizar y agrupar nuestro código en módulos lógicos para evitar colisiones de nombres entre diferentes partes de nuestro programa.

// Un espacio de nombres en Typescript encapsula variables, funciones, clases y otros elementos en un contenedor. Esto nos permite agrupar y organizar nuestro código, evitando conflictos y mejorando la legibilidad y mantenibilidad del mismo.

// Para definir un espacio de nombres en Typescript, utilizamos la palabra clave namespace seguida del nombre que deseamos asignarle al espacio. Por ejemplo:


// namespace MiEspacio {
//   export function saludar() {
//     console.log("¡Hola desde MiEspacio!");
//   }
// }
// En este ejemplo,

// Creamos un espacio de nombres llamado MiEspacio
// Este contiene una función saludar.
// La declaración export permite que la función sea accesible fuera del espacio de nombres.
// Uso de espacios de nombres
// Una vez que hemos definido un espacio de nombres, podemos utilizarlo en otras partes de nuestro programa. Para acceder a los elementos dentro de un espacio de nombres, utilizamos la sintaxis NombreEspacio.NombreElemento. Por ejemplo:


// MiEspacio.saludar();
// En este caso, estamos llamando a la función saludar que se encuentra dentro del espacio de nombres MiEspacio.

// Anidación de espacios de nombres
// En Typescript, también es posible anidar espacios de nombres dentro de otros espacios de nombres. Esto nos permite organizar aún más nuestro código y evitar colisiones de nombres. Por ejemplo:


// namespace MiEspacio {
//   export namespace SubEspacio {
//     export function despedir() {
//       console.log("¡Adiós desde SubEspacio!");
//     }
//   }
// }
// En este caso,

// Hemos anidado un espacio de nombres llamado SubEspacio dentro del espacio de nombres MiEspacio
// La función despedir se encuentra dentro del espacio de nombres SubEspacio
// Para acceder a esta función, utilizamos la sintaxis MiEspacio.SubEspacio.despedir()