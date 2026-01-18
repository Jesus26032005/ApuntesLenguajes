package Persona;

public class Persona {
        String nombre,apellido;
        int numero;
        
        public Persona() {
            this("Zaddkiel", "Jesus");
        }

        public Persona(String texto) {
            this(texto, "Martinez");
        }

        public Persona(String nombre, String apellido) {
            this.nombre=nombre;
            this.apellido=apellido;
        }

        public void setNombre (String nombre) {
            this.nombre=nombre;
        }

        public void setApellido(String apellido) {
            this.apellido=apellido;
        }

        public void getnombre() {
            System.out.println("El nombre es: "+nombre);
        }
        
        public void getApellido() {
            System.out.println("El apellido es:"+ apellido);
        }

        void imprimirPersona(){
            System.out.println("Nombre: " + nombre + " " + apellido);
        }
}
