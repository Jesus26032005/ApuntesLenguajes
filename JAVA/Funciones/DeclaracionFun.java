public class DeclaracionFun {
    
    //FUNCION CON METODO ESTATICO
    public static int suma(int a, int b) {
        return a+b;
    }

    //FUNCION SIN METODO ESTATICO
    public int resta(int a,int b) {
        return a-b;
    }


    public static void main(String[] args) {
        //INVOCACION METODO ESTATICO
        System.out.println(suma(5, 5));
        DeclaracionFun resta= new DeclaracionFun();
        System.out.println(resta.resta(5, 4));
    }
    
}