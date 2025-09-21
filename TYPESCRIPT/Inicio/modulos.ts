// Un módulo en TypeScript es un archivo que contiene código y puede exportar a otros ficheros partes de ese código para que sean utilizadas en otros archivos.

// Esto nos permite dividir nuestro código en módulos más pequeños y mantener una estructura organizada y modular en nuestro proyecto.

// Creación de un módulo en TypeScript
// Para crear un módulo en TypeScript, simplemente debemos utilizar la palabra clave export antes de la declaración de una clase, función, constante o variable que deseamos hacer accesible desde otros archivos. Veamos un ejemplo:

// export function sum(a: number, b: number): number {
//   return a + b;
// }
// export const PI = 3.1416;
// export default class Person {
//   constructor(public name: string) {}
// }
// En el ejemplo anterior,
// Creamos un módulo llamado utils.ts
// Este exporta una clase Person por defecto
// Exporta una función sum y una constante Pi con nombre.
// Estas funcionalidades ahora pueden ser importadas y utilizadas en otros archivos TypeScript.

// Exportación del módulo
// Exportación por defecto
// Podemos exportar una única entidad por defecto desde un módulo utilizando la palabra clave export default. Esto nos permite importar esa entidad sin necesidad de usar llaves de desestructuración.
// export default class MiClase {
// }
// Para importar la entidad exportada por defecto, simplemente utilizamos el nombre que queremos asignarle en nuestra importación.
// import MiClase from './ruta/al/modulo';

// También podemos exportar varias entidades desde un módulo utilizando la palabra clave export seguida del nombre de la entidad que queremos exportar.
// export class Clase1 {
// }
// export interface Interfaz1 {
// }

// Es posible utilizar un alias para la exportación de una entidad utilizando la palabra clave as seguida del nombre del alias.
// export { nombreEntidad as alias } from './ruta/al/modulo';

// Importación de módulos
// La importación de módulos nos permite utilizar el código exportado desde otro archivo en nuestro propio archivo.
// Para importar un módulo en TypeScript, utilizamos la palabra clave import seguida del nombre del módulo que queremos importar.
// import { nombreModulo } from './ruta/al/modulo';

// Para utilizar los elementos exportados desde un módulo en otro archivo TypeScript, debemos importarlos. La sintaxis para importar un módulo es la siguiente:
// import Person from './utils';
// En el ejemplo anterior, estamos importando la clase Person utilizando la sintaxis de importación por defecto}

// Si necesitamos importar más de un elemento podemos usar la sintaxis de llaves de desestructuración en nuestra importación.

// import { Clase1, Interfaz1 } from './ruta/al/modulo';
// Por ejemplo

// import { sum, PI } from './utils';