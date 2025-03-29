from typing import Union

from decorators import log
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card
from utils import json_transformation

examples_all = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305",
]

examples_cards = [
    "1596837868705199",
    "7158300734726758",
    "6831982476737658",
    "8990922113665229",
    "5999414228426353",
]

examples_accaunt = ["64686473678894779589", "35383033474447895560", "73654108430135874305"]

exemple_processing = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

exemple_processing_no_state = [
    {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
]

print("список маски номерка карты и номера счета:\n")
for example in examples_all:
    print(mask_account_card(example))

print("список маски номерка карты:\n")
for example_card in examples_cards:
    print(get_mask_card_number(example_card))

print("список маски номерка счета:\n")
for example_accaunt in examples_accaunt:
    print(get_mask_account(example_accaunt))

print(get_date("2024-03-11T02:26:18.671407"))
print(f"отфильтрованный список:\n{filter_by_state(exemple_processing)}\n")
print(f"отфильтрованный список без state:\n{filter_by_state(exemple_processing_no_state)}\n")
print(f"отсортрованный список по убыванию:\n{sort_by_date(exemple_processing)}\n")
print(f"отсортрованный список по возростанию:\n{sort_by_date(exemple_processing, False)}\n")


@log(filename="mylog.txt")
def my_function(x: Union[int, float], y: Union[int, float]) -> float:
    """Функция проверки декоратора"""
    return x / y


my_function(1, 1)

transactions = json_transformation("data/operations.json")
print(transactions)
