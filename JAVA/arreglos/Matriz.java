public class Matriz {
    public static void main(String[] args) {
        //DECLARACION DE LAS DOS FORMAS
        int[][] matriz = new int[3][3];
        var matriz2=new int[3][3];

        //INICIALIZACION
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                matriz[i][j]=i+j;
                matriz2[i][j]=i+j;
                }
                }

        //IMPRESION VALORES
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(matriz[i][j] + " ");
                System.out.print(matriz2[i][j] + " ");
                }
        }
    }
}
