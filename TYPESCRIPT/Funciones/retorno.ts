// En programación, una función puede devolver un valor después de ejecutar su bloque de código. Este valor se llama “retorno” de la función. En TypeScript, se puede especificar el tipo de retorno de una función para asegurarse de que la función devuelve el tipo de dato esperado. Esto ayuda a prevenir errores y mejora la legibilidad del código. La sintaxis para definir el tipo de retorno de una función es colocar dos puntos (:) seguidos del tipo de dato después de los paréntesis de los parámetros de la función.

// Ejemplo 1: Función que devuelve un número
function sumar(a: number, b: number): number {
    return a + b;
}

// Ejemplo 2: Función que devuelve un string
function saludar(nombre: string): string {
    return `Hola, ${nombre}!`;
}

// Tipos de retorno primitivos: TypeScript permite especificar tipos de retorno primitivos (como number, string, boolean, etc).
function esMayorDeEdad(edad: number): boolean {
    return edad >= 18;
}

// Tipos de retorno complejos: Además de los tipos primitivos, las funciones en TypeScript también pueden devolver tipos complejos (como objetos, arrays, o tuplas).

function crearUsuario(nombre: string, edad: number): { nombre: string; edad: number } {
    return { nombre, edad };
}
console.log(crearUsuario("Juan", 30));

function obtenerArreglos(): number[] {
    return [1, 2, 3, 4, 5];
}
console.log(obtenerArreglos());

//TypeScript también permite devolver tipos personalizados, como los creados mediante type o interface.
type Persona = {
    nombre: string;
    edad: number;
};

function obtenerPersona(): Persona {
    return { nombre: "Ana", edad: 25 };
}
console.log(obtenerPersona());

//Funciones que no retornan valores: En TypeScript, si una función no devuelve ningún valor, se utiliza el tipo void como tipo de retorno. Esto es útil para funciones que solo realizan acciones y no necesitan devolver un valor.
function imprimirMensaje(mensaje: string): void {
    console.log(mensaje);
}
imprimirMensaje("Hola, mundo!");

// Retornos opcionales: En TypeScript, es posible definir funciones que pueden devolver un valor o no, utilizando el tipo de retorno union con undefined.
function obtenerValor(opcional: boolean): number | undefined {
    if (opcional) {
        return 42;
    } else {
        return undefined;
    }
}