//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
fun main() {
    // En kotlin las variables son multitipado y no es necesario definir su tipo
    // La forma basica de definir una variable es con la palabra reservada var
    var nombre = "Juan"
    println("Hola $nombre")

    // Si queremos definir una variable que no va a cambiar su valor usamos la palabra reservada val, se
    // podria decir que es una constante
    val apellido = "Perez"
    println("Hola $nombre $apellido")

    // Tambien podemos definir el tipo de la variable, la sintaxis es:
    // var nombre: Tipo = valor
    var edad: Int = 30
    var apellido: String = "Perez"
    // Los tipos de datos mas comunes en kotlin son:
    // Int: para numeros enteros
    // Double: para numeros con decimales
    // Float: para numeros con decimales (menos precision que Double), se define con la letra f al final del numero
    // Boolean: para valores true o false
    // Char: para un solo caracter
    // Byte: para numeros enteros de 8 bits
    // Short: para numeros enteros de 16 bits
    // Long: para numeros enteros de 64 bits
    // String: para cadenas de texto


    // Si queremos definir una variable sin inicializarla, debemos definir su tipo
    var altura: Double
    altura = 1.75
    println("Hola $nombre $apellido, tienes $edad años y mides $altura metros")

}