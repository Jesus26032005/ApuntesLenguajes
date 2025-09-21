package clasesyArreglos.clase1.clase;

public class clase {
    public int atributo1;
    public int atributo2;

    public clase() {
        atributo1=5;
        atributo2=10;
    }
    
    public clase(int uno, int dos) {
        this.atributo1=uno;
        this.atributo2=dos;
    }

    @Override
    public String toString() {
        return "Persona con valor atributo1 de "+ atributo1 + " y atributo 2 es " + atributo2;
    }
    
}
