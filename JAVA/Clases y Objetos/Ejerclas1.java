class aritmeticaa {
    int atributo1,atributo2;

    void sumar() {
        System.out.println(atributo1+atributo2);
    }

    void resta() {
        System.out.println(atributo1-atributo2);
    }

    void multiplicacion() {
        System.out.println(atributo1*atributo2);
    }

    void division() {
        System.out.println(atributo1/atributo2);
    }
}



public class Ejerclas1 {
    public static void main(String[] args) {
        var objeto = new aritmeticaa();
        objeto.atributo1=5;
        objeto.atributo2=10;

        objeto.sumar();
    }
}
