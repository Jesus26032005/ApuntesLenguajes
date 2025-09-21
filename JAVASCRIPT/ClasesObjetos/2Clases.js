// CLASES
// Las clases son plantillas para crear objetos. Definen propiedades y métodos que los objetos creados a partir de la clase tendrán. En JavaScript, las clases se introdujeron en ECMAScript 2015 (ES6) y son una forma más clara y concisa de crear objetos y manejar la herencia. La sintaxis es la siguiente: class NombreClase { constructor(parametros) { ... } } 
/*
Una importante diferencia entre las declaraciones de funciones y las declaraciones de clases es que las declaraciones de funciones son alojadas y las declaraciones de clases no lo son. En primer lugar necesitas declarar tu clase y luego acceder a ella, de otro modo el ejemplo de código siguiente arrojará un ReferenceError
*/

class Persona {
    _nombre
    _edad
    _apellido
    //dentro de la clase no es obligatorio si ya lo defines en el constructor, pero puede servir para declarar la propiedad explícitamente (buena práctica en código moderno, sobre todo con TypeScript o para mayor claridad).
    // generalmente tambien se colocan dichos atributos en caso de que no se neceiten inicializar, o en caso contrario podemos coolocarles valores por defecto.
    email = "ejemplo@dominio.com"; // Valor por defecto

    constructor(nombre, edad, apellido) { //Parametros para inicializar el objeto (opcionales, pero es generalmente asi)
        this._nombre = nombre; // Inicializar propiedad "nombre"
        this._edad = edad;     // Inicializar propiedad "edad"
        this.apellido= apellido
    }

    //Metodos get y set, se acostumbra a colocar los nombres de propiedades con un guion bajo al inicio para la creacion de metodos get y set al declararse estos como atributos privados, sin embargo, no es necesario declararlos asi pues en automatico ya tienen sus metodos getter y setter, al declararse privados se les puede acceder solo dentro de la clase. Es una forma vieja de encapsulamiento y se sigue usando al usar guion bajo, sin embargo ya existe otra forma de encapsulamiento mejorada. Mientras tanto se podria decir que getter y setter ademas de obtener atributos privados actuan como funciones para propiedades calculadas.
    // Un getter (get) en una clase es un método especial que se ejecuta cuando accedemos a una propiedad como si fuera un valor. Un setter (set) es un método que se ejecuta cuando asignamos un valor a una propiedad.
    // Aunque comunmente tambien se pueden usar todavia para crear propiedades calculadas y modificar las propiedades al modificar dichas propiedades calculadas pues como vimos anteriormente.

    get nombre() {
        return this._nombre;
    }

    set nombre(nuevoNombre) {
        this._nombre = nuevoNombre;
    }

    get edad() {
        return this._edad;
    }

    set edad(nuevaEdad) {
        this._edad = nuevaEdad;
    }

    get nombreEdad() {
        return `${this._nombre} tiene ${this._edad} años.`;
    }

    set nombreEdad(nuevoNombreEdad) {
        let [nombre, edad] = nuevoNombreEdad.split(" tiene ");
        this._nombre = nombre;
        this._edad = parseInt(edad);
    }
}

//Crear instancia
let persona1 = new Persona("Juan", 30, "Pérez");
// Imprimir todo el objeto
console.log(persona1);
console.log(persona1.nombre); // Juan
console.log(persona1.edad);   // 30
console.log(persona1.apellido); // Pérez
persona1.nombre = "Ana"; // Cambiar nombre
persona1.edad = 25;      // Cambiar edad
console.log(persona1.nombreEdad);
persona1.nombreEdad = "Luis tiene 40"; // Cambiar nombre y edad usando el setter
console.log(persona1.nombre); // Luis
console.log(persona1.edad);   // 40


