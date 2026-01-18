public class EjerS2 {
    public static void main(String[] args) {
        int estacion=5;

        switch (estacion){
            case 9,10-> System.out.println("Tu calificacion es una A");
            case 8 -> System.out.println("Tu calificacion es una B");
            case 7 -> System.out.println("Tu calificacion es una C");
            case 6 -> System.out.println("Tu calificacion es una D");
            case 0,1,2,3,4,5 -> System.out.println("Tu calificacion es una F");
            default -> System.out.println("No hay calificacion valida para el numero");
        }
    }
}