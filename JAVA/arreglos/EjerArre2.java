public class EjerArre2 {
    public static void main(String[] args) {
        var matriz=new int[3][3];

        //INICIALIZACION
        matriz[0][0]=100;
        matriz[0][1]=200;
        matriz[0][2]=300;
        matriz[1][0]=400;
        matriz[1][1]=500;
        matriz[1][2]=600;
        matriz[2][0]=700;
        matriz[2][1]=800;
        matriz[2][2]=900;
        
        //OPERACION DIAGONAL
        int sumaDiagonalPrincipal=0;

        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                if (i==j) {
                    sumaDiagonalPrincipal+=matriz[i][j];
                }
            }
        }

        System.out.println("La suma total es: "+sumaDiagonalPrincipal);


    }
}
