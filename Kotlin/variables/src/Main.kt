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
    var apellido2: String = "Perez"
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
    
    // Para hacer casteos entre tipos de datos, usamos la palabra "to" despues de la variable
    // y el tipo al que queremos convertir
    var alturaInt: Int = altura.toInt()
    println("Hola $nombre $apellido, tienes $edad años y mides $altura metros, o $alturaInt metros en enteros")


    // Tambien podemos hacer casteos usando la funcion "as" pero esto solo funciona para tipos de clases
    // que tengan cierta herencia jerarquia entre ellos

    // Para usar valores en una cadena de string, o string templates, usamos la sintaxis $variable
    // Tambien podemos usar expresiones dentro de las string templates, por ejemplo:
    println("Hola $nombre $apellido, tienes ${edad + 1} años y mides $altura metros")
    
    // STRINGS
    // Para definir una cadena de texto se puede usar comillas dobles o simples
    // Las comillas dobles permiten usar string templates, mientras que las simples no
    // Las comillas dobles tambien permiten usar escape de caracteres, por ejemplo:
    println("Hola $nombre $apellido, tienes ${edad + 1} años y mides $altura metros")
    println('Hola $nombre $apellido, tienes ${edad + 1} años y mides $altura metros')
    //Funciones de string
    println("Hola $nombre $apellido, tienes ${edad + 1} años y mides $altura metros".length)
    println("Hola $nombre $apellido, tienes ${edad + 1} años y mides $altura metros".lowercase())
    println("Hola $nombre $apellido, tienes ${edad + 1} años y mides $altura metros".uppercase())
    // Tambien podemos usar funciones de string como trim, trimStart, trimEnd, etc.
    println("   Hola $nombre $apellido, tienes ${edad + 1} años y mides $altura metros   ".trim())
    println("   Hola $nombre $apellido, tienes ${edad + 1} años y mides $altura metros   ".trimStart())
    println("   Hola $nombre $apellido, tienes ${edad + 1} años y mides $altura metros   ".trimEnd())
    // Tambien podemos usar funciones de string como split, replace, etc.
    println("Hola $nombre $apellido, tienes ${edad + 1} años y mides $altura metros".split(" "))
    println("Hola $nombre $apellido, tienes ${edad + 1} años y mides $altura metros".replace(" ", "-"))
    // Tambien podemos usar funciones de string como startsWith, endsWith, etc.
    println("Hola $nombre $apellido, tienes ${edad + 1} años y mides $altura metros".startsWith("Hola"))
    println("Hola $nombre $apellido, tienes ${edad + 1} años y mides $altura metros".endsWith("metros"))
    // Tambien podemos usar funciones de string como contains, indexOf, etc.
    println("Hola $nombre $apellido, tienes ${edad + 1} años y mides $altura metros".contains("Juan"))
    println("Hola $nombre $apellido, tienes ${edad + 1} años y mides $altura metros".indexOf("Juan"))
}   