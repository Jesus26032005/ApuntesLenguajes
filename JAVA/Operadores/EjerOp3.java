import java.util.Scanner;

public class EjerOp3 {
    public static void main(String[] args) {
    final String usuario="ZADDKIEL";
    final String contraseña="EZIO";
    var sc=new Scanner(System.in);
    System.out.println("Ingrese su usuario:");
    String usuarioIngresado=sc.nextLine().trim().toUpperCase();
    System.out.println(usuarioIngresado);
    System.out.println("Ingrese la contraseña");
    String contraseñaIngresada=sc.nextLine().trim().toUpperCase();
    System.out.println(contraseñaIngresada);
    sc.close();
    var Autorizacion= (usuarioIngresado.equals(usuario) && contraseñaIngresada.equals(contraseña));
    System.out.println(Autorizacion);

    }
}
