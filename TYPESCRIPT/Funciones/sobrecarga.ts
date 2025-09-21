//La sobrecarga de funciones permite declarar varias versiones de una función con diferentes parámetros y tipos de retorno. Cada versión de la función (o firma) se llama sobrecarga. La implementación real de la función debe manejar todas las combinaciones de parámetros definidos en las sobrecargas.

//Para crear sobrecargas de funciones en TypeScript debemos hacer lo siguiente
    //Definir las firmas de las funciones sobrecargadas.
    //Proveer una única implementación de la función que maneje todas las combinaciones de parámetros.

function combinar(a: number, b: number): number;
function combinar(a: string, b: string): string;

function combinar(a: string | number, b: string | number): string | number {
    if (typeof a === "number" && typeof b === "number") {
        return a + b; // Suma de números
    } else if (typeof a === "string" && typeof b === "string") {
        return a + b; // Concatenación de strings
    }
    return "Tipos no compatibles";
}
console.log(combinar(5, 10)); // Salida: 15
console.log(combinar("Hola, ", "mundo!"));
//console.log(combinar(5, "mundo!")); // No se permite, ya que no hay una sobrecarga que acepte un número y un string

//Sobrecarga con diferentes números de parámetros
//También es posible sobrecargar funciones con diferentes cantidades de parámetros. Por ejemplo, una función que puede tomar uno o dos parámetros:
function mostrarMensaje(mensaje: string): void;
function mostrarMensaje(mensaje: string, numero: number): void;

function mostrarMensaje(mensaje: string, numero?: number): void {
    if (numero !== undefined) {
        console.log(`Mensaje: ${mensaje}, Número: ${numero}`);
    } else {
        console.log(`Mensaje: ${mensaje}`);
    }
}