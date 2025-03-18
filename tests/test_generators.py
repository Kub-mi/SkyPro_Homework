import pytest

from generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions, transactions_usd):
    assert list(filter_by_currency(transactions, "USD")) == transactions_usd


def test_transaction_descriptions(transactions, transactions_dis):
    assert list(transaction_descriptions(transactions)) == transactions_dis


@pytest.mark.parametrize(
    "value_start, value_end, expected_nums",
    [
        (1999999999999999, 2000000000000000, ['1999 9999 9999 9999', '2000 0000 0000 0000']),
        (1999999999999999, 1999999999999999, ['1999 9999 9999 9999']),
        (1, 2, ['0000 0000 0000 0001', '0000 0000 0000 0002'])
    ]
)
def test_card_number_generator(card_num, value_start, value_end, expected_nums):
    assert list(card_number_generator(1999999999999990, 2000000000000000)) == card_num
    assert list(card_number_generator(value_start, value_end)) == expected_nums
