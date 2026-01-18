class Ejemplo {
    static int contador = 0; // Variable compartida por todas las instancias
    
    Ejemplo() {
        contador++;
    }
}
public class VariablesEstati {
    public static void main(String[] args) {
        new Ejemplo();
        new Ejemplo();
        new Ejemplo();
        System.out.println(Ejemplo.contador); // Salida: 3
    }
}
