package Persona;
// Superclase (Clase Padre)
class Animal {
    String nombre;

    protected void hacerSonido() {
        System.out.println("El animal hace un sonido");
    }
}

// Subclase (Clase Hija)
class Perro extends Animal {
    void ladrar() {
        System.out.println("El perro ladra");
    }
}

public class Herencia {
    public static void main(String[] args) {
        Perro miPerro = new Perro();
        miPerro.nombre = "Firulais"; // Heredado de Animal
        miPerro.hacerSonido();       // Heredado de Animal
        miPerro.ladrar();            // Método propio de Perro
    }
}
