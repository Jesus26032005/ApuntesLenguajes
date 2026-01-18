public class DO_WHILE {
    public static void main(String[] args) {
        boolean salida=false;
        int numero=1;
        
        do {
            System.out.println(numero);
            if (numero==5) {
                salida=true;
            }
            numero++;
        } while (!salida);
    }
}
