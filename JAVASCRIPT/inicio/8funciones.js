// Funcion
// Una funcion es un bloque de código reutilizable que realiza una tarea específica. Puede tener parametros y tambien devolver un valor de salida

function holamundo(){ // Funcion sin parametros
    console.log("¡Hola, mundo!");
}

function suma(a, b) { //Funcion con parametros y return
    return a + b;
}

function resta(a, b) {
    console.log(a - b); //Funcion con parametros sin return
}

// Parametros y argumentos
// Los parametros son las variables que se definen en la funcion
// Los argumentos son los valores que se pasan a la funcion


// Procedimiento y función
// Un procedimiento es una función que no devuelve un valor
// Una función puede ser un procedimiento si no tiene una declaración de retorno

holamundo(); //Procedimiento
console.log(suma(5, 3)); //Función
resta(10, 4); //Procedimiento

// Paso por valor y referencia
// El paso por valor significa que se pasa una copia del valor a la función
// El paso por referencia significa que se pasa una referencia al valor original

function incremento(a) { //Es cuando se pasan valores de tipo primitivo, como números o cadenas
    console.log(a++);
}
a = 5;
incremento(a);
console.log(a); //5

function modificarString(arreglo) { //Es cuando se pasan tipos de datos complejos arrays o objetos
    arreglo[0] = arreglo[0].toUpperCase();
}
palabra= ["hola"];  
modificarString(palabra);
console.log(palabra);


