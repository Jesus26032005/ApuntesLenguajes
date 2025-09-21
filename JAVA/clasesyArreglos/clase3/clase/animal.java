package clasesyArreglos.clase3.clase;

public class animal {
    protected int edad;

    public animal() {
        edad=1000;
    }

    public void imprimirMensaje(int mensaje) {
        System.out.println(mensaje);
    }

    public void imprimirMensaje(String mensaje){ 
        System.out.println(mensaje);
    }
    public void aullar() {
        System.out.println("auuuuxd");
    }
}