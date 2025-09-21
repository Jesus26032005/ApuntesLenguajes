package clasesyArreglos.clase2.llamada;

import clasesyArreglos.clase2.clase.Aritmetica;

public class llamadaAritm {
    public static void main(String[] args) {
        Aritmetica arti1= new Aritmetica();
        arti1.setoperador1(220);
        arti1.setoperador2(10);
        System.err.println(arti1.getoperador1());
        System.out.println(arti1.getoperador2());
    }
}