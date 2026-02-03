import { useState } from "react"


export function ItemCounter() {
    return (
        <>
        <h1>Carrito de compras</h1>
        <ContatorWithProps initialValue={10}/>
        <ContatorWithProps initialValue={20}/>
        </>
    )
}


export function Contator () {
    return (
        <section style={{display:"flex"}}>
            <h2>Contador de items</h2>
            <button>+1</button>
            <span>0</span>
            <button>-1</button>
        </section>
    )
}

// PROPEDADES (PROPS)
// Las propiedades (props) son una forma de pasar datos a los componentes de React
// Para definir las props de un componente, se utiliza un objeto como parametro de la funcion del componente
interface ContatorProps {
    initialValue: number
}
// y para usarlas, se accede a las propiedades del objeto, usando la destructuracion de objetos
// otra forma es pasando el objeto completo y accediendo a sus propiedades con el punto (.)

export function ContatorWithProps ({initialValue}: ContatorProps) {
    return (
        <section style={{display:"flex"}}>
            <h2>Contador de items</h2>
            <button>+1</button>
            <span>{initialValue}</span>
            <button>-1</button>
        </section>
    )
}

// En el caso de llamar al componente, se pasan los propos como atributos del componente, si se 
// tuvieran se separan por espacios

// Si son numeros o booleanos, se pasan entre llaves {}
// Si son strings, se pueden pasar entre comillas "" o entre llaves {}
export function ItemCounterApp() {
    return (
        <>
        <h1>Carrito de compras</h1>
        <ContatorWithProps initialValue={10} />
        {/* <ContatorWithProps initialValue="Zaddkiel" /> */}
        </>
    )
}


// LISTA DE ITEMS
// Para renderizar listas de elementos en React, se puede usar el metodo map de los arrays
// que recibe una funcion que retorna un elemento JSX por cada item del array
interface ItemInCart {
    productName: string
    quantity: number
}
const itemsInCart: ItemInCart[] = [
    {productName: "Manzanas", quantity: 3},
    {productName: "Bananas", quantity: 5},
    {productName: "Naranjas", quantity: 2},
]

export function ItemList() {
    return (
        <>
        <h1>Lista de items</h1>
        {
            // Para renderizar listas en React, usamos el metodo map de los arrays
            // que recibe una funcion que retorna un elemento JSX por cada item del array
            // El metodo map retorna un nuevo array con los elementos JSX
            // Su argumento es una funcion que recibe como parametro cada item del array
            // Cada elemento renderizado en una lista debe tener una propiedad "key" unica
            itemsInCart.map(item => (
                <ContatorWithPropsEventsHocksCSS key={item.productName} initialValue={item.quantity} />
            ))
        }
        </>
    )
}

//EVENTOS EN LOS ELEMENTOS
// Los eventos en React se manejan mediante atributos en los elementos JSX
// Los nombres de los eventos en React usan camelCase en lugar de minusculas
// Por ejemplo, el evento click se maneja con el atributo onClick
// El valor del atributo es una funcion que sera llamada cuando el evento ocurra
// Usualmente se usan funciones flecha para definir los manejadores de eventos o se pasan funciones ya definidas
// Se colocan como funciones lambda o referencias a funciones para evitar que se ejecuten inmediatamente al renderizar 
// el componente, sino solo cuando ocurra el evento, se colocan como referencias si no se necesitan parametros adicionales
// o como funciones lambda si se necesitan parametros adicionales o se quiere evitar el paso del evento por defecto

export function ContatorWithPropsEvents ({initialValue}: ContatorProps) {
    return (
        <section style={{display:"flex"}}>
            <h2>Contador de items</h2>
            <button
            onClick={() => imprimirIncremento()}            
            >+1</button>
            <span>{initialValue}</span>
            <button
            onClick={() => console.log("Decrementando")}
            >-1</button>
        </section>
    )
}

function imprimirIncremento() {
    console.log("Incrementando desde funcion externa")
}

// HOCKS 
// Los hocks son funciones especiales en React que permiten usar el estado y otras caracteristicas de React en 
// componentes funcionales
// El hock mas comun es useState, que permite agregar estado a un componente funcional
// El estado es una forma de almacenar datos que pueden cambiar a lo largo del tiempo y que afectan la 
// renderizacion del componente
// El hock useState retorna un array con dos elementos: el valor actual del estado y una funcion para actualizar el estado
// Se puede usar la desestructuracion de arrays para obtener ambos valores

// Los hocks mas comunes en React son:
// useState: Permite agregar estado a un componente funcional
// useEffect: Permite manejar efectos secundarios en un componente funcional, como llamadas a APIs o suscripciones a eventos
// useContext: Permite compartir datos entre componentes sin tener que pasar props manualmente en cada nivel del arbol
//  de componentes

// Reglas de los hocks:
// Solo se pueden usar en componentes funcionales o en otros hocks
// Siempre se llama a los hocks en el mismo orden
// los hocks deben comenzar con la palabra "use"


export function ContatorWithPropsEventsHocks ({initialValue=1}: ContatorProps) {
    // Usestate devuelve un array con dos elementos: el valor actual del estado y una funcion para actualizar el estado
    const [itemCounter, setItemCounter] = useState(initialValue) // Si no se coloca un argumento inicial, el estado sera undefined


    // SetItemCounter es una funcion que actualiza el estado y provoca la re-renderizacion del componente
    // Por lo que cada vez que se llame a setItemCounter, el componente se volvera a renderizar con el nuevo valor del estado
    // Se puede llamar a setItemCounter desde cualquier parte del componente, incluyendo manejadores de eventos
    // Al llamarla el parametro que se le pasa es el nuevo valor del estado

    const imprimirIncremento = () => {
        if (itemCounter >= 10) return;
        // Una forma comun de actualizar el estado es pasando el nuevo valor directamente
        // setItemCounter(itemCounter + 1)
        else setItemCounter(itemCounter + 1)
    }

    const imprimirDecremento = () => {
        if (itemCounter <= 0) return;
        else setItemCounter(itemCounter - 1)
    }

    return (
        <section style={{display:"flex"}}>
            <h2>Contador de items</h2>
            <button
            onClick={imprimirIncremento}            
            >+1</button>
            <span>{itemCounter}</span>
            <button
            onClick={imprimirDecremento}
            >-1</button>
        </section>
    )
}

// AÑADIR ARCHVO CSS 
// Para añadir estilos a un componente, se puede crear un archivo CSS y importarlo en el componente
import './itemCounter.css'
export function ContatorWithPropsEventsHocksCSS ({initialValue=1}: ContatorProps) {
    const [itemCounter, setItemCounter] = useState(initialValue) 

    const imprimirIncremento = () => {
        if (itemCounter >= 10) return;
        else setItemCounter(itemCounter + 1)
    }

    const imprimirDecremento = () => {
        if (itemCounter <= 0) return;
        else setItemCounter(itemCounter - 1)
    }

    return (
        // Se usa className en lugar de class para asignar clases CSS en JSX
        <section className="item-counter">
            <h2>Contador de items</h2>
            <button
            onClick={imprimirIncremento}            
            >+1</button>
            <span style={
                // Se pueden estilos condicionales que dependen del estado del componente en este caso 
                // se cambia el color del texto segun el valor del contador
                {color: itemCounter >= 5 ? 'green' : 'red'}
            }>{itemCounter}</span>
            <button
            onClick={imprimirDecremento}
            >-1</button>
        </section>
    )
}
// Si quisieramos usarlos como modulos CSS, se importaria el archivo CSS como un objeto
// import styles from './itemCounter.module.css'
// y se usaria asi: className={styles.itemCounter}