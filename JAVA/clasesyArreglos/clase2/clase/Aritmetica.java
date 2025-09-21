package clasesyArreglos.clase2.clase;

public class Aritmetica {
    private int operador1;
    private int operador2;
    public int sumar() {
        return this.operador1+this.operador2;
    }

    public int resta() {
        return this.operador1-this.operador2;
    }

    public int getoperador1() {
        return operador1;
    }

    public int getoperador2() {
        return operador2;
    }

    public void setoperador2(int sustituto) {
        operador2=sustituto;
    }

    public void setoperador1(int sustituto) {
        this.operador1=sustituto;
    }
}
