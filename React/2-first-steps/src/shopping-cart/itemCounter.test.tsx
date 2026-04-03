import { render, screen, fireEvent} from "@testing-library/react";
import { afterEach, describe, expect, test, vi } from "vitest";
import { ContatorWithPropsEventsHocksCSS } from "./itemCounter";
import { ItemList} from "./itemList";

describe("ItemCounter", () => {
    test("SHOULD RENDER WITH DEAFAULT VALUES", () => {
        render(<ContatorWithPropsEventsHocksCSS initialValue={5} />);

        // El metodo toBeDefined verifica que el elemento exista (no sea null ni undefined)
        expect(screen.getByText("Contador de items")).toBeDefined();
    });


    test("SHOULD INCREMENT AND DECREMENT VALUES", () => {
        render(<ContatorWithPropsEventsHocksCSS initialValue={5} />);
        // obtener el boton de incremento usando getByText
        const incrementButton = screen.getByText("+1");
        // obtener el boton de decremento usando getByText
        const decrementButton = screen.getByText("-1");
        // Para disparar eventos de usuario, se usa el fireEvent de Testing Library
        // El metodo fireEvent tiene varios metodos para simular eventos como click, change, submit, etc.
        fireEvent.click(incrementButton); // Simula un click en el boton de incremento
        expect(screen.getByText("6")).toBeDefined(); // Verifica que el contador sea 6

        fireEvent.click(decrementButton); // Simula un click en el boton de decremento
        expect(screen.getByText("5")).toBeDefined(); // Verifica que el contador sea 5
    });

    test("SHOULD NOT DECREMENT BELOW ZERO", () => {
        render(<ContatorWithPropsEventsHocksCSS initialValue={0} />);
        const decrementButton = screen.getByText("-1");
        fireEvent.click(decrementButton);
        expect(screen.getByText("0")).toBeDefined(); // Verifica que el contador no sea menor que 0
    });

    // COMPROBAR ESTILSO
    test("SHOULD CHANGE COLOR BASED ON VALUE", () => {
        render(<ContatorWithPropsEventsHocksCSS initialValue={4} />);
        const itemText = screen.getByText("4");
        const estilo = itemText.style
        expect(estilo.color).toBe("red"); // Verifica que el color sea verde cuando el valor es mayor o igual a 5
    });
});


vi.mock('./itemCounterFortest', () => ({
    ContatorWithPropsEventsHocksCSS: (props:unknown) => itemCounterFortest(props)
}));


// vi.mock('./itemCounterFortest', () => ({
//     ContatorWithPropsEventsHocksCSS: (props:unknown) => <div>Mocked Item Counter Component</div>
// }));

// vi.fn crea una funcion mock para pruebas
const itemCounterFortest = vi.fn((props:unknown) => {
    return (<div>Mocked Item Counter Component</div>)
}) 
/*
vi.fn() crea una función espía vacía (o con una implementación simple) que sirve para rastrear todo lo que le sucede.
Sirve para responder estas tres preguntas en tus tests:
¿Fue llamada? (Si se ejecutó o no).
¿Cuántas veces? (1 vez, 5 veces, 0 veces).
¿Con qué argumentos? (Si le pasaron un "10", un objeto, etc.).
*/


// TESTING COMPONENTES DE LISTA
describe('ITEMLIST', () => {
    // BEFORE EACH-AFTER EACH
    // BEFORE EACH se ejecuta antes de cada test
    // AFTER EACH se ejecuta despues de cada test
    afterEach(() => {
        vi.clearAllMocks();
    });

    test("SHOUULD MATCH SNAPSHOT", () => {
        const {container} = render(<ItemList />);
        expect(container).toMatchSnapshot();
    });

    // MOCK COMPONENTS: Un mock es una version simulada de un componente o modulo que se usa para pruebas unitaria
    test("SHOULD RENDER MOCKED COMPONENT", () => {
        render(<ItemList />);
        screen.debug();
        const elementos = screen.getAllByText("Mocked Item Counter Component");
        expect(elementos.length).toBe(3);
    });

    test("SHOULD CALL MOCKED COMPONENT WITH CORRECT PROPS", () => {
        render(<ItemList />);
        // to have been called times verifica cuantas veces se llamo la funcion mock
        expect(itemCounterFortest).toHaveBeenCalledTimes(3);
        // to hace been called with verifica que la funcion mock haya sido llamada con los argumentos correctos
        // los argumentos son los props que se le pasaron al componente mockeado
        expect(itemCounterFortest).toHaveBeenCalledWith({initialValue: 3});
        expect(itemCounterFortest).toHaveBeenCalledWith({initialValue: 5});
        expect(itemCounterFortest).toHaveBeenCalledWith({initialValue: 2});
    });
});

/**
 * ---------------------------------------------------------------------
 * 🧪 ¿QUÉ ES UN MOCK? (RESUMEN)
 * ---------------------------------------------------------------------
 * * DEFINICIÓN:
 * Un Mock es un objeto o función "falsa" que reemplaza a una dependencia real
 * (como una API, una base de datos o un componente hijo complejo).
 * Es como usar un "doble de acción" en una película.
 * * ¿PARA QUÉ SIRVE? (Los 3 Pilares):
 * 1. AISLAMIENTO: Prueba tu componente sin que le afecten los errores de sus hijos.
 * 2. CONTROL: Puedes forzar situaciones difíciles (ej. simular que la API falla).
 * 3. VELOCIDAD: Evita llamadas reales a internet o cálculos pesados.
 * * ¿CÓMO SE HACE EN VITEST?
 * Se usa `vi.mock` antes de los tests.
 * * SINTAXIS:
 * vi.mock("RUTA_AL_ARCHIVO", () => ({
 * NombreExportacion: () => valor_falso
 * }));
 * * ⚠️ REGLAS DE ORO:
 * 1. La ruta apunta al ARCHIVO, no a la función (ej: "./ItemList", no "./ItemList/func").
 * 2. Si retornas un objeto en una arrow function, envuélvelo en paréntesis: ({ ... }).
 * ---------------------------------------------------------------------
 */