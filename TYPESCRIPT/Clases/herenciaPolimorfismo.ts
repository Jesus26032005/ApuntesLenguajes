// HERENCIA
//La HERENCIA es un mecanismo que nos permite definir una nueva clase basada en una clase existente. La clase existente se conoce como la clase base o superclase, y la nueva clase se conoce como la clase derivada o subclase. La subclase hereda las propiedades y métodos de la superclase, y puede agregar sus propias propiedades y métodos o sobrescribir los existentes.

// En TypeScript, podemos usar la palabra clave extends para crear una subclase que herede de una superclase.
class Animal {
    nombre: string;
    edad: number;

    constructor(nombre: string, edad: number) {
        this.nombre = nombre;
        this.edad = edad;
    }

    hacerSonido(): void {
        console.log(`${this.nombre} hace un sonido.`);
    }
}

class Perro extends Animal {
    raza: string;
    constructor(nombre: string, edad: number, raza: string) {
        // Cuando tu clase hereda de otra, tienes que llamar a super() antes de usar this, porque this no existe hasta que el constructor padre se ejecute.
        super(nombre, edad); // Llamada al constructor de la superclase
        this.raza = raza;
    }

    // Puedes llamar métodos de la clase padre dentro de métodos, usando super.metodo()
    llamarHacerSonido(): void {
        super.hacerSonido(); // Llamada al método de la superclase
    }
}

// SOBREESCRITURA DE MÉTODOS
// La sobreescritura de métodos es una característica de la programación orientada a objetos que permite a una subclase proporcionar una implementación específica de un método que ya está definido en su superclase. Cuando se llama al método en una instancia de la subclase, se ejecuta la versión sobrescrita del método en lugar de la versión de la superclase.
class Gato extends Animal {
    color: string;
    constructor(nombre: string, edad: number, color: string) {
        super(nombre, edad);
        this.color = color;
    }

    hacerSonido(): void {  // Sobrescritura del método de la superclase
        console.log(`${this.nombre} hace el sonido de un gato.`);
    }
}

// POLIMORFISMO
//El POLIMORFISMO es otro concepto clave en la programación orientada a objetos. Nos permite tratar objetos de diferentes clases de manera uniforme, siempre y cuando compartan una interfaz o superclase común. En Typescript, podemos lograr el polimorfismo utilizando interfaces.
interface Volador {
    volar(): void;
}

class Pajaro implements Volador {
    nombre: string;
    constructor(nombre: string) {
        this.nombre = nombre;
    }

    volar(): void {
        console.log(`${this.nombre} está volando.`);
    }
}

class Avion implements Volador {
    modelo: string;
    constructor(modelo: string) {
        this.modelo = modelo;
    }

    volar(): void {
        console.log(`${this.modelo} está volando.`);
    }
}

// Tambien se puede lograr polimorfismo con clases y herencia
class acuatico {
    nadar(): void {
        console.log(`El animal acuático está nadando.`);
    }
}

class Delfin extends acuatico {
    nombre: string;
    constructor(nombre: string) {
        super();
        this.nombre = nombre;
    }

    nadar(): void {
        console.log(`${this.nombre} está nadando.`);
    }
}

class Tiburon extends acuatico {
    especie: string;
    constructor(especie: string) {
        super();
        this.especie = especie;
    }

    nadar(): void {
        console.log(`El tiburón ${this.especie} está nadando.`);
    }
}