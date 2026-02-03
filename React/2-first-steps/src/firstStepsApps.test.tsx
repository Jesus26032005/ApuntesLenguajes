// Para realizar las pruebas de componentes se usa Vitest junto con React Testing Library
// Testing Library facilita la renderización de componentes y la interacción con ellos en un entorno de prueba.

import { describe, expect, test } from "vitest";    
import { FirstStepsApp } from "./firstStepsApp";
import { render, screen } from "@testing-library/react";


describe("Pruebas de componentes en React", () => {
    test("Componente FirstStepsApp debe renderizar correctamente", () => {
        // La función render de Testing Library renderiza el componente en un entorno de prueba.
        // nos devuelve varios utilitarios para interactuar con el componente renderizado.
        const { container } = render(<FirstStepsApp />);
        //container tiene el HTML renderizado del componente

        // Del render tambien se puede tomar screenshot para hacer comparaciones visuales
        screen.debug(); // Muestra el HTML renderizado en la consola


        // screen (Recomendado): Es un objeto global que representa todo el document.body. Es la forma moderna y 
        // estándar de hacer consultas (queries), ya que simula cómo un usuario ve la página completa. Se recomienda en caso
        // de que se necesite evaluar elementos iniciales
        // container: Es el nodo del DOM (usualmente un <div>) que envuelve específicamente al componente que 
        // acabas de renderizar. Se usa para casos muy específicos (como snapshots o acceder a atributos del nodo raíz),
        // pero no se recomienda para buscar elementos.
        // En general, es mejor usar screen para consultas.

        // USO DE CONTAINER
        // El metodo querySelector permite buscar elementos en el HTML renderizado usando selectores CSS.
        // devuelve el primer elemento que coincide o null si no se encuentra ninguno.
        const h1 = container.querySelector("h1");
        console.log(h1?.innerHTML); // Muestra el contenido del h1 en la consola
        expect(h1?.innerHTML).toContain("Hola mundo"); // Verifica que el contenido del h1 contenga "Hola mundo"

        // USO DE SCREEN
        // El metodo getByRole busca elementos por su rol accesible (como "button", "heading", etc.)
        // Sus parametros son el rol y un objeto con opciones adicionales para afinar la búsqueda.
        const h12 = screen.getByRole("heading", { level: 1 }); // Busca un elemento con el rol de encabezado (h1)
        expect(h12.innerHTML).toContain("Hola mundo"); // Verifica que el contenido del h1 contenga "Hola mundo"

        // El metdodo getByTestId busca elementos por su atributo data-testid.
        // Es útil para pruebas cuando no hay otros selectores disponibles.
        const h13 = screen.getByTestId("test-h1"); // Busca el elemento con data-testid="test-h1"
        expect(h13.innerHTML).toContain("Hola mundo"); // Verifica que el contenido del h1 contenga "Hola mundo"
    });
    test("Snapshot de FirstStepsApp", () => {
        // SNAPSHOT TESTING
        // Un snapshot es una representación guardada del HTML renderizado en un momento dado.
        // Se usa para comparar cambios inesperados en la UI entre ejecuciones de pruebas.

        // USANDO CONTAINER
        const { container } = render(<FirstStepsApp />);
        // La funcion toMatchSnapshot compara el HTML renderizado con un snapshot guardado previamente.
        // Al ejecutarlo por primera vez, crea el snapshot. En ejecuciones posteriores, verifica que no haya 
        // cambios inesperados. Si hay diferencias, la prueba falla.
        expect(container).toMatchSnapshot();
        // USANDO SCREEN: Screen no es adecuado para snapshots porque representa todo el document.body,
        // lo que puede incluir elementos fuera del componente bajo prueba. Por eso, se prefiere container
        // para este propósito.
        // Sin embargo, si se quisiera usar screen, se haria asi:
        expect(screen.getByTestId("test-h1")).toMatchSnapshot();
    });
});



/*
• `screen` (Estándar/Recomendado): Representa todo el `document.body`. Es la forma correcta de buscar 
elementos (`getByRole`, `getByText`) porque simula cómo el usuario ve la aplicación.

• `container` (Técnico/Legacy): Es el nodo envolvente (wrapper) del componente renderizado. Úsalo 
solo para Snapshots o acceder a atributos del nodo raíz, no para buscar elementos.
Un snapshot es una representación guardada del HTML renderizado en un momento dado. Se usa para
comparar cambios inesperados en la UI entre ejecuciones de pruebas.
*/

/*
A. Prioridad Alta (Accesibles para todos)
ByRole (El mejor 🏆): Busca por rol ARIA (button, link, heading, textbox) y su nombre accesible.

screen.getByRole('button', { name: /enviar/i })

ByLabelText: Ideal para formularios. Busca el input asociado a un label.

screen.getByLabelText('Nombre de usuario')

ByPlaceholderText: Si no hay label (aunque debería), busca por el placeholder.

screen.getByPlaceholderText('Ingresa tu correo')

ByText: Busca elementos no interactivos (divs, spans, párrafos) por su contenido de texto.

screen.getByText('Bienvenido a la página')

ByDisplayValue: Busca inputs (text, textarea, select) por el valor que muestran actualmente.

screen.getByDisplayValue('Juan Perez')

B. Prioridad Media (Semánticos)
ByAltText: Específico para imágenes (<img />).

screen.getByAltText('Logo de la empresa')

ByTitle: Busca por el atributo title (el tooltip nativo), aunque no es muy común hoy en día.

screen.getByTitle('Cerrar ventana')

C. Prioridad Baja (Último recurso)
ByTestId: Busca por el atributo data-testid. Úsalo solo si no puedes seleccionar el elemento de
ninguna otra forma (por ejemplo, un div dinámico sin texto ni rol).

HTML: <div data-testid="custom-element" />

Test: screen.getByTestId('custom-element')

*/