/* NOTAS:
En JavaScript, un campo es una propiedad que pertenece a una instancia de la clase.
Campo público → accesible desde cualquier lugar.
Campo privado → solo accesible dentro de la propia clase.
2️⃣ Campos públicos
Son los más comunes.
Se pueden leer, modificar y borrar desde cualquier parte del código.
Por defecto, cualquier propiedad definida con this.propiedad es pública
Campos privados reales (#)
Introducidos en ES2022.
Solo accesibles desde dentro de la clase.
No se pueden leer, modificar ni borrar desde fuera.
Empiezan con # y deben declararse al inicio de la clase.
*/

/* ATRIBUTOS PRIVADOS
En JavaScript ES2022 introdujo la sintaxis de campos privados. Para ello se antepone el nombre de la propiedad con el prefijo #.
Las propiedades que utilizan este prefijo son accesibles solo dentro de la clase en la que están definidas (no pueden ser accedidas ni modificadas desde fuera de la clase).
*/

class Persona1 {
    #nombre;

    constructor(nombre) {
        this.#nombre = nombre;
    }

    obtenerNombre() {
        return this.#nombre;
    }
}
const persona1PRUEBA = new Persona1("Juan");
// Acceso correcto a través de un método público
console.log(persona1PRUEBA.obtenerNombre()); // "Juan"
// Esto causará un error: "Cannot read private member"
//console.log(persona1PRUEBA.#nombre); // Error


//Los métodos también pueden ser privados. Al igual que las propiedades, se definen con el prefijo #:
class Usuario {
    #claveSecreta;

    constructor(clave) {
        this.#claveSecreta = clave;
    }

    #mostrarClave() {
        console.log(`La clave secreta es: ${this.#claveSecreta}`);
    }

    autenticar() {
        this.#mostrarClave(); // Llamada válida desde dentro de la clase
    }
}
const usuario1 = new Usuario("12345");
usuario1.autenticar(); // La clave secreta es: 12345
// Esto causará un error: "Cannot read private member"
// usuario1.#mostrarClave(); // Error


//La encapsulación encaja muy bien con el uso de métodos getter y setter.
class PersonaDos {
    #edad;

    constructor(edad) {
        this.#edad = edad;
    }

    get edad() {
        return this.#edad;
    }

    set edad(nuevaEdad) {
        if (nuevaEdad > 0) {
            this.#edad = nuevaEdad;
        } else {
            console.log("La edad debe ser positiva.");
        }
    }
}
const persona2 = new PersonaDos(25);
console.log(persona2.edad); // 25
persona2.edad = 30;         // Modifica la edad
console.log(persona2.edad); // 30
persona2.edad = -5;         // La edad debe ser positiva.
/*
AQUI los metodos: un método getter es una función especial que permite acceder a una propiedad de un objeto. Si empleamos la palabra get antes de un método, estamos indicando que queremos que esta sea un getter. Ahora puedes obtener el valor de una función get como si fuera una variable, pero internamente estás ejecutando un método cada vez que obtienes el valor.
En cambio un setter un método setter es una función especial que permite asignar una propiedad de un objeto.
La principal ventaja de los métodos set es que te permiten validar y modificar los valores antes de que sean asignados a las propiedades.
*/


// VARIABLES Y METODOS ESTATICOS
// Variables estáticas:En JavaScript, las variables estáticas se definen utilizando la palabra clave static, que indica que esa propiedad pertenece a la propia clase. Es decir se podran acceder desde  cualquier instancia de la clase, sin que sea necesario crear una instancia de la clase. Se accede a ellas utilizando el nombre de la clase seguido del operador de acceso a propiedades (.) y el nombre de la propiedad estática. Su valor cambia para todas las instancias de la clase. Es ddecir es de uso compartido las variables estáticas.  

class Contador {
    static contador = 0;

    constructor() {
        Contador.contador++;
    }
}

const c1 = new Contador();
const c2 = new Contador();
const c3 = new Contador();

console.log(Contador.contador); // Muestra 3

