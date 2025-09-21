// En TypeScript, podemos declarar variables utilizando la palabra clave let o const, seguida del nombre de la variable (opcionalmente, su tipo).

// La palabra clave let declara variables que tienen un ámbito de bloque (block scope). Esto significa que la variable solo es accesible dentro del bloque donde las definimos.

let nombre: string = "Luis";
nombre = "Carlos"; // Correcto
console.log(nombre); // Carlos
// La palabra clave const se utiliza para declarar constantes (es decir, variables cuyo valor no cambiará una vez asignado). También tienen un ámbito de bloque.

const PI: number = 3.1416;
console.log(PI); // 3.1416
// PI = 3.14; // Error: No se puede asignar un nuevo valor a una constante

// En TypeScript, es recomendable especificar el tipo de dato al declarar una variable para aprovechar las ventajas del sistema de tipos estáticos. Sin embargo, TypeScript también puede inferir el tipo automáticamente si no se especifica.
//El sistema de tipos en TypeScript es un poco “especial” frente a otros lenguajes. Algunas de las características que lo hacen especial son:
    // Estática: La tipificación se verifica en tiempo de compilación, lo que permite detectar errores antes de ejecutar el código.
    // Opcional: Aunque TypeScript es un lenguaje fuertemente tipado, la tipificación es opcional y puede ser progresivamente añadida a un proyecto.
    // Estructural: TypeScript utiliza una tipificación estructural, donde dos tipos son compatibles si tienen la misma forma o estructura

//Para declarar una variable asignando un tipo específico, se utiliza la sintaxis: <tipo> <nombre_variable> = <valor>;


// Tipos primitivos en typescript: Los tipos básicos que se encuentran en casi todos los lenguajes de programación.
let numero: number = 5; //Representa números (enteros y decimales)
let cadenaTexto:  string; //Representa texto
cadenaTexto= "hola we"  
//cadenaTexto = 5 mandara error
let booleano: boolean = true; //Representa valores true o false
let enteroGrande: bigint = 12345678901234567890n; //Representa enteros grandes
let simbolo: symbol = Symbol("id"); //Representa un valor unico y mutable
let cualquiera: any = "puede ser cualquier cosa"; //Representa cualquier tipo de valor (deshabilita la verificación de tipos)
let desconocido: unknown = 10; //Representa un valor desconocido (requiere verificación de tipo antes de usarlo)
let vacio : void = undefined; //Representa la ausencia de valor (usado principalmente en funciones que no retornan nada)
let nulo: null = null; //Representa un valor nulo
let indefinido: undefined = undefined; //Representa una variable que no ha sido asignada
let nunca: never; //Representa un valor que nunca ocurre (usado en funciones que lanzan errores o no retornan)

// Tipos de datos personalizados : Definidos por el usuario para satisfacer necesidades específicas.
// Literales: Permiten definir un conjunto específico de valores que una variable puede tomar, su sintaxis es <tipo_literal1> | <tipo_literal2> | ... ;
let estado: "activo" | "inactivo" | "pendiente";
estado = "activo"; // Correcto

// enum: Permiten definir un conjunto de constantes con nombre mas descriptivos, su sintaxis es enum <nombre_enum> { <valor1>, <valor2>, ... };
enum Color {
    rojo = "ROJO",
    verde = "VERDE",
    azul = "AZUL"
}
let colorFavorito: Color = Color.azul;

// tuplas : Permiten definir un array con un número fijo de elementos y tipos específicos para cada posición, su sintaxis es let <nombre_variable>: [<tipo1>, <tipo2>, ...] = [<valor1>, <valor2>, ...];
let coordenadas: [number, number] = [10, 20];

// arrays: Permiten definir una colección de elementos del mismo tipo, su sintaxis es let <nombre_variable>: <tipo>[] = [<valor1>, <valor2>, ...];
let numeros: number[] = [1, 2, 3, 4, 5];
let nombres: string[] = ["Juan", "María", "Pedro"];
let generico: Array<any> = [1, "dos", true]; // Array de cualquier tipo

// Tipos compuestos
// Tipó unión: Permiten definir una variable que puede contener valores de diferentes tipos, su sintaxis es <tipo1> | <tipo2> | ... ;
let valor: string | number;
valor = "Hola";

// Tipo intersección: Permiten combinar múltiples tipos en uno solo, su sintaxis es <tipo1> & <tipo2> & ... ;
type A = { nombre: string };
type B = { edad: number };
type C = A & B;
let persona: C = { nombre: "Ana", edad: 30 };

// Uso de alias: Un Alias de tipo en TypeScript nos permite crear un nombre alternativo para un tipo específico (ya sea estándard, o definido por nosotros). Los alias son una gran ayuda para mejorar la legibilidad del código. Son especialmente útiles cuando trabajamos con tipos complejos (como uniones, intersecciones y tipos personalizados). La sintaxis para definir un alias de tipo es: type <nombre_alias> = <tipo>;
type Punto = { x: number; y: number };
let origen: Punto = { x: 0, y: 0 };

type resultado = "éxito" | "error" | "pendiente";
let estadoResultado: resultado = "éxito";
// Mas adelante se veran mas funciones de alias

//Tipos genéricos: Permiten definir componentes reutilizables que pueden trabajar con diferentes tipos de datos, su sintaxis es function <nombre_funcion><T>(<parametro>: T): T { ... } o class <nombre_clase><T> { ... };
function identidad<T>(arg: T): T {
    return arg;
}

//alias con tipos genericos
type Caja<T> = { contenido: T };
let cajaDeNumeros: Caja<number> = { contenido: 123 };
let cajaDeCadenas: Caja<string> = { contenido: "Hola" };