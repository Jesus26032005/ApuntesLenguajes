//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
fun main() {
    // De forma predeterminada las variables en kotlin no pueden ser nulas
    var numero1: Int = 10
    // numero1 = null // Error

    // Para permitir que una variable sea nula se debe usar el operador ? despues del tipo de dato
    var numero2: Int? = 5
    numero2 = null // Correcto

    // Para realizar operaciones con variables que pueden ser nulas se debe usar el operador ?.
    // Si la variable es nula, el resultado de la operacion sera nulo
    var suma: Int? = numero1 + (numero2 ?: 0) // Si numero2 es nulo, se usa 0
    println("Suma: $suma")

    // Tambien con ello se puede usar el operador Elvis ?: el cual permite asignar un valor por defecto
    // si la variable es nula
    // var suma2: Int = numero1 + (numero2 ?: 0) // Si numero2 es nulo, se usa 0
    // println("Suma2: $suma2")
    
    //Se puede ahorrar en sentencias if/else usando el operador Elvis ?: y el operador ?.
    var division: Int? = numero1 / (numero2 ?: 1) // Si numero2 es nulo, se usa 1
    var division1 = division ?: 0 // Si division es nulo, se usa 0
    var incremento = numero1?.plus(1)  // Si numero1 no es nulo, se incrementa en 1

    // Asimiso, se puede usar para preguntar si una variable es nula y en caso de no serlo usar alguna operacion
    var multiplicacion: Int? = numero2?.let { numero1 * it } // Si numero2 es nulo, multiplicacion sera nulo
    println("Multiplicacion: $multiplicacion")

    // El operador !! se usa para indicar que una variable no es nula, es decir, queremos forzar que no sea nula
    // Si la variable es nulo, se lanza una excepcion NullPointerException
    // var resta: Int = numero1 - numero2!! // Si numero2 es nulo, lanza excepcion
    var resta: Int = numero1 - (numero2 ?: 0) // Si numero2 es nulo, se usa 0
    println("Resta: $resta")
}