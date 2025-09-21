import logging 

# Configuración del logger
logging.basicConfig(
    level=logging.DEBUG,  # Nivel mínimo de mensajes a capturar
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(filename)s:%(lineno)d',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8',
    handlers=[
        logging.FileHandler('SQL/ProyectoPosgresSQL/registros.log', mode='a', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

log= logging.getLogger("log")  # Crea un logger con el nombre especificado