from UsuarioDao import UsuarioDao
from Usuario import Usuario
from loogerBase import log
from Conexion import Conexion

opcion = None
while opcion != 5:
    print('Opciones:')
    print('1. Listar usuarios')
    print('2. Agregar usuario')
    print('3. Modificar usuario')
    print('4. Eliminar usuario')
    print('5. Salir')
    opcion = int(input('Escribe tu opcion (1-5): '))
    if opcion == 1:
        usuarios = UsuarioDao.seleccionar()
        if not usuarios:
            log.error('No se encontraron usuarios.')
        else:
            for usuario in usuarios:
                log.info(usuario)
    elif opcion == 2:
        nombre_var = input('Escribe el nombre: ')
        apellido_var = input('Escribe el apellido: ')
        usuario = Usuario(nombre=nombre_var, apellido=apellido_var)
        usuarios_insertados = UsuarioDao.insertar(usuario)
        log.info(f'Usuarios insertados: {usuarios_insertados}')
    elif opcion == 3:
        id_usuario_var = int(input('Escribe el id_usuario a modificar: '))
        nombre_var = input('Escribe el nuevo nombre: ')
        apellido_var = input('Escribe el nuevo apellido: ')
        usuario = Usuario(id_usuario=id_usuario_var, nombre=nombre_var, apellido=apellido_var)
        usuarios_actualizados = UsuarioDao.actualizar(usuario)
        log.info(f'usuarios actualizados: {usuarios_actualizados}')
    elif opcion == 4:
        id_usuario_var = int(input('Escribe el id_usuario a eliminar: '))
        usuarios_eliminados = UsuarioDao.eliminar(id_usuario_var)   
else:
    log.info('Salimos de la aplicación...')
    Conexion.cerrarConexiones()