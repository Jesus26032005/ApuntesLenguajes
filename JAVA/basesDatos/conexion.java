import java.sql.Connection;
import java.sql.DriverManager;

public class conexion {
    public static Connection getConexion() {
        Connection conexion = null;
        //String baseDatos="zona_fit_db";
        String url="jdbc:mysql://localhost:3306/zona_fit_db";
        String usuario="root";
        String pwd="zadd";
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            conexion = DriverManager.getConnection(url, usuario, pwd);

        } catch (Exception e) {
            System.out.println("Error al conectarse a la base de datos");
        }
        return conexion;
    }
}
