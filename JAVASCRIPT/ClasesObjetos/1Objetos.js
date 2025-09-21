// OBJETOS
//  Un objeto es una colección de propiedades, y una propiedad es una asociación entre un nombre (o clave) y un valor. Los objetos son una parte fundamental de JavaScript y se utilizan para representar entidades del mundo real. Estos objetos pueden contener valores de cualquier tipo, incluidos otros objetos, funciones y arreglos.

// CREACION DE OBJETOS
let objeto = {
    nombre: "objeto", //Se colocan propiedades dentro del objeto, ademas de para agregar mas de una se usan comas
    edad: 15, // Para inicializar las propiedades se usan dos puntos (:)
    arreglo: [1, 2, 3]
};      //Son parecidos a los diccionarios de otros lenguajes, pero mas acercados tambien a los objetos en cierta manera porque pueden contener otros objetos y funciones.

// ACCEDER A PROPIEDADES, se usa la sintaxis objeto.propiedad
console.log(objeto.nombre);  // Acceder a la propiedad "nombre"
console.log(objeto.edad);     // Acceder a la propiedad "edad"
console.log(objeto.arreglo);  // Acceder a la propiedad "arreglo"


// ACCESO A PROPIEDADES CON CORCHETES , se usa la sintaxis objeto["propiedad"]
console.log(objeto["nombre"]);  // Acceder a la propiedad "nombre"
console.log(objeto["edad"]);     // Acceder a la propiedad "edad"
console.log(objeto["arreglo"]);  // Acceder a la propiedad "arreglo"

// IMPRIMIR TODO EL OBJETO
console.log(objeto);

// AGREGAR METODOS A OBJETOS
let objetoMetodo = {
    nombre: "objeto",
    edad: 15,
    arreglo: [1, 2, 3],
    saludar: function() {
        console.log( "hola mundo");
    }
};

// LLAMAR AL METODO
objetoMetodo.saludar();

// USAR PROPIEDADES (ATRIBUTOS) EN METODOS
let objetoMetodo1 = {
    nombre: "objeto",
    edad: 15,
    arreglo: [1, 2, 3],
    saludar: function() {
        console.log("Hola, soy " + this.nombre); //se usa "this" para referirse al objeto actual seguido de su propiedad
    },
    sumar: function(a,b){ 
        console.log("La suma es: " + (a + b)); //se puede usar this para referirse a las propiedades del objeto
    }
};

// LLAMAR AL METODO
objetoMetodo1.saludar();
objetoMetodo1.sumar(5, 10);

// CREACION DE OBJETOS FORMA 2
let objeto2 = new Object(); // Usando el constructor Object, indicamos que vamos a crear un objeto, se crea un objeto vacio aqui

// AGREGAR PROPIEDADES AL OBJETO, se usa la sintaxis objeto.propiedadNueva= valor
objeto2.nombre = "objeto 2"; //Se agrega la propiedad "nombre" con el valor "objeto 2"
objeto2.edad = 20;
objeto2.arreglo = [4, 5, 6];

// ACCEDER A PROPIEDADES
console.log(objeto2.nombre);
console.log(objeto2.edad);
console.log(objeto2.arreglo);

//AGREGAR FUNCIONES
objeto2.saludar = function() {
    console.log("Hola, soy " + this.nombre);
};
objeto2.sumar = function(a, b) {
    console.log("La suma es: " + (a + b));
};

// LLAMAR A LOS METODOS
objeto2.saludar();
objeto2.sumar(5, 10);

// USAR FOR IN PARA RECORRER EL OBJETO, su sintaxis es la siguiente: for (let propiedad in objeto) {}
for (let propiedad in objeto2) {
    console.log("Propiedad: " + propiedad + ", Valor: " + objeto2[propiedad]);
    //ACCEDER A LOS VALORES
    console.log(objeto2[propiedad]); // la sintaxis es objeto2["propiedad"] para acceder a los valores
}

// AGREGAR Y ELIMINAR PROPIEDADES
objeto2.nuevaPropiedad = "Soy una nueva propiedad"; // Agregar nueva propiedad usando la sintaxis objeto.nuevaPropiedad= valor
console.log(objeto2.nuevaPropiedad);

objeto2.nuevaPropiedad = "He cambiado"; // Cambiar el valor de la nueva propiedad
console.log(objeto2.nuevaPropiedad);

