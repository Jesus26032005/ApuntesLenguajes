from loogerBase import log

class Usuario:
    def __init__(self, id_usuario= None, nombre= None, apellido= None):
        self._id_usuario = id_usuario
        self._nombre = nombre
        self._apellido = apellido
    
    def __str__(self):
        return f"Usuario(id_usuario={self._id_usuario}, nombre={self._nombre}, apellido={self._apellido})"
    
    @property
    def id_usuario(self):
        return self._id_usuario

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido
    
    @id_usuario.setter
    def id_usuario(self, value):
        log.debug(f"Modificacion de id_usuario: {self._id_usuario} a {value}")
        self._id_usuario = value

    @nombre.setter
    def nombre(self, value):
        log.debug(f"Modificacion de nombre: {self._nombre} a {value}")
        self._nombre = value

    @apellido.setter
    def apellido(self, value):
        log.debug(f"Modificacion de apellido: {self._apellido} a {value}")
        self._apellido = value