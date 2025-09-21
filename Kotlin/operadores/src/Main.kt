//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
fun main() {
    var numero1 = 10
    var numero2: Int = 5

    // OPERADORES ARITMETICOS
    // Suma
    var suma = numero1 + numero2
    // Resta
    var resta = numero1 - numero2
    // Multiplicacion
    var multiplicacion = numero1 * numero2
    // Division
    var division = numero1 / numero2
    // Modulo
    var modulo = numero1 % numero2
    // Incremento
    numero1++
    // Decremento
    numero2--
    println("Suma: $suma")
    println("Resta: $resta")
    println("Multiplicacion: $multiplicacion")
    println("Division: $division")
    println("Modulo: $modulo")
    println("Incremento: $numero1")
    println("Decremento: $numero2")
    // El resultado es del tipo de los operandos

    // CAMBIAR TIPO DE DATO
    // Convertir a diferentes tipos existe las funciones toTipo()
    // toInt(), toDouble(), toFloat(), toLong(), toShort(), toByte(), toChar(), toString()
    var numero3: Double = 10.5
    var numero4: Int = numero3.toInt() // Convierte Double a Int
    println("Numero3: $numero3")
    println("Numero4: $numero4")

    // La conversion de tipos no es implicita, se debe hacer de forma explicita
    var numero5: Int = 10
    // var numero6: Double = numero5 // Error
    var numero6: Double = numero5.toDouble() // Correcto
    println(numero6)
    var suma3 = numero5 + numero3.toInt() // Correcto

    // Concatenacion string
    var nombre: String = "Juan"
    var apellido: String = "Perez"
    var nombreCompleto = nombre + " " + apellido // Concatenacion con +
    println("Nombre Completo: $nombreCompleto")
    // Concatenacion con template string
    var nombreCompleto2 = "$nombre $apellido" // Concatenacion con template string

    //El simbolo $ permite insertar valores de variables directamente dentro de una cadena de texto.
    // Es muy útil para construir cadenas dinámicas sin necesidad de concatenar explícitamente.
    println("Nombre Completo 2: $nombreCompleto2")
    // Si se necesita usar una expresion se usa ${expresion}
    println("Suma de numero5 y numero3: ${numero5 + numero3.toInt()}")

    // OPERADORES DE ASIGNACION
    var numero7 = 10
    numero7 += 5 // numero7 = numero7 + 5
    println("Numero7: $numero7")
    numero7 -= 3 // numero7 = numero7 - 3
    println("Numero7: $numero7")
    numero7 *= 2 // numero7 = numero7 * 2
    println("Numero7: $numero7")
    numero7 /= 4 // numero7 = numero7 / 4
    println("Numero7: $numero7")
    numero7 %= 3 // numero7 = numero7 % 3
    println("Numero7: $numero7")

    // OPERADORES DE COMPARACION
    var numero8 = 10
    var numero9 = 5
    println("Numero8 == Numero9: ${numero8 == numero9}") // Igualdad
    println("Numero8 != Numero9: ${numero8 != numero9}") // Desigualdad
    println("Numero8 > Numero9: ${numero8 > numero9}") // Mayor que
    println("Numero8 < Numero9: ${numero8 < numero9}") // Menor que
    println("Numero8 >= Numero9: ${numero8 >= numero9}") // Mayor o igual que
    println("Numero8 <= Numero9: ${numero8 <= numero9}") // Menor o igual que

    // OPERADORES LOGICOS
    var boolean1 = true
    var boolean2 = false
    println("boolean1 && boolean2: ${boolean1 && boolean2}") // AND
    println("boolean1 || boolean2: ${boolean1 || boolean2}") // OR
    println("!boolean1: ${!boolean1}") // NOT
}