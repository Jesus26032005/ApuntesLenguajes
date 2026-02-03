interface ItemInCart {
    productName: string
    quantity: number
}
const itemsInCart: ItemInCart[] = [
    {productName: "Manzanas", quantity: 3},
    {productName: "Bananas", quantity: 5},
    {productName: "Naranjas", quantity: 2},
]
import { ContatorWithPropsEventsHocksCSS } from "./itemCounterFortest";

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