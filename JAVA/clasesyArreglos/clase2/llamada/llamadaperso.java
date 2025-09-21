package clasesyArreglos.clase2.llamada;

import clasesyArreglos.clase2.clase.persona;

public class llamadaperso {
    public static void main(String[] args) {
        persona zadd= new persona();
        System.out.println(zadd.getNombre());
        System.out.println(zadd.getApellido());
        System.out.println(zadd.getEmail());
        System.out.println(zadd.getCelular());


        zadd.setNombre("Jesus");
        zadd.setApellido("Alor");
        zadd.setEmail("xddxe3fr");
        zadd.setCelular(554654654);

        System.out.println(persona.obtenerNumeroPersonas());
    }
}
