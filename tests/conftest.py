import pytest


@pytest.fixture
def exemple_processing():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def exemple_processing_no_state():
    return [
        {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def exemple_processing_no_type():
    return [
        {"id": 41428829, "state": ["EXECUTED"], "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": 123, "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 512352345,
            "state": "EXECUTED",
            "date": "2020-05-15T10:30:00.000000",
            "operationAmount": {"amount": "1500.50", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 123456789",
            "to": "Счет 987654321",
        },
        {
            "id": 678912345,
            "state": "EXECUTED",
            "date": "2021-07-20T14:15:30.123456",
            "operationAmount": {"amount": "3000.00", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод с карты на карту",
            "from": "Карта 4321567812345678",
            "to": "Карта 8765432112345678",
        },
        {
            "id": 789123456,
            "state": "EXECUTED",
            "date": "2022-09-10T09:05:10.654321",
            "operationAmount": {"amount": "5000.75", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 5678901234567890",
            "to": "Счет 0987654321098765",
        },
    ]


@pytest.fixture
def transactions_usd():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 789123456,
            "state": "EXECUTED",
            "date": "2022-09-10T09:05:10.654321",
            "operationAmount": {"amount": "5000.75", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 5678901234567890",
            "to": "Счет 0987654321098765",
        },
    ]


@pytest.fixture
def transactions_dis():
    return [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


@pytest.fixture
def card_num():
    return [
        "1999 9999 9999 9990",
        "1999 9999 9999 9991",
        "1999 9999 9999 9992",
        "1999 9999 9999 9993",
        "1999 9999 9999 9994",
        "1999 9999 9999 9995",
        "1999 9999 9999 9996",
        "1999 9999 9999 9997",
        "1999 9999 9999 9998",
        "1999 9999 9999 9999",
        "2000 0000 0000 0000",
    ]
