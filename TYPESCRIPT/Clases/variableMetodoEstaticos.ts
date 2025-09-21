//En TypeScript, los métodos y variables estáticos son aquellos que pertenecen a la clase en sí misma en lugar de a una instancia específica de la clase. Se utilizan para definir comportamientos que están relacionados con la clase en su conjunto, y no con instancias individuales.

//Para definir una variable o método estático, se utiliza la palabra clave static antes del nombre de la variable o método.
// Sintaxis de variable estática: static <nombre_variable>: <tipo> = <valor>;
// Sintaxis de método estático: static <nombre_metodo>(<parametros>): <tipo_retorno> { ... }

//Cabe mencionar que los métodos y variables estáticos se acceden utilizando el nombre de la clase en lugar de una instancia de la clase.
class Matematica {
    // variable estática
    static PI: number = 3.1416;
    // metodo estatico
    static imprimirPi(): void {
        console.log(`El valor de PI es: ${Matematica.PI}`);
    }
}


// Accediendo a la variable y método estáticos sin crear una instancia de la clase
console.log(Matematica.PI); // 3.1416
Matematica.imprimirPi(); // El valor de PI es: 3.1416

// Nota: Los metodos estaticos no pueden acceder a variables o metodos de instancia directamente, ya que no tienen acceso a una instancia específica de la clase. Solo pueden acceder a otros miembros estáticos de la clase. Ademas en cuestion de herencia, los metodos y variables estaticos se heredan, pero no se pueden sobrescribir en las clases derivadas.

class Geometria extends Matematica {
    static areaCirculo(radio: number): number {
        return this.PI * radio * radio; // Accediendo a la variable estática PI de la clase base
    }
}

console.log(Geometria.areaCirculo(5));