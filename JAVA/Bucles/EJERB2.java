import java.util.Scanner;

public class EJERB2 {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        String cadena;
        do {
            System.out.println("Ingrese una cadena de texto de mas de 6 caracteres: ");
            cadena=sc.nextLine();
        } while (cadena.length()<6);

        sc.close();
        System.err.println("Se ingreso una cadena valida");
    }
}
