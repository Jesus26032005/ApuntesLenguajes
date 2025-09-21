package clasesyArreglos.clase5.clases;

/*
 Una clase puede extender una sola clase abstracta, pero puede implementar múltiples interfaces al mismo tiempo.
 s interfaces originalmente sólo definían métodos abstractos, aunque desde Java 8 pueden incluir métodos default con
  implementación y métodos estáticos.
 */

public interface interfaz { 
    void llorarPorsemestrE();

    //metodo por default
    default void saludarwe() {
        System.out.println("buenas tardes xd");
    }
}
