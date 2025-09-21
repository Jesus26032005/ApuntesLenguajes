package clasesyArreglos.clase3.clase;

public class perro extends animal {
    public String toString() {
        return String.valueOf(super.edad);
    }

        public void imprimirMensaje(double mensaje) {
        System.out.println(mensaje);
    }


    @Override
    public void aullar() {
        super.aullar();
    }
}
