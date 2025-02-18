from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_number: str) -> str:
    """маскирует значение и карты и счета"""
    account_card_number_list = account_card_number.split()

    if "Счет" in account_card_number_list:
        return f"{account_card_number_list[0]} {get_mask_account(account_card_number_list[1])}"
    elif "Maestro" in account_card_number_list or "MasterCard" in account_card_number_list:
        return f"{account_card_number_list[0]} {get_mask_card_number(account_card_number_list[1])}"
    elif "Visa" in account_card_number_list:
        return (
            f"{account_card_number_list[0]} {account_card_number_list[1]} "
            f"{get_mask_card_number(account_card_number_list[2])}"
        )
    # Обработка случая, когда передан неизвестный тип карты/счета
    raise ValueError("Некорректный формат входных данных: не удалось определить тип карты или счета.")


def get_date(my_date: str) -> str:
    """функция вывода даты в фомате ДД.ММ.ГГГГ"""
    date_obj = datetime.strptime(my_date, "%Y-%m-%dT%H:%M:%S.%f")
    # Преобразуем в нужный формат
    return date_obj.strftime("%d.%m.%Y")
