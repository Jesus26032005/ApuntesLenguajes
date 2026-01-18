public class Inmutabilidad {
    public static void main(String[] args) {
        //Cadena inicial
        String cadena = "Hola, soy un ejemplo de inmutabilidad en Java";
        System.out.println("Cadena inicial: " + cadena);
        cadena="Soy la cadena modificada";
        System.out.println("Cadena modificada con nueva direccion de memoria: " + cadena);
    }
    
}
