from src.widget import mask_account_card
from src.masks import get_mask_card_number
from src.masks import get_mask_account
from src.widget import get_date
examples_all = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305"
]

examples_cards = [
    "1596837868705199",
    "7158300734726758",
    "6831982476737658",
    "8990922113665229",
    "5999414228426353",
]

examples_accaunt = [
    "64686473678894779589",
    "35383033474447895560",
    "73654108430135874305"
]

for example in examples_all:
    print(mask_account_card(example))

for example_card in examples_cards:
    print(get_mask_card_number(example_card))

for example_accaunt in examples_accaunt:
    print(get_mask_account(example_accaunt))

print(get_date("2024-03-11T02:26:18.671407"))