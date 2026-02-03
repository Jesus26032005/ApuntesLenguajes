


// Para crear pruebas unitarias en TypeScript con vitest
// se empieza con la palabra test 

import { test, expect, describe } from 'vitest';
import { suma, resta, multiplicacion, division} from './math.helper';

// test es una función que recibe dos parámetros
// el primero es una descripción de la prueba
// el segundo es una función que contiene la lógica de la prueba
// dentro de la función se hacen las aserciones
// una aserción es una comparación entre un valor esperado y un valor real
// si la comparación es verdadera, la prueba pasa
// si la comparación es falsa, la prueba falla

test('suma de 2 + 3 debe ser 5', () => {
    const resultado = suma(2, 3);
    // Para hacer una aserción se usa la función expect
    // expect recibe un valor real y se le pueden encadenar
    // métodos para hacer comparaciones
    // en este caso se usa el método toBe para comparar
    // el valor real con el valor esperado
    expect(resultado).toBe(5);
})


// arrage, act, assert
// arrenge: preparar el escenario
// act: ejecutar la acción a probar
// assert: verificar el resultado
test('resta de 5 - 3 debe ser 2', () => {
    // arrange
    const a = 5;
    const b = 3;
    // act
    const resultado = resta(a, b);
    // assert
    expect(resultado).toBe(2)
})

// FUNCION DESCRIBE: La funcion describe se usa para agrupar
// varias pruebas relacionadas entre sí
// recibe dos parámetros
// el primero es una descripción del grupo de pruebas
// el segundo es una función que contiene las pruebas

describe('Pruebas de multiplicación', () => {
    test('multiplicación de 2 * 3 debe ser 6', () => {
        const resultado = multiplicacion(2, 3);
        expect(resultado).toBe(6);
    })
    test('multiplicación de -2 * 3 debe ser -6', () => {
        const resultado = multiplicacion(-2, 3);
        expect(resultado).toBe(-6);
    })
})


describe("Pruebas de operaciones suma, resta , multiplicacion", () => {
    const argumento1 = 5
    const argumento2 = 8

    test("suma de 5+8", ()=> {
        const resultadoSuma = suma(argumento1,argumento2);
        expect(resultadoSuma).toBe(13)
    })
    test("Resta de 5-8",()=> {
        const resultadoResta= resta(argumento1,argumento2);
        expect(resultadoResta).toBe(-3)
    })
    test("Multiplicacion 5*8", ()=> {
        const resultadoMultiplicacion = multiplicacion(argumento1,argumento2);
        expect(resultadoMultiplicacion).toBe(40)
    })
})