// Funciones recursivas
// Son funciones que se llaman a sí mismas para resolver un problema
function factorial(n) {
    if (n === 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}
console.log(factorial(5)); //120

// hoisting en funciones: n JavaScript, el Hoisting es un comportamiento del motor de JavaScript que afecta la forma en que se interpretan las declaraciones de variables y funciones. El hoisting hace que las declaraciones de variables y funciones sean “elevadas” al inicio de su contexto de ejecución. Con “elevar” la declaración queremos decir, que el intérprete sabe que existe una función, aunque la declaremos más adelante en el código.
//El hoisting es una característica muy útil, que nos facilita el desarrollo. Sin embargo, también es uno de los conceptos menos entendidos y que generan más confusión.
//Como decía, el Hoisting consiste en que el intérprete conoce las variables o funciones, antes de su declaración. Es decir, que podemos hacer esto.

saludar(); // Output: "Hola, mundo!"

function saludar() {
    console.log("Hola, mundo!");
}

//En este caso, La función saludar se puede llamar antes de su declaración Esto es así porque porque el Hoisting “eleva” la declaración. Si no tuviéramos Hoisting, tendríamos que escribir las funciones en el mismo orden en el que las usamos. Lo cuál puede parecer un problema pequeño. Pero a medida que escribes código, tendrías que estar constantemente cambiando el orden de las funciones (para que estén en el mismo orden en que las usas). Así que el intérprete primero se da una vuelta por todo el fichero recopilando las definiciones, para que sea más cómodo para nosotros.

//CLOSURE: un closure (o clausura) es una funcionalidad que permite a las funciones tener acceso al ámbito de la función que las contiene, incluso después de que esta función externa haya terminado de ejecutarse. En otras palabras, un closure “cierra” el ámbito de la función que lo creó, lo que permite que las variables locales de esa función permanezcan accesibles. Las closures son una funcionalidad automática. JavaScript gestiona las closures por nosotros cuando es necesario (es decir, que no tenemos que hacer nada).
// las closures se crean de forma automática. Esto ocurre cuando una función interna se define dentro de otra función. La closure permite que la función interna tenga acceso a las variables de la función externa, incluso después de que la función externa haya finalizado su ejecución. Ejemplo
function crearContador() {
    let cuenta = 0;
    
    return function() {
        cuenta++;
        return cuenta;
    };
}

const contador = crearContador();
console.log(contador()); // 1
console.log(contador()); // 2
console.log(contador()); // 3

//Para entender cómo funcionan los closures, es importante entender cómo JavaScript maneja el ámbito y la memoria. JavaScript utiliza el concepto de ámbito léxico (o lexical scope), lo que significa que el ámbito de una función se determina en el momento de su creación, no en el momento de su ejecución. Cuando se crea un closure, la función interna “recuerda” el entorno léxico en el que fue creada, lo que incluye todas las variables y parámetros de la función externa. Cuando se accede a una variable en una función, JavaScript sigue una cadena de ámbito (o scope chain). Primero, busca la variable en el ámbito local. Si no se encuentra, busca en el ámbito de la función externa, y así sucesivamente hasta llegar al ámbito global. Los closures preservan esta cadena de ámbito, permitiendo el acceso a las variables de la función externa. Aunque los closures son útiles y tienen muchas ventajas, también pueden llevar a un consumo mayor de memoria (si no se manejan adecuadamente).
//Si una closure mantiene referencias a variables que ya no son necesarias, puede causar que estas variables no sean recolectadas por el recolector de basura, lo que resulta en fugas de memori


// CURRYING :El currying es una técnica que transforma una función con múltiples parámetros en una secuencia de funciones, cada una con un solo parámetro. En otras palabras, en lugar de pasar todos los argumentos a la función de una vez, el currying permite “descomponer” la función en pasos más simples.

//funcion normal
function sumarNumeros(a, b) {
    return a + b;
}

//funcion curry
function sumarNumerosCurried(a) {
    return function(b) {
        return a + b;
    }; 
} //Ahora, en lugar de llamar a nuestra funcion sumar(a, b), tenemos una función que acepta un parámetro, y devuelve otra función que acepta otro parámetro.

const sumar5 = sumarNumerosCurried(5);

console.log(sumar5(3));  // Output: 8
console.log(sumar5(10)); // Output: 15

//Hemos visto como convertir una función en una versión “curried” de forma manual, en el ejemplo anterior con la función suma. Sin embargo, lo normal es que hagamos alguna solución genérica, para convertir cualquier función. Vamos a ver alguna de ellas.

//funcion utilitaria
function currying(fn) {
    return function(arg1) {
        return function(arg2) {
            return fn(arg1, arg2);
        };
    };
}

// Uso
function multiplicar(a, b) {
    return a * b;
}

const multiplicarCurried = currying(multiplicar);
const multiplicarPor2 = multiplicarCurried(2);
console.log(multiplicarPor2(4)); // Output: 8

// GENERADORES
// En JavaScript una función generadora es un tipo especial de función que puede pausar su ejecución y luego reanudarla en un momento posterior.

// Las funciones generadoras son útiles cuando necesitamos trabajar con una gran cantidad de datos o con secuencias grandes, ya que solo calculan los valores a medida que los solicitamos (en lugar de calcular todos los valores de una vez).

// Sintaxis básica de las funciones generadoras
// Las funciones generadoras se definen utilizando la sintaxis function* (el asterísco indica que la función es una generadora).

// Por otro lado, dentro de la función vamos a usar la palabra clave yield (que pausa la ejecución y devolver un valor)

// Funcionamiento de yield
// Cada vez que se encuentra con un yield, la función devuelve el resultado y se suspende en ese punto.
// Cuando se llama a next() de nuevo, la función generadora continúa ejecutándose justo después del yield que la suspendió.
// Se ejecutará hasta que encuentre otro yield o termine la ejecución.
// El resultado devuelto por yield es un objeto con las propiedades value (el valor generado) y done (un booleano que indica si la secuencia ha terminado).

//SINTAXIS: function* nombre(){ proceso.. yield; processo; yield;}
function* generadorEjemplo() {
  yield 1; // Pausa aquí y devuelve 1
  yield 2; // Pausa aquí y devuelve 2
  yield 3; // Pausa aquí y devuelve 3
}
const generador = generadorEjemplo();

console.log(generador.next()); // { value: 1, done: false }
console.log(generador.next()); // { value: 2, done: false }
console.log(generador.next()); // { value: 3, done: false }
console.log(generador.next()); // { value: undefined, done: true }

/*
La relación entre funciones generadoras e iteradores es muy estrecha (de hecho, están diseñados para trabajar juntas).
Un iterador es un objeto que debe tener un método next(), que devuelva un objeto con las propiedades value y done.
Como hemos visto, este es exactamente el comportamiento de las funciones generadores cuando usamos yield.
Es decir, que cualquier función generadora es también un iterador. De hecho, podemos usarlas en un bucle for...of
*/

function* colores() {
  yield 'rojo';
  yield 'verde';
  yield 'azul';
}

for (const color of colores()) {
  console.log(color); // 'rojo', 'verde', 'azul'
}

// FUNCIONES ARROW (flecha)
// Una función arrow en JavaScript es una sintaxis concisa para definir una función anónima que se puede definir en línea sin necesidad de nombrarla formalmente.
// Se les conoce formalmente como una “función flecha” debido a la notación de flecha (=>) que se utiliza para definirla (también se les puede llamar funciones lambda).
// Estas funciones ofrecen una forma más breve de escribir funciones. Es especialmente útil en situaciones donde necesitas definir una función simple, que vas a usar una única vez.
// Además, tienen comportamientos específicos relacionados con el contexto de this (que simplifican su uso). Aqui no aplica el hoisting

/* La sintaxis de una función flecha es la siguiente:
const nombreFuncion = (param1, param2, ...) => {
    Bloque de código
};

nombreFuncion: El nombre de la variable que contiene la función lambda.
param1, param2, …: Los parámetros que la función acepta.
=>: El operador de flecha que define la función lambda.
Bloque de código: El cuerpo de la función que realiza la operación deseada.
*/

const sumarflecha = (a,b) => { return a+b;}
console.log(sumarflecha(5,5))
// una funcion flecha puede o no retornar valores

//Existe otra variacion de sintaxis donde tiene un return implicito, siendo este const nombreFuncion = (param1, param2, ...) =>  expresion;
//Si se quiere mas de dos sentencias se debe optar por usar llaves y la palabra return si es que se retornara un valor

// Nota: Si solo hay un parametro para la funcion se pueden omitir los paréntesis

/*
Una de las características más importantes de las funciones lambda es que no tienen su propio contexto de this.
En lugar de eso, this se hereda del contexto en el que se define la función. Esto puede ser útil cuando se trabaja con métodos dentro de objetos y se desea mantener el contexto de this
*/
class Contador {
    constructor() {
        this.numero = 0;
    }

    incrementar() {
        setTimeout(() => {
            this.numero++; //Por ejemplo aqui this hereda de la clase
            console.log(this.numero);
        }, 1000);
    }
}

const contadorxd = new Contador();
contadorxd.incrementar(); // Salida después de 1 segundo: 1

/* LIMITACIONES
Las funciones lambda no se pueden usar como constructores. No pueden ser invocadas con el operador new, y si se intenta hacerlo, se produce un error.
*/

// FUNCIONES ANONIMAS
// Las funciones anónimas son aquellas que no tienen nombre y se declaran en línea. Se utilizan comúnmente como argumentos para otras funciones o para declarar una función dentro de otra.
// La sintaxis de una función anónima es la siguiente:
// let nombreFuncion = function(parametro1, parametro2) {
        // Código a ejecutar
// }
// Un ejemplo de una función anónima podría ser:
let sumar = function(a, b) {
  return a + b;
}

//Tipos de parámetros en JavaScript:En JavaScript, los parámetros pueden adoptar diferentes formas según cómo los definamos. Vamos a ver algunos de los tipos de parámetros más importantes.

// Posicionales: Los parámetros posicionales son los más comunes. Son aquellos que se definen en el orden en que se espera que se pasen al invocar la función. La función asigna automáticamente los argumentos pasados a estos parámetros en el orden especificado.
function presentarPersona(nombre, edad) {
    console.log(`Hola, me llamo ${nombre} y tengo ${edad} años.`);
}
presentarPersona("Luis", 30); // Salida: Hola, me llamo Luis y tengo 30 años.

// Por defecto: Los parámetros por defecto nos permiten definir valores predeterminados para los parámetros de una función.Si no se pasa un argumento para un parámetro en particular, se usará el valor por defecto undefined.
function presentarPersonaConDefecto(nombre, edad = 0) {
    console.log(`Hola, me llamo ${nombre} y tengo ${edad} años.`);
}
presentarPersonaConDefecto("Luis"); // Salida: Hola, me llamo Luis y tengo 0 años.

//Parametros REST: Los parámetros REST permiten a una función recibir un número indefinido de argumentos como un array. Se definen usando tres puntos (...) antes del nombre del parámetro.
function sumarTodo(...numeros) {
    return numeros.reduce((acumulador, numero) => acumulador + numero, 0);
}

console.log(sumarTodo(1, 2, 3)); // Salida: 6
console.log(sumarTodo(10, 20, 30, 40)); // Salida: 100

// PARAMETROS DEESTRUCTURADOS:Los parámetros desestructurados nos permiten descomponer objetos o arrays en parámetros individuales (esto es útil para trabajar con objetos en funciones)Por ejemplo, podemos destructurar objetos
function mostrarDatos({ nombre, edad }) {
    console.log(`Nombre: ${nombre}, Edad: ${edad}`);
}
const persona = { nombre: "Luis", edad: 30 };
mostrarDatos(persona); // Salida: Nombre: Luis, Edad: 30

//O destructurar Arrays.
function mostrarColores([color1, color2]) {
    console.log(`Primer color: ${color1}, Segundo color: ${color2}`);
}

const colores = ["Rojo", "Azul"];
mostrarColores(colores); // Salida: Primer color: Rojo, Segundo color: Azul

//Llamar a la función con más o menos argumentos
//En JavaScript cuando llamas a una función y pasas más o menos parámetros de los que la función espera, el lenguaje no lanza un error automáticamente, sino que maneja esta situación de forma flexible.

//Argumentos de menos
//Si no proporcionas un valor para un parámetro esperado, ese parámetro tendrá automáticamente el valor undefined.
function saludar(nombre, edad) {
  console.log(`Hola, mi nombre es ${nombre} y tengo ${edad} años.`);
}

saludar("Luis"); 
// Imprime: Hola, mi nombre es Luis y tengo undefined años.

// Argumentos de más
// Si proporcionas más argumentos de los que la función espera, los parámetros adicionales simplemente se ignorarán.
function saludar(nombre, edad) {
  console.log(`Hola, mi nombre es ${nombre} y tengo ${edad} años.`);
}

saludar("Luis", 30, "extra"); 
// Imprime: Hola, mi nombre es Luis y tengo 30 años.