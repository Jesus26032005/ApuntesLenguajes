import java.util.Scanner;

public class TERNIARIO {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        var numero= Integer.parseInt(sc.nextLine());
        sc.close();
        var xd= (numero==18)? "Mayor de edad" : "MENOR DE EDAD";
        System.out.println(xd);
        
        //TERNIARIO ANIDADO
        numero = 0;
        var resultado = (numero > 0) ? "Positivo" : (numero < 0) ? "Negativo" : "Cero";
        System.out.println("\nEl número " + numero + " es " + resultado);
    }
}
