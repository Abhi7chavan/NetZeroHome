#centralize logger
import logging

#create logger
logger = logging.getLogger('logger')
# logger.setLevel(logging.INFO)

#create file handler
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)

#create formater
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(pathname)s:%(lineno)d - %(message)s"
)
file_handler.setFormatter(formatter)

#add handler to logger

logger.addHandler(file_handler)

error_handler = logging.FileHandler("error.log")
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)



logger.addHandler(error_handler)
