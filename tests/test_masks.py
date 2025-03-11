import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_mask_card_number():
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"
    assert get_mask_card_number(1234567890123456) == "1234 56** **** 3456"

    with pytest.raises(ValueError):
        get_mask_card_number("1234") == "Номер карты должен состоять из 16 цифр."

    with pytest.raises(ValueError):
        get_mask_card_number("123467890123456789") == "Номер карты должен состоять из 16 цифр."


def test_mask_account():
    assert get_mask_account("12345678901234567890") == "**7890"
    assert get_mask_account(12345678901234567890) == "**7890"

    with pytest.raises(ValueError):
        get_mask_account("1234") == "Номер счета должен состоять из 20 цифр."

    with pytest.raises(ValueError):
        get_mask_account("123456789012345678912345") == "Номер счета должен состоять из 20 цифр."
