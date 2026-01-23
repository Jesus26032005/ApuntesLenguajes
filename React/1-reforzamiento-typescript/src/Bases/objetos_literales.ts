// Los objetos literales son una forma de agrupar datos relacionados en una sola estructura. Son una representación común de 
// datos en JavaScript y TypeScript.

// Definición de un objeto literal
/* const objetoNombre: { propiedad1: tipo1, 
                        propiedad2: tipo2, } = {
*/
const userProfile = {
    nombre: "Juan",
    edad: 30
}
// Aunque este definida como constante, los valores internos pueden cambiar, pues se esta apuntando en realidad
// a una referencia en memoria de la persona.
userProfile.edad = 31; // Modificando una propiedad del objeto
console.log(userProfile);

// Si asignamos el objeto a otra variable, ambas apuntan a la misma referencia en memoria, es decir , no es una copia, sino
// una referencia al mismo objeto.
const otroPerfil = userProfile;
otroPerfil.nombre = "Pedro";
console.log(userProfile); 

// Para realizar una copia real del objeto, se puede usar el operador spread (...)
const copiaPerfil = { ...userProfile }; // Se dice que tome todas las propiedades de userProfile y crea un nuevo objeto
// esto rompe la referencia de primer nivel, pero si el objeto tiene propiedades que son a su vez objetos, esas
//  si mantienen la referencia, por tanto no es una copia profunda.
console.log(copiaPerfil);

// Para realizar una copia profunda se usa structuredClone(objeto), donde las referencias internas tambien se rompen.
const copiaProfunda = structuredClone(userProfile);
console.log(copiaProfunda);
// otra forma de hacer copia profunda es usando JSON, sin embargo, no es recomendable para objetos que contienen metodos y/o
// valores serializables como funciones, undefined, entre otros.
const copiaProfundaJSON = JSON.parse(JSON.stringify(userProfile));
console.log(copiaProfundaJSON);

// DESESTRUCTURACIÓN DE OBJETOS
// La desestructuración es una característica de JavaScript y TypeScript que permite extraer valores de objetos o arreglos
// y asignarlos a variables de manera más concisa.
const producto = {
    id: 1,
    nombre: "Laptop",
    precio: 1500
};

// La forma tradicional de extraer valores de un objeto sería:
// const idProducto = producto.id;
// const nombreProducto = producto.nombre;
// const precioProducto = producto.precio;
// console.log(idProducto, nombreProducto, precioProducto);

// Con desestructuración, podemos extraer los valores de manera más concisa:
// No importa el orden de las propiedades al desestructurar
// Solo se colocan las llaves {} y dentro los nombres de las propiedades que queremos extraer
const { id, nombre, precio } = producto
console.log(id, nombre, precio);
// Se pueden usar alias para las variables extraídas
// const { id: identificador, nombre: nombreProducto, precio: costo } = producto
//  Busca la propiedad 'n', pero entrégamela en una variable llamada..
const { id: identificador, nombre: nombreProducto} = producto;
console.log(identificador, nombreProducto);

// Se puede aplicar la desestructuración en los parámetros de una función
interface Usuario {
    nombre: string;
    edad: number;
}
const mostrarUsuario = ({ nombre }: Usuario): void => {
    console.log(`Nombre: ${nombre}`);
}
const Ana = {
    nombre: "Ana",
    edad: 25
}
mostrarUsuario(Ana);

// Nota adicional si se quiere crear una propiedad con el mismo nombre que una variable ya existente en el scope, se puede usar la sintaxis:
interface Alumno {
    nombre: string;
    edad: number;
    boleta : {
        id: number;
        carrera: string;
    }
}
const crearObjeto = (nombre: string, edad: number): Alumno => {
    return {
        nombre,
        edad,   
        boleta: {
            id: 0,
            carrera: "Desconocida"
    }
    }
}
console.log(crearObjeto("Carlos", 20));

// Si el objeto tiene propiedades anidadas, se puede desestructurar de la siguiente manera:
// la sintaxis es { propiedadPadre: { propiedadHijo } }
const estudiante: Alumno = {
    nombre: "Luis",
    edad: 22,
    boleta: {
        id: 12345,
        carrera: "Ingeniería en Sistemas"
    }
}
const { boleta: {carrera} } = estudiante;
console.log(`Carrera extraída: ${carrera}`);

// Sintaxis: ({ propiedadPadre: { propiedadHijo } }: Tipo)
const obtenerCarrera = ({boleta: { carrera } }: Alumno): void => {
    // Aquí 'boleta' NO existe, solo existe 'carrera'
    console.log(`Carrera: ${carrera}`); 
}
obtenerCarrera(estudiante);

// Para obtener una propiedad y las otras en una variable aparte, se usa el operador rest (...)
const { nombre: nombreEstudiante, ...resto } = estudiante;
console.log(nombreEstudiante);
console.log(resto); // Resto contiene las demás propiedades del objeto estudiante

// NO CONFUNDIR LO SIGUIENTE:
// : seguido de texto = es para definir el tipo o alias de la variable
// :{segundoTexto} = es para desestructurar un objeto anidado
// ...resto = es para obtener el resto de las propiedades en un nuevo objeto
// = valorPorDefecto  es para asignar un valor por defecto en caso de que la propiedad no exista

// Ejemplo de valor por defecto al desestructurar
interface Libro {
    titulo: string;
    autor: string;
    año: number;
    editorial?: string;
}
const libro: Libro = {
    titulo: "El Quijote",
    autor: "Miguel de Cervantes",
    año: 1605,
};
const { titulo, editorial = "Desconocida" } = libro;
console.log(titulo, editorial);

// Desestructuracion de alto tipado
// Se usa la siguiente sintaxis const { propiedad }: { propiedad: tipo } = objeto;, generalmente no se usa
const { año }: { año: number } = libro;
console.log(año);