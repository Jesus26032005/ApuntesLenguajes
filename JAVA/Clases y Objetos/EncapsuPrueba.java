import Encapsulamiento.Encapsulamiento;

public class EncapsuPrueba {
    public static void main(String[] args) {
        // Creamos un objeto de la clase encapsulamiento
        var encapsulamiento = new Encapsulamiento(5,5);
        // Llamamos al método para obtener el valor de la variable privada
        encapsulamiento.getAtributo1();
        encapsulamiento.getAtributo2();

        encapsulamiento.setAtributo1(20);
        encapsulamiento.setAtributo2(50);
        encapsulamiento.sumar();
    }
}
