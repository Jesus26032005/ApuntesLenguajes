package Encapsulamiento;

public class Encapsulamiento {
    private int atributo1,atributo2;

    public Encapsulamiento() {
        atributo1=atributo2=0;
    }

    public Encapsulamiento(int valor) {
        atributo1=atributo2=valor;
    }

    public Encapsulamiento(int atributo1,int atributo2) {
        this.atributo1=atributo1;
        this.atributo2=atributo2;
    }

    public void setAtributo1(int atributo1) {
        this.atributo1=atributo1;
    }

    public void setAtributo2(int atributo2) {
        this.atributo2=atributo2;
    }

    public void getAtributo1() {
        System.out.println("El valor del atributo 1 es "+this.atributo1);
    }

    public void getAtributo2() {
        System.out.println("El valor del atributo 2 es "+this.atributo2);
    }

    public void sumar() {
        System.out.println(this.atributo1+this.atributo2);
    }

    public void resta() {
        System.out.println(atributo1-atributo2);
    }

    public void multiplicacion() {
        System.out.println(atributo1*atributo2);
    }

    public void division() {
        System.out.println(atributo1/atributo2);
    }
}