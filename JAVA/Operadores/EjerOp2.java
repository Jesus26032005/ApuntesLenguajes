import java.util.Scanner;

public class EjerOp2 {
    public static void main(String[] args) {
    var sc=new Scanner(System.in);
    System.out.println("Tienes credencial de estudiante");
    var credencialAprobacion=Boolean.parseBoolean(sc.nextLine());
    System.out.println("Cuantos kilometros a la redonda vives?");
    var kilometros=Double.parseDouble(sc.nextLine());
    sc.close();
    var distanciaAprobacion= kilometros<=3;
    
    var resultado= credencialAprobacion|| distanciaAprobacion;
    System.out.println("Autorizacion para prestamos: "+resultado);

    }
}
