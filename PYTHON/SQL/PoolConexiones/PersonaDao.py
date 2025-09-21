import cursorDePool
from Persona import Persona

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
        with cursorDePool.cursorDePool() as cursor: #Nota cuando usamos una clase con el with, es necesario que esta tenga los metodos __enter__ y __exit__ porque sino mandara error
            cursor.execute(cls._seleccionar)
            registros= cursor.fetchall()
            personas=[]
            for registro in registros:
                persona= Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas
    
    @classmethod
    def insertar(cls, persona):
        with cursorDePool.cursorDePool() as cursor:
            try:
                print(f'Persona a insertar: {persona}')
                valores= (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._insertar, valores)
                return cursor.rowcount
            except Exception as e:
                print("Error al hacer la inserción:", e)

    @classmethod
    def actualizar(cls, persona):
        with cursorDePool.cursorDePool() as cursor:
            try:
                print(f'Id a actualizar {persona.id_persona}')
                valores= (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._actualizar, valores)
                return cursor.rowcount
            except Exception as e:
                print("Error al hacer la actualización:", e)

    @classmethod
    def eliminar(cls, id_persona):
        with cursorDePool.cursorDePool() as cursor:
            try:
                print(f'Id a eliminar {id_persona}')
                cursor.execute(cls._eliminar, (id_persona,))
                return cursor.rowcount
            except Exception as e:
                print("Error al hacer la eliminación:", e)

if __name__=="__main__":
    persona1= Persona(nombre="pancho", apellido="martinez", email="pancho@gmail.com", id_persona=16 )
    print(f"Numero de registros exitoos insertado {PersonaDao.eliminar(16)}")

