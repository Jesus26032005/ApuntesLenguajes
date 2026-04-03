export interface Hero {
    id: number;
    name: string;
    owner: Owner;
}

// Type: Son estructuras que permiten definir un conjunto de valores posibles para una variable. Se usan cuando 
// se desea restringir el valor de una variable a un conjunto específico de opciones.
// Enumeraciones: Son una forma de definir un conjunto de constantes con nombre, lo que facilita la lectura
// y el mantenimiento del código. Se usan cuando se tiene un conjunto fijo de valores relacionados.

// Ejemplo usando type
// type Owner = 'DC' | 'Marvel';
// Ejemplo usando enumeraciones
export enum Owner {
    DC = 'DC',
    MARVEL = 'Marvel',
}


export const heroes: Hero[] = [
    {
    id: 1,
    name: 'Batman',
    owner: Owner.DC,
    },
    {
    id: 2,
    name: 'Spiderman',
    owner: Owner.MARVEL,
    },
    {
    id: 3,
    name: 'Superman',
    owner: Owner.DC,
    },
    {
    id: 4,
    name: 'Flash',
    owner: Owner.DC,
    },
    {
    id: 5,
    name: 'Wolverine',
    owner: Owner.MARVEL,
    },
];
console.log(heroes);