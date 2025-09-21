package clasesyArreglos.clase5.clases;
//Para ser una clase java beans se usa la interfaz seriablisable, se usa un constructor vacio, se usan getter y setter y ya
import java.io.Serializable;

public class clasepadre extends claseAbstracta implements interfaz, Serializable{
    public clasepadre(){};
    
    public void dibujar() {
        System.out.println("hola we");
    }

    public void calcularArea() {
        System.out.println("area we");
    }

    public void llorarPorsemestrE() {
        System.out.println("lloro xd");
    }
}
