import java.util.Scanner;
import java.util.Random;

public class EJERB3 {
    public static void main(String[] args) {
        boolean flag=true;
        
        do {
            System.out.println("Ingrese el numero a adivinar entre 1 y 50");
            var numero_aleatorio=new Random();
            var sc = new Scanner(System.in);
            var numero_aleatorio_int=numero_aleatorio.nextInt(10)+1;
            var numero_usuario=Integer.parseInt(sc.nextLine());
            if (numero_usuario==numero_aleatorio_int) {
                flag=false;
                sc.close();
            }
            
        } while (flag);
    }
}
