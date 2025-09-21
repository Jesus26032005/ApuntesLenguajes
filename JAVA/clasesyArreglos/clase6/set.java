package clasesyArreglos.clase6;
import java.util.TreeSet;
import java.util.Set;

public class set {
    public static void main(String[] args) {
        /*Un set es una coleccion ordenada que no acepta elementos duplicados
            Tipos comunes de Set:
            HashSet: No mantiene orden, rápido para operaciones básicas.
            LinkedHashSet: Mantiene el orden de inserción.
            TreeSet: Mantiene los elementos ordenados de forma natural o con un comparador.
        */
        Set<String> conjunto = new TreeSet<>();
        conjunto.add("Carlos");
        conjunto.add("Carlos");
        conjunto.add("Karla");
        conjunto.add("Victoria");

        System.out.println("Elementos del Set");
        conjunto.forEach(System.out::println);

        conjunto.remove("Karla");
        System.out.println("\nNuevos Elementos del Set");
        conjunto.forEach(System.out::println);
    }
}