//METODOS ESTATICOS: De igual forma, método estático es un método que pertenece a la clase en lugar de a una instancia de la clase. Esto quiere decir que puedes invocar el método directamente en la clase sin necesidad de crear un objeto.Mientras que los metodos estaticos son funciones que pertenecen a la clase en sí misma y no a las instancias individuales de la clase. Se definen utilizando la palabra clave static dentro de la definición de la clase. Los métodos estáticos se llaman directamente en la clase sin necesidad de crear una instancia de la clase. Se accede a ellos utilizando el nombre de la clase seguido del operador de acceso a propiedades (.) y el nombre del método estático. Al igual que las variables, los métodos estáticos también se definen utilizando la palabra clave static.

class Matematica {
    static sumar(a, b) {
        return a + b;
    }

    static restar(a, b) {
        return a - b;
    }
}

console.log(Matematica.sumar(5, 3));  // Muestra 8
console.log(Matematica.restar(5, 3)); // Muestra 2

// HERENCIA: Se hereda a partir de una clase padre. La herencia es una característica que permite crear nuevas clases basadas en clases existentes. Con la herencia, una clase puede disponer de las propiedades y métodos de otra, a la vez que añade o sobreescribe, con sus propios métodos. Esta relación entre clases se conoce como relación padre-hijo o superclase-subclase.
//En JavaScript para crear una subclase que herede de la clase base, usamos la palabra clave extends. En primer lugar necesitamos definir una clase base, y a continuación crearíamos la clase derivada. 

class figura {
    constructor(area, perimetro) {
        this.area = area;
        this.perimetro = perimetro;
    }

    decirhola() {
        console.log("Hola desde la clase figura");
    }
}

class cuadrado extends figura {
    constructor(lado) {
        super(lado * lado, 4 * lado); //Llama al constructor de la clase base figura
        this.lado = lado;
    }

    decirhola() {
        super.decirhola(); // Llama al método de la clase base
        console.log("Hola desde la clase cuadrado");
    }
}
//nota: si tenemos atributos en la clase padre y creamos subclase, se requiere que se llame explícitamente al constructor de la clase padre utilizando super().

// CONSTANTES ESTATICAS: Las constantes estáticas son propiedades que pertenecen a la clase en sí misma, en lugar de a instancias individuales de la clase. Se definen utilizando la palabra clave static y se accede a ellas utilizando el nombre de la clase seguido del operador de acceso a propiedades (.) y el nombre de la constante estática.

class Matematica {
    static PI = 3.14159;
    static areaCirculo(radio) {
        return Matematica.PI * radio * radio;
    }
}

console.log(Matematica.PI); // Muestra 3.14159
console.log(Matematica.areaCirculo(5)); // Muestra 78.53975

// OTRA FORMA ES USANDO UNA funcion get estatica, con nombre de constante en mayusculas y el cuerpo dela clase retornara el valor estatico

class MatematicaDos {
    static get PI() {
        return 3.14159;
    }

    static areaCirculo(radio) {
        return MatematicaDos.PI * radio * radio;
    }
}

console.log(MatematicaDos.PI); // Muestra 3.14159
console.log(MatematicaDos.areaCirculo(5)); // Muestra 78.53975

//SUPER: La palabra clave super() nos permite obtener una referencia a la clase base, desde la clase derivada. Por ejemplo, sirve para, Llamar al constructor de la superclase: Cuando necesitamos inicializar las propiedades heredadas desde la clase base. Acceder a los métodos de la superclase: Para hacer uso de métodos de la superclase dentro de la subclase.

//Cuando una subclase hereda de una superclase, hereda sus propiedades y métodos. Esto significa que podemos acceder a las propiedades y métodos de la superclase como si estuvieran definidos directamente en la subclase.
class Animal {
  constructor(nombre) {
    this.nombre = nombre;
  }

  hablar() {
    console.log(`${this.nombre} hace un sonido`);
  }
}

class Gato extends Animal {
}

const miGato = new Gato('Whiskers'); // Crea una instancia de Gato donde como no hay constructor definido, se utiliza el de la clase base Animal
miGato.hablar(); // "Whiskers hace un sonido"

//SOBREESCRITURA METODOS: Una característica de la herencia es que podemos sobrescribir los métodos de la clase base en la subclase. Esto nos permite personalizar el comportamiento. Esto es útil cuando queremos que las subclases tengan comportamientos específicos, mientras conservamos la base de la clase original.

