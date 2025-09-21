package arreglos;

import java.util.ArrayList;
import java.util.Scanner;

public class arreglo1 {
    public static void main(String[] args) {
        ArrayList<Integer> Zaddkiel= new ArrayList<>();
        Zaddkiel.add(5);
        Zaddkiel.add(120);
        Zaddkiel.add(500);
        Zaddkiel.add(2500);
        /*

        int[] enteros= new int[3];
        enteros[0]=5;
        enteros[1]=10;
        enteros[2]=15;

        Scanner scan= new Scanner(System.in);
        scan.close();

        int[] enteros2= new int[5];
        enteros2=enteros.clone();

        for (int i = 0; i < enteros2.length; i++) {
            System.out.println(i);
        }

        for (int i = 0; i < Zaddkiel.size(); i++) {
            System.out.println(Zaddkiel.get(i));
        }

        */
        Scanner scanf= new Scanner(System.in);
        System.out.println("Ingrese el numero de calificaciones a ingresar");
        int numero= Integer.parseInt(scanf.nextLine());
        
        float[] calificaciones= new float[numero];
        for (int i = 0; i < calificaciones.length; i++) {
            System.err.print("Ingrese el valor de la primer calificacion");
            calificaciones[i]= Float.parseFloat(scanf.nextLine());
        }

        System.err.println("El promedio de calificaciones es:" + 5);

        scanf.close();
    

    }
}
