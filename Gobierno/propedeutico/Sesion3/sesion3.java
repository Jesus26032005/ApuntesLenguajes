public class sesion3 {
    public static void main(String[] args) {
        /*
         * COMENTARIOS
         */
        // De una linea
        System.out.println("Hola mundo");
        System.out.println("Hola mundo");
        // Identificadores
        // Los unicos simbolos validos son $ y _
        // No pueden comenzar con un numero
        // Son sensibles a mayusculas y minusculas
        // No pueden ser palabras reservadas
        // No pueden ser reservadas
        int _variable = 1;
        int variable_ = 2;
        int variable$ = 3;
        int variable = 4;
        System.out.println(_variable);
        System.out.println(variable_);
        System.out.println(variable$);
        System.out.println(variable);
        
        // snake_case y camelCase
        // snake_case: Se colocan guiones bajos entre palabras
        // camelCase: Se colocan mayusculas en las palabras iniciales

        // Palabras reservadas
        // Son aquellas que no pueden ser usadas como identificadores
        // ej int, double, String, boolean, case, etc

        // Tipos de datos
        // Son aquellas que definen el tipo de datos que se van a usar
        // ej int, double, String, boolean, case, etc
        // int: Entero
        // double: Decimal
        // String: Cadena de caracteres
        // boolean: True o false

        // Tipos de datos primitivos
        // Datos que java proporciona por defecto
        // int, char, boolean, double, float, text, byte.
        // Ejemplos
        int numero = 1;
        char letra = 'a';
        boolean booleano = true;
        double decimal = 1.1;
        float flotante = 1.1f;
        text texto = "Hola";
        byte numeroByte = 1;
        System.out.println(numero);
        System.out.println(letra);
        System.out.println(booleano);
        System.out.println(decimal);
        System.out.println(flotante);
        System.out.println(texto);
        System.out.println(numeroByte);
        


    }
}