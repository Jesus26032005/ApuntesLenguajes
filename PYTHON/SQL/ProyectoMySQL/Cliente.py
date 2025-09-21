class Cliente:
    def __init__(self, idCliente=None, nombre=None, apellido=None, email=None):
        self._idCliente = idCliente
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self):
        return f"Cliente[ID: {self.idCliente}, Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}]"
    
    @property
    def idCliente(self):
        return self._idCliente
    @property
    def nombre(self):
        return self._nombre
    @property
    def apellido(self):
        return self._apellido
    @property
    def email(self):
        return self._email

    @idCliente.setter
    def idCliente(self, idCliente):
        self._idCliente = idCliente
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    @email.setter
    def email(self, email):
        self._email = email