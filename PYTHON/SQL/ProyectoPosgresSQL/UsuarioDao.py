from loogerBase import log
from CursorDelPool import CursorDelPool

class UsuarioDao:
    _select = 'SELECT * FROM Usuario'
    _insert = 'INSERT INTO Usuario (username, password) VALUES (%s, %s)'
    _update = 'UPDATE Usuario SET username = %s, password = %s WHERE id_usuario = %s'
    _delete = 'DELETE FROM Usuario WHERE id_usuario = %s'


    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            try:
                cursor.execute(cls._select)
                registros = cursor.fetchall()
                return registros
            except Exception as e:
                log.error(f'Error al seleccionar usuarios: {e}')
                return None
            
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            try:
                valores = (usuario.nombre, usuario.apellido)
                cursor.execute(cls._insert, valores)
                log.info(f'Usuario insertado: {usuario.nombre}')
                return cursor.rowcount
            except Exception as e:
                log.error(f'Error al insertar usuario: {e}')
                return None

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            try:
                valores = (usuario.nombre, usuario.apellido, usuario.id_usuario)
                cursor.execute(cls._update, valores)
                log.info(f'Usuario actualizado: {usuario.nombre}')
                return cursor.rowcount
            except Exception as e:
                log.error(f'Error al actualizar usuario: {e}')
                return None
            
    @classmethod
    def eliminar(cls, id_usuario):
        with CursorDelPool() as cursor:
            try:
                cursor.execute(cls._delete, (id_usuario,))
                log.info(f'Usuario eliminado con ID: {id_usuario}')
                return cursor.rowcount
            except Exception as e:
                log.error(f'Error al eliminar usuario: {e}')
                return None