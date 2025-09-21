// FUNCIONES
// Una función es un bloque de código diseñado para realizar una tarea específica. En TypeScript, las funciones se definen utilizando la palabra clave function, seguida del nombre de la función, una lista de parámetros entre paréntesis y un bloque de código entre llaves. 
// Podemos especificar los tipos de los parámetros y el tipo de retorno de la función para aprovechar las ventajas del tipado estático de TypeScript.
//La sintaxis básica para definir una función en TypeScript es la siguiente: function nombreDeLaFuncion(parametro1: tipo1, parametro2: tipo2, ...): tipoDeRetorno { // cuerpo de la función }

function saludar(nombre: string): string {
    return `Hola, ${nombre}!`;
}

//TypeScript permite una gran variedad de tipos de parámetros en sus funciones. Vamos a ver cada uno de ellos
// PARAMETROS OBLIGATORIOS: Los parámetros obligatorios son aquellos que deben ser proporcionados cuando se llama a la función. Estos parámetros se definen en la declaración de la función sin ningún modificador especial.
function sumar(a: number, b: number): number {
    return a + b;
}

// PARAMETROS OPCIONALES: En TypeScript, también podemos hacer que los parámetros de una función sean opcionales (esto significa que no es necesario proporcionar un valor para esos parámetros al llamar a la función). Para hacer un parámetro opcional, simplemente agregamos un signo de interrogación (?) después del nombre del parámetro.

function multiplicar( a: number, b?: number ): number {
    if (b !== undefined) {
        return a * b;
    }
    return a;
}

// PARAMETROS POR DEFECTO: Los parámetros por defecto son aquellos que tienen un valor predeterminado asignado en la declaración de la función. TypeScript también permite especificar valores por defecto para los parámetros de una función (esto significa que si no se proporciona un valor para un parámetro, se utilizará el valor por defecto especificado). Para asignar un valor por defecto a un parámetro, utilizamos el operador de asignación (=) después del tipo de dato.

function dividir(a: number, b: number = 1): number {
    return a / b;
}

// PARAMETROS REST: Los parámetros rest permiten a una función aceptar un número variable de argumentos como un array. En TypeScript, podemos definir un parámetro rest utilizando la sintaxis ...nombreDelParametro: tipo[] en la declaración de la función. Esto indica que la función puede recibir cero o más argumentos adicionales, que se agruparán en un array.

function concatenar( ...cadenas: string[] ): string {
    return cadenas.join(' ');
}

// PARAMETROS CON LITERALES
function configurar( modo: 'auto' | 'manual', nivel: 1 | 2 | 3 ): string {
    return `Modo: ${modo}, Nivel: ${nivel}`;
}

// PARAMETROS DE FUNCION COMO TIPO
function operar( a: number, b: number, operacion: (x: number, y: number) => number ): number {
    return operacion(a, b);
}