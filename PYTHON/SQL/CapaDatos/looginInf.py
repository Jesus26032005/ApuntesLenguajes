# En Python, el logging (registro o bitácora) es un módulo estándar que permite llevar un registro de los eventos que suceden mientras se ejecuta un programa. Es muy útil para:
# Depurar errores.
# Monitorear el comportamiento del sistema.
# Guardar información relevante sin tener que imprimir en consola directamente con print().

# ¿Qué hace el módulo logging?
# Permite registrar mensajes en diferentes niveles de severidad, como:

# Nivel	Descripción
# DEBUG	Detalles de depuración (muy detallado).
# INFO	Información general sobre la ejecución.
# WARNING	Advertencias sobre posibles problemas.
# ERROR	Errores que no detienen el programa.
# CRITICAL	Errores graves que podrían detenerlo.

# Ventajas frente a print():
# Puedes guardar los registros en un archivo.
# Puedes definir diferentes niveles de importancia.
# Puedes activarlo o desactivarlo fácilmente en producción.

# Como programador, el logging te sirve para tener el control y seguimiento de lo que pasa en tu programa, tanto durante el desarrollo como cuando ya está en producción. Aquí te explico para qué te sirve realmente en la práctica:

# 🎯 ¿Para qué te sirve el logging como programador?
# 1. Detectar errores sin romper el programa
# Puedes registrar errores con logging.error() sin necesidad de detener el programa ni mostrarle mensajes feos al usuario.
# 2. Saber qué hizo el programa y cuándo
# Cuando algo falla, puedes revisar los archivos .log para ver qué hizo el sistema paso a paso, en qué orden, y en qué parte ocurrió el problema.
# 3. Depurar sin usar print() por todos lados
# En lugar de llenar el código con print(), usas logging.debug() o logging.info() para ver valores de variables, flujos de ejecución, etc.
# 4. Registrar información crítica en producción
# En aplicaciones reales (como páginas web, APIs, automatizaciones...), puedes guardar fallos, advertencias o eventos importantes sin mostrarle nada al usuario.
# 5. Analizar comportamientos anómalos
# Si un usuario reporta que "algo no funciona", puedes revisar los logs para entender qué ocurrió, incluso si no tienes acceso al equipo del usuario.

import logging #Se importa el módulo de logging

# Configuración básica del logging, al usar basicConfig congfigura el comportamiento del módulo logging, es decir, define como se comportaran todos los loggers a menos que se especifique lo contrario en otro logger idnvividualmente. Esto incluye el nivel de registro, el formato de los mensajes, el archivo donde se guardarán los registros, etc.
logging.basicConfig(
    level=logging.DEBUG,  # Nivel de registro (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    #El ir cambiando el nivel de logging permite controlar la cantidad de información que se registra. y que mensajes se muestran, por default es Warning
    format='%(asctime)s - %(levelname)s - %(message)s - %(filename)s:%(lineno)d - %(name)s',  # Formato del mensaje, acstime es la hora en que se registró el mensaje, levelname es el nivel del mensaje (DEBUG, INFO, etc.) y message es el mensaje en sí. Tambien se puede agregar el nombre del archivo y la línea donde se registró el mensaje con %(filename)s y %(lineno)d respectivamente. names añade el nombre del log de donde proviene el mensaje, lo que es útil si tienes múltiples módulos y quieres saber de dónde proviene un mensaje específico.
    # filename='app.log',  # Archivo donde se guardarán los registros
    # filemode='w',  # Modo de apertura del archivo (w para escribir, 'a' para agregar)
    datefmt='%Y-%m-%d %H:%M:%S',  # Formato de fecha y hora, permite personalizar cómo se muestra la fecha y hora en los registros. Por ejemplo, '%Y-%m-%d %H:%M:%S' mostrará la fecha en el formato "Año-Mes-Día Hora:Minuto:Segundo" (2023-10-01 12:00:00)
    encoding='utf-8',  # Codificación del archivo, se recomienda usar 'utf-8' para evitar problemas con caracteres especiales. Esto asegura que los mensajes se guarden correctamente en el archivo, especialmente si contienen caracteres no ASCII.
    handlers=[  # Manejadores de logging, permiten definir dónde se guardarán los registros
        logging.FileHandler('SQL/CapaDatos1/app.log', mode='a', encoding='utf-8'),  # Manejador para escribir en un archivo
        logging.StreamHandler()  # Manejador para mostrar en la consola
    ]
)
log = logging.getLogger("auxiliar") # Crea un logger con el nombre del módulo actual, permite identificar de dónde provienen los mensajes de log. Esto es útil cuando tienes múltiples módulos y quieres saber cuál generó un mensaje específico, ademas de que permite configurar diferentes loggers con diferentes niveles de registro o manejadores si es necesario.

if __name__ == "__main__":
    log.debug("Este es un mensaje de depuración")  # Mensaje de depuración
    log.info("Este es un mensaje informativo")  # Mensaje informativo
    log.warning("Este es un mensaje de advertencia")  # Mensaje de advertencia
    log.error("Este es un mensaje de error")  # Mensaje de error
    log.critical("Este es un mensaje crítico")  # Mensaje crítico


# ------------------------------------------------------
# Además, para proyectos más grandes, es buena práctica
# centralizar la creación y configuración de loggers en un archivo aparte.

# Ejemplo de archivo: logger_config.py
import logging

def crear_logger(nombre, nivel=logging.DEBUG):
    """
    Crea y configura un logger con un nombre y nivel específicos.
    Retorna el logger configurado.
    """
    logger = logging.getLogger(nombre) # Crea un logger con el nombre especificado
    logger.setLevel(nivel)
    logger.encoding = 'utf-8'  # Configura la codificación del logger
    logger.propagate = False  # Evita que los mensajes se propaguen a loggers superiores

    # Evita agregar múltiples handlers si ya tiene alguno
    if not logger.hasHandlers():
        handler = logging.StreamHandler()  # Mostrar en consola
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

# Crear y exportar loggers para usar en el proyecto
logger_db = crear_logger('database', nivel=logging.INFO)
logger_api = crear_logger('api', nivel=logging.DEBUG)

# Así en otros módulos importas y usas:
# from logger_config import logger_db, logger_api
# logger_db.info("Mensaje desde módulo de base de datos")
# logger_api.debug("Mensaje desde módulo API")


# 1. Crear o obtener un logger con un nombre único
# logger = logging.getLogger("mi_logger_personalizado")
# 2. Establecer el nivel mínimo de mensajes a procesar
# logger.setLevel(logging.DEBUG)  # Acepta todos los mensajes desde DEBUG hacia arriba
# 3. Crear un handler para la consola (StreamHandler)
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.DEBUG)  # Nivel para la consola
# 4. Crear un handler para archivo (FileHandler) con encoding utf-8
# file_handler = logging.FileHandler('mi_log.log', mode='a', encoding='utf-8')
# file_handler.setLevel(logging.INFO)  # Sólo guarda mensajes INFO o superiores
# 5. Crear un formatter para definir el formato de los mensajes de log
# formatter = logging.Formatter(
#     fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(filename)s:%(lineno)d',
#     datefmt='%Y-%m-%d %H:%M:%S')
# 6. Asignar el formatter a cada handler
# console_handler.setFormatter(formatter)
# file_handler.setFormatter(formatter)
# 7. Añadir los handlers al logger
# logger.addHandler(console_handler)
# logger.addHandler(file_handler)