delete objeto2.nuevaPropiedad; // Eliminar la propiedad "nuevaPropiedad", usando la sintaxis delete objeto.propiedadBorrar
console.log(objeto2.nuevaPropiedad); // undefined

// DISTINTAS FORMAS DE IMPRIMIR UN OBJETO
console.log(objeto2); // Imprimir todo el objeto

//Concatener cada valor de la propiedad
console.log("Nombre: " + objeto2.nombre + ", Edad: " + objeto2.edad + ", Arreglo: " + objeto2.arreglo);

// iterar sobre las propiedades del objeto
for (let propiedad in objeto2) {
    console.log("Propiedad: " + propiedad + ", Valor: " + objeto2[propiedad]);
}

// Usar sintaxis objeto.values  que regresa un arreglo con los valores de las propiedades
console.log(Object.values(objeto2)); // [ "objeto 2", 20, [ 4, 5, 6 ], [Function], [Function] ]

// usar sintaxis objeto.keys, que regresa un arreglo con los nombres de las propiedades
console.log(Object.keys(objeto2)); // [ "nombre", "edad", "arreglo", "saludar", "sumar", "nuevaPropiedad" ]

// usar sintaxis objeto.entries, que regresa un arreglo de pares [clave, valor]
console.log(Object.entries(objeto2)); // [ [ "nombre", "objeto 2" ], [ "edad", 20 ], [ "arreglo", [ 4, 5, 6 ] ], [ "saludar", [Function] ], [ "sumar", [Function] ], [ "nuevaPropiedad", "He cambiado" ] ]

// Usar JSON.stringify para convertir el objeto en una cadena JSON
console.log(JSON.stringify(objeto2)); // '{"nombre":"objeto 2","edad":20,"arreglo":[4,5,6],"saludar":{},"sumar":{},"nuevaPropiedad":"He cambiado"}'

// METODO GET, se utiliza para obtener el valor de una propiedad. En JavaScript, get es una palabra clave usada para definir un método getter en un objeto o clase. Un getter permite acceder a una propiedad calculada como si fuera una propiedad normal, pero ejecuta una función cuando se accede. su sintaxis es get propiedadCalculada(argumentosOpcionales) { bloquecodigo}
let objeto3 = {
    nombre: "objeto 3",
    edad: 30,
    apellido: "apellido 3",
    arreglo: [7, 8, 9],
    get NombreCompleto() {
        return this.nombre + " " + this.apellido;
    }
};

// LLAMAR A LOS METODOS GET
console.log(objeto3.NombreCompleto); // "objeto 3 apellido 3"

// METODO SET, se utiliza para establecer el valor de una propiedad. En JavaScript, set es una palabra clave usada para definir un método setter en un objeto o clase. En JavaScript, set se usa para definir un método setter en un objeto o clase. Un setter permite ejecutar una función cuando se asigna un valor a una propiedad, permitiendo controlar o modificar cómo se guarda ese valor.
let objeto4 = {
    nombre: "objeto 3",
    edad: 30,
    apellido: "apellido 3",
    idioma: "español",
    arreglo: [7, 8, 9],
    get NombreCompleto() {
        return this.nombre + " " + this.apellido;
    },
    set NombreCompleto(nuevoNombreCompleto) {
        let partes = nuevoNombreCompleto.split(" ");
        this.nombre = partes[0];
        this.apellido = partes[1];
    }

};

/*
En JavaScript, los métodos get y set permiten definir propiedades “accesoras” en los objetos, es decir, propiedades cuyo valor se calcula al obtenerlo o que ejecutan código al asignarlo. Funcionan como si fueran variables, pero en realidad son funciones detrás de escena.

get

Permite definir un método que se ejecuta al acceder a la propiedad.
Se usa como si fuera un atributo normal (obj.propiedad), no se usan paréntesis.
Útil para calcular valores derivados de otras propiedades.

set
Permite definir un método que se ejecuta al asignar un valor a la propiedad.
Recibe un parámetro que representa el valor que se está asignando.
Útil para validar o transformar datos antes de guardarlos.

get (getter):
Es una función que se ejecuta al acceder a una propiedad. Permite calcular o derivar un valor basado en otras propiedades del objeto.

set (setter):
Es una función que se ejecuta al asignar un valor a una propiedad. Permite validar, modificar o procesar datos antes de guardarlos.Ese método puede modificar propiedades internas del objeto, validar valores, o realizar cualquier lógica antes de almacenar algo. Se puede usar para cualquier propiedad del objeto. Se ejecuta al asignar la propiedad que define el setter.
*/

