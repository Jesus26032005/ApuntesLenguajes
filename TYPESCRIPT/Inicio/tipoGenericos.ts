//Los genéricos en TypeScript nos permiten definir funciones, clases o componentes que admiten un tipo como parte de su definición. De esta forma, pueden comportarse diferente de forma diferente, en función del tipo recibido, adaptando su comportamiento genérico a los diferentes tipos.

// FUNCIONES GENERICAS
//Los genéricos se definen utilizando el símbolo < >, y se pueden aplicar tanto a variables como a funciones. Es muy habitual usar “T” (de “Type”) para denominar al tipo que recibe la función. Pero es posible usar cualquier otra letra o nombre. <T> es el tipo genérico que se puede utilizar para representar cualquier tipo de dato. La función imprimirValor acepta un parámetro valor de tipo T y simplemente lo imprime en la consola. La sintaxis <T> indica que la función es genérica y puede trabajar con cualquier tipo de dato.
// Si va a hbaer otrros valores pero que no son genericos, se ponen despues de los genericos
// Si no se especifica el tipo al llamar a la función, TypeScript intentará inferirlo automáticamente en función del valor pasado.

function imprimirValor<T>(valor: T): void {
    console.log(valor);
}
imprimirValor<string>("Hola"); // Imprime "Hola"
imprimirValor<number>(42);


function mostrarTipo<T>(arg: T): void {
    console.log(typeof arg);
}
mostrarTipo<string>("Hola"); // Imprime "string"
mostrarTipo<number>(42);

// varios parametros genericos
function combinar<T, U>(arg1: T, arg2: U): [T, U] {
    return [arg1, arg2];
}

// CLASES GENERICAS
// Además de las funciones, también podemos crear clases genéricas en TypeScript. Esto nos permite crear clases que pueden trabajar con diferentes tipos de datos.
class Caja<T> {
    contenido: T;
    constructor(contenido: T) {
        this.contenido = contenido;
    }
}
const cajaDeNumeros = new Caja<number>(123);
const cajaDeTexto = new Caja<string>("Hola");
console.log(cajaDeNumeros.contenido); // 123
console.log(cajaDeTexto.contenido); // "Hola"

// RESTRICCIONES EN TIPOS GENERICOS
// A veces, queremos limitar los tipos que se pueden usar con nuestros genéricos. Podemos hacer esto utilizando restricciones.
interface TieneLongitud {
    length: number;
}
function imprimirLongitud<T extends TieneLongitud>(arg: T): void {
    console.log(arg.length); 
}
imprimirLongitud("Hola");

// INFERENCIA DE TIPOS
// TypeScript puede inferir automáticamente el tipo genérico basado en el valor que se pasa a la función o clase.
function identidad<T>(arg: T): T {
    return arg;
}
const numero = identidad(42); // TypeScript infiere que T es number
const texto = identidad("Hola"); // TypeScript infiere que T es string