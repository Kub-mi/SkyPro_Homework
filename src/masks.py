import logging
from typing import Union

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция для создания маски номера карты в виде ХХХХ ХХ** **** ХХХХ"""
    logger.info("Начало создания маски для номера карты")
    # Преобразуем номер карты в строку
    card_number_str = str(card_number)

    # Проверим, что длина номера карты соответствует стандарту (16 символов)
    if len(card_number_str) != 16:
        logger.error("Ошибка, количество цифр карты != 16")
        raise ValueError("Номер карты должен состоять из 16 цифр.")

    # Разбиваем номер карты по частям
    first_part_card = card_number_str[:6]
    last_part_card = card_number_str[-4:]

    # Формируем итоговый результат
    logger.info("Получение маски для номера карты")
    masked_card_number = f"{first_part_card[:4]} {first_part_card[4:]}** **** {last_part_card}"
    return masked_card_number


def get_mask_account(acc_number: Union[int, str]) -> str:
    """Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX"""
    logger.info("Начало создания маски для номера счета")
    # Преобразуем номер счета в строку
    logger.info("Преобразование номера счета в строку")
    acc_number_str = str(acc_number)

    # Проверим, что длина номера счета соответствует стандарту (20 символов)
    if len(acc_number_str) != 20:
        logger.error("Ошибка, количество цифр счета != 20")
        raise ValueError("Номер счета должен состоять из 20 цифр.")

    # Разбиваем номер счета по частям
    last_part_acc = acc_number_str[-4:]

    # Формируем итоговый результат
    logger.info("Получение маски для номера счета")
    mask_account = f"**{last_part_acc}"
    return mask_account
