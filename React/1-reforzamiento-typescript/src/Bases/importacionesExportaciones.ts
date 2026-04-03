import { heroes ,  type Hero, Owner } from "../data/interfacesEnumeraciones";

// Cuando se importan interfaces o tipos se debe utilizar la palabra reservada type, asi se indica que solo se 
// esta importando un tipo de dato, no una variable o funcion. Otra opcion es activar verbalTypeImports en tsconfig.json
// como true para que no sea necesario usar la palabra reservada type al importar tipos o interfaces



// Para poder exportar algun elemento se utiliza la palabra reservada export antes de la declaracion
// export const heroes = [ ... ]
// Para importar algun elemento exportado se utiliza la palabra reservada import seguida del nombre del elemento y la ruta del archivo
// import { heroes } from "../data/interfacesEnumeraciones";

// Si queremos colocar un alias al elemento importado se utiliza la palabra reservada as
// import { heroes as misHeroes } from "../data/interfacesEnumeraciones";

// Se conoce como exportacion por defecto cuando un archivo solo exporta un elemento
// export default function getHeroeById( id: number ) { ... }
// Para importar un elemento exportado por defecto no se utilizan las llaves {}
// import getHeroeById from "../data/funciones";
// y se le puede colocar cualquier nombre al elemento importado pues solo este se esta importado

const getHeroeById = (id: number): Hero | undefined => {
    const heroe = heroes.find( heroe => heroe.id === id );
    return heroe;
}

const getHeroeByOwner = ( owner: Owner ): Hero[] => {
    return heroes.filter( heroe => heroe.owner === owner );
}

console.log(getHeroeByOwner(Owner.DC));
console.log(getHeroeById(2));

// Nota: Si se desea importar todo el contenido de un archivo se puede utilizar el siguiente formato
// import * as InterfaceEnumeraciones from "../data/interfacesEnumeraciones";