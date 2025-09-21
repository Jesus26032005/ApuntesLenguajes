package archivos.clase;
import java.io.*;

public class archivo {
    public static void main(String[] args) {
        String nombreArchivo= "prueba.txt";
        File archivo = new File(nombreArchivo);

        if (archivo.exists()) {
            System.out.println("El archivo ya existe");
        }

        /*LECTURA ARCHIVO LINEA POR LINEA
        try {
            System.out.println("Contenido del archivo para lectura");
            BufferedReader entrada= new BufferedReader(new FileReader(archivo));
            String linea= entrada.readLine();
            while (linea!=null) {
                System.out.println(linea);
                linea=entrada.readLine();
            }
            entrada.close();
        } catch (Exception e) {
            System.out.println("Error al leer archivo");
        }*/

        /*LECTURA DE TODAS LAS LINEAS DEL ARCHIVO EN UNA SOLA PASADA SIN WHILE 
        try {
            List<String> lineas= Files.readAllLines(Paths.get(nombreArchivo));
            lineas.forEach(System.out::println);
        } catch(Exception e) {
            System.out.println("Error al leer archivo completamente");
        }*/

        /*CREACION ARCHIVO
        try {
            PrintWriter salida= new PrintWriter(new FileWriter(archivo));
            salida.close();
            System.out.println("Se creo el archivo correctamente");
        } catch(Exception e) {
            System.out.println("Error al crear el archivo");
        }
        */
    
        /*ESCRITURA EN ARCHIVO
        try {
            PrintWriter salida= new PrintWriter(new FileWriter(archivo,true));      //Se añade true o false para saber si se cobreescrie o añade
            salida.println("xddddddddddddddddddddddddddddddd");
            salida.close();            
        } catch (Exception e) {
            System.out.println("Error al escribir en el archivo");
        }*/
    }
}

/*DESCRIPCION DE Q HACE CADA COSA
 * 
 * 1. Abrir archivo para ESCRIBIR

FileWriter fw = new FileWriter("archivo.txt"); // Abre archivo para escribir (sobrescribe)
PrintWriter pw = new PrintWriter(fw);           // Envuelve para imprimir fácilmente (println, printf)

- FileWriter abre el archivo físico para escribir caracteres.
- PrintWriter añade métodos cómodos para escribir texto formateado.
- Si quieres agregar al archivo sin borrar, usa:
FileWriter fw = new FileWriter("archivo.txt", true); // true para agregar (append)
caso contrario se usa false
2. Escribir texto
pw.println("Hola Mundo");       // Escribe línea con salto
pw.printf("Número: %d\\n", 10);  // Escribe texto formateado
- println agrega automáticamente salto de línea.
- printf permite formatear texto (números, decimales, etc.).

3. Cerrar archivo (muy importante)
pw.close();  // Cierra PrintWriter y FileWriter, libera recursos
- Siempre cierra el archivo para asegurar que se guarden los datos y se liberen recursos.

4. Abrir archivo para LEER
FileReader fr = new FileReader("archivo.txt");   // Abre archivo para lectura
BufferedReader br = new BufferedReader(fr);      // Envuelve para leer líneas completas eficientemente
- FileReader abre el archivo físicamente.
- BufferedReader permite leer línea por línea con readLine().
5. Leer texto línea por línea
String linea;
while ((linea = br.readLine()) != null) {
    System.out.println(linea);  // Procesa cada línea leída
}
- readLine() devuelve una línea completa o null si se termina el archivo.

6. Cerrar archivo de lectura
br.close();  // Cierra BufferedReader y FileReader
¿Por qué hacerlo así?

Paso                       | Explicación
-------------------------- | -----------------------------------------------------------------------------
Usar FileWriter + PrintWriter | FileWriter abre el archivo para escribir, PrintWriter facilita escritura con métodos como println y printf.
Usar FileReader + BufferedReader | FileReader abre el archivo para leer, BufferedReader optimiza la lectura y permite leer líneas completas fácilmente.
Cerrar los flujos           | Para evitar pérdida de datos y liberar recursos del sistema, siempre se deben cerrar.
 */

 /*DESCRIPCION CADA CLASE
  * 1. FileWriter
Función: Abre un archivo para escribir caracteres en él.
Lo que hace:
Se conecta directamente con el archivo físico y escribe texto básico.
Limitación: No tiene métodos para escribir líneas completas con saltos de línea fácilmente.
Ejemplo de uso:
FileWriter fw = new FileWriter("archivo.txt");
fw.write("Texto simple");
fw.close();

2. PrintWriter
Función: Facilita la escritura de texto formateado y líneas completas.
Lo que hace:
Envuelve a un Writer (como FileWriter) y te da métodos como print(), println(), printf().
Ventaja: Puedes escribir texto, números, y formatos de manera sencilla y con saltos de línea automáticos.
Ejemplo de uso:
java
Copiar
Editar
PrintWriter pw = new PrintWriter(new FileWriter("archivo.txt"));
pw.println("Hola Mundo");
pw.printf("Número: %d\n", 10);
pw.close();

3. FileReader
Función: Abre un archivo para leer caracteres.
Lo que hace:
Se conecta directamente con el archivo y permite leer carácter por carácter.
Limitación: Leer carácter por carácter es lento y poco práctico para texto con líneas.
Ejemplo de uso:
FileReader fr = new FileReader("archivo.txt");
int c = fr.read();
fr.close();

4. BufferedReader
Función: Facilita la lectura de texto línea por línea y mejora el rendimiento.
Lo que hace:
Envuelve a un Reader (como FileReader) y agrega un buffer en memoria para leer más rápido. Además tiene el 
método readLine() que devuelve una línea completa.
Ventaja: Leer líneas completas es mucho más cómodo para archivos de texto.
Ejemplo de uso:
BufferedReader br = new BufferedReader(new FileReader("archivo.txt"));
String linea = br.readLine();
br.close();
  */