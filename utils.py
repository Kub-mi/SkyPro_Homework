import json
import logging
import os

logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/utils.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

def json_transformation(file_path: str) -> list:
    """
    Функция преобразует json файл в строку или словарь.
    Или возвращает пустую строку, если нет json
    """
    logger.info('Начало преобразования json файла')
    if not os.path.exists(file_path):
        logger.error('Нет файла для обработки')
        return []
    try:
        logger.info('Преобразование json файла')
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info('Получение Python объекта из json файла')
                return data
    except (json.JSONDecodeError, IOError):
        logger.error(f'Ошибка преобразования файла {IOError}')

    return []