class GatoDos extends Animal {
  hablar() {
    console.log(`${this.nombre} dice ¡Miau!`);
  }
}

const miGato1 = new GatoDos('Rufus el gato');
miGato1.hablar(); // "Rufus el gato dice ¡Miau!"


// PROPIEDADES ESTATICAS Y HERENCIA, Las subclases también heredan las propiedades estáticas. La clase base y la clase derivada comparten las variables y métodos estáticos (la clase derivada no tiene sus propias versiones) Para acceder a ellas en la clase, solamente se coloca el nombre de la clase seguido de un punto y el nombre de la propiedad estática.  
class AnimalDos {
  static especie = 'Animal'; // Propiedad estática

  static hablar() {
    console.log(AnimalDos.especie); // Acceso a la propiedad estática
  }
  //... más cosas
}

class PerroDos extends AnimalDos {}

console.log(PerroDos.especie); // "Animal"
AnimalDos.hablar();

PerroDos.especie = "Perraco";
console.log(AnimalDos.especie); // "Perraco"
console.log(PerroDos.especie); // "Perraco"

// POLIMORFISMO: En otras palabras, el polimorfismo permite que los objetos de diferentes clases tengan diferentes comportamientos para el mismo método. En JavaScript, el polimorfismo se puede lograr utilizando la herencia y la sobrescritura de métodos. Vamos a verlo con un ejemplo:
class mamifero {
    hablar() {
        console.log("El mamífero hace un sonido");
    }
}

class PerroTres extends mamifero {
    hablar() {
        console.log("El perro ladra");
    }
}

class GatoTres extends mamifero {
    hablar() {
        console.log("El gato maulla");
    }
}

const miPerroTres = new PerroTres();
const miGatoTres = new GatoTres();

miPerroTres.hablar(); // "El perro ladra"
miGatoTres.hablar(); // "El gato maulla"


// ENCAPSULACION: a encapsulación es un concepto que proviene de la programación orientada a objetos (POO) que consiste en ocultar y proteger los detalles internos de una clase

//n JavaScript ES2022 introdujo la sintaxis de campos privados. Para ello se antepone el nombre de la propiedad con el prefijo #. Las propiedades que utilizan este prefijo son accesibles solo dentro de la clase en la que están definidas (no pueden ser accedidas ni modificadas desde fuera de la clase).
class PersonaTres {
    #nombre;

    constructor(nombre) {
        this.#nombre = nombre;
    }

    obtenerNombre() {
        return this.#nombre;
    }
}

const personatresPrueba = new PersonaTres("Juan");
// Acceso correcto a través de un método público
console.log(personatresPrueba.obtenerNombre()); // "Juan"

// Esto causará un error: "Cannot read private member"
//console.log(personatresPrueba.#nombre); // Error

//Los métodos también pueden ser privados. Al igual que las propiedades, se definen con el prefijo #:
class UsuarioPrivado {
    #claveSecreta;

    constructor(clave) {
        this.#claveSecreta = clave;
    }

    #mostrarClave() {
        console.log(`La clave secreta es: ${this.#claveSecreta}`);
    }

    autenticar() {
        this.#mostrarClave(); // Llamada válida desde dentro de la clase
    }
}

const usuarioXD = new UsuarioPrivado("12345");
usuarioXD.autenticar(); // La clave secreta es: 12345
// Esto causará un error: "Cannot read private member"
// usuarioXD.#mostrarClave(); // Error

// METODOS GETTER Y SETTER SEGUNDA PARTE ,La encapsulación encaja muy bien con el uso de métodos getter y setter.
class PersonaCuatro {
    #edad;

    constructor(edad) {
        this.#edad = edad;
    }

    get edad() {
        return this.#edad;
    }

    set edad(nuevaEdad) {
        if (nuevaEdad > 0) {
            this.#edad = nuevaEdad;
        } else {
            console.log("La edad debe ser positiva.");
        }
    }
}

