import './itemCounter.css'
import { useState } from 'react';

interface ContatorProps {
    initialValue: number
}


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