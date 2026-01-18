import java.util.ArrayList;

public class DeclaraAreg {
    public static void main(String[] args) {
        //DECLARACION ARREGLO
        int[] arreglo;
        //INICIALIZACION ARREGLO
        arreglo=new int[5];
        //ASIGNACION VALORES
        arreglo[0]=10;
        arreglo[1]=2;
        arreglo[2]=5;
        arreglo[3]=8;
        arreglo[4]=9;


        //INICIALIZACION Y DECLARACION
        float[] arreglo2=new float[5];  //Al declararse las celdas se inicializan con 0.0f, los valores por defecto de float
        //ASIGNACION VALORES
        arreglo2[0]=10.5f;
        arreglo2[1]=2.5f;
        arreglo2[2]=5.5f;
        arreglo2[3]=8.5f;
        arreglo2[4]=9.5f;

        //ACCESO A ELEMENTOS ARREGLO
        System.out.println(arreglo[0]);
        System.out.println(arreglo[1]);
        System.out.println(arreglo[2]);

        //DECLARACION CON INICIALIZACION
        int[] arreglo3={10,2,5,8,9};
        //ACCESO A ELEMENTOS ARREGLO
        System.out.println(arreglo3[0]);


        //ARREGLO DINAMICO
        ArrayList<Integer>arreglodinamico=new ArrayList<>();
        arreglodinamico.add(10);
        arreglodinamico.add(2);
        arreglodinamico.add(5);
        arreglodinamico.add(11);

        //Impresion arreglo
        for (int entero : arreglodinamico) {
            System.out.println(entero);
        }
    }
}
