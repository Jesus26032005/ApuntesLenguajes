/// Operadores
// Aritméticos
let suma = 5 + 3;
let resta = 5 - 3;
let multiplicacion = 5 * 3;
let division = 5 / 3;
let modulo = 5 % 3; //Es el residuo de la division
let potencia = 5 ** 2; //Es la potencia
console.log(suma);
console.log(resta);
console.log(multiplicacion);
console.log(division);
console.log(modulo);
console.log(potencia);

/// Pre-incremento y pre-decremento
let valor = 10;
console.log("Valor inicial:", valor);
// Pre-incremento: primero incrementa, luego usa el valor
console.log("Pre-incremento:", ++valor);
// Post-incremento: primero usa el valor, luego incrementa
console.log("Post-incremento:", valor++);
console.log("Valor después del post-incremento:", valor);

// Pre-decremento: primero decrementa, luego usa el valor
console.log("Pre-decremento:", --valor);
// Post-decremento: primero usa el valor, luego decrementa
console.log("Post-decremento:", valor--);
console.log("Valor después del post-decremento:", valor);

/// Operadores de asignacion 
let asignacion= 5
console.log("asignacion normal: ", asignacion)
console.log("asignacion compuesta de suma: ", asignacion += 5)
console.log("asignacion compuesta de resta: ", asignacion -= 3)
console.log("asignacion compuesta de multiplicacion: ", asignacion *= 2)
console.log("asignacion compuesta de division: ", asignacion /= 2)
console.log("asignacion compuesta de modulo: ", asignacion %= 3)
console.log("asignacion compuesta de potencia: ", asignacion **= 2)


// Operadores de comparacion
console.log("Comparacion de igualdad (==): ", 5 == "5"); // compara valores
console.log("Comparacion de igualdad estricta (===): ", 5 === "5"); // compara valor y tipo
console.log("Comparacion de desigualdad (!=): ", 5 != "5"); // compara valores
console.log("Comparacion de desigualdad estricta (!==): ", 5 !== "5"); // compara valor y tipo
console.log("Comparacion mayor que (>): ", 5 > 3); // mayor que
console.log("Comparacion menor que (<): ", 5 < 3); // menor que
console.log("Comparacion mayor o igual que (>=): ", 5 >= 5); // mayor o igual que
console.log("Comparacion menor o igual que (<=): ", 5 <= 3); // menor o igual que


// Operadores logicos
console.log("Comparacion AND (&&): ", true && false); // Regresa true si ambos valores son verdaderos
console.log("Comparacion OR (||): ", true || false); // Regresa true si al menos uno de los valores es verdadero
console.log("Comparacion NOT (!): ", !true); // Regresa true si el valor es falso


/* PRECEDENCIA DE OPERADORES
En JavaScript, los operadores se evalúan según su precedencia. 
1. Parentesis y Corchetes
2. Operadores unarios, como -, ++, --, !
3. Aritmeticos *, / y %
4. Aritmeticos + y -
5. Relacionales <, <=, > y >=
6. Igualdad == y !=
7. Logicos && y ||
8. Asignacion =, =+, -=, *=, etc

Se revisa de izq a der

*/