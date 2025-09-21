from Conexion import Conexion
from Persona import Persona
from looginInf import log

class PersonaDao:
    """
    Dao (Data Acces Object)
    Clase para manejar las operaciones de acceso a datos de la entidad Persona.
    Esta clase define las operaciones básicas de acceso a datos como seleccionar, insertar, actualizar y eliminar registros de la tabla Persona.
    CRUD (Create, Read, Update, Delete) para la entidad Persona.
    """
    _seleccionar= "SELECT * FROM Persona ORDER BY id_persona ASC"
    _insertar= "INSERT INTO Persona (nombre, apellido, email) VALUES (%s, %s, %s)"
    _actualizar= "UPDATE Persona SET nombre = %s, apellido = %s , email = %s WHERE id_persona = %s"
    _eliminar= "DELETE FROM Persona WHERE id_persona = %s"

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(cls._seleccionar)
                registros= cursor.fetchall()
                personas=[]
                for registro in registros:
                    persona= Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas
    
    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion() as conn:
            with conn.cursor() as cursor:
                try:
                    log.debug(f'Persona a insertar:{persona}')
                    valores= (persona.nombre, persona.apellido, persona.email)
                    cursor.execute(cls._insertar, valores)
                    return cursor.rowcount
                except Exception as e:
                    log.error("Error al hacer la insercion")

    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtenerConexion() as conn:
            with conn.cursor() as cursor:
                log.debug(f'Id a actualizar {persona.id_persona}')
                valores= (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._actualizar, valores)
                return cursor.rowcount

    @classmethod
    def eliminar(cls, id_persona):
        with Conexion.obtenerConexion() as conn:
            with conn.cursor() as cursor:
                log.debug(f'Id a eliminar {id_persona}')
                cursor.execute(cls._eliminar, (id_persona,))
                return cursor.rowcount

if __name__=="__main__":
    persona1= Persona(nombre="pancho", apellido="martinez", email="pancho@gmail.com", id_persona=16 )
    log.debug(f"Numero de registros exitoos insertado {PersonaDao.eliminar(15)}")
                