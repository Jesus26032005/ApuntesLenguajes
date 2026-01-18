import java.util.Random;
import java.util.Scanner;

public class Ejerci4 {
    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    
    System.out.println("GENERADOR DE ID UNICO");
    System.out.print("Ingrese su nombre: ");
    var nombre=sc.nextLine().substring(0,2).toUpperCase();
    System.out.print("Ingrese su apellido: ");
    var apellido=sc.nextLine();
    System.out.print("Ingrese su edad: ");
    var edad=sc.nextLine();
    sc.close();

    System.out.println("Generando ID aleatorio");
    Random aleatorio = new Random();
    var numero= String.format("%04d", aleatorio.nextInt(9999)+1);
    
    System.out.println("El numero aleatorio es"+ nombre
    +apellido.substring(0,2).toUpperCase()
    +edad.substring(2,edad.length())+ numero);
    }
}
