package clasesyArreglos.clase6;

import java.util.ArrayList;
import java.util.List;
import java.util.function.BiConsumer;
import java.util.function.BiFunction;
import java.util.function.BinaryOperator;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Supplier;
import java.util.function.UnaryOperator;

public class funcionesLambda {
    /* Una función lambda es una forma concisa de representar una 
     * función anónima (es decir, una función sin nombre) que puede ser pasada como argumento, 
     * almacenada o ejecutada. Introducidas en Java 8, las lambdas permiten escribir código más
     * limpio y expresivo, especialmente cuando se trabaja con interfaces funcionales.
     * 
     * Las funciones lambda se usan principalmente para implementar interfaces funcionales.
     * Una interfaz funcional es una interfaz que solo tiene un método abstracto (ejemplo: Runnable,
     * Callable, Comparator, o interfaces de la API de Streams).
     * 
     * Sintaxis básica
     * (parametros) -> expresión 
     * o si la función es más compleja:
     * (parametros) -> {
     *           // bloque de código
     * }
     * 
     * 
     * No instancias la interfaz directamente.
     * Le pasas al compilador la implementación del método único de la interfaz funcional usando una lambda.
     * El compilador genera el objeto con esa implementación.
     * Ese objeto es lo que se asigna a la variable.
     * 
     * Para usar funciones anonimas se requiere 
     * Java 8 o superior
        Las lambdas fueron introducidas en Java 8, no están disponibles en versiones anteriores.
        Interfaz funcional obligatoria
        La lambda solo puede usarse con interfaces funcionales, que cumplen:
        Tienen solo un método abstracto.
        Pueden tener métodos default o static, pero solo un abstracto.
        Puedes usar @FunctionalInterface para obligar al compilador a verificarlo.
        La lambda debe coincidir con la firma del método
        La cantidad y tipo de parámetros, así como el tipo de retorno, deben coincidir con el 
        método abstracto de la interfaz funcional.
        Contexto claro del tipo (inferencia)
        Java necesita saber a qué tipo de interfaz estás refiriéndote.
        Esto se logra:
        ✅ Al asignarla a una variable de tipo interfaz funcional.
        ✅ Al pasarla como argumento a un método que espera una interfaz funcional.
        Métodos que acepten interfaces funcionales como parámetros
        Puedes usar lambdas donde un método reciba una interfaz funcional, como:
        forEach(Consumer<T>)
        filter(Predicate<T>)
        map(Function<T, R>)
        sort(Comparator<T>), etc.
        En estos casos, la lambda actúa como implementación del método esperado.
     */
    public static void main(String[] args) {

        // Runnable: no recibe parámetros ni retorna valor
        Runnable r = () -> System.out.println("Ejecutando Runnable");
        r.run();

        // Supplier<T>: no recibe parámetros, retorna un valor de tipo T
        Supplier<Double> randomSupplier = () -> Math.random();
        System.out.println("Random: " + randomSupplier.get());

        // Consumer<T>: recibe un parámetro y no retorna nada
        Consumer<String> imprimir = s -> System.out.println("Recibido: " + s);
        imprimir.accept("Hola Lambda");

        // Function<T,R>: recibe un parámetro T y retorna un valor R
        Function<String, Integer> largo = s -> s.length();
        System.out.println("Largo de 'Hola': " + largo.apply("Hola"));

        // BiFunction<T,U,R>: recibe dos parámetros y retorna un valor
        BiFunction<Integer, Integer, Integer> sumar = (a, b) -> a + b;
        System.out.println("3 + 4 = " + sumar.apply(3, 4));

        // BiConsumer<T,U>: recibe dos parámetros y no retorna nada
        BiConsumer<String, Integer> imprimirEdad = (nombre, edad) -> 
        System.out.println(nombre + " tiene " + edad + " años.");
        imprimirEdad.accept("Ana", 25);

        // UnaryOperator<T>: recibe un parámetro y retorna el mismo tipo
        UnaryOperator<String> alReves = s -> new StringBuilder(s).reverse().toString();
        System.out.println("Al revés: " + alReves.apply("Java"));

        // BinaryOperator<T>: recibe dos parámetros del mismo tipo y retorna ese tipo
        BinaryOperator<Integer> maximo = (a, b) -> a > b ? a : b;
        System.out.println("Max entre 5 y 9: " + maximo.apply(5, 9));

        //Usando lambda en un forEach (más sencillo)
        List<String> lista= new ArrayList<>();
        lista.add("hola");
        lista.add("XD");
        lista.forEach(s -> System.out.println(s));
        lista.forEach(System.out::println);
        /*
         * ¿Qué es una referencia a método?
         * Es una forma corta de usar un método existente como función, sin escribir la lambda completa.
         * En lugar de: lista.forEach(s -> System.out.println(s))
         * Puedes hacer:    lista.forEach(System.out::println);
         * 
         * Tipos principales:
         *  Método estático
         *          Clase::metodoEstatico
         *                  Ejemplo:
         *                         Function<String, Integer> parseInt = Integer::parseInt;
         *  Método de instancia de un objeto:
         *          objeto::metodo
         *                  Ejemplo:
         *                          String texto = "hola";
         *                          Supplier<String> mayus = texto::toUpperCase;
         *  Método de instancia de cualquier objeto del tipo:
         *          Clase::metodo
         *                  Ejemplo:
         *                          List<String> nombres = Arrays.asvalList("Ana", "Luis");
         *                          nombres.forEach(String::toUpperCase);
         * 
         * Las referencias a método permiten usar métodos existentes (propios o de librerías) como funciones en lambdas, 
         * sin escribir el cuerpo
         * Pueden usarse tanto para métodos estáticos como no estáticos.
         */
    }
}

/*

¡Claro! Aquí tienes un código completo que muestra ambas formas de funciones anónimas en Java:

Usando clase anónima.
Usando función lambda.

@FunctionalInterface
interface MiFuncion {
    void ejecutar(String mensaje);
}

public class EjemploFuncionesAnonimas {
    
    public static void procesarMensaje(String msg, MiFuncion funcion) {
        System.out.println("Antes de ejecutar la función...");
        funcion.ejecutar(msg);
        System.out.println("Después de ejecutar la función...");
    }

    public static void main(String[] args) {
        // 1. Usando clase anónima
        MiFuncion funcionClaseAnonima = new MiFuncion() {
            @Override
            public void ejecutar(String mensaje) {
                System.out.println("Clase anónima: " + mensaje.toUpperCase());
            }
        };
        
        procesarMensaje("Hola desde clase anónima", funcionClaseAnonima);
        
        System.out.println("------");
            
        // 2. Usando función lambda
        MiFuncion funcionLambda = (mensaje) -> {
            System.out.println("Lambda: " + mensaje.toLowerCase());
        };
        
        procesarMensaje("HOLA DESDE LAMBDA", funcionLambda);
        
        System.out.println("------");
        
        // 3. Pasando lambda directamente sin asignar a variable
        procesarMensaje("Mensaje directo con lambda", m -> System.out.println("Directo: " + m.length()));
    }
}


 */