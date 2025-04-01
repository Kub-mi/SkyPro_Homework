from src.filter_trans import filter_by_description
from src.masks import get_mask_card_number, get_mask_account
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date
from csv_xlsx_reader import csv_reader, excel_reader
from generators import filter_by_currency
from utils import json_transformation


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    while True:
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        choice = input("Ваш выбор: ")

        if choice == "1":
            file_path = input("Введите путь к JSON-файлу: ")
            transactions = json_transformation(file_path)
        elif choice == "2":
            file_path = input("Введите путь к CSV-файлу: ")
            transactions = csv_reader(file_path)
        elif choice == "3":
            file_path = input("Введите путь к XLSX-файлу: ")
            transactions = excel_reader(file_path)
        else:
            print("Неверный выбор. Попробуйте снова.")
            continue

        if not transactions:
            print("Файл не содержит данных или указан неверный путь.")
            continue

        while True:
            print("Введите статус, по которому необходимо выполнить фильтрацию.")
            print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
            state = input("Ваш выбор: ").strip().upper()

            if state not in ["EXECUTED", "CANCELED", "PENDING"]:
                print(f"Статус операции \"{state}\" недоступен.")
            else:
                transactions = filter_by_state(transactions, state)
                print(f"Операции отфильтрованы по статусу \"{state}\".")
                break

        sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
        if sort_choice == "да":
            order_choice = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
            descending = order_choice == "по убыванию"
            transactions = sort_by_date(transactions, descending)

        currency_choice = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
        if currency_choice == "да":
            transactions = list(filter_by_currency(transactions, "RUB"))

        search_choice = input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
        if search_choice == "да":
            search_query = input("Введите слово для поиска в описании: ")
            transactions = filter_by_description(transactions, search_query)

        print("Распечатываю итоговый список транзакций...")
        if not transactions:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        else:
            print(f"Всего банковских операций в выборке: {len(transactions)}")

            for transaction in transactions:
                date = get_date(transaction["date"])
                description = transaction.get("description", "Нет описания")
                amount = transaction.get("operationAmount", {}).get("amount", "Нет суммы")
                currency = transaction.get("operationAmount", {}).get("currency", {}).get("code", "Нет валюты")
                sender = transaction.get("from", "")
                receiver = transaction.get("to", "")

                sender_masked = sender  # По умолчанию оставляем как есть
                receiver_masked = receiver

                if sender:
                    sender_parts = sender.split()
                    last_part = sender_parts[-1]

                    if last_part.isdigit():
                        if len(last_part) == 16:
                            sender_masked = " ".join(sender_parts[:-1]) + " " + get_mask_card_number(last_part)
                        elif len(last_part) == 20:
                            sender_masked = " ".join(sender_parts[:-1]) + " " + get_mask_account(last_part)

                if receiver:
                    receiver_parts = receiver.split()
                    last_part = receiver_parts[-1]

                    if last_part.isdigit():
                        if len(last_part) == 16:
                            receiver_masked = " ".join(receiver_parts[:-1]) + " " + get_mask_card_number(last_part)
                        elif len(last_part) == 20:
                            receiver_masked = " ".join(receiver_parts[:-1]) + " " + get_mask_account(last_part)

                print(f"{date} {description}")
                if sender:
                    print(f"{sender_masked} -> {receiver_masked}")
                print(f"Сумма: {amount} {currency}\n")

        repeat = input("Хотите выполнить новую операцию? Да/Нет: ").strip().lower()
        if repeat != "да":
            print("Спасибо за использование программы!")
            break




if __name__ == "__main__":
    main()
