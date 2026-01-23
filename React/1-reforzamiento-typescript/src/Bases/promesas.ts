// PROMESAS
/*
En JavaScript las Promesas son un mecanismo fundamental para facilitar la programación asíncrona.
Nos permiten gestionar operaciones que no se completan inmediatamente (como solicitudes de red, 
operaciones de lectura de archivos o temporizadores) de una manera más estructurada y menos propensa a 
errores en comparación con los callbacks.
Una promesa es como un “contenedor” para un valor que puede estar disponible ahora, en el futuro,
o nunca (por eso se llama promesa)

Una promesa es un objeto que representa el posible éxito o fallo de una operación asíncrona.
Para reflejar esto, durante su ejecución la promesa tiene una propiedad Estado, que puede ser uno de los siguientes:
    Pendiente (Pending): Estado inicial. La operación asíncrona aún no se ha completado.
    Cumplida (Fulfilled): La operación se ha completado con éxito y la promesa tiene un valor resultante.
    Rechazada (Rejected): La operación falló y la promesa tiene un motivo de error.
*/

// Podemos crear una promesa utilizando el constructor Promise. Este constructor toma una función (llamada executor) 
//  que recibe dos funciones como argumentos:
// resolve se llama si la operación es exitosa, y se cambia el estado de la promesa a cumplida.
// reject se llama si hay un error, y se cambia el estado a rechazada.
// Estos argumentos son funciones que se llaman para cambiar el estado de la promesa. Vamos a verlo con un ejemplo,


// La sintaxis básica para crear una promesa es la siguiente:
/*
new Promise((resolve, reject) => {
    Aquí iría la lógica de la operación asíncrona
});
En este ejemplo, la función pasada al constructor Promise contiene la lógica de la operación asíncrona.
Dependiendo del resultado de esa operación, se llamaría a resolve() si fue exitosa o a reject() si hubo un error.
*/

const miPromesa = new Promise((resolve, reject) => {
    const exito = true; // Simulamos el resultado de una operación asíncrona
    setTimeout(() => {
        if (exito) {
            resolve("Operación exitosa");
        } else {
            reject("Error en la operación");
        }
    }, 2000);
})

// MANEJO DE PROMESAS: Para manejar el resultado de una promesa, normalmente utilizamos los métodos .then() y .catch():

// metodo then: Este método se llama cuando la promesa se cumple o se rechaza. Recibe el valor resultante de la promesa 
// si se cumple , es decir recibe el valor de resolve, su sintaxis es miPromesa.then(onFulfilled, onRejected) donde 
// onFulfilled es una función que se ejecuta cuando la promesa se cumple y recibe el valor de resolve, y 
// onRejected es una función que se ejecuta cuando la promesa se rechaza y recibe el valor de reject.

// metodo catch: Este método se utiliza para manejar errores en la promesa. SEste método se utiliza para manejar
// errores. Es un atajo para .then(null, onRejected) y se llama cuando la promesa es rechazada comunmente por errores 
// en la operación asíncrona. Recibe el valor enviado por reject

// metodo finally: Este método se llama cuando la promesa se ha cumplido o rechazado, independientemente del resultado.
// Se utiliza para ejecutar código de limpieza o acciones que deben realizarse después de que la promesa se haya resuelto,
// sin importar si fue exitosa o no.

miPromesa
    .then((valor) => {
        console.log(valor); 
    })
    .catch((error) => {
        console.error(error);
    })
    .finally(() => {
        console.log("Operación finalizada");
    });


// Debido a que el valor de respuesta en then y catch puede ser de cualquier tipo, podemos tipar las promesas en TypeScript
// especificando el tipo de dato que esperamos recibir cuando la promesa se cumpla. Esto se hace utilizando genéricos.
// esto se realiza despues del new Promise<tipoDeDato>

const promesaTipada = new Promise<string>((resolve, reject) => {
    const exito = true; // Simulamos el resultado de una operación asíncrona
    setTimeout(() => {
        if (exito) {
            resolve("Operación exitosa");
        } else {
            reject("Error en la operación");
        }
    }, 2000);
})

promesaTipada
    .then((valor) => {
        console.log(valor.toUpperCase()); 
    })
    .catch((error) => {
        console.error(error);
    });

