/*
Las Interface son una herramienta fundamental en la programación orientada a objetos, ya que nos permiten definir la estructura y el comportamiento de un objeto.

Una interfaz en TypeScript nos permite definir la estructura de un objeto, especificando los nombres y los tipos de sus propiedades y métodos.

Posteriormente, las clases pueden implementar este interface (en este caso, deben definir todas las variables y métodos que incluya el interfaz).
*/

//Para declarar una interfaz en Typescript, utilizamos la palabra clave interface seguida del nombre de la interfaz y las propiedades y métodos que queremos definir.
interface Persona {
    nombre: string;
    edad: number;
    saludar(): void;
}

//Una vez creada una interfaz para utilizarla en una clase, utilizamos la palabra reservada implements seguida del nombre de la interfaz.
class Estudiante implements Persona {
    nombre: string;
    edad: number;
    grado: string;
    //Si faltara alguna propiedad o método, TypeScript nos mostrará un error indicándonos que la clase no cumple con la interfaz.

    constructor(nombre: string, edad: number, grado: string) {
        this.nombre = nombre;
        this.edad = edad;
        this.grado = grado;
    }

    saludar(): void {
        console.log(`Hola, soy ${this.nombre} y tengo ${this.edad} años.`);
    }
}
//Cabe mencionar que una clase puede implementar múltiples interfaces separándolas con comas.
interface Trabajador {
    empresa: string;
    puesto: string;
    trabajar(): void;
}
class Empleado implements Persona, Trabajador {
    nombre: string;
    edad: number;
    empresa: string;
    puesto: string;
    saludar(): void {
        console.log(`Hola, soy ${this.nombre} y tengo ${this.edad} años.`);
    }
    trabajar(): void {
        console.log(`Estoy trabajando en ${this.empresa} como ${this.puesto}.`);
    }
}

// también podemos definir propiedades opcionales en una interfaz utilizando el símbolo ? después del nombre de la propiedad.
interface Vehiculo {
    marca: string;
    modelo: string;
    color?: string;
}

class Coche implements Vehiculo {
    marca: string
    modelo: string
}

// Extension de interfaces: podemos crear una nueva interfaz que extienda de una interfaz existente.
interface VehiculoConRuedas extends Vehiculo {
    numeroDeRuedas: number;
}

class Bicicleta implements VehiculoConRuedas {
    marca: string;
    modelo: string;
    numeroDeRuedas: number; 

    constructor(marca: string, modelo: string, numeroDeRuedas: number) {
        this.marca = marca;
        this.modelo = modelo;
        this.numeroDeRuedas = numeroDeRuedas;
    }
}

// Propiudades de solo lectura: podemos definir propiedades de solo lectura en una interfaz utilizando la palabra clave readonly.
interface Punto {
    readonly x: number;
    readonly y: number;
}
let punto: Punto = { x: 10, y: 20 };
console.log(`Punto: (${punto.x}, ${punto.y})`);
// punto.x = 30; // Error: no se puede asignar a una propiedad de solo lectura