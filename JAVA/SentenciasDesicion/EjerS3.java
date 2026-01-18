import java.util.Scanner;

public class EjerS3 {
    public static void main(String[] args) {
    var sc=new Scanner(System.in);
    
    System.out.printf("Ingrese el tipo de envio (Nacional o Internacional): ");
    var tipoEnvio=sc.nextLine().trim().toUpperCase();
    System.out.printf("Ingrese el pedo en KG de su paquete: ");
    var pesoPaquete=Float.parseFloat(sc.nextLine());
    sc.close();

    if (tipoEnvio.equals("INTERNACIONAL")) {
        System.out.printf("El costo de su paquete de %.2f kg es de %.2f", pesoPaquete, pesoPaquete*10);
    } else if (tipoEnvio.equals("NACIONAL")) {
        System.out.printf("El costo de su paquete de %.2f kg es de %.2f",pesoPaquete,pesoPaquete*20);
    } else {
        System.out.println("Tipo de envio invalido");
    }
    }
}