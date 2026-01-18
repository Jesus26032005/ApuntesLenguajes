class aritmetica {
    int atributo1,atributo2;

    public aritmetica() {
        atributo1=atributo2=0;
    }

    public aritmetica(int valor) {
        atributo1=atributo2=valor;
    }

    public aritmetica(int valor1,int valor2) {
        atributo1=valor1;
        atributo2=valor2;
    }

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


public class Constructores {
    public static void main(String[] args) {
        aritmetica obj1 = new aritmetica();
        obj1.sumar();

        aritmetica obj2= new aritmetica(10);
        obj2.sumar();

        aritmetica obj3= new aritmetica(10,20);
        obj3.sumar();
    }
}