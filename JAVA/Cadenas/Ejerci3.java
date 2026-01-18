import java.util.Scanner;

public class Ejerci3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Ingrese el nombre de la receta");
        var nombre= sc.nextLine();

        System.out.print("Ingrese los ingredientes separados por coma");
        var ingredientes=sc.nextLine();

        System.out.print("Ingrese el tiempo de cocinacion");
        var tiempo=Integer.parseInt(sc.nextLine());

        System.out.print("Ingrese la dificultad");
        var dificultad=sc.nextLine();
        sc.close();

        System.out.println("El nombre de la receta es " + nombre);
        System.out.println("Los ingredientes son" + ingredientes.replace(",", "\n"));
        System.out.println("El tiempo de cocinacion es " + tiempo + " minutos");
        System.out.println("La dificultad es " + dificultad);
    }
}
