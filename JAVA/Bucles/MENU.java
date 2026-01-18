import java.util.Scanner;

public class MENU {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean salida=true;
        do {
            System.out.println("MENU EJEMPLO");
            System.out.println("1. Ejemplo 1");
            System.out.println("2. Ejemplo 2");
            System.out.println("3. Ejemplo 3");
            System.out.println("Ingrese una opcion: ");
            var opcion=Integer.parseInt(sc.nextLine());

            switch (opcion) {
                case 1 -> System.out.println("Hola mundo");
                case 2 -> System.out.println("Hola mundo");
                case 3 -> System.out.println("Hola mundo");
                case 4 -> {salida=false;
                            System.out.println("Adios mundo");
                            }
                default -> System.out.println("XD");
            }
        } while (salida);


        sc.close();
    }
}
