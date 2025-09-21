package clasesyArreglos.clase6;

// Clase que realiza operaciones aritméticas
class Aritmetica {
    // Método que puede lanzar una excepción, se indica con throws, esto se hace para que arriba se encargen de ella, pero sino
    //aqui mismo se puede usar el try catch
    static int division(int numerador, int denominador) throws ArithmeticException {
        if (denominador == 0) {
            throw new ArithmeticException("Error: División entre cero no permitida");
        }
        return numerador / denominador;
    }
}

// Clase principal para probar excepciones
public class excepciones {
    public static void main(String[] args) {
        int numero1 = 10, numero2 = 0;
        int resultado = 0;

        try {
            // Llamamos a un método que puede lanzar una excepción
            resultado = Aritmetica.division(numero1, numero2);
            System.out.println("Resultado: " + resultado);
        } catch (ArithmeticException e) {
            System.out.println("Ocurrió una excepción: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("Excepción desconocida: " + e.getMessage());
        } finally {
            System.out.println("Finalizando bloque try-catch-finally.");
        }

        System.out.println("Programa continúa...");
    }
}
