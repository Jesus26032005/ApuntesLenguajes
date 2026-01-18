public class Ejerci1 {
    public static void main(String[] args) {
        String nombre="Zaddkiel de Jesus Martinez Alor";
        String empresa="Global Mentoring";
        String domonio="com.mx";

        var correo=new StringBuilder().append(nombre.toLowerCase().replace(" ", ".")).append("@")
        .append(empresa.substring(0, empresa.indexOf(" "))).append(empresa.substring(empresa.indexOf(" ")+1))
        .append(".").append(domonio);

        System.out.println(correo);
        System.out.println(correo.length());

        var correo2=new StringBuilder().append(nombre.toLowerCase().replace(" ", ".")).append("@")
        .append(empresa.replace(" ", ""))
        .append(".").append(domonio);

        System.out.println(correo2.length());
    }
    
}
