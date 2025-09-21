package clasesyArreglos.clase6;
import java.util.LinkedHashMap;
import java.util.Map;

public class mapas {
    public static void main(String[] args) {
        /*un mapa es una coleccion o un arreglo que practicamente es un dicccionario
         * Tipos comunes de Map:
                HashMap: No mantiene el orden de inserción. Es rápido.
                LinkedHashMap: Mantiene el orden de inserción.
                TreeMap: Ordena las claves de forma natural o con un comparador.
         */
        Map<String, Integer> mapa= new LinkedHashMap<>();
        mapa.put("nombre", 5);
        mapa.put("apellido", 30);
        mapa.put("xdd", 10);
        System.out.println("valores del mapa");
    

        for (Map.Entry<String, Integer> entrada : mapa.entrySet()) {
            System.out.println(entrada.getKey() + " tiene " + entrada.getValue() + " años.");
        }
    }
}
