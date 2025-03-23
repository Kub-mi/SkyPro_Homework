import json
import os


def json_transformation(file_path: str) -> list:
    """
    Функция преобразует json файл в строку или словарь.
    Или возвращает пустую строку, если нет json
    """

    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except (json.JSONDecodeError, IOError):
        pass
    return []