let objeto5 = {
    nombre: "objeto 3",
    edad: 30,
    apellido: "apellido 3",
    idioma: "español",
    arreglo: [7, 8, 9],
    get NombreCompleto() {
        return this.nombre + " " + this.apellido;
    },
    set NombreCompleto(nuevoNombreCompleto) {
        let partes = nuevoNombreCompleto.split(" ");
        this.nombre = partes[0];
        this.apellido = partes[1];
    }

};

console.log(objeto5.NombreCompleto)
objeto5.NombreCompleto = "Nuevo Nombre Nuevo Apellido"; // Asigna un nuevo nombre completo
console.log(objeto5.nombre)
console.log(objeto5.apellido)


// METODO CONSTRUCTOR, es una funcion especial que se utiliza para crear e inicializar objetos. En el caso de JavaScript, se define una función que actúa como plantilla para crear objetos. Esta función se llama con la palabra clave new, lo que crea una nueva instancia del objeto. Los métodos y propiedades se definen dentro de la función constructora y se asignan al objeto usando this. Un constructor es una función especial que se usa para crear objetos con ciertas propiedades iniciales. En JavaScript, antes de ES6 se usaban funciones constructoras, y desde ES6 se usan clases, pero aún podemos hablar de objetos literales con funciones constructoras .Cada vez que llamas al constructor con new, se crea un nuevo objeto independiente. Dentro del constructor, this se refiere al objeto que se está creando.

function Objeto5(nombre, edad, apellido) {
    this.nombre = nombre; //this indica q estamos trabajando con una propiedad del objeto, generalmente el nombre del  atributo es igual al nombre del parámetro
    this.edad = edad;
    this.apellido = apellido;
    this.arreglo = [7, 8, 9];
}

objetoPrueba = new Objeto5("objeto 5", 30, "apellido 3"); // Crea una nueva instancia de Objeto5
console.log(objetoPrueba.nombre); // "objeto 5"
// Al crear una funcion que contenga this, se vuelve un constructor



// AGREGAR METODOS A UN CONSTRUCTOR: Cuando añadimos métodos a un constructor, estamos definiendo funciones que pueden ser utilizadas por las instancias de ese objeto. Pues si se hace desde cada instancia solo sera para ella
function Objeto7(nombre, edad, apellido) {
    this.nombre = nombre; //this indica q estamos trabajando con una propiedad del objeto, generalmente el nombre del  atributo es igual al nombre del parámetro
    this.edad = edad;
    this.apellido = apellido;
    this.arreglo = [7, 8, 9];
    this.NombreCompleto = function() { //Al hacer esto, estamos definiendo un método, sin embargo, este método se crea para cada instancia de Objeto7 por lo que cada objeto tendrá su propia copia de la función. 
        return this.nombre + " " + this.apellido;
    };
}

// DISTINTAS FORMAS DE CREAR OBJETOS
let varMioB = new Object() //Forma 1
let varMioC = {} //Forma 2 , mas corta y recomendable
let miCadena1 = new String("Hola") //Forma 1 para string
let miCadena2 = "Hola" //Forma 2 para string, mas corta y recomendable
let miNumero1 = new Number(10) //Forma 1 para number
let miNumero2 = 10 //Forma 2 para number, mas corta y recomendable
let miBolean= new Boolean(true) //Forma 1 para boolean
let miBolean2 = true //Forma 2 para boolean, mas corta y recomendable
let miArreglo1 = new Array(1, 2, 3) //Forma 1 para array
let miArreglo2 = [1, 2, 3] //Forma 2 para array, mas corta y recomendable
let funcion1 = new Function("a", "b", "return a + b") //Forma 1 para function
let funcion2 = function(a, b) {
    return a + b;
}; //Forma 2 para function, mas corta y recomendable

// USO DE PROTOTYPE, permite metodos y propiedades compartidas entre todas las instancias de un objeto. En lugar de definir métodos y propiedades dentro del constructor, se pueden agregar al prototype del constructor. Esto ahorra memoria, ya que todas las instancias comparten el mismo método en lugar de tener su propia copia.
Objeto7.prototype.saludar = function() {
    console.log("Hola, soy " + this.nombre);
};

Objeto7.prototype.saludo = "adios"

