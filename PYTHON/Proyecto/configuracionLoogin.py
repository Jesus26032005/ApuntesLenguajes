import logging

logging.basicConfig(
    level= logging.DEBUG,
    format= '%(asctime)s - %(levelname)s - %(message)s - %(filename)s:%(lineno)d - %(name)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8',
    handlers= [
        logging.FileHandler('Proyecto/respuestasServer.log', mode='a', encoding='utf-8'),
    ]
)

log= logging.getLogger("log")