from looginInf import log

class Persona:
    def __init__(self, id_persona=5 , nombre= None, apellido= None, email= None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self):
        return f"Persona(id_persona={self.id_persona}, nombre='{self.nombre}', apellido='{self.apellido}', email='{self.email}')"
    
    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, new_id):
        self._id_persona = new_id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, new_nombre):
        self._nombre = new_nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, new_apellido):
        self._apellido = new_apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        self._email = new_email