//No se puede asignar métodos al prototipo directamente dentro del cuerpo de la función constructora. El prototipo pertenece a la función constructora (no a la instancia), así que siempre se modifica fuera del constructor.

// PROPIEDADES CALCULADAS Y CONTROLADAS SET Y GET
//Se pueden añadir propiedades calculadas o controladas usando Object.defineProperty, siendo la sintaxis Object.defineProperty(objeto, "nombrePropiedad", { get: function() {...}, set: function(valor) {...} }); en el caso de estar en el constructor se usa this para referenciar a dicho objeto, si es afuera se usa el nombre del objeto
//Dentro del constructor
function Persona(nombre, apellido) {
    this.nombre = nombre;
    this.apellido = apellido;

    Object.defineProperty(this, "nombreCompleto", {
        get: function() {
            return `${this.nombre} ${this.apellido}`;
        },
        set: function(valor) {
            const partes = valor.split(" ");
            this.nombre = partes[0];
            this.apellido = partes[1];
        }
    });
}
//Fuera del constructor
Object.defineProperty(Persona.prototype, "saludo", {
    get: function() {
        return `Hola, soy ${this.nombre} ${this.apellido}`;
    }
});

// USO DE CALL, el metodo call permite invocar una funcion desde otro objeto, su sintaxis es funcion.call(objeto, arg1, arg2, ...);
let persona1 = {
    nombre: "Juan",
    apellido: "Pérez",
    NombreCompleto: function(xd) {
        return `${this.nombre} ${this.apellido} ${xd}`;
    }
}

let persona2 = {
    nombre: "Ana",
    apellido: "Gómez",
};

console.log(persona1.NombreCompleto.call(persona2, "XD")); // "Ana Gómez XD"
//practicamente se cambia el objeto sobre el que se llama la funcion siendo que para hacer uso de call si requerimos ciertos parametros necesitamos que existan sino el valor sera undefined


//Metodo apply, actua de manera similar a call, pero en lugar de pasar los argumentos de forma individual, se pasan como un array., su sintaxis es funcion.apply(thisArg, [argsArray])
console.log(persona1.NombreCompleto.apply(persona2, ["XD"])); // "Ana Gómez XD"


// METODOS TIPOS OBJETCT
/*
Object.create()	Crea un nuevo objeto utilizando un objeto existente como prototipo.
Object.assign()	Copia todas las propiedades enumerables de uno o más objetos a un objeto destino.
Object.fromEntries()	Crea un nuevo objeto a partir de una lista de pares clave-valor.
*/

// Objeto create
const proto = { greet: function() { return "Hello"; } };
const obj = Object.create(proto);
console.log(obj.greet()); // "Hello"

const target = { a: 1 };
const source = { b: 2, c: 3 };
const result = Object.assign(target, source);
console.log(result); // { a: 1, b: 2, c: 3 }

const entries = [['name', 'Alice'], ['age', 30]];
const obj1 = Object.fromEntries(entries);
console.log(obj1); // { name: 'Alice', age: 30 }


//ITERACION EN OBJETOS
/*
Object.keys()	Devuelve un array con los nombres de las propiedades
Object.values()	Devuelve un array con los valores de las propiedades
Object.entries()	Devuelve un array de pares [clave, valor] de las propiedades enumerables de un objeto
*/

const obj2 = { a: 1, b: 2, c: 3 };
const keys = Object.keys(obj2);
console.log(keys); // ["a", "b", "c"]
const obj3 = { a: 1, b: 2, c: 3 };
const values = Object.values(obj3);
console.log(values); // [1, 2, 3]

const obj4 = { a: 1, b: 2, c: 3 };
const entradas = Object.entries(obj4);
console.log(entradas); // [["a", 1], ["b", 2], ["c", 3]]

// ACCESO A PROPIEDADES
/*Object.hasOwnProperty()	Devuelve un booleano que indica si el objeto tiene la propiedad como propia.
Object.hasOwn()	Similar a hasOwnProperty pero más moderno.
Object.getOwnPropertyNames()	Devuelve un array con los nombres de todas las propiedades de un objeto.
Object.getOwnPropertyDescriptor()	Devuelve el descriptor de una propiedad específica de un objeto.
*/

const obj6 = { a: 1 };
console.log(obj6.hasOwnProperty('a')); // true
console.log(obj6.hasOwnProperty('b')); // false

const obj7 = { a: 1, b: 2, c: 3 };
const propNames = Object.getOwnPropertyNames(obj7);
console.log(propNames); // ["a", "b", "c"]

