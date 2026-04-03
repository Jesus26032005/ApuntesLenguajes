import type { GiphyRandomResponde } from "../data/giphy_response";

const API_KEY = "9c6fTNb7RTw4FyZhXxddOKvCm35XfBeb";

// Fetch API, es una interfaz que permite realizar solicitudes HTTP desde el navegador de manera sencilla y moderna.
// El metodo fetch() devuelve una promesa que se resuelve con la respuesta de la solicitud.
// Podemos utilizar fetch para obtener datos de una API, enviar datos a un servidor, entre otras cosas.
const MyRequest = fetch(`https://api.giphy.com/v1/gifs/random?api_key=${API_KEY}&tag=&rating=g`)
// Fetch no permite especificar el tipo de dato que esperamos recibir en la respuesta.

MyRequest
    .then((response) => {
        console.log("Se logro la conexión con la API", response);
        return response.json()//El método json() de la interfaz Response toma un objeto Response y lee su cuerpo 
        // para devolver una promesa que se resuelve con el resultado de analizar el cuerpo como JSON.
        // respuesta.then((data) => { //El método json() también devuelve una promesa, por lo que debemos manejarla con otro then
        //     console.log(data);
        // });
    })
    // Ahora podemos tipar la promesa devuelta por response.json() con la interfaz creada para la respuesta de la API
    .then(({data}: GiphyRandomResponde) => {  // Aqui encadenamos el .then para manejar la promesa devuelta por response.json()
        
        // FORMA SIN TIPAR LA RESPUESTA
        // Aqui se vera mas adelante pues existen las interfaces en TypeScript
        // const imagenUrl = data.data.images.original.url;
        // console.log(imagenUrl);
        // const imgElement = document.createElement("img");
        // imgElement.src = imagenUrl;
        // document.body.append(imgElement);

        // FORMA TIPADA DE LA RESPUESTA
        const imagenUrl = data.images.original.url;
        console.log(imagenUrl);
        const imgElement = document.createElement("img");
        imgElement.src = imagenUrl;
        document.body.append(imgElement);
        // Las funciones tienen que ser lo mas limpias posibles, en este caso el request se podria separar en otra función
    })
    .catch((error) => {
        console.error("Error al conectar con la API:", error);
    })

// response.json() es un método del objeto Response que lee el cuerpo de la respuesta y lo transforma en un objeto JavaScript 
// a partir de una cadena de texto en formato JSON. Devuelve una promesa que se resuelve con el objeto JavaScript resultante.
// Si el cuerpo de la respuesta no es un JSON válido, la promesa es rechazada con un error de tipo `SyntaxError`, 
// lo que sería capturado por el bloque `.catch()` de la cadena de promesas.

// En resumen: Sí, `response.json()` toma la respuesta del servidor (que es texto en formato JSON) y la convierte en un objeto de JavaScript.
// En el código, `.then((data: GiphyRandomResponde) => { ... })`, a ese objeto JavaScript resultante se le asigna el nombre de parámetro 
// `data` para poder usarlo dentro de esa función.