const personaCuatroPrueba = new PersonaCuatro(25);
console.log(personaCuatroPrueba.edad); // 25
personaCuatroPrueba.edad = 30;         // Modifica la edad
console.log(personaCuatroPrueba.edad); // 30
personaCuatroPrueba.edad = -5;         // La edad debe ser positiva.


// CLASE OBJECTO, METOTO TO STRING
// Todas las clases en JavaScript heredan de Object , siendo que se heredan sus métodos como toString() que es aquel que se llama cuando se intenta convertir un objeto a una cadena o se imprime.

class PersonaCinco {
    constructor(nombre, edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    toString() {
        return `Nombre: ${this.nombre}, Edad: ${this.edad}`;
    }
}

const persona3 = new PersonaCinco("Carlos", 28);
console.log(persona3.toString()); // "Nombre: Carlos, Edad: 28"


//SINTAXIS FINAL DE CREACION DE CLASE
// =====================================================
//  Clase con propiedades públicas, privadas y estáticas
// =====================================================

class PersonaFinal {
  // --- 1. Propiedad pública --------------------------
  nombre = "Sin nombre"; // accesible desde fuera de la clase con valor por defaut
  email = "ejemplo@dominio.com"; // valor por defecto, se puede colocar en caso de no querer inicializarlo

  // --- 2. Propiedad privada --------------------------
  #edad = 0; // accesible SOLO dentro de la clase

  // --- 3. Propiedad estática -------------------------
  static especie = "Humano"; // pertenece a la clase, no a las instancias

  constructor(nombre, edad) {
    this.nombre = nombre; // inicializa propiedad pública
    this.#edad = edad;    // inicializa propiedad privada
  }

  // Método público
  saludar() {
    console.log(`Hola, me llamo ${this.nombre} y tengo ${this.#edad} años.`);
  }

  // Método para modificar la edad (getter/setter manual)
  cumplirAnios() {
    this.#edad++;
    console.log(`${this.nombre} ahora tiene ${this.#edad} años.`);
  }

  // Método estático (se usa con el nombre de la clase)
  static queSoy() {
    console.log(`Soy de la especie ${Persona.especie}`);
  }
}

// ===== Ejemplo de uso =====
const p1 = new PersonaFinal("Juan", 25);

// Propiedad pública -> se puede acceder y modificar
console.log(p1.nombre); // Juan
p1.nombre = "Pedro";
console.log(p1.nombre); // Pedro

// Propiedad privada -> ❌ error si intentas acceder fuera
// console.log(p1.#edad); // SyntaxError

// Usar métodos para interactuar con propiedades privadas
p1.saludar();       // Hola, me llamo Pedro y tengo 25 años.
p1.cumplirAnios();  // Pedro ahora tiene 26 años.

// Propiedad estática -> se accede desde la clase, no desde el objeto
console.log(PersonaFinal.especie); // Humano
PersonaFinal.queSoy(); // Soy de la especie Humano


// METODOS GENERICOS: En JavaScript, los métodos genéricos son funciones que pueden trabajar con diferentes tipos de datos o estructuras, sin estar ligados a un tipo específico. No existen "métodos genéricos" como en TypeScript o Java, pero puedes crear funciones que aceptan cualquier tipo de argumento y funcionan para distintos casos.

function mostrarElemento(elemento) {
  console.log(elemento);
}

mostrarElemento(5);           // número
mostrarElemento("hola");      // cadena
mostrarElemento([1, 2, 3]);   // arreglo
mostrarElemento({a: 1});      // objeto


// PALABRA INSTANCEOF, la palabra instanceof nos permite verificar si un objeto es una instancia de una clase específica. Su uso es el siguiente:
// Devuelve true o false, true cuando es de la instancia e incluso con clases padre.
const p2 = new PersonaFinal("Ana", 30);
console.log(p2 instanceof PersonaFinal); // true porque p2 es una instancia de PersonaFinal
console.log(p2 instanceof Object);       // true porque todas las clases en JavaScript heredan de Object