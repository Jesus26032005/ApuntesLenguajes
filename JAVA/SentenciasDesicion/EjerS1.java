import java.util.Scanner;

public class EjerS1 {
    public static void main(String[] args) {
        final float MONTO_MINIMO=1000.0f;
        Scanner sc = new Scanner(System.in);
        System.out.printf("Introduzca el monto de la cuenta: ");
        float monto=Float.parseFloat(sc.nextLine());
        System.out.printf("Es miembro de la tienda (true/false): ");
        boolean esMiembro=Boolean.parseBoolean(sc.nextLine());
        sc.close();

        if (esMiembro && monto>=MONTO_MINIMO) {
            System.out.println("Es merecedor de descuento");
            System.out.println("Su descuento es de %.2f".formatted(monto*0.10));
        } else if (esMiembro && monto<MONTO_MINIMO) {
            System.out.println("Es merecedor de descuento");
            System.out.println("Su descuento es de %.2f".formatted(monto*0.05));
        } else {
            System.out.println("No merece descuento");
            System.out.println("Su total es %.2f".formatted(monto));
        }
    }
    
}
