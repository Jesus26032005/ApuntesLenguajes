import java.util.Scanner;

public class LeerTiposDatos {
    public static void main(String[] args) {
        // Leer distintos tipos de datos
        // Leer un tipo int
        var consola = new Scanner(System.in);
        System.out.print("Ingresa tu edad: ");
        var edad = consola.nextInt();
        System.out.println("edad = " + edad);
        // Leer un tipo double
        System.out.print("Ingresa tu altura: ");
        var altura = consola.nextDouble();
        System.out.println("altura = " + altura);
        // Consumimos el caracter de salto de linea
        consola.nextLine();
        // Leer un tipo String
        System.out.print("Ingresa tu nombre: ");
        var nombre = consola.nextLine();
        System.out.println("nombre = " + nombre);
        // Conversion de datos
        consola.close();


        //FORMA MAS ELABORADA CON CONVERSION DE DATOS USANDO CLASES ENVOLVENTES
        var escaneo=new Scanner(System.in);
        var edad2=Integer.parseInt(escaneo.nextLine());
        var altura2=Double.parseDouble(escaneo.nextLine());
        System.out.println(edad2);
        System.out.println(altura2);
        
        //FORMA CON PRINTLN INCLUIDO
        System.out.println("El dato escaneado en tipo int es: "+ Integer.parseInt(escaneo.nextLine()));
        escaneo.close();

    }
}
