// El modo estrico 
/*
Modo estricto ("strict mode") en JavaScript es una forma especial de ejecutar el código que ayuda a detectar errores y hacer que el lenguaje sea más seguro.

Se activa agregando "use strict"; al inicio de un archivo o función. Ejemplo:
¿Para qué sirve?
No permite usar variables sin declarar.
Prohíbe ciertas acciones inseguras (como asignar a propiedades no configurables).
Hace que algunos errores que antes se ignoraban ahora generen excepciones.
Evita el uso de palabras reservadas para nombres de variables.
Ventajas:

Ayuda a escribir código más limpio y seguro.
Facilita la depuración y el mantenimiento.
*/
    
"use strict";

let x = 10;
console.log(x);

miFuncion();

function miFuncion(){
    "use strict"
    y = 15;
    console.log(y);
}