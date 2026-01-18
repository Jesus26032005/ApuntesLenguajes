import java.util.Scanner;

public class EjerOp1 {
    public static void main(String[] args) {
    final int MAX = 100;
    final int MIN =0;
    Scanner sc=new Scanner(System.in);
    System.out.print("Ingrese un valor de numero entre 0 y 100: ");
    var escaneado=Integer.parseInt(sc.nextLine());
    sc.close();
    System.out.println("El valor obtenido esta entre el rango: " + (escaneado>=MIN && escaneado<=MAX));

}
}
