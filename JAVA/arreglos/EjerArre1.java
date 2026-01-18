import java.util.Scanner;

public class EjerArre1 {
    public static void main(String[] args) {
        var sc=new Scanner(System.in);
        System.out.println("Ingrese las calificaciones a ingresar");
        int noCalif=Integer.parseInt(sc.nextLine());
        float[] calif=new float[noCalif];
        for (int i = 0; i < noCalif; i++) {
            System.out.print("Ingrese el valor de la calificación "+(i+1));
            calif[i]=Float.parseFloat(sc.nextLine());
        }
        sc.close();

        float promedio=0.0f;
        for (float cali:calif) {
            promedio+=cali;
        }
        promedio/=noCalif;

        System.out.println("EL promedio de las calificaciones es: "+promedio);
    }
}
