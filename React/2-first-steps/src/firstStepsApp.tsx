import type { CSSProperties } from "react"

export function FirstStepsApp() {
    // Un componente siempre debe retornar un unico elemento JSX y debe empezar con mayuscula
    return <h1 data-testid="test-h1">Hola mundo</h1>
}

export function SecondComponent() {
    // Si quisieramos retornar multiples elementos, debemos envolverlos en un contenedor fragmento
    // esto es un elemento que no es renderizado en el DOM y sirve para agrupar sin afectar la estructura
    // tambien se puede con un div
    return (
        <>
        <h2>Hola mundo 2</h2>
        <p>Que paso we</p>
        </>
    )
}

export function MyAwesomeApp() {
    return (
        <>
        <h3>Jesus</h3>
        <h4>Martinez</h4>
        </>
    )
}

// Se pueden tener componentes dentro de otros componentes para crear interfaces mas complejas o reutilizables
export function AppWithComponents() {
    return (
        <>
        <FirstStepsApp />
        <SecondComponent />
        <MyAwesomeApp />
        </>
    )
}

// Atributos dentro de componentes
export function ComponentWithAttributes() {
    // Es recomendable pasar los const fuera de los componentes para evitar que se redefinidan en cada renderizado
    const primerNombre = "Jesus"
    const apellido = "Martinez"
    const listaDeFrutas = ['Manzana', 'Banana', 'Cereza']
    const Persona = {
        nombre: "Jesus",
        apellido: "Martinez",
        edad: 20
    }

    return (
        <>
        {/* Podemos usar llaves para insertar expresiones de JavaScript dentro del JSX como colocar variables*/}
        <h1>Hola, {primerNombre} {apellido}</h1>
        <p>Estas son mis frutas favoritas:</p>
        <p>{listaDeFrutas.join(", ")}</p>
        {/* Tambien podemos insertar objetos, pero debemos convertirlos a string para que se rendericen correctamente */}
        <p>{JSON.stringify(Persona)}</p>
        </>
    )
}

// AÑADIENDO ESTILOS
// Para crear un objeto de estilos en React, usamos un objeto de clase CSSProperties
const estilosParrafo: CSSProperties ={
    fontFamily: "Arial",
    fontSize: "24px",
}


export function ComponentWithStyles() {
    const primerNombre = "Jesus"
    // Una forma de tener el estilo es con una variable que contenga un objeto con los estilos
    const estilos = {
        fontFamily: "Arial",
        fontSize: "24px",
    }


    // Podemos agregar estilos en linea usando el atributo style
    // Primero es un corchete para indicar que vamos a usar una expresion de JavaScript
    // El segundo corchete es para definir un objeto con los estilos
    return (
        <>
        <p style={estilos}>Hola, {primerNombre}</p>
        <p style={{fontFamily: "Arial", fontSize: "24px"}}>Hola, {primerNombre}</p>
        <p style={estilosParrafo}>Hola, {primerNombre}</p>
        </>
    )
}