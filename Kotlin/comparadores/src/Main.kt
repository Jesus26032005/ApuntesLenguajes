//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
fun main() {
    // Como en java, existen cuatro de comparadores
    // El if, else, else if y el when

    val numero = 5

    // Ejemplo de if, else, else if
    if (numero==5){
        println("El numero es 5")
    } else if (numero > 5) {
        println("El numero es mayor que 5")
    } else {
        println("El numero es menor que 5")
    }

    // Kotlin tiene la capacidad de definir una sesion de valores con puntos iniciales y finales a esto se le llama
    // rango. La forma mas sencilla de definir un rango es con el operador .. (dos puntos)
    val rango = 1..10 // Rango del 1 al 10
    val rangoLetras = 'a'..'z' // Rango de letras de

    if (numero in rango) { // Verifica si el numero esta en el rango
        println("El numero $numero esta en el rango")
    } else {
        println("El numero $numero no esta en el rango")
    }

    // En el caso de when, este es similar a el switch, siendo una sintaxis basica de este:
    when (numero) {
        1 -> println("El numero es 1")
        2 -> println("El numero es 2")
        3,4 -> println("El numero es 3 o 4") // Se pueden agrupar casos
        in 5..10 -> println("El numero esta entre 5 y 10") // Rango de valores
        !in 11..20 -> println("El numero no esta entre 11 y 20") // Rango de valores negado
        else -> println("El numero no es ni 1, ni 2, ni 3, ni 4, ni esta entre 5 y 10") // Default
    }

    // Es decir su sintaxis es:
    /*
    when (variable) {
        valor1 -> accion1
        valor2 -> accion2
        valor3, valor4 -> accion3 // Agrupacion de casos
        in rango -> accion4 // Rango de valores
        !in rango -> accion5 // Rango de valores negado
        else -> accionDefault // Default
     */

    // El when tambien puede usarse sin argumento, funcionando como un if, else if, else
    when {
        numero % 2 == 0 -> println("El numero es par")
        numero % 2 != 0 -> println("El numero es impar")
        else -> println("El numero no es ni par ni impar") // Este caso nunca se dara
    }


}