import pytest
from src.widget import mask_account_card, get_date


def test_mask_account_card():
    assert mask_account_card('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'
    assert mask_account_card('Счет 64686473678894779589') == 'Счет **9589'

    with pytest.raises(ValueError):
        mask_account_card('1234') == 'Некорректный формат входных данных: не удалось определить тип карты или счета.'

def test_get_date():
    assert get_date('2024-03-11T02:26:18.671407') == '11.03.2024'