public class sesion4 {
    public static void main(String[] args) {
        // Estructuras de desicion
        
        /*
        EL IF
         if: Si la condicion es verdadera, se ejecuta el codigo
         if (condicion) {
            codigo
         }
         */

        int num1 = 3;
        int num2 = 5;

        if (num1 > num2) {
            System.out.println(num1 + " es mayor que " + num2);
        }

        /*
        EL IF-ELSE
         if-else: Si la condicion es verdadera, se ejecuta el codigo, si no, se ejecuta el codigo del else
         if (condicion) {
            codigo
         } else {
            codigo
         }
         */

        if (num1 > num2) {
            System.out.println(num1 + " es mayor que " + num2);
        } else {
            System.out.println(num1 + " no es mayor que " + num2);
        }
    }
}
