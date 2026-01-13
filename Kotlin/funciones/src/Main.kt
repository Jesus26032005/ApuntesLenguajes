// Una funcion es un bloque de codigo que realiza una tarea especifica y
// puede recibir valores y retornar valores
// La sintaxis basica de una funcion es:
// fun nombreDeLaFuncion(parametros): tipoDeRetorno = cuerpoDeLaFuncion

// Funcion sin retorno
fun imprimirHola() {
    println("Hola")
}

// Funcion con retorno
fun obtenerNombre(): String {
    return "Juan"
}

// Funcion con parametros, siempre deben los parametros tener un tipo de dato
fun saludar(nombre: String) {
    println("Hola $nombre")
}

// Funcion con parametros y retorno
fun sumar(a: Int, b: Int): Int {
    return a + b
}

// Sintaxis completa
// fun nombreDeLaFuncion(parámetros: Tipo): TipoDeRetorno {
// // Cuerpo de la función
// // Código que realiza la acción
// return valor // Si la función tiene un tipo de retorno
// }

// Funcion con valores predeterminados, aqui se puede especificar un valor predeterminado para el parametro 
// despues de especficar el tipo de dato, algo asi parametro: Tipo = valorPredeterminado
fun saludarPredeterminado(nombre: String = "Mundo") {
    println("Hola $nombre")
}

fun completa(nombre: String = "Juan", apellido: String = "Perez", edad: Int = 25): String {
    return "Hola $nombre $apellido, tienes $edad años"
}

fun holamundo(nombre: String) {
    println("Hola $nombre")
}

fun main() {
    imprimirHola()
    saludar("Juan")
    println(sumar(2, 3))
    println(sumar(5, 7))
    saludarPredeterminado()
    println(completa())
    println(completa(nombre = "Pedro", apellido = "Gomez", edad = 30))
    // Pasar parametros por nombre, esto permite especificar el valor de un parametro en particular 
    // sin tener que especificar los demas
    println(completa(apellido = "Lopez", edad = 40))
    println(completa(nombre = "Ana", edad = 20))
}