const obj8 = { a: 1 };
const descriptor = Object.getOwnPropertyDescriptor(obj8, 'a');
console.log(descriptor);
// { value: 1, writable: true, enumerable: true, configurable: true }
/*
writable: Si es true, el valor puede cambiarse; si es false, no se puede modificar.
enumerable: Si es true, la propiedad aparece en bucles como for...in y en Object.keys(). Si es false, no aparece.
configurable: Si es true, la propiedad puede eliminarse o cambiar su descriptor. Si es false, no se puede borrar ni modificar el descriptor.
*/


// MANIPULACION DE PROPIEDADES
/*
Object.defineProperty()	Define o modifica una propiedad de un objeto
Object.defineProperties()	Define o modifica múltiples propiedades de un objeto.
*/

const obj9 = {};
Object.defineProperty(obj9, 'name', { value: 'Alice', writable: false });
console.log(obj9.name); // "Alice"
obj9.name = 'Bob'; // No cambia porque writable es false
console.log(obj9.name); // "Alice"

const obj10 = {};
Object.defineProperties(obj10, {
    name: { value: 'Alice', writable: true },
    age: { value: 30, writable: false }
});
console.log(obj10.name); // "Alice"
console.log(obj10.age); // 30


// SELLADO, CONGELACION Y EXTENSIBILIDAD
/*
Object.seal()	Previene la adición y eliminación de propiedades en un objeto, pero permite la modificación de propiedades existentes.
Object.freeze()	Previene la adición, eliminación y modificación de propiedades en un objeto.
Object.preventExtensions()	Previene la adición de nuevas propiedades a un objeto.
*/

const obj14 = { a: 1 };
Object.freeze(obj14);
obj14.a = 2; // No se puede modificar, se ignora en modo estricto.
obj14.b = 2; // No se puede añadir, se ignora en modo estricto.
console.log(obj14); // { a: 1 }

const obj15 = { a: 1 };
Object.seal(obj15);
obj15.b = 2; // No se puede añadir, se ignora en modo estricto.
delete obj15.a; // No se puede eliminar, se ignora en modo estricto.
console.log(obj15); // { a: 1 }

const obj16 = { a: 1 };
Object.preventExtensions(obj16);
obj16.b = 2; // No se puede añadir, se ignora en modo estricto.
console.log(obj16); // { a: 1 }

// COMPARACION Y VERIFICACION
/*
Object.is()	Determina si dos valores se consideran el mismo valor. más preciso que === para NaN y +0 vs -0
Object.isExtensible()	Determina si un objeto puede tener nuevas propiedades añadidas. 
Object.isFrozen()	Determina si un objeto está congelado.  (no se pueden añadir, eliminar o modificar propiedades)
Object.isSealed()	Determina si un objeto está sellado.  (no se pueden añadir o eliminar propiedades, pero las existentes pueden modificarse)
*/

console.log(Object.is(NaN, NaN)); // true
console.log(Object.is(0, -0)); // false

const obj11q = {};
console.log(Object.isExtensible(obj11q)); // true
Object.preventExtensions(obj11q);
console.log(Object.isExtensible(obj11q)); // false

const obj12 = { a: 1 };
console.log(Object.isSealed(obj12)); // false
Object.seal(obj12);
console.log(Object.isSealed(obj12));// true

const obj13 = { a: 1 };
console.log(Object.isFrozen(obj13)); // false
Object.freeze(obj13);
console.log(Object.isFrozen(obj13)); // true

// DESTRUCTURACION: La desestructuración de objetos es una característica de JavaScript que permite extraer propiedades de un objeto y asignarlas a variables de forma individual. La desestructuración de objetos utiliza llaves ({}) para extraer las propiedades del objeto y asignarlas a variables. La clave de cada propiedad debe coincidir con el nombre de la variable. La sintaxis básica es la siguiente: let o const { propiedad, propiedad2, ... } = objeto;

const producto = { nombre: "Ordenador", precio: 1000 };
const { nombre, precio } = producto;

console.log(nombre); // "Ordenador"
console.log(precio); // 1000

//Si necesitas usar un nombre de variable distinto al de la propiedad, puedes renombrarlas al momento de la desestructuración.
const producto1 = { nombre: "Ordenador", precio: 1000 };
const { nombre: nombreProducto, precio: costo } = producto1;

