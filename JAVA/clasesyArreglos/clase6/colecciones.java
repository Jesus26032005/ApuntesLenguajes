package clasesyArreglos.clase6;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/* CONCEPTOS
 * UNA COLECCION REPRESENTA UN GRUPO DE OBJETOS ALGUNAS COLECCIONES PERMITEN ELEMENTOS DUPLICADOS Y OTRAS NO, ALGUNAS TIENEN SUS
 * ELEMENTOS ORDENADOS Y OTRAS NO
 * 
 * Ejemeplo java.util
 * interface colecction: Tiene las interfaces hijas de list y set, y estas tienen clases como arrayList o sortedSet
 * interface map: tiene la clase hashmap que nos ayuda a los hasheos
 * 
 * List en Java es una interfaz de la colección de datos que representa una lista ordenada de elementos. A diferencia de otros tipos de colecciones, 
 * una List permite elementos duplicados y mantiene el orden de inserción.
 * List<Tipo que es clase envolvente o objeto> nombreLista = new ArrayList<>();
 * 
 * ✅ 1. Importar List y su implementación (ej. ArrayList)
import java.util.List;
import java.util.ArrayList;
✅ 2. Declarar y crear una lista
List<Tipo> nombreLista = new ArrayList<>();
Ejemplos:
List<String> nombres = new ArrayList<>();
List<Integer> numeros = new ArrayList<>();
✅ 3. Agregar elementos
nombres.add("Juan");
nombres.add("Ana");
✅ 4. Acceder a elementos (por índice)
String primerNombre = nombres.get(0); // "Juan"
✅ 5. Modificar un elemento
nombres.set(1, "Lucía"); // Reemplaza "Ana" con "Lucía"
✅ 6. Eliminar un elemento
nombres.remove(0); // Elimina el primer elemento ("Juan")
✅ 7. Recorrer la lista
for (String nombre : nombres) {
    System.out.println(nombre);}
✅ 8. Tamaño de la lista
int cantidad = nombres.size();
✅ 9. Verificar si contiene un elemento
boolean existe = nombres.contains("Lucía"); // true o false
 */

public class colecciones {
    public static void main(String[] args) {
        //Listas, tienen un tipo de dato
        List<String> milista= new ArrayList<>(); //list es una clase abstracta
        milista.add("Lunes");  
        milista.add("xd");     

        //otra forma de crerar listas
        List<String> nombres= Arrays.asList("hola", "xd");
        nombres.forEach(System.out::printf);
    }
}
