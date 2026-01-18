public class ELSEIFELSE {
    public static void main(String[] args) {
        int edad=100;
        if(edad<=18){
            System.out.println("Eres un niño");
        } else if (edad>=18 && edad<=65) {
            System.out.println("Eres un adulto");
        } else {
            System.out.println("Eres un anciano");
        }
    }
}
