public class Mas_concatenacion {
    public static void main(String[] args) {
        var cadena1="hola";
        var cadena2="mundo";

        var cadena_conca=cadena1.concat(cadena2);
        var cadena_build=new StringBuilder().append(cadena1).append(cadena2).append(cadena1).append(cadena1).toString().toUpperCase();
        var cadena_buffer=new StringBuffer().append(cadena1).append(cadena2).toString().toUpperCase();
        var cadena_join=String.join(" ",cadena1,cadena2);

        System.out.println(cadena_conca);
        System.out.println(cadena_build);
        System.out.println(cadena_buffer);
        System.out.println(cadena_join);
    }
}