console.log(nombreProducto); // "Ordenador"
console.log(costo); // 1000

//También podemos asignar valores predeterminados a los valores. Si la propiedad no existe en el objeto, se usará el valor por defecto.
const producto3 = { nombre: "Ordenador" };
const { nombre1, precio2 = 500 } = producto3;

console.log(nombre1); // "Ordenador"
console.log(precio2); // 500

//Objetos anidados Cuando las propiedades están anidadas dentro de objetos, puedes desestructurarlas de manera jerárquica.
const usuario = {
  id: 1,
  perfil: { nombrePersona: "Ana", edadPersona: 30 },
};

const {
  perfil: { nombrePersona, edadPersona },
} = usuario;

console.log(nombrePersona); // "Ana"
console.log(edadPersona); // 30

//Uso en funciones: La desestructuración también se puede aplicar directamente en los parámetros de las funciones.

function mostrarInfoUsuario({ perfil: { nombrePersona, edadPersona } }) {
  console.log(nombrePersona);
  console.log(edadPersona);
}

mostrarInfoUsuario(usuario);

// CLONAR OBJETOS: Clonar un objeto implica crear una copia independiente que pueda modificarse sin afectar al objeto original. Esto es especialmente importante porque en JavaScript todos objetos son tipos de referencia. Es decir, que cuando asignas un objeto a una nueva variable, ambas variables apuntan al mismo objeto en memoria. Si modificas una, la otra también se verá afectada

const original = { nombre: "Juan", edad: 25 };
const copia = { ...original }; // MANTIENE LA REFERENCIA

copia.nombre = "María";
console.log(original.nombre); // "María" (el objeto original también cambió)

//La clonación superficial (shallow copy) crea una nueva instancia de un objeto y copia las propiedades de nivel superior. Sin embargo, si alguna de estas propiedades es un objeto en sí, solo se copiará la referencia.  Las propiedades primitivas (números, strings, booleanos, null, undefined, symbol, bigint) se copian por valor. Las propiedades que son objetos o arreglos se copian por referencia, no por valor. Esto significa que la copia y el original siguen compartiendo las mismas subestructuras internas. Si modificas esas subestructuras en la copia, también se modifican en el original.
/*
Operador de propagación	Superficial	❌	❌	Baja: El operador de propagación (...) es una forma moderna y concisa de clonar un objeto. Este método crea una copia superficial del objeto, lo que significa que copia las propiedades de nivel superior, pero no los objetos o arrays anidados. 
Object.assign()	Superficial	❌	❌	Baja: Object.assign() es otra forma de realizar una clonación superficial. Este método copia las propiedades propias de un objeto (no las heredadas) al objeto de destino.
*/

const original1 = { nombre: "Juan", edad: 25, arreglo: [1, 2, 3] };
const clon1 = { ...original1 };

clon1.arreglo[0] = 4;
console.log(original1.arreglo); // [4, 2, 3] (el original también cambió)

clon1.edad = 30;
console.log(original1.edad); // 25 (el original no cambió)

// Clonacion profunda (deep copy) crea una copia completa de un objeto, incluyendo todos los objetos anidados.Esto asegura que las modificaciones en la copia no afecten al objeto original (es la clonación “de verdad”). Aqui si haces un cambio en el clon no se hace en el original

/*
structuredClone()	Profunda	✅	✅	Baja: A partir de ES2021, JavaScript introdujo el método structuredClone, que permite realizar clonaciones profundas de manera nativa.
JSON.parse(JSON.stringify)	Profunda	✅	❌	Media: Una técnica sencilla para clonar objetos que no contienen métodos ni valores no serializables (como funciones, undefined, o propiedades circulares) es usar JSON.stringify() y JSON.parse().
_.cloneDeep() (Lodash)	Profunda	✅	✅	Media
Clonación manual	Depende	✅	Depende	Alta: Cuando necesitas una solución robusta para clonar objetos complejos, puedes usar bibliotecas como Lodash. El método cloneDeep de Lodash realiza una clonación profunda completa.
*/

const original2 = { nombre: "Juan", detalles: { edad: 25, ciudad: "Madrid" } };
const clon2 = structuredClone(original2);

clon2.detalles.ciudad = "Barcelona";
console.log(original2.detalles.ciudad); //Madrid"

const original4 = { nombre: "Juan", detalles: { edad: 25, ciudad: "Madrid" } };
const clon4 = JSON.parse(JSON.stringify(original4));

