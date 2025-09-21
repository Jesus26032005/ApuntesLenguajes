package clasesyArreglos.clase3.llamada;
import clasesyArreglos.clase3.clase.*;

public class llamadaPerro {
    public static void main(String[] args) {
        perro perrxd= new perro();
        System.out.println(perrxd);
        perrxd.aullar();
        perrxd.imprimirMensaje("xddd");
        perrxd.imprimirMensaje(10);
        perrxd.imprimirMensaje(10.5);
        System.out.println(perrxd instanceof animal);
        
    }
}
