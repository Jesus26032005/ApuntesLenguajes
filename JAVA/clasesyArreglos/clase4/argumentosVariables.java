package clasesyArreglos.clase4;

public class argumentosVariables {
    public static void main(String[] args) {
        imprimirNumeros(10,20,30,40,50,60,8,95595);
        imprimirVarios("Juana", 5,10,20,30,50,40,60,80);
    }


    //funcion que acepta un tipo de dato pero infinad de datos
    static void imprimirNumeros(int... numeros) { //Tienen q ser de un mismo tipo de dato, pero esto permite que se accedan mas de un dato
        for(int i=0; i< numeros.length; i++) {
            System.out.println(numeros[i]);
        }
    }

    //funcion que acepta un dato especifico y depsues infinitad de datos de mismo o diferente tipo
    static void imprimirVarios(String nombre, int... numeros) {
        System.out.println(nombre);
            //Ciclo for each sirve para recorrer arreglos
        for (int i : numeros) {
            System.out.println(i);
        }
    }
}
