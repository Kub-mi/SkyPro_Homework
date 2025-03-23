from unittest.mock import patch
from external_api import get_exchange_rate, convert_to_rub

@patch("external_api.requests.get")
def test_convert_to_rub(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"rates": {"RUB": 75.0}}

    assert get_exchange_rate("USD") == 75.0

@patch("external_api.get_exchange_rate", return_value=75.0)
def test_convert_to_rub_usd(mock_get):
    transaction = {"operationAmount": {"amount": "100","currency": {"name": "доллар","code": "USD"}}}
    assert convert_to_rub(transaction) == 7500.0

def test_convert_to_rub_rub():
    transaction = {"operationAmount": {"amount": "5000","currency": {"name": "руб.","code": "RUB"} }}
    assert convert_to_rub(transaction) == 5000.0

