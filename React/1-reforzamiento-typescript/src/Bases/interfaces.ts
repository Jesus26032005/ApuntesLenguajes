// Las Interface son una herramienta fundamental en la programación orientada a objetos, ya que nos permiten 
// definir la estructura y el comportamiento de un objeto. Una interfaz en TypeScript nos permite definir la 
// estructura de un objeto, especificando los nombres y los tipos de sus propiedades y métodos. Obligando con ello
// a que cualquier objeto que implemente esa interfaz cumpla con esa estructura definida.
// Posteriormente, las clases pueden implementar este interface (en este caso, deben definir todas las variables
// y métodos que incluya el interfaz).

//Para declarar una interfaz en Typescript, utilizamos la palabra clave interface seguida del nombre de la interfaz y las propiedades y métodos que queremos definir.
interface Persona { // Generalmente se usa la primera letra mayuscula para nombrar interfaces y camelCase para las propiedades
    nombre: string
    edad: number
}
// Crear un objeto que implemente la interfaz Persona
const persona1: Persona = {
    nombre: "Ana",
    edad: 25 // si cambiaramos el tipo de dato o eliminamos alguna propiedad, TS nos marcara un error
};
console.log(persona1);

// METODOS EN INTERFACES
// Se pueden añadir la especificación de métodos en las interfaces, siendo que establece la firma del método 
// (nombre, parámetros y tipo de retorno)
interface Calculadora {
    sumar(a: number, b: number): number; // Definición del método sumar
    restar(a: number, b: number): number; // Definición del método restar
}
// Crear un objeto que implemente la interfaz Calculadora
const miCalculadora: Calculadora = {
    sumar(a: number, b: number): number {
        return a + b;
    },
    restar(a: number, b: number): number {
        return a - b;
    }
};
console.log(miCalculadora.sumar(5, 3));

// PROPIEDADES-METODOS OPCIONALES
// Podemos definir propiedades o métodos opcionales en una interfaz utilizando el símbolo "?" después del nombre de la propiedad o método.
interface Vehiculo {
    marca: string;
    modelo: string;
    anio?: number; // Propiedad opcional
    arrancar?(): void; // Método opcional
}
const miVehiculo: Vehiculo = {
    marca: "Toyota",
    modelo: "Corolla"
    // anio y arrancar son opcionales por tanto no me mandara error si no los incluyo
};
console.log(miVehiculo);


// INTERFACES EN INTERFACES
// Una interfaz puede contener otras interfaces, permitiendo crear estructuras de datos más complejas y reutilizables, 
// siendo que generalmente se crean las dos de manera separada y se hace referencia a la interfaz interna desde la externa.
interface Animal {
    nombre: string;
    edad: number;
}
interface Mascota {
    tipo: string;
    animal: Animal; 
}
const miMascota: Mascota = {
    tipo: "Perro",
    animal: {
        nombre: "Fido",
        edad: 3
    }
};
console.log(miMascota);