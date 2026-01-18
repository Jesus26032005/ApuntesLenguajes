public class Metodos {
    public static void main(String[] args) {
        var cadena1="Hola mundo";

        var longitud=cadena1.length();
        var reemplazo=cadena1.replace("Hola", "MUNDO");
        var mayusculas=cadena1.toUpperCase();
        var minusculas=cadena1.toLowerCase();

        System.out.println(longitud);
        System.out.println(reemplazo);
        System.out.println(mayusculas);
        System.out.println(minusculas);
    }
}
