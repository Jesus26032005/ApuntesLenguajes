// Las clases son una forma de definir objetos con métodos y propiedades. Permiten crear instancias de objetos y heredar propiedades y métodos de otras clases. Las clases en TypeScript proporcionan una manera estructurada para definir objetos con propiedades y métodos asociados. Las clases son fundamentales en la programación orientada a objetos, ya que nos permiten definir objetos que encapsulan datos y comportamientos relacionados.

//Se usa la siguiente sintaxis para definir una clase en TypeScript:
class Persona {
    // Propiedades de la clase
    nombre: string;
    edad: number;
    // Constructor de la clase: El constructor es un método especial que se invoca automáticamente al crear una nueva instancia de una clase. Su propósito principal es inicializar las propiedades del objeto con los valores proporcionados durante la instanciación.
    constructor(nombre: string, edad: number) {
        this.nombre = nombre;
        this.edad = edad;
    }
    // Método de la clase
    saludar(): string {
        return `Hola, mi nombre es ${this.nombre} y tengo ${this.edad} años.`;
    }
}

let persona1 = new Persona("Juan", 30);
console.log(persona1.saludar()); 

// MODIFICADORES DE ACCESO
// Los modificadores de acceso controlan la visibilidad de las propiedades y métodos de una clase. Los modificadores comunes son:
// public: Accesible desde cualquier lugar (por defecto).
// private: Accesible solo dentro de la clase.
// protected: Accesible dentro de la clase y sus subclases.
class Vehiculo {
    public marca: string;
    private modelo: string;
    protected color: string;

    constructor(marca: string, modelo: string, color: string) {
        this.marca = marca;
        this.modelo = modelo;
        this.color = color;
    }
}

let vehiculo1 = new Vehiculo("Toyota", "Corolla", "Rojo");
console.log(vehiculo1.marca); // Accesible
// console.log(vehiculo1.modelo); // Error: 'modelo' es privado
// console.log(vehiculo1.color); // Error: 'color' es protegido



// Forma simplificada de definir una clase con propiedades y constructor en TypeScript, su sintaxis es más concisa y directa. Se utiliza el modificador de acceso (public, private, protected) directamente en los parámetros del constructor para definir y inicializar las propiedades de la clase en una sola línea. Siendo la sitnaxis la siguiente: constructor(public propiedad1: tipo1, private propiedad2: tipo2) {}
class Animal {
    constructor(public especie: string, public edad: number) {}

    describir(): string {
        return `Este animal es un ${this.especie} y tiene ${this.edad} años.`;
    }
}
let animal1 = new Animal("Perro", 5);
console.log(animal1.describir());