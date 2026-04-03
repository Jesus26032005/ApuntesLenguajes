/*
Las excepciones son eventos que ocurren durante la ejecución de un programa que interrumpen su flujo normal (generalmente representa un error ocurrido en el programa).
Cuando se lanza una excepción, se interrumpe la ejecución del código normal y el control se transfiere al manejador de excepciones (try…catch) más cercano, si existe.

Es decir, cuando se produce una Excepcion esta puede,
Ser capturada por un bloque try-catch
Si no, pasa a la función que invocó a la que genero el error
Si no se maneja, el programa se detiene 💥

Tipos de errores
JavaScript clasifica los errores en varias categorías, cada una con características y causas específicas. Los principales tipos de errores son:

Tipo de Error	Descripción
Error	Error genérico, la clase base para todas las excepciones.
TypeError	Ocurre cuando una operación es realizada en un tipo inapropiado.
RangeError	Se lanza cuando un valor está fuera del rango permitido.
ReferenceError	Ocurre al intentar acceder a una variable no definida.
SyntaxError	Se lanza por errores de sintaxis en el código JavaScript.
URIError	Ocurre al usar funciones de codificación de URI con un URI mal formado.
EvalError	Se lanza en situaciones de uso incorrecto de la función eval().


El bloque try…catch se utiliza para capturar excepciones que pueden ocurrir durante la ejecución de código en JavaScript.
Nos permite gestionar errores que ocurren durante la ejecución, sin interrumpir el flujo general del programa (gestionándolo de forma controlada).
La sintaxis básica de try...catch es la siguiente:

try {
    // Código que puede generar un error
} catch (error) {
    // Código que se ejecuta si ocurre un error
} finally {
    // Código que se ejecuta siempre, independientemente de si ocurrió un error o no
}

try: Contiene el bloque de código que se desea ejecutar y que podría lanzar una excepción.
catch: Captura la excepción lanzada en el bloque try y permite manejar el error.
finally (opcional): Contiene código que se ejecuta siempre, ya sea que ocurriera un error o no.
*/

let x=0, y=0
try {
    throw new Error("Error intencional");
} catch (error) {
    console.log("Error capturado:", error.message);
    /*
    El bloque catch captura el error lanzado dentro del try. El error capturado se pasa como un objeto (error), que suele tener propiedades útiles como:
    error.message: mensaje de error legible
    error.name: tipo de error (TypeError, ReferenceError, etc.)
    error.stack: rastreo de la pila de llamadas
    */
} finally {
    console.log("Bloque finally ejecutado");
}

//Se pueden añadir más bloques catch para manejar diferentes tipos de errores, sin embargo, en JavaScript, a diferencia de algunos otros lenguajes como Java o C#, un bloque try solo puede tener un catch. Es decir, no puedes escribir varios catch para capturar diferentes tipos de errores directamente. Si quieres diferenciar el tipo de error, dentro del mismo catch debes usar condicionales con instaceof para ver si el error es de una clase de error especifica: 
try {
    let x = y; // ReferenceError si y no está definido
} catch (error) {
    if (error instanceof ReferenceError) {
        console.log("Capturado ReferenceError:", error.message);
    } else if (error instanceof TypeError) {
        console.log("Capturado TypeError:", error.message);
    } else {
        console.log("Otro tipo de error:", error.message);
    }
}

// LANZAR EXCEPCIONES: Podemos lanzar excepciones en JavaScript utilizando la palabra clave throw. Esto permite indicar que ha ocurrido un error y proporcionar información adicional sobre él. la sintaxis basica es throw new tipoError("Mensaje de error"); generalmente se usa un ojeto error es decir throw new Error("Mensaje de error"); cuasando q al hacer esto se detenga la ejecucion del programa y se transfiere el control al bloque catch mas cercano si es que existe sino termina el programa

function validarEdad(edad) {
    if (edad < 18) {
        throw new Error("La edad debe ser al menos 18 años.");
    }
    return "Edad válida";
}

try {
    console.log(validarEdad(15));
} catch (error) {
    console.error("Se produjo un error:", error.message);
}

// CREACION DE EXCEPCIONES PERSONALIZADAS: Además de lanzar excepciones estándar, podemos crear nuestras propias excepciones personalizadas. Esto sirve para proporcionar información más específica sobre los errores en tu aplicación.Para crear una excepción personalizada, puedes extender la clase Error de JavaScript:

class MiExcepcion extends Error {
    constructor(mensaje = "Error personalizado") {  //El mensaje puede ser recibido como argumento o tambien escrito por defecto si no se proporciona uno o no se quiere que haya uno
        super(mensaje);
        this.name = "MiExcepcion"; // Establece el nombre de la excepción
    }
}

function validarNombre(nombre) {
    if (typeof nombre !== 'string' || nombre.length === 0) {
        throw new MiExcepcion("El nombre debe ser una cadena no vacía.");
    }
    return "Nombre válido";
}

try {
    console.log(validarNombre("")); // Lanzará una excepción
} catch (error) {
    console.error(`${error.name}: ${error.message}`);
}