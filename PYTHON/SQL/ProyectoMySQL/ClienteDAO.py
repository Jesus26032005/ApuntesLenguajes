from  Conexion import Conexion
from Cliente import Cliente

class ClienteDAO:
    senteniaSelect = "SELECT * FROM persona"    
    senteniaInsert = "INSERT INTO persona(nombre, apellido, membresia) VALUES(%s, %s, %s)"
    senteniaUpdate = "UPDATE persona SET nombre=%s, apellido=%s, membresia=%s WHERE id_cliente=%s"
    senteniaDelete = "DELETE FROM persona WHERE id_cliente=%s"

    @classmethod
    def seleccionar(cls):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = conexion.cursor()
            cursor.execute(cls.senteniaSelect)
            registros = cursor.fetchall()
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f"Error al seleccionar clientes: {e}")
            return []
        
    @classmethod
    def insertar(cls, cliente):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.email)
            cursor.execute(cls.senteniaInsert, valores)
            Conexion.cerrarConexion(conexion)
            return cursor.rowcount
        except Exception as e:
            print(f"Error al insertar cliente: {e}")
            return 0
    
    @classmethod
    def actualizar(cls, cliente):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.email, cliente.idCliente)
            cursor.execute(cls.senteniaUpdate, valores)
            Conexion.cerrarConexion(conexion)
            return cursor.rowcount
        except Exception as e:
            print(f"Error al actualizar cliente: {e}")
            return 0

    @classmethod
    def eliminar(cls, idCliente):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = conexion.cursor()
            cursor.execute(cls.senteniaDelete, (idCliente,))
            Conexion.cerrarConexion(conexion)
            return cursor.rowcount
        except Exception as e:
            print(f"Error al eliminar cliente: {e}")
            return 0

if __name__ == "__main__":
    print(ClienteDAO.insertar(Cliente(nombre="Juan", apellido="Pérez", email="juan.perez@example.com")))