// PROMESAS
/*
En JavaScript las Promesas son un mecanismo fundamental para facilitar la programación asíncrona.
Nos permiten gestionar operaciones que no se completan inmediatamente (como solicitudes de red, operaciones de lectura de archivos o temporizadores) de una manera más estructurada y menos propensa a errores en comparación con los callbacks.
Una promesa es como un “contenedor” para un valor que puede estar disponible ahora, en el futuro, o nunca (por eso se llama promesa)

Una promesa es un objeto que representa el posible éxito o fallo de una operación asíncrona.
Para reflejar esto, durante su ejecución la promesa tiene una propiedad Estado, que puede ser uno de los siguientes:
    Pendiente (Pending): Estado inicial. La operación asíncrona aún no se ha completado.
    Cumplida (Fulfilled): La operación se ha completado con éxito y la promesa tiene un valor resultante.
    Rechazada (Rejected): La operación falló y la promesa tiene un motivo de error.
*/

// Podemos crear una promesa utilizando el constructor Promise. Este constructor toma una función (llamada executor) que recibe dos funciones como argumentos:
    // resolve se llama si la operación es exitosa, y se cambia el estado de la promesa a cumplida.
    // reject se llama si hay un error, y se cambia el estado a rechazada.
// Estos argumentos son funciones que se llaman para cambiar el estado de la promesa. Vamos a verlo con un ejemplo,

const miPromesa = new Promise((resolve, reject) => {
  // Simulación de una operación asíncrona
  let exito = true; // Simula el resultado de la operación

  if (exito) {
    resolve('Operación exitosa'); //Devuelve 'Operación exitosa' en caso de éxito y pasa el valor
  } else {
    reject('Error en la operación'); //Devuelve 'Error en la operación' en caso de fallo y para el error
  }
});

// MANEJO DE PROMESAS: Para manejar el resultado de una promesa, normalmente utilizamos los métodos .then() y .catch():
// metodo then: Este método se llama cuando la promesa se cumple o se rechaza. Recibe el valor resultante de la promesa si se cumple , es decir recibe el valor de resolve, su sintaxis es miPromesa.then(onFulfilled, onRejected) donde onFulfilled es una función que se ejecuta cuando la promesa se cumple y recibe el valor de resolve, y onRejected es una función que se ejecuta cuando la promesa se rechaza y recibe el valor de reject.

//metodo catch: Este método se utiliza para manejar errores en la promesa. SEste método se utiliza para manejar errores. Es un atajo para .then(null, onRejected) y se llama cuando la promesa es rechazada comunmente por errores en la operación asíncrona. Recibe el valor enviado por reject

//Ejemplo de una promesa normalmente
miPromesa
  .then(result => {
    console.log(result); // 'Operación exitosa'
  })
  .catch(error => {
    console.error(error); // 'Error en la operación'
  });


// ENCADENAMIENTO DE PROMESAS: Las promesas permiten encadenar múltiples .then() para manejar secuencias de operaciones asíncronas. Cada .then() devuelve una nueva promesa, lo que facilita la composición de tareas asíncrona
miPromesa
  .then(result => {
    console.log(result); // 'Operación exitosa'
    return 'Otro valor';
  })
  .then(otroResultado => {
    console.log(otroResultado); // 'Otro valor' //Obtiene el valor devuelto por el anterior .then()
  })
  .catch(error => {
    console.error(error);
  });

// PROMESAS ANIDADAS: También podríamos anidar promesas dentro de otras promesas para gestionar operaciones que dependen de resultados anteriores.
miPromesa 
  .then(result => {
    console.log(result); // 'Operación exitosa'
    return new Promise((resolve, reject) => {
      setTimeout(() => resolve('Operación asíncrona adicional'), 50);
    });
  })
  .then(adicional => {
    console.log(adicional); // 'Operación asíncrona adicional'
  })
  .catch(error => {
    console.error(error);
  });

