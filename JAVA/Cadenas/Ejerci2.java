import java.util.Scanner;

public class Ejerci2 {
    public static void main(String[] args) {
        System.out.println("Sistema de empleados");
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingrese el nombre del empleado");
        var cadena= scanner.nextLine();

        System.out.println("Ingrese la edad del empleado");
        var lectura= Integer.parseInt(scanner.nextLine());

        System.out.println("Ingrese el salario del empleado");
        var salario= Double.parseDouble(scanner.nextLine());

        System.out.println("Es jefe de departamento");
        var real= Boolean.parseBoolean(scanner.nextLine());

        System.out.println(cadena);
        System.out.println(lectura);
        System.out.println(salario);
        System.out.println(real);

        scanner.close();
    }
    
}
