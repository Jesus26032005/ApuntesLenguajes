import java.util.Scanner;

public class ValorPosi {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un numero");
        var numero=Double.parseDouble(sc.nextLine());
        sc.close();

        if (numero<0) {
            System.out.println("El numero es negativo");
        } else if (numero==0) {
            System.out.println("El numero es cero");
        } else {
            System.out.println("El numero es positivo");
        }

    }
}
