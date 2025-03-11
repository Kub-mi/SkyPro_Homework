from generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions, transactions_usd):
    assert list(filter_by_currency(transactions, "USD")) == transactions_usd


def test_transaction_descriptions(transactions, transactions_dis):
    assert list(transaction_descriptions(transactions)) == transactions_dis


def test_card_number_generator(card_num):
    assert list(card_number_generator(1999999999999990, 2000000000000000)) == card_num
