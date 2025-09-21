// Sentencia de operadores

//Sentencia if: Si la condicion es verdadera se ejecuta el bloque de codigo, su sintaxis es if (condicion) { bloque }
if (5 > 3) {
    console.log("5 es mayor que 3");
}

//Sentencia if-else: Si la condicion es verdadera se ejecuta el bloque de codigo del if, si es falsa se ejecuta el bloque del else, su sintaxis es if (condicion) { bloque } else { bloque }
if (5 > 3) {
    console.log("5 es mayor que 3");
} else {
    console.log("5 no es mayor que 3");
}

// Operador terniario: Es una forma corta de escribir una sentencia if-else, su sintaxis es cond ? expr1 : expr2, donde la expresion1 es la que pasa cuando la condicion es verdadera
let resultado = (5 > 3) ? "5 es mayor que 3" : "5 no es mayor que 3";
console.log(resultado);

// Sentencia switch: Permite evaluar una expresion y ejecutar diferentes bloques de codigo segun el valor de la expresion, su sintaxis es switch (expresion) { case valor: bloque; break; }
let dia = 2;
switch (dia) {
    case 1:
        console.log("Lunes");
        break;
    case 2:
        console.log("Martes");
        break;
    case 3:
        console.log("Miércoles");
        break;
    default:
        console.log("Día no válido");
}