clon4.detalles.ciudad = "Barcelona";
console.log(original4.detalles.ciudad); // "Madrid"

import _ from "lodash";

const original5 = { nombre: "Juan", detalles: { edad: 25, ciudad: "Madrid" } };
const clon5 = _.cloneDeep(original5);

clon5.detalles.ciudad = "Barcelona";
console.log(original5.detalles.ciudad); // "Madrid"


// PROTOTIPOS
/*
JavaScript es un lenguaje orientado a objetos basado en prototipos, lo que significa que la herencia y la reutilización de código se gestionan a través de un sistema de prototipos. El prototipo permite a los objetos heredar propiedades y métodos de otros objetos. Este mecanismo de herencia se denomina herencia prototípica. Esto es permite que los objetos compartan métodos y propiedades, lo cual optimiza el uso de memoria.

El prototipo es simplemente un objeto que todos los objetos tienen como propiedad interna, y al que pueden acceder.

Todos los objetos en JavaScript tienen la propiedad [[Prototype]], que a su vez es una referencia a otro objeto “padre”.
Esta secuencia de objetos conectados por prototipos se denomina cadena de prototipos.
Cuando intentas acceder a una propiedad o método que no existe en el objeto, JavaScript buscará si existe en el prototipo del objeto.

1. Creacion de objetos y prototipos
Cuando creas un objeto usando una notación literal, JavaScript asigna automáticamente Object.prototype como el prototipo del nuevo objeto.
*/

const persona5 = {
  nombre: "Carlos",
  edad: 30
};

console.log(persona5.__proto__ === Object.prototype); // true

//También podemos crear un nuevo objeto con un prototipo específico usando Object.create(proto):
const animal = {
  hacerSonido() {
    console.log("Sonido");
  }
};

const perro = Object.create(animal);
perro.hacerSonido(); // "Sonido"

//Cuando usamos una función constructora con el operador new, se crea un nuevo objeto que hereda del prototype de esa función constructora.
function Persona(nombre, edad) {
  this.nombre = nombre;
  this.edad = edad;
}

Persona.prototype.saludar = function() {
  console.log(`¡Hola, mi nombre es ${this.nombre} y tengo ${this.edad} años!`);
};

// Creamos una nueva instancia de Persona
let persona6 = new Persona("Luis", 30);

// Llamamos al método `saludar` desde el prototipo
persona6.saludar();  // Salida: ¡Hola, mi nombre es Luis y tengo 30 años!

// PROPIEDAD PROTO: Generalmente el prototipo de un objeto está disponible de forma pública a través de la propiedad __proto__.El acceso directo a la propiedad __proto__ no está recomendado. En lugar de __proto__, es preferible utilizar los métodos estáticos proporcionados por el objeto Object

// Object.getPrototypeOf(obj): Obtiene el prototipo del objeto 
// Object.setPrototypeOf(obj, nuevoProto): Establece el prototipo del objeto
console.log(Object.getPrototypeOf(persona6) === Persona.prototype); // true

const nuevoProto = { nuevaPropiedad: "valor" };
Object.setPrototypeOf(persona6, nuevoProto);
console.log(persona6.nuevaPropiedad); // "valor"


//Podemos añadir métodos a un prototipo después de que se han creado instancias, lo que es útil para ampliar funcionalidades. Con la sintaxis objeto.prototype.metodo = function() { ... }
Persona.prototype.aniversario = function() {
    this.edad++;
    console.log(`Felicidades ${this.nombre}, ahora tienes ${this.edad} años.`);
};

persona6.aniversario(); // Salida: "Felicidades Luis, ahora tienes 31 años."

//Herencia prototípica en JavaScript: La herencia prototípica es lo que permite que un objeto herede las propiedades y métodos de otro objeto. Esta característica es el núcleo del sistema de herencia de JavaScript.

// Creamos un objeto base: Animal
let Animal = {
  saludar: function() {
    console.log(`Hola, soy un ${this.tipo}`);
  }
};

// Creamos un nuevo objeto que hereda de Animal
let Perro = Object.create(Animal);

// Definimos propiedades específicas para Perro
Perro.tipo = "perro";
Perro.ladrar = function() {
  console.log("¡Guau!");
};

// Usamos el objeto Perro
Perro.saludar(); // "Hola, soy un perro"
Perro.ladrar();  // "¡Guau!"

//Perro va a hereder de animal mediante el prototipo