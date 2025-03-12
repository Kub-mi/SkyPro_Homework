from typing import List, Dict, Iterator


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """Принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""

    return (
        transaction
        for transaction in transactions
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency
    )


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    return (transaction.get("description", "no") for transaction in transactions)


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for number in range(start, end + 1):
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[
            8:12
        ] + " " + f"{number:016d}"[12:]
