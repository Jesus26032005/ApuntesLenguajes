public class subcadenas {
public static void main(String[] args) {
    String cadena = "hola mundo hola";

    var subcadena=cadena.substring(5);
    var subcadena2=cadena.substring(2,5);
    var subcadena3pos=cadena.indexOf("hola");
    var subcadena4pos=cadena.lastIndexOf("hola");

    System.out.println(subcadena);
    System.out.println(subcadena2);
    System.out.println(subcadena3pos);
    System.out.println(subcadena4pos);
    
    var cadenaSubReplace=cadena.replace("hola", "saludos");
    System.out.println(cadenaSubReplace);
    }
}
