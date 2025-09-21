//TypeScript admite funciones anónimas y funciones de flecha, que son formas más concisas de escribir funciones.
//Las funciones anónimas son funciones sin nombre, comúnmente utilizadas como argumentos de otras funciones.

//Las funciones de flecha (arrow functions) son una sintaxis más corta para escribir funciones anónimas y tienen un comportamiento diferente con respecto al contexto de this. Ademas de que no tienen su propio this, arguments, super o new.target. Estas funciones son mejor para funciones que no son métodos y no se utilizan como constructores.

//Funciones anónimas: Las funciones anónimas son funciones sin nombre, comúnmente utilizadas como argumentos de otras funciones.
const saludar = function(nombre: string): void {
    console.log(`Hola ${nombre}.`);
};

// Función de flecha: Sintaxis más corta y sin su propio this. Las funciones arrow son una sintaxis compacta de definir funciones en JavaScript y TypeScript. Se caracterizan por usar la sintaxis => y tienen varias ventajas sobre las funciones tradicionales, especialmente en términos de manejo de this. Las funciones arrow permiten escribir funciones de manera más concisa y legible, especialmente cuando se trata de funciones cortas o funciones de una sola línea.
const despedir = (nombre: string): void => { console.log(`Adiós ${nombre}.`);}
    // Si la función tiene una sola expresión, se pueden omitir las llaves y el return implícito.
    // const despedir = (nombre: string): void => console.log(`Adiós ${nombre}.`);
    // Si la función tiene un solo parámetro, se pueden omitir los paréntesis.
    // const despedir = nombre: string => console.log(`Adiós ${nombre}.`);
    // Si la función no tiene parámetros, se deben usar paréntesis vacíos.
    // const despedir = (): void => console.log(`Adiós.`);
    // Si la función tiene múltiples parámetros, se deben usar paréntesis.
    // const despedir = (nombre: string, apellido: string): void => console.log(`Adiós ${nombre} ${apellido}.`);
    // Si la función tiene un cuerpo más complejo, se deben usar llaves y return explícito.
    // const despedir = (nombre: string): string => { 
    //     const mensaje = `Adiós ${nombre}.`;
    //     return mensaje;
    // };

    