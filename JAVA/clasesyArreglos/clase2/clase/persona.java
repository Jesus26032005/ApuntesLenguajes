package clasesyArreglos.clase2.clase;

public class persona {
    static int numeroPersonas=0;
    private String nombre;
    private String apellido;
    private String email;
    private int celular;

    public static int obtenerNumeroPersonas() {
        return persona.numeroPersonas;
    }

    public persona() {
        this.nombre="Zaddkiel";
        this.apellido="Martinez";
        this.email="XD";
        this.celular=555555;
    }

    public void setNombre(String sustitutoNombre){ 
        this.nombre=sustitutoNombre;
    }

    public void setApellido(String sustitutoApellido) {
        this.apellido=sustitutoApellido;
    }

    public void setEmail(String sustitutoEmail) {
        this.email=sustitutoEmail;
    }

    public void setCelular(int sustitutoNumero) {
        this.celular= sustitutoNumero;
    }

    public String getNombre() {
        return this.nombre;
    }

    public String getApellido() {
        return this.apellido;
    }

    public String getEmail() {
        return this.email;
    }

    public int getCelular() {
        return this.celular;
    }
}
