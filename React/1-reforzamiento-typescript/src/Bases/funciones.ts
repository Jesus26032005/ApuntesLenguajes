// FUNCIONES
// Una función es un bloque de código diseñado para realizar una tarea específica. En TypeScript, las funciones se definen 
// utilizando la palabra clave function, seguida del nombre de la función, una lista de parámetros entre paréntesis y un
//  bloque de código entre llaves.  Podemos especificar los tipos de los parámetros y el tipo de retorno de la función para 
// aprovechar las ventajas del tipado estático de TypeScript. lLa sintaxis básica para definir una función en TypeScript es la 
// siguiente: function nombreDeLaFuncion(parametro1: tipo1, parametro2: tipo2, ...): tipoDeRetorno { // cuerpo de la función }

function saludar(nombre: string): string {
    return `Hola, ${nombre}!`;
}
console.log(saludar("jesus"))

// PARAMETROS OPCIONES O OBLIGATORIOS
// Para colcocar un parametro opcional se coloca al igual que en interfaces el signo de interrogacion despues del nombre
//  del parametro
function sumar(a: number, b?: number): number {
    if (b !== undefined) {
        return a + b;
    }
    return a;
}
console.log(sumar(5, 10));

// PARAMETROS POR DEFECTO: Se pueden asignar valores por defecto a los parametros en caso de no recibir ningun valor
//  al llamar la funcion
function multiplicar(a: number, b: number = 1): number {
    return a * b;
}
console.log(multiplicar(5));

// PARAMETROS REST: Los parámetros rest permiten a una función aceptar un número variable de argumentos como un array. En 
// TypeScript,  podemos definir un parámetro rest utilizando la sintaxis ...nombreDelParametro: tipo[] en la declaración 
// de la función. Esto indica que la función puede recibir cero o más argumentos adicionales, que se agruparán en un array.
function concatenar( ...cadenas: string[] ): string {
    return cadenas.join(' ');
}
console.log(concatenar("Hola", "mundo", "!"));

// PARAMETROS CON LITERALES: Permiten restringir los valores que puede tomar un parametro a un conjunto especifico de
// valores literales
function configurar( modo: 'auto' | 'manual', nivel: 1 | 2 | 3 ): string {
    return `Modo: ${modo}, Nivel: ${nivel}`;
}
console.log(configurar('auto', 2));

// FUNCIONES COMO PARAMETROS
// En TypeScript, las funciones pueden ser pasadas como parámetros a otras funciones. Para hacer esto, debemos definir el 
// tipo de la función que se espera como parámetro, incluyendo los tipos de sus argumentos y su tipo de retorno.
function operar( a: number, b: number, operacion: (x: number, y: number) => number ): number {
    return operacion(a, b);
}
const suma = (x: number, y: number): number => x + y;
console.log(operar(5, 10, suma));


// RETORNOS
// En ts existen diferentes tipos de retornos, desde los primitivos hasta los complejos, pasando por los personalizados.
// 1. Retornos primitivos, devuelven tipos de datos simples como number, string, boolean, etc.
// 2. Retornos complejos, devuelven tipos de datos más elaborados como objetos, arrays o tuplas.
// 3. Retornos personalizados, devuelven tipos definidos por el usuario mediante type o interface.
// 4. Funciones que no retornan valores, utilizan el tipo void como tipo de retorno.
// 5. Retornos opcionales, pueden devolver un valor o no, utilizando el tipo de retorno union con undefined.

function esMayorDeEdad(edad: number): boolean {
    return edad >= 18;
}
console.log(esMayorDeEdad(20));
function crearUsuario(nombre: string, edad: number): { nombre: string; edad: number } {
    return { nombre, edad };
}
console.log(crearUsuario("Juan", 30));
function obtenerArreglos(): number[] {
    return [1, 2, 3, 4, 5];
}
console.log(obtenerArreglos());
type Persona = {
    nombre: string;
    edad: number;
};
function obtenerPersona(): Persona {
    return { nombre: "Ana", edad: 25 };
}
console.log(obtenerPersona());
function imprimirMensaje(mensaje: string): void {
    console.log(mensaje);
}
imprimirMensaje("Hola, mundo!");
function obtenerValor(opcional: boolean): number | undefined {
    if (opcional) {
        return 42;
    } else {
        return undefined;
    }
}
console.log(obtenerValor(true));

// FUNCIONES ANONIMAS Y FLECHA
// Funciones anónimas: Son funciones que no tienen un nombre asociado. Se utilizan comúnmente como funciones de 
// devolución de llamada (callbacks) o en expresiones de función. En TypeScript, las funciones anónimas pueden definirse 
// utilizando la sintaxis de función tradicional o la sintaxis de función flecha.

// Para crear una función anónima utilizando la sintaxis tradicional: 
// const miFuncion = function(parametro1: tipo1, parametro2: tipo2): tipoDeRetorno { // cuerpo de la función };

const saludarAnonimo = (nombre: String): string => { return `Hola, ${nombre}!`; };
console.log(saludarAnonimo("Jesús"));
    // Si la función tiene una sola expresión, se pueden omitir las llaves y el return implícito.
    // const despedir = (nombre: string): void => console.log(`Adiós ${nombre}.`);
    // Si la función tiene un solo parámetro, se pueden omitir los paréntesis.
    // const despedir = nombre: string => console.log(`Adiós ${nombre}.`);
    // Si la función no tiene parámetros, se deben usar paréntesis vacíos.
    // const despedir = (): void => console.log(`Adiós.`);
    // Si la función tiene múltiples parámetros, se deben usar paréntesis.
    // const despedir = (nombre: string, apellido: string): void => console.log(`Adiós ${nombre} ${apellido}.`);
    // Si la función tiene un cuerpo más complejo, se deben usar llaves y return explícito.
    // const despedir = (nombre: string): string => { 
    //     const mensaje = `Adiós ${nombre}.`;
    //     return mensaje;
    // };
    // Si la funcion solo tiene un retorno, se puede simplificar aun mas
    // const despedir = (nombre: string): string => `Adiós ${nombre}.`;
    // Si se regresa un objeto se usa parentesis para evitar confusiones con el cuerpo de la funcion
    // const crearUsuario = (uid: string, username: string): { uid: string; username: string } => ({ uid, username });
    // Si se tiene un tipo de retorno compuesto se coloca despues de los parametros, sin embargo, si es un objeto, la forma
    // normal es usando una interfaz o sino se coloca {{atributo: tipo}} para evitar confusiones con el cuerpo de la funcion

// Ejercicio 
const getUser = ()=>{return {uid: "ABC", username: "Zaddkiel"}}
console.log(getUser())

const getUsuarioActivo = (nombre: string) => ({uid: "ABC567", username: nombre});
console.log(getUsuarioActivo("Zaddkiel"))

// Usando funcion flecha en un forEach
// la for each es una funcion que recibe una funcion como parametro, en este caso una funcion flecha, dondeel parametro
// es el elemento actual del arreglo que se esta iterando
const nombres: string[] = ["Ana", "Luis", "Carlos"];
nombres.forEach( (nombre) => console.log(nombre) );

// Retorno con const
// Si se tiene un retorno que se esta seguro como van a devolver los datos
// Se pede usar as const para que el tipado sea mas estricto
// as const en el retorno de una función es un truco esencial para crear Custom Hooks en React.
// Su función principal es evitar el "Ensanchamiento de Tipos" (Type Widening) y convertir un Array 
// flexible en una Tupla Fija, esto permite que los Hooks personalizados devuelvan estructuras de datos 
// con tipos más precisos y predecibles y si aplicamos desestrcutruración, los tipos se mantienen intactos.
function useUsuario() {
    return ['Zaddkiel', 30] as const;
}
const [nombre] = useUsuario();
console.log(nombre+ ", ");