/*CREAR PROMESAS: Para crear una promesa que reciba un valor. Creas una función que recibe los parámetros que quieras. Esa función devuelve una Promise. Dentro de la promesa pones la lógica que depende de esos parámetros y decides si llamas a resolve() (éxito) o reject() (error). Una sintaxis basica seria

function promesaPersonalizada(parametros) {
  return new Promise((resolve, reject) => {
    // Lógica que depende de los parámetros
    if (condición de éxito ) {
      resolve('Éxito');
    } else {
      reject('Error');
    }
  });
}

De la siguiente forma se puede ver:
*/

function promesaPersonalizada(valor){
  return new Promise((resolve, reject) => {
    if (valor) {
      resolve('Éxito');
    } else {
      reject('Error');
    }
  });
}

promesaPersonalizada(5) //Tiene estado pendiente
  .then(resultado => {  //Como se resuelve la promesa pasa a estado cumplido
    console.log(resultado); // 'Éxito'
  })
  .catch(error => { //Si manda un valor que no es verdadero, se rechaza la promesa y se pasa al estado rechazado
    console.error(error); // 'Error'
  });

// FUNCION setTimeout y promesas
let promesaConTimeout = new Promise((resolve, reject) => {
  console.log('Creando promesa...');
  setTimeout(() => {
    resolve('Operación completada');
  }, 1000);
  console.log('Promesa creada, esperando 1 segundo...'); // Esto se ejecuta inmediatamente
});

promesaConTimeout
  .then(resultado => {
    console.log(resultado); // 'Operación completada'
  })
  .catch(error => {
    console.error(error);
  });

// METODOS ESTATICOS DE PROMESAS:JavaScript proporciona varios métodos estáticos en el objeto Promise para manejar múltiples promesas simultáneamente. Estos métodos devuelven una nueva promesa, que es una composición de las promesas que le pasamos como argumentos.

// Promise.all(): Promise.all() recibe un iterable de promesas y devuelve una nueva promesa que se resuelve cuando todas las promesas del iterable se cumplen. Si alguna promesa es rechazada, la promesa devuelta será rechazada inmediatamente.
const promesa1 = Promise.resolve(1); //Promise.resolve es un método estático que crea una promesa ya resuelta (cumplida) con el valor que le pases.
const promesa2 = Promise.resolve(2);
const promesa3 = Promise.resolve(3);

Promise.all([promesa1, promesa2, promesa3])
  .then(results => {
    console.log(results); // [1, 2, 3]
  })
  .catch(error => {
    console.error(error);
  });

// Promise.race(): Promise.race() devuelve una promesa que se resuelve o se rechaza tan pronto como una de las promesas en el iterable se resuelve o se rechaza.
const promesaLenta = new Promise(resolve => setTimeout(() => resolve('Lenta'), 2000));
const promesaRápida = new Promise(resolve => setTimeout(() => resolve('Rápida'), 1000));

Promise.race([promesaLenta, promesaRápida])
  .then(result => {
    console.log(result); // 'Rápida'
  });

//Promise.allSettled(): Promise.allSettled() devuelve una promesa que se resuelve cuando todas las promesas del iterable han terminado (ya sea que se hayan cumplido o rechazado) y devuelve un array con los resultados de todas las promesas.
const promesa11 = Promise.resolve(1);
const promesa22 = Promise.reject('Error');
const promesa33 = Promise.resolve(3);

Promise.allSettled([promesa11, promesa22, promesa33])
  .then(results => {
    console.log(results);
    // [{status: 'fulfilled', value: 1}, {status: 'rejected', reason: 'Error'}, {status: 'fulfilled', value: 3}]
  });


//Promise.any(): Promise.any() devuelve una promesa que se resuelve tan pronto como una de las promesas en el iterable se resuelve.
const promesa111 = Promise.reject('Error 1');
const promesa222 = Promise.reject('Error 2');
const promesa333 = Promise.resolve('Éxito');

Promise.any([promesa111, promesa222, promesa333])
  .then(result => {
    console.log(result); // 'Éxito'
  });
