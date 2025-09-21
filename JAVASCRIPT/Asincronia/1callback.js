// FUNCIONES CALLBACK
/*
En JavaScript, una de las formas más comunes de implementar la programación asincrónica es mediante el uso de callbacks.
Un callback es una función que se pasa como argumento a otra función y se ejecuta después de que esta última complete su tarea.
La idea básica de una función callback es que se “llama de vuelta” una vez que se realiza una tarea.
Un ejemplo común es el manejo de eventos. Por ejemplo, cuando se hace clic en un botón en una página web, se puede pasar una función de callback como argumento a la función addEventListener() para que se ejecute cuando se haga clic en el botón.*/

//Es llamar a una función después de que otra función haya terminado de ejecutarse.

/*
Funcionamiento de los Callbacks
Definición de una función callback: Una función callback se define como cualquier función que puede ser pasada como argumento a otra función.
Pasar el callback como argumento: El callback se pasa como argumento a la función principal. Esta función principal ejecutará el callback en el momento apropiado.
Ejecución del Callback: Una vez que la función principal completa su tarea principal, invoca el callback.

SINTAXIS BASICA PARA USO DE CALLBACKS
function conCallback(parametrosOpcionales,callback) { //se acepta como parametro una funcion callback
    callback();
}

function funcionNormal(parametrosOpcionales) {Hacer algo}
USO:
conCallback(funcionNormal);

Tambien pueden incluirse returns pero hay que entender donde regresa el valor, ejemplo El return queda dentro de la función callback, si la funcion que recibe la callback devuelve un valor. Si la función que los llama usa ese valor, se puede aprovechar el return
*/

function saludar(funcionCallback) {
    console.log("hola we");
    funcionCallback();
}
function despedida(){
    console.log("adios we");
}
saludar(despedida)

/*
Los callbacks se emplean para realizar operaciones asíncronas. A diferencia de las operaciones sincrónicas, que se ejecutan en secuencia, las operaciones asíncronas permiten que el programa continúe ejecutándose mientras espera que una operación se complete.
*/