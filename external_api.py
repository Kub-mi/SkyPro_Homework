import os
import requests
from dotenv import load_dotenv


def get_exchange_rate(currency: str) -> float:
    """Получает текущий курс валюты к рублю."""
    load_dotenv()
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API ключ не найден в переменных окружения")

    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"
    headers = {"apikey": api_key}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise ValueError("Ошибка при получении курса валют")

    data = response.json()
    return data["rates"].get("RUB", 0.0)


def convert_to_rub(transactions: dict) -> float:
    """Конвертирует сумму транзакции в рубли."""
    amount = float(transactions.get("operationAmount", {}).get("amount", 0.0))
    currency = transactions.get("operationAmount", {}).get("currency").get("code", "RUB")

    if currency == "RUB":
        return amount

    rate = get_exchange_rate(currency)
    return amount * rate
