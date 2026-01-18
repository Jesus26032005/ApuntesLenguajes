public class datos_variables {
    public static void main(String[] args) {
        // Declaración de variables

        //Enteros (VALOR POR DEFAULT ES 0)
        
        //BYTE
        byte tipoByte=127;  //Su maximo es 127, para añdir mas datos se debe de hacer un casteo
        tipoByte=(byte)128; //Casteo de byte
        System.out.println("El tipo de byte es" + tipoByte);

        //SHORT
        short tipoShort=32767; //Su maximo es 32767, para añdir mas datos se debe de hacer su conversion
        tipoShort=(short)32768;
        System.out.println("El tipo short es" + tipoShort);

        //INT
        int tipoInt=2147483647; //Su maximo es 2147483647, igual si se supera nos mandara error
        System.out.println(tipoInt);

        //LONG
        long tipoLong=9223372036854775807L; //Su maximo es 9223372036854775807, para indicar que es de tipo long se coloca L al final
        System.out.println(tipoLong);
        
        //Punto flotante (VALOR POR DEFAULT 0.0 )
        float tipoFloat=35.4F;  //Se debe de indicar que es tipo float colocando una F al final porq sino por default sera double
        double tipoDouble=35.4; //No se necesita indicar que es double pq es el default, este tipo de datos permite mas decimales
        System.out.println(tipoFloat+" Y el otro tipo flotante es "+ tipoDouble);

        //Caracter (valor por default es \u0000, osea 0)
        char tipoChar='A'; //Solo se puede almacenar un caracter del juego de caracteres UNICODE
        tipoChar=65; //Se puede almacenar el valor numerico del caracter pero que sea en formato UNICODE
        System.out.println(tipoChar);

        //Boleano (VALOR POR DEFAULT ES 0)
        boolean tipoBooleano=true; //Solo puede almacenar dos valores true o false
        System.out.println(tipoBooleano);

        //En tipos object su valor por default es NULL
    }    
}