// ENCADENAMIENTO DE PROMESAS: Podemos encadenar múltiples operaciones asíncronas utilizando promesas.
// Cada llamada a .then() devuelve una nueva promesa, lo que permite encadenar varias operaciones de manera secuencial.

const promesaEncadenada = new Promise<number>((resolve, reject) => {
    setTimeout(() => {
        resolve(10);

        reject("Error en la operación");
    }, 2000);
})
promesaEncadenada
    .then((valor) => {
        console.log("Primer valor:", valor);
        return valor * 2;// El valor retornado se pasa al siguiente then y asi sucesivamente
    })
    .then((valor) => {
        console.log("Segundo valor:", valor);
        return valor + 5;
    })
    .then((valor) => {
        console.log("Tercer valor:", valor);
    })

// PROMESAS ANIDADAS: A veces, una operación asíncrona puede depender del resultado de otra operación asíncrona.
// En estos casos, podemos anidar promesas dentro de otras promesas.
const promesaAnidada = new Promise<number>((resolve, reject) => {
    setTimeout(() => {
        resolve(5);
        reject("Error en la operación");
    }, 2000);
})
promesaAnidada
    .then((valor) => {
        console.log("Valor inicial:", valor);
        return new Promise<number>((resolveAnidada, rejectAnidada) => {
            setTimeout(() => {
                resolveAnidada(valor * 2);
                rejectAnidada("Error en la promesa anidada");
            }, 2000);
        });
    })
    .then((valorAnidado) => { // El valor de la promesa anidada se maneja aquí
        console.log("Valor anidado:", valorAnidado);
    })
    .catch((error) => {
        console.error("Error en la promesa anidada:", error);
    });

// METODOS ESTATICOS DE PROMESAS:JavaScript proporciona varios métodos estáticos en el objeto 
// Promise para manejar múltiples promesas simultáneamente. Estos métodos devuelven una nueva promesa, 
// que es una composición de las promesas que le pasamos como argumentos.
// Promise.all(): Promise.all() recibe un iterable de promesas y devuelve una nueva promesa que se 
// resuelve cuando todas las promesas del iterable se cumplen. Si alguna promesa es rechazada, la promesa devuelta será rechazada inmediatamente.
const promesa1 = Promise.resolve(1); //Promise.resolve es un método estático que crea una promesa ya 
// resuelta (cumplida) con el valor que le pases.
const promesa2 = Promise.resolve(2);
const promesa3 = Promise.resolve(3);

Promise.all([promesa1, promesa2, promesa3])
.then(results => {
    console.log(results); // [1, 2, 3]
    })
    .catch(error => {
    console.error(error);
    });

// Promise.race(): Promise.race() devuelve una promesa que se resuelve o se rechaza tan pronto como una de 
// las promesas en el iterable se resuelve o se rechaza.
const promesaLenta = new Promise(resolve => setTimeout(() => resolve('Lenta'), 2000));
const promesaRápida = new Promise(resolve => setTimeout(() => resolve('Rápida'), 1000));

Promise.race([promesaLenta, promesaRápida])
    .then(result => {
    console.log(result); // 'Rápida'
    });

//Promise.allSettled(): Promise.allSettled() devuelve una promesa que se resuelve cuando todas
//  las promesas del iterable han terminado (ya sea que se hayan cumplido o rechazado) y 
// devuelve un array con los resultados de todas las promesas.
const promesa11 = Promise.resolve(1);
const promesa22 = Promise.reject('Error');
const promesa33 = Promise.resolve(3);

Promise.allSettled([promesa11, promesa22, promesa33])
    .then(results => {
    console.log(results);
    // [{status: 'fulfilled', value: 1}, {status: 'rejected', reason: 'Error'}, {status: 'fulfilled', value: 3}]
    });


//Promise.any(): Promise.any() devuelve una promesa que se resuelve tan pronto como una de las 
// promesas en el iterable se resuelve.
const promesa111 = Promise.reject('Error 1');
const promesa222 = Promise.reject('Error 2');
const promesa333 = Promise.resolve('Éxito');

Promise.any([promesa111, promesa222, promesa333])
    .then(result => {
    console.log(result); // 'Éxito'
    });