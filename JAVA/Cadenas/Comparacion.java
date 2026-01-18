public class Comparacion {
    public static void main(String[] args) {
        var cadena1="Hola";
        var cadena2="HOLA";
        var cadena3=new String("HOLA");

        System.out.println("Las cadenas son iguales? "+ (cadena1==cadena2));
        
        System.out.println("Las cadenas son iguales? "+ (cadena2.equals(cadena3)));
    }
}
