from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(account_card_number: str) -> str:
    """маскирует значение и карты и счета"""

    account_card_number_list = account_card_number.split()

    if "Счет" in account_card_number_list:
        return f'{account_card_number_list[0]} {get_mask_account(account_card_number_list[1])}'
    elif "Maestro" in account_card_number_list or "MasterCard" in account_card_number_list:
        return f'{account_card_number_list[0]} {get_mask_card_number(int(account_card_number_list[1]))}'
    elif "Visa" in account_card_number_list:
        return f'{account_card_number_list[0]} {account_card_number_list[1]} {get_mask_card_number(int(account_card_number_list[2]))}'