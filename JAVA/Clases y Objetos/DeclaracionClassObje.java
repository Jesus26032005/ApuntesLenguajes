public class DeclaracionClassObje {
    String nombre,apellido;
    int numero;

    void imprimirPersona(){
        System.out.println("Nombre: " + nombre + " " + apellido);
    }

    public static void main(String[] args) {
        var persona = new DeclaracionClassObje();
        persona.nombre="jUAN";
        persona.apellido="lopez";

        persona.imprimirPersona();
    }
}