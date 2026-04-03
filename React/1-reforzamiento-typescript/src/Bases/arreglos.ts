// Los arreglos en TypeScript pueden definirse de varias maneras, aquí hay algunas formas comunes:
// Son una colección de elementos del mismo tipo.
// Sin embargo, también pueden contener elementos de diferentes tipos si se usa 'any'.
// En ts no es recomendable usar 'any' ya que pierde la ventaja del tipado fuerte.

// 1. Usando corchetes [], donde se coloca el tipo de dato seguido de los corchetes
let numeros: number[] = [1, 2, 3, 4, 5];
console.log(numeros);
// 2. Usando la sintaxis Array<tipo> para definir un arreglo de cadenas
let frutas: Array<string> = ['manzana', 'banana', 'cereza'];
console.log(frutas);
// 4. Arreglo de cualquier tipo (no recomendado, pero posible)
let mixto: any[] = [1, 'dos', true, { clave: 'valor' }];
console.log(mixto);
// 5. Arreglo multidimensional
let matriz: number[][] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9] 
];
console.log(matriz);
// 6. Tipos de datos especificos en arreglos, se usan los literales
let numerosYStrings: (number | string)[] = [1, 'dos', 3, 'cuatro'];
console.log(numerosYStrings);

// Los arreglos son mutables, lo que significa que puedes agregar, eliminar o modificar elementos después de su creación.
numeros.push(6);
console.log(numeros);
numeros.pop();
console.log(numeros);

// Al igual que los objetos, los arreglos se pueden colocar como constantes usando 'const', pues esto no impide modificar su contenido,
//  solo evita que se reasigne la variable a un nuevo arreglo, se almacena en memoria la referencia al arreglo.
const colores: string[] = ['rojo', 'verde', 'azul'];
colores.push('amarillo');
console.log(colores);

// Copiar arreglos
const copiaColores: string[] = [...colores]; // se puede usar el operador spread
console.log(copiaColores);
const copiaProfundaColores : string[] = structuredClone(colores); // se puede usar structuredClone
console.log(copiaProfundaColores);


// DESESTRUCTURACIÓN DE ARREGLOS
// La desestructuración de arreglos permite extraer valores de un arreglo y asignarlos a variables individuales de manera concisa.
// Aqui el orden importa
const numerosDesestructuradosOriginal: number[] = [10, 20, 30, 40, 50];
// La sintaxis es: const [var1, var2, ...resto] = arreglo;
// A diferencia de los objetos que usa llaves {}, los arreglos usan corchetes []
const [primero, segundo, tercero, ...resto] = numerosDesestructuradosOriginal;
console.log(primero);
console.log(segundo);
console.log(tercero);
console.log(resto);

// Se pueden obtener solo algunos valores y omitir otros usando comas
const [primeroSolo, , terceroSolo] = numerosDesestructuradosOriginal;
console.log(primeroSolo);
console.log(terceroSolo);

// Se puede obtener solo algunso
const [primeroUnico] = numerosDesestructuradosOriginal;
console.log(primeroUnico);

// Ejemplo
const retornarArreglo = ():number[] => {
    return [1, 2, 3, 4, 5];
}
const [a, b, c] = retornarArreglo();
console.log(a);
console.log(b);
console.log(c);


// TAREA
/* Debe retornar un arreglo con dos elementos:
#1 - Un string (el valor inicial).
#2 - Una función anónima de flecha que:
Recibe un string.
Imprime ese string en consola.*/

function useState(nombre: String) {
    return [nombre, (nombre: string) => console.log(nombre)] as const
}
const [nombre, setNombre] = useState('Goku');
console.log(nombre);
setNombre('